from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"


class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readInteger", MType(list(), IntegerType()), CName(self.libName)),
                Symbol("printInteger", MType([IntegerType()],
                       VoidType()), CName(self.libName))
                ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value


class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path

    def visitProgram(self, ast, c):
        [self.visit(i, c)for i in ast.decl]
        return c

    def visitClassDecl(self, ast, c):
        self.className = ast.classname.name
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        self.emit.printout(self.emit.emitPROLOG(
            self.className, "java.lang.Object"))
        [self.visit(ele, SubBody(None, self.env))
         for ele in ast.memlist if type(ele) == MethodDecl]
        # generate default constructor
        self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(
        ), None, Block([], [])), c, Frame("<init>", VoidType()))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(
            consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayType(0, StringType())] if isMain else list(
            map(lambda x: x.typ, consdecl.param))
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                Id(self.className)), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(
                0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            local = reduce(lambda env, ele: SubBody(
                frame, [self.visit(ele, env)]+env.sym), consdecl.param, SubBody(frame, []))
            glenv = local.sym+glenv

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, o.sym, frame)
        return Symbol(ast.name, MType([x.typ for x in ast.param], ast.returnType), CName(self.className))

    def visitVarDecl(self, ast, o):
        frame = o.frame
        sym = Symbol(ast.variable.name, ast.varType)
        if frame:
            frame.enterScope(False)
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(
                idx, sym.name, sym.mtype, frame.getStartLabel(), frame.getEndLabel(), frame))
            frame.exitScope()
        return sym

    def visitParamDecl(self, ast, o):
        frame = o.frame
        sym = Symbol(ast.variable.name, ast.varType)
        if frame:
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(
                idx, sym.name, sym.mtype, frame.getStartLabel(), frame.getEndLabel(), frame))
        return sym

    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = next(filter(lambda x: ast.method.name == x.name, nenv), None)
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + ast.method.name, ctype, frame))

    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntegerType()

    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(str(ast.value), o.frame), BooleanType()

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST('"' + ast.value + '"', StringType(), o.frame), StringType()

    def visitArrayLiteral(self, ast, o):
        return self.visit(ast.value, o)

    def visitBinaryOp(self, ast, o):
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)
        return e1c + e2c + self.emit.emitADDOP(ast.op, e1t, o.frame), e1t

    def visitUnaryOp(self, ast, o):
        ec, et = self.visit(ast.val, o)
        return ec + self.emit.emitNEGOP(et, o.frame), et

    def visitId(self, ast, o):
        sym = next(filter(lambda x: ast.name == x.name, o.sym), None)
        if sym.value is None:
            return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype
        else:
            return self.emit.emitGETSTATIC(sym.value.value + "/" + sym.name, sym.mtype, o.frame), sym.mtype

    def visitArrayCell(self, ast, o):
        ec, et = self.visit(ast.arr, Access(o.frame, o.sym, False))
        ec1, et1 = self.visit(ast.idx, Access(o.frame, o.sym, False))
        return ec + ec1 + self.emit.emitALOAD(et, o.frame), et.eleType

    def visitIf(self, ast, o):
        # Code gen for cond
        ec, et = self.visit(ast.cond, Access(o.frame, o.sym, False))
        self.emit.printout(ec)

        # Jump to FLABEL if False
        FLABEL = o.frame.getNewLabel()
        code = self.emit.emitIFFALSE(FLABEL, o.frame)
        self.emit.printout(code)

        # Code gen for true statement
        self.visit(ast.tstmt, o)

        # Jump to ELABEL to finish if else statement
        ELABEL = o.frame.getNewLabel()
        code = self.emit.emitGOTO(ELABEL, o.frame)
        self.emit.printout(code)

        if ast.estmt:
            # Place FLABEL here for upcoming jump
            code = self.emit.emitLABEL(FLABEL, o.frame)
            self.emit.printout(code)

            # Code gen for else statement
            self.visit(ast.estmt, o)

        # Place ELABEL here for upcoming jump
        code = self.emit.emitLABEL(ELABEL, o.frame)
        self.emit.printout(code)

    def visitWhile(self, ast, o):
        o.frame.enterLoop()

        # Get BREAKLABEL and CONTINUELABEL
        BREAKLABEL = o.frame.getBreakLabel()
        CONTINUELABEL = o.frame.getContinueLabel()

        # Place CONTINUELABEL here for repeating while statement
        code = self.emit.emitLABEL(CONTINUELABEL, o.frame)
        self.emit.printout(code)

        # Code gen for cond
        ec, et = self.visit(ast.cond, Access(o.frame, o.sym, False))
        self.emit.printout(ec)

        # Jump to BREAKLABEL if False
        code = self.emit.emitIFFALSE(BREAKLABEL, o.frame)
        self.emit.printout(code)

        # Code gen for stmt
        self.visit(ast.stmt, o)

        # Jump to CONTINUELABEL to repeat while statement
        code = self.emit.emitGOTO(CONTINUELABEL, o.frame)
        self.emit.printout(code)

        # Place BREAKLABEL here for upcoming jump
        code = self.emit.emitLABEL(BREAKLABEL, o.frame)
        self.emit.printout(code)

        o.frame.exitLoop()

    def visitDoWhile(self, ast, o):
        o.frame.enterLoop()

        # Get BREAKLABEL and CONTINUELABEL
        BREAKLABEL = o.frame.getBreakLabel()
        CONTINUELABEL = o.frame.getContinueLabel()

        # Place CONTINUELABEL here for repeating do while statement
        code = self.emit.emitLABEL(CONTINUELABEL, o.frame)
        self.emit.printout(code)

        # Code gen for stmt
        self.visit(ast.stmt, o)

        # Code gen for cond
        ec, et = self.visit(ast.cond, Access(o.frame, o.sym, False))
        self.emit.printout(ec)

        # Jump to BREAKLABEL if False
        code = self.emit.emitIFFALSE(BREAKLABEL, o.frame)
        self.emit.printout(code)

        # Jump to CONTINUELABEL to repeat do while statement
        code = self.emit.emitGOTO(CONTINUELABEL, o.frame)
        self.emit.printout(code)

        # Place BREAKLABEL here for upcoming jump
        code = self.emit.emitLABEL(BREAKLABEL, o.frame)
        self.emit.printout(code)

        o.frame.exitLoop()

    def visitFor(self, ast, o):
        o.frame.enterLoop()

        # Get BREAKLABEL and CONTINUELABEL
        BREAKLABEL = o.frame.getBreakLabel()
        CONTINUELABEL = o.frame.getContinueLabel()

        # Code gen for init: AssignStmt
        if ast.init:
            self.visit(ast.init, o)

        # Place CONTINUELABEL here for repeating for statement
        code = self.emit.emitLABEL(CONTINUELABEL, o.frame)
        self.emit.printout(code)

        # Code gen for cond
        if ast.cond:
            ec, et = self.visit(ast.cond, Access(o.frame, o.sym, False))
            self.emit.printout(ec)

            # Jump to BREAKLABEL if False
            code = self.emit.emitIFFALSE(BREAKLABEL, o.frame)
            self.emit.printout(code)

        # Code gen for stmt
        self.visit(ast.stmt, o)

        # Code gen for upd: Expr
        if ast.upd:
            ec, et = self.visit(ast.upd, Access(o.frame, o.sym, False))
            self.emit.printout(ec)

        # Jump to CONTINUELABEL to repeat for statement
        code = self.emit.emitGOTO(CONTINUELABEL, o.frame)
        self.emit.printout(code)

        # Place BREAKLABEL here for upcoming jump
        code = self.emit.emitLABEL(BREAKLABEL, o.frame)
        self.emit.printout(code)

        o.frame.exitLoop()

    def visitBreak(self, ast, o):
        code = self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame)
        self.emit.printout(code)

    def visitContinue(self, ast, o):
        code = self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame)
        self.emit.printout(code)

    def visitReturn(self, ast, o):
        if ast.expr:
            ec, et = self.visit(ast.expr, Access(o.frame, o.sym, False))
            self.emit.printout(ec)
            code = self.emit.emitRETURN(et, o.frame)
            self.emit.printout(code)
        else:
            code = self.emit.emitRETURN(VoidType(), o.frame)
            self.emit.printout(code)

    def visitBlock(self, ast, o):
        frame = o.frame
        frame.enterScope(False)
        list(map(lambda x: self.visit(x, o), ast.body))
        frame.exitScope()

    def visitAssign(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = next(filter(lambda x: ast.lhs.name == x.name, nenv), None)
        if sym.value is None:
            ec, et = self.visit(ast.rhs, Access(frame, nenv, False, True))
            self.emit.printout(ec)
            self.emit.printout(self.emit.emitWRITEVAR(
                sym.name, sym.mtype, sym.value.value, frame))
        else:
            ec, et = self.visit(ast.rhs, Access(frame, nenv, False, True))
            self.emit.printout(ec)
            self.emit.printout(self.emit.emitPUTSTATIC(
                sym.value.value + "/" + sym.name, sym.mtype, frame))

    def visitIntegerType(self, ast, o):
        return "int", IntegerType()

    def visitFloatType(self, ast, o):
        return "float", FloatType()

    def visitBooleanType(self, ast, o):
        return "boolean", BooleanType()

    def visitStringType(self, ast, o):
        return "String", StringType()

    def visitVoidType(self, ast, o):
        return "void", VoidType()

    def visitArrayType(self, ast, o):
        return self.visit(ast.typ, o)
