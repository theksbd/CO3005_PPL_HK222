from AST import *
from StaticError import *
from Visitor import Visitor


class Symbol(ABC):
    def __init__(self, name, typ, kind=Function(), inherit=None, o=None, isGlobal=False):
        self.name = name
        self.typ = typ
        self.kind = kind
        self.inherit = inherit
        self.o = o
        self.isGlobal = isGlobal

    def return_type(self):
        return self.typ


class Loop(ABC):
    pass


class If(ABC):
    pass


class Util:
    @staticmethod
    def flatten(lst, o=[]):
        if type(lst) is ArrayLit:
            if type(lst.explist) is list:
                for i in lst.explist:
                    o = Util.flatten(i, o)
            else:
                o = o + [lst.explist]
        else:
            o = o + [lst]
        return o

    @staticmethod
    def findSymbol(lst, name, typ):
        for sub in lst:
            for mem in sub:
                if type(mem) is typ and mem.name == name:
                    return mem
        return

    @staticmethod
    def setSymbol(lst, name, kind, typ):
        for sub in lst:
            for mem in sub:
                if type(mem) is kind and mem.name == name:
                    if kind is FuncDecl:
                        mem.return_type = typ
                    elif kind is VarDecl:
                        mem.typ = typ

    @staticmethod
    def getDimensions(ctx):
        if type(ctx) is ArrayLit and isinstance(ctx.explist, list):
            return [len(ctx.explist)] + Util.getDimensions(ctx.explist[0])
        else:
            return []


class StaticChecker(Visitor):
    def __init__(self, ctx):
        self.ctx = ctx

    def check(self):
        return self.visitProgram(self.ctx, [])

    # class Program(AST): #decls: List[Decl]
    def visitProgram(self, ctx: Program, o):
        o = [[]]
        for decl in ctx.decls:
            o = self.visit(decl, o)

        env = [[]] + o
        for decl in ctx.decls:
            env = self.visit(decl, env)

        isMain = False
        for decl in ctx.decls:
            if type(decl) is FuncDecl and decl.name == "main" and len(decl.params) == 0 and type(decl.return_type) is VoidType:
                isMain = True
                break
        if not isMain:
            raise NoEntryPoint()
        return []

    # class VarDecl(Decl): #name: str, #typ: Type, #init: Expr or None
    def visitVarDecl(self, ctx: VarDecl, o):
        for identifier in o[0]:
            if identifier.name == ctx.name:
                if type(identifier) is VarDecl or type(identifier) is ParamDecl:
                    raise Redeclared(Variable(), ctx.name)

        if ctx.init is not None:
            expression_type = self.visit(ctx.init, o)
            # print(ctx.name, ctx.init, ctx.typ, expression_type)
            if type(expression_type) is not type(ctx.typ):
                if type(expression_type) is VoidType:
                    raise TypeMismatchInVarDecl(ctx)
                if type(ctx.typ) is AutoType:
                    ctx.typ = self.visit(expression_type, o)
                elif type(ctx.init) is not FuncCall:
                    raise TypeMismatchInVarDecl(ctx)

            if type(expression_type) is ArrayType and type(ctx.typ) is ArrayType:
                if type(expression_type.typ) is not type(ctx.typ.typ):
                    raise TypeMismatchInVarDecl(ctx)
                if len(expression_type.dimensions) == len(ctx.typ.dimensions):
                    length = len(expression_type.dimensions)
                    for i in range(length):
                        if expression_type.dimensions[i] != ctx.typ.dimensions[i]:
                            raise TypeMismatchInVarDecl(ctx)

            if type(expression_type) is AutoType and type(ctx.init) is FuncCall:
                for sub in o:
                    for mem in sub:
                        if mem.name == ctx.init.name and type(mem) is FuncDecl:
                            mem.return_type = self.visit(ctx.typ, o)
                            break
        else:
            if type(ctx.typ) is AutoType:
                raise Invalid(Variable(), ctx.name)

        o[0] += [ctx]
        return o

    # class ParamDecl(Decl): #name: str, #typ: Type, #out: bool, #inherit: bool
    def visitParamDecl(self, ctx: ParamDecl, o):
        for param in o[0]:
            if type(param) is ParamDecl and param.name == ctx.name:
                raise Redeclared(Parameter(), ctx.name)
        o[0] += [ctx]
        return o

    # class FuncDecl(Decl): #name: str, #return_type: Type, #params: List[ParamDecl], #inherit: str or None, #body: BlockStmt
    def visitFuncDecl(self, ctx: FuncDecl, o):
        for mem in o[0]:
            if type(mem) is FuncDecl and mem.name == ctx.name and type(mem.return_type) is type(ctx.return_type):
                raise Redeclared(Function(), ctx.name)

        if ctx.name in ["readInteger", "printInteger", "readFloat", "writeFloat", "readBoolean", "printBoolean", "readString", "printString",  "super", "preventDefault"]:
            raise Redeclared(Function(), ctx.name)

        o[0] += [ctx]

        if len(o) > 1:
            if ctx.inherit is not None:
                isDeclared = Util.findSymbol(o, ctx.inherit, FuncDecl)
                if isDeclared is None:
                    raise Undeclared(Function(), ctx.inherit)
            env = [[Symbol(ctx.name, ctx.return_type, Function(),
                           ctx.inherit, ctx.params)]] + o
            for paramdecl in ctx.params:
                env = self.visit(paramdecl, env)
            env = self.visit(ctx.body, env)
        return o

    # class CallStmt(Stmt): #name: str, #args: List[Expr]
    def visitCallStmt(self, ctx: CallStmt, o):
        def check_name(ast, lst):
            for sub in lst:
                for mem in sub:
                    if type(mem) is Symbol:
                        continue
                    if mem.name == ast.name and type(mem) is FuncDecl:
                        if mem.return_type is AutoType:
                            mem.return_type = VoidType()
                        return True, mem
            return False, None

        if ctx.name not in ["super", "preventDefault"]:
            isDeclared, func = check_name(ctx, o)
            if isDeclared is False:
                raise Undeclared(Function(), ctx.name)

            param_func = [[]] + o
            for paramdecl in func.params:
                param_func = self.visit(paramdecl, param_func)
            if len(ctx.args) != len(param_func[0]):
                raise TypeMismatchInStatement(ctx)
            for i in range(len(ctx.args)):
                if type(param_func[0][i].typ) is not AutoType:
                    typ_ast = self.visit(ctx.args[i], o)
                    if type(param_func[0][i].typ) is not type(typ_ast):
                        raise TypeMismatchInStatement(ctx)
        elif ctx.name == "super":
            return o
        return o

    # class ReturnStmt(Stmt): #expr: Expr or None
    def visitReturnStmt(self, ctx: ReturnStmt, o):
        return_typ = self.visit(ctx.expr, o) if ctx.expr is not None else None
        for sub in o:
            for mem in sub:
                if type(mem) is Symbol and type(mem.kind) is Function:
                    if type(mem.typ) is type(return_typ):
                        return mem.typ
                    if type(mem.typ) is AutoType:
                        if return_typ is None:
                            Util.setSymbol(o, mem.name, FuncDecl, VoidType())
                            mem.typ = VoidType()
                        else:
                            Util.setSymbol(o, mem.name, FuncDecl,
                                           self.visit(return_typ, o))
                            mem.typ = self.visit(return_typ, o)
                    if type(mem.typ) is VoidType and return_typ is None:
                        return VoidType()
                    if type(mem.typ) is not type(return_typ):
                        raise TypeMismatchInStatement(ctx)
                    else:
                        return o
        raise TypeMismatchInStatement(ctx)

    # class ContinueStmt(Stmt):
    def visitContinueStmt(self, ctx: ContinueStmt, o):
        for sym in o:
            for mem in sym:
                if type(mem) is Symbol and mem.name == "Loop" and type(mem.kind) is Loop:
                    return ContinueStmt()
        raise MustInLoop(ctx)

    # class BreakStmt(Stmt):
    def visitBreakStmt(self, ctx: BreakStmt, o):
        for sub in o:
            for mem in sub:
                if type(mem) is Symbol and mem.name == "Loop" and type(mem.kind) is Loop:
                    return BreakStmt()
        raise MustInLoop(ctx)

    # class DoWhileStmt(Stmt): #cond: Expr, #stmt: BlockStmt
    def visitDoWhileStmt(self, ctx: DoWhileStmt, o):
        cond = self.visit(ctx.cond, o)
        if type(cond) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        env = [[Symbol("Loop", None, Loop())]] + o
        self.visit(ctx.stmt, env)
        return o

    # class WhileStmt(Stmt): #cond: Expr, #stmt: Stmt
    def visitWhileStmt(self, ctx: WhileStmt, o):
        cond = self.visit(ctx.cond, o)
        if type(cond) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        env = [[Symbol("Loop", None, Loop())]] + o
        self.visit(ctx.stmt, env)
        return o

    # class ForStmt(Stmt): #init: AssignStmt, #cond: Expr, #upd: Expr, #stmt: Stmt
    def visitForStmt(self, ctx: ForStmt, o):
        self.visit(ctx.init, o)
        typ = self.visit(ctx.cond, o)
        if type(typ) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        self.visit(ctx.upd, o)

        env = [[Symbol("Loop", None, Loop())]] + o
        env = self.visit(ctx.stmt, env)
        return o

    # class IfStmt(Stmt): #cond: Expr, #tstmt: Stmt, #fstmt: Stmt or None
    def visitIfStmt(self, ctx: IfStmt, o):
        condition = self.visit(ctx.cond, o)
        if type(condition) is not BooleanType:
            raise TypeMismatchInStatement(ctx)

        self.visit(ctx.tstmt, o)
        if ctx.fstmt is not None:
            self.visit(ctx.fstmt, o)

        # tenv = [[Symbol(None, None, IfStmt())]] + o
        # tenv = self.visit(ctx.tstmt, tenv)
        # if ctx.fstmt is not None:
        #     fenv = [[Symbol(None, None, IfStmt())]] + o
        #     fenv = self.visit(ctx.fstmt, fenv)
        return o

    # class BlockStmt(Stmt): #body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ctx: BlockStmt, o):
        func = o[0][0]
        if type(func) is Symbol and func.inherit is not None:
            if type(ctx.body[0]) is not CallStmt:
                raise InvalidStatementInFunction(func.name)
            if ctx.body[0].name != "super" and ctx.body[0].name != "preventDefault":
                raise InvalidStatementInFunction(func.name)
            member = Util.findSymbol(o, func.inherit, FuncDecl)
            if member is not None and len(member.params) != 0:
                raise TypeMismatchInStatement(ctx.body[0])
        for mem in ctx.body:
            self.visit(mem, o)
        return o

    # class AssignStmt(Stmt): #lhs: LHS, #rhs: Expr
    def visitAssignStmt(self, ctx: AssignStmt, o):
        rhs_t = self.visit(ctx.rhs, o)
        lhs_t = self.visit(ctx.lhs, o)

        if type(rhs_t) is VoidType:
            raise TypeMismatchInStatement(ctx)
        if type(rhs_t) is AutoType and type(ctx.rhs) is not FuncCall:
            raise Invalid(Variable(), ctx.rhs.name)
        if type(lhs_t) is not type(rhs_t) and type(lhs_t) is not AutoType:
            raise TypeMismatchInStatement(ctx)
        if type(rhs_t) is AutoType:
            for sub in o:
                for mem in sub:
                    if type(mem) is Symbol:
                        continue
                    elif type(mem) is FuncDecl and mem.name == ctx.rhs.name:
                        if (type(mem.return_type) is AutoType):
                            if (type(ctx.lhs.typ) is AutoType):
                                raise Invalid(Variable(), mem.name)
                            else:
                                mem.return_type = self.visit(ctx.lhs.typ, o)
                                break
        for sub in o:
            for mem in sub:
                if type(mem) is Symbol:
                    continue
                elif mem.name == ctx.lhs.name and type(mem.typ) is AutoType:
                    mem.typ = self.visit(rhs_t, o)
                    break
        return o

    # class FuncCall(Expr): #name: str, #args: List[Expr]
    def visitFuncCall(self, ctx: FuncCall, o):
        def check_name(ast, lst):
            for sub in lst:
                for mem in sub:
                    if type(mem) is Symbol:
                        continue
                    if mem.name == ast.name and type(mem) is FuncDecl:
                        return True, mem
            return False, None

        isDeclared, func = check_name(ctx, o)
        if isDeclared is False:
            raise Undeclared(Function(), ctx.name)

        if len(ctx.args) != len(func.params):
            raise TypeMismatchInExpression(ctx)
        return func.return_type

    # class ArrayCell(LHS): #name: str, #cell: List[Expr]
    def visitArrayCell(self, ctx: ArrayCell, o):
        for sub in o:
            for mem in sub:
                if type(mem) is Symbol:
                    continue
                if mem.name == ctx.name and type(mem) is VarDecl:
                    if type(mem.typ) is not ArrayType:
                        raise TypeMismatchInExpression(ctx)
                    if len(mem.typ.dimensions) != len(ctx.cell):
                        raise TypeMismatchInStatement(ctx)
                    for cell in ctx.cell:
                        if type(self.visit(cell, o)) is not IntegerType:
                            raise TypeMismatchInExpression(ctx)
                    return mem.typ.typ
        raise Undeclared(Identifier(), ctx.name)

    # class Id(LHS): #name: str
    def visitId(self, ctx: Id, o):
        for sub in o:
            for mem in sub:
                if type(mem) is Symbol:
                    continue
                if (type(mem) is VarDecl or type(mem) is ParamDecl) and mem.name == ctx.name:
                    return mem.typ
        raise Undeclared(Identifier(), ctx)

    # class BinExpr(Expr): #op: str, #left: Expr, #right: Expr
    def visitBinExpr(self, ctx: BinExpr, o):
        lt = self.visit(ctx.left, o)
        rt = self.visit(ctx.right, o)

        if type(lt) is AutoType:
            for sub in o:
                for mem in sub:
                    if type(mem) is FuncDecl and mem.name == ctx.left.name:
                        if type(mem.return_type) is AutoType and type(rt) is not AutoType:
                            mem.return_type = self.visit(rt, o)
                            lt = self.visit(rt, o)
                            break
                        else:
                            raise TypeMismatchInExpression(ctx)
                    elif type(mem) is ParamDecl and mem.name == ctx.left.name:
                        if type(mem.typ) is AutoType and type(rt) is not AutoType:
                            mem.typ = self.visit(rt, o)
                            lt = self.visit(rt, o)
                            break
                        else:
                            raise TypeMismatchInExpression(ctx)

        if type(rt) is AutoType:
            for sub in o:
                for mem in sub:
                    if type(mem) is FuncDecl and mem.name == ctx.right.name:
                        if type(mem.return_type) is AutoType and type(lt) is not AutoType:
                            mem.return_type = self.visit(lt, o)
                            rt = self.visit(lt, o)
                            break
                        else:
                            raise TypeMismatchInExpression(ctx)
                    elif type(mem) is ParamDecl and mem.name == ctx.right.name:
                        if type(mem.typ) is AutoType and type(lt) is not AutoType:
                            mem.typ = self.visit(lt, o)
                            rt = self.visit(lt, o)
                            break
                        else:
                            raise TypeMismatchInExpression(ctx)

        # if type(lt) is AutoType and type(rt) is not AutoType:
        #     lt = rt
        #     for identifier in o[0]:
        #         if (type(identifier) is ParamDecl or type(identifier) is FuncDecl) and identifier.name == ctx.left.name:
        #             identifier.typ = lt
        #             break
        # elif type(lt) is not AutoType and type(rt) is AutoType:
        #     rt = lt
        #     for identifier in o[0]:
        #         if (type(identifier) is ParamDecl or type(identifier) is FuncDecl) and identifier.name == ctx.right.name:
        #             identifier.typ = rt
        #             break

        if ctx.op in ['+', '-', '*', '/']:
            if type(lt) is not IntegerType and type(lt) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            if type(rt) is not IntegerType and type(rt) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            if type(lt) is FloatType or type(rt) is FloatType:
                return FloatType()
            return IntegerType()
        elif ctx.op in ['%']:
            if type(lt) is not IntegerType or type(rt) is not IntegerType:
                raise TypeMismatchInExpression(ctx)
            return IntegerType()
        elif ctx.op in ['&&', '||']:
            if type(lt) is not BooleanType or type(rt) is not BooleanType:
                raise TypeMismatchInExpression(ctx)
            return BooleanType()
        elif ctx.op in ['==', '!=']:
            if type(lt) is IntegerType and type(rt) is IntegerType:
                return BooleanType()
            if type(lt) is BooleanType and type(rt) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ctx)
        elif ctx.op in ['>', '<', '>=', '<=']:
            if type(lt) is not IntegerType and type(lt) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            if type(rt) is not IntegerType and type(rt) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return BooleanType()
        elif ctx.op in ['::']:
            if type(lt) is StringType and type(rt) is StringType:
                return StringType()
            raise TypeMismatchInExpression(ctx)

    # class UnExpr(Expr): #op: str, #val: Expr
    def visitUnExpr(self, ctx: UnExpr, o):
        et = self.visit(ctx.val, o)
        if type(et) is AutoType:
            raise Invalid(Variable(), ctx.val.name)
        if ctx.op in ['!']:
            if type(et) is not BooleanType:
                raise TypeMismatchInExpression(ctx)
            return BooleanType()
        if ctx.op in ['-']:
            if type(et) is not IntegerType and type(et) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return IntegerType() if type(et) is IntegerType else FloatType()

    # class IntegerLit(Expr): #val: int
    def visitIntegerLit(self, ctx: IntegerLit, o):
        return IntegerType()

    # class FloatLit(Expr): #val: float
    def visitFloatLit(self, ctx: FloatLit, o):
        return FloatType()

    # class StringLit(Expr): #val: str
    def visitStringLit(self, ctx: StringLit, o):
        return StringType()

    # class BooleanLit(Expr): #val: bool
    def visitBooleanLit(self, ctx: BooleanLit, o):
        return BooleanType()

    # class ArrayLit(Expr): #explist: List[Expr]
    def visitArrayLit(self, ctx: ArrayLit, o):
        flattened = Util.flatten(ctx)

        def getSize(lst):
            res = 1
            for num in lst:
                res *= num
            return res

        def checkType(lst):
            typ = self.visit(lst[0], o)
            for mem in lst:
                typ_ = self.visit(mem, o)
                if type(typ) is not type(typ_):
                    return False, None
            return True, typ

        dimension = Util.getDimensions(ctx)
        check, typ = checkType(flattened)
        isIllegal = (getSize(dimension) == len(flattened)) and check
        if isIllegal is False:
            raise IllegalArrayLiteral(ctx)
        return ArrayType(dimension, self.visit(typ, o))

    def visitIntegerType(self, ctx: IntegerType, o):
        return IntegerType()

    def visitFloatType(self, ctx: FloatType, o):
        return FloatType()

    def visitBooleanType(self, ctx: BooleanType, o):
        return BooleanType()

    def visitStringType(self, ctx: StringType, o):
        return StringType()

    # Class ArrayType(Type): #dimensions: List[int], #typ: AtomicType
    def visitArrayType(self, ctx: ArrayType, o):
        return ArrayType(ctx.dimensions, ctx.typ)

    def visitAutoType(self, ctx: AutoType, o):
        return AutoType()

    def visitVoidType(self, ctx: VoidType, o):
        return VoidType()
