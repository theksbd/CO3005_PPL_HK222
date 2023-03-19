from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from functools import reduce

class ASTGeneration(MT22Visitor):
    # program: decls+ EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        # If vardecl -> we get a list of VarDecl
        # If funcdecl -> we get a FuncDecl
        # Need to check if it's a list or not
        declList = []
        for decl in ctx.decls():
            x = self.visit(decl)
            declList.extend(x) if isinstance(x, list) else declList.append(x)
        return Program(declList)
    
    # decls: vardecl | funcdecl;
    def visitDecls(self, ctx: MT22Parser.DeclsContext):
        return self.visitChildren(ctx)

    # vardecl: vardeclAssign | vardeclNoAssign;
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        return self.visitChildren(ctx)

    # vardeclAssign: vardeclAssignment SEMI;
    def visitVardeclAssign(self, ctx: MT22Parser.VardeclAssignContext):
        vardeclAssignment = self.visit(ctx.vardeclAssignment())
        #  Input: a, b, c, d: integer = 1, 2, 3, 4
        #  -> vardeclAssignment: [a, [b, [c, [d, integer, 1], 2], 3], 4]

        #  Need to flatten vardeclAssignment list first
        def flatten(lst):
            result = []
            for element in lst:
                if isinstance(element, list):
                    result.extend(flatten(element))
                else:
                    result.append(element)
            return result
        
        flattenedVardeclAssignment = flatten(vardeclAssignment)
        #  flattenedVardeclAssignment: [a, b, c, d, integer, 1, 2, 3, 4]

        middle = len(flattenedVardeclAssignment) // 2

        identifierList = flattenedVardeclAssignment[:middle]
        typ = flattenedVardeclAssignment[middle]
        expressionList = flattenedVardeclAssignment[middle + 1:]

        return list(map(lambda identifier, expression: VarDecl(identifier, typ, expression), identifierList, expressionList))
    
    # vardeclAssignment: IDENTIFIER COMMA vardeclAssignment COMMA expression | vardeclAssignBaseCase;
    def visitVardeclAssignment(self, ctx: MT22Parser.VardeclAssignmentContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.vardeclAssignBaseCase())
        identifier = ctx.IDENTIFIER().getText()
        vardeclAssignment = self.visit(ctx.vardeclAssignment())
        expression = self.visit(ctx.expression())
        return [identifier, vardeclAssignment, expression]
    
    # vardeclAssignBaseCase: IDENTIFIER COLON (typ | arrayType) ASSIGN expression;
    def visitVardeclAssignBaseCase(self, ctx: MT22Parser.VardeclAssignBaseCaseContext):
        identifier = ctx.IDENTIFIER().getText()
        typ = self.visit(ctx.typ()) if ctx.typ() else self.visit(ctx.arrayType())
        expression = self.visit(ctx.expression())
        return [identifier, typ, expression]

    # vardeclNoAssign: identifierList COLON (typ | arrayType) SEMI;
    def visitVardeclNoAssign(self, ctx: MT22Parser.VardeclNoAssignContext):
        identifierList = self.visit(ctx.identifierList())
        typ = self.visit(ctx.typ()) if ctx.typ() else self.visit(ctx.arrayType())
        return [VarDecl(identifier, typ) for identifier in identifierList]

    # parameter: INHERIT? OUT? IDENTIFIER COLON (typ | arrayType);
    def visitParameter(self, ctx: MT22Parser.ParameterContext):
        inherit = True if ctx.INHERIT() else False
        out = True if ctx.OUT() else False
        identifier = ctx.IDENTIFIER().getText()
        typ = self.visit(ctx.typ()) if ctx.typ() else self.visit(ctx.arrayType())
        return ParamDecl(identifier, typ, out, inherit)
    
    # identifierList: IDENTIFIER COMMA identifierList | IDENTIFIER;
    def visitIdentifierList(self, ctx: MT22Parser.IdentifierListContext):
        if ctx.getChildCount() == 1:
            return [ctx.IDENTIFIER().getText()]
        identifier = ctx.IDENTIFIER().getText()
        identifierList = self.visit(ctx.identifierList())
        return [identifier] + identifierList
    
    # typ: BOOLEAN | INTEGER | FLOAT | STRING | AUTO;
    def visitTyp(self, ctx: MT22Parser.TypContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        return AutoType()
    
    # funcdecl: IDENTIFIER COLON FUNCTION returnType LP parameterList RP inheritanceSubpart? blockStmt;
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        identifier = ctx.IDENTIFIER().getText()
        returnType = self.visit(ctx.returnType())
        parameterList = self.visit(ctx.parameterList())
        inheritanceSubpart = self.visit(ctx.inheritanceSubpart()) if ctx.inheritanceSubpart() else None
        blockStmt = self.visit(ctx.blockStmt())
        return FuncDecl(identifier, returnType, parameterList, inheritanceSubpart, blockStmt)

    # returnType: BOOLEAN | INTEGER | FLOAT | STRING | VOID | AUTO | arrayType;
    def visitReturnType(self, ctx: MT22Parser.ReturnTypeContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.VOID():
            return VoidType()
        elif ctx.AUTO():
            return AutoType()
        return self.visit(ctx.arrayType())

    # parameterList: parameterPrime | ;
    def visitParameterList(self, ctx: MT22Parser.ParameterListContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.parameterPrime())

    # parameterPrime: parameter COMMA parameterPrime | parameter;
    def visitParameterPrime(self, ctx: MT22Parser.ParameterPrimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.parameter())]
        parameter = self.visit(ctx.parameter())
        parameterPrime = self.visit(ctx.parameterPrime())
        return [parameter] + parameterPrime

    # inheritanceSubpart: INHERIT IDENTIFIER;
    def visitInheritanceSubpart(self, ctx: MT22Parser.InheritanceSubpartContext):
        return ctx.IDENTIFIER().getText()
    
    # arrayType: ARRAY LSB dimensions RSB OF elementTyp;
    def visitArrayType(self, ctx: MT22Parser.ArrayTypeContext):
        dimensions = self.visit(ctx.dimensions())
        elementTyp = self.visit(ctx.elementTyp())
        return ArrayType(dimensions, elementTyp)

    # dimensions: INTEGERLIT COMMA dimensions | INTEGERLIT;
    def visitDimensions(self, ctx: MT22Parser.DimensionsContext):
        if ctx.getChildCount() == 1:
            return [ctx.INTEGERLIT().getText()]
        integerLit = ctx.INTEGERLIT().getText()
        dimensions = self.visit(ctx.dimensions())
        return [integerLit] + dimensions

    # elementTyp: BOOLEAN | INTEGER | FLOAT | STRING;
    def visitElementTyp(self, ctx: MT22Parser.ElementTypContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        return StringType()

    # arrayLit: LB expressionListNonnull RB;
    def visitArrayLit(self, ctx: MT22Parser.ArrayLitContext):
        expressionList = self.visit(ctx.expressionListNonnull())
        return ArrayLit(expressionList)
    
    # expression: expr1 DOUBLECOLON expr1 | expr1;
    def visitExpression(self, ctx: MT22Parser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1(0))
        op = ctx.DOUBLECOLON().getText()
        expression1 = self.visit(ctx.expr1(0))
        expression1_ = self.visit(ctx.expr1(1))
        return BinExpr(op, expression1, expression1_)
    
    # expr1: expr2 (EQUAL | NOTEQUAL | LESSTHAN | GREATERTHAN | LESSEQUAL | GREATEREQUAL) expr2 | expr2;
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
        op = ''
        if ctx.EQUAL():
            op = ctx.EQUAL().getText()
        elif ctx.NOTEQUAL():
            op = ctx.NOTEQUAL().getText()
        elif ctx.LESSTHAN():
            op = ctx.LESSTHAN().getText()
        elif ctx.GREATERTHAN():
            op = ctx.GREATERTHAN().getText()
        elif ctx.LESSEQUAL():
            op = ctx.LESSEQUAL().getText()
        elif ctx.GREATEREQUAL():
            op = ctx.GREATEREQUAL().getText()
        expression2 = self.visit(ctx.expr2(0))
        expression2_ = self.visit(ctx.expr2(1))
        return BinExpr(op, expression2, expression2_)
    
    # expr2: expr2 (AND | OR) expr3 | expr3;
    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        op = ctx.AND().getText() if ctx.AND() else ctx.OR().getText()
        expression2 = self.visit(ctx.expr2())
        expression3 = self.visit(ctx.expr3())
        return BinExpr(op, expression2, expression3)
    
    # expr3: expr3 (ADD | MINUS) expr4 | expr4;
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        op = ctx.ADD().getText() if ctx.ADD() else ctx.MINUS().getText()
        expression3 = self.visit(ctx.expr3())
        expression4 = self.visit(ctx.expr4())
        return BinExpr(op, expression3, expression4)
    
    # expr4: expr4 (MUL | DIV | MODUL) expr5 | expr5;
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        op = ctx.MUL().getText() if ctx.MUL() else (ctx.DIV().getText() if ctx.DIV() else ctx.MODUL().getText())
        expression4 = self.visit(ctx.expr4())
        expression5 = self.visit(ctx.expr5())
        return BinExpr(op, expression4, expression5)
    
    # expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        notOp = ctx.NOT().getText()
        expression = self.visit(ctx.expr5())
        return UnExpr(notOp, expression)
    
    # expr6: MINUS expr6 | expr7;
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        minus = ctx.MINUS().getText()
        expression = self.visit(ctx.expr6())
        return UnExpr(minus, expression)
    
    # expr7: IDENTIFIER LSB expressionListNonnull RSB | expr8;
    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr8())
        identifier = Id(ctx.IDENTIFIER().getText())
        expressionList = self.visit(ctx.expressionListNonnull())
        return ArrayCell(identifier, expressionList)

    # expr8: LP expression RP | factor;
    def visitExpr8(self, ctx: MT22Parser.Expr8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor())
        return self.visit(ctx.expression())

    # factor: INTEGERLIT | FLOATLIT | BOOLEANLIT | STRINGLIT | IDENTIFIER | functionCall | arrayLit;
    def visitFactor(self, ctx:MT22Parser.FactorContext):
        if ctx.INTEGERLIT():
            return IntegerLit(int(ctx.INTEGERLIT().getText()))
        if ctx.FLOATLIT():
            return FloatLit(float(ctx.FLOATLIT().getText()))
        if ctx.BOOLEANLIT():
            return BooleanLit(ctx.BOOLEANLIT().getText() == "true")
        if ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        if ctx.functionCall():
            return self.visit(ctx.functionCall())
        if ctx.arrayLit():
            return self.visit(ctx.arrayLit())
    
    # expressionListNullable: expressionPrime | ;
    def visitExpressionListNullable(self, ctx: MT22Parser.ExpressionListNullableContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.expressionPrime())
    
    # expressionPrime: expression COMMA expressionPrime | expression;
    def visitExpressionPrime(self, ctx: MT22Parser.ExpressionPrimeContext):
        if ctx.getChildCount() == 1:
            expression = self.visit(ctx.expression())
            return [expression]
        expression = self.visit(ctx.expression())
        expressionPrime = self.visit(ctx.expressionPrime())
        return [expression] + expressionPrime

    # expressionListNonnull: expression COMMA expressionListNonnull | expression;
    def visitExpressionListNonnull(self, ctx: MT22Parser.ExpressionListNonnullContext):
        if ctx.getChildCount() == 1:
            expression = self.visit(ctx.expression())
            return [expression]
        expression = self.visit(ctx.expression())
        expressionList = self.visit(ctx.expressionListNonnull())
        return [expression] + expressionList
    
    # statement: assignStmt | ifStmt | forStmt | whileStmt | doWhileStmt | breakStmt | continueStmt | returnStmt | callStmt | blockStmt;
    def visitStatement(self, ctx: MT22Parser.StatementContext):
        # if ctx.assignStmt():
        #     return self.visit(ctx.assignStmt())
        # elif ctx.ifStmt():
        #     return self.visit(ctx.ifStmt())
        # elif ctx.forStmt():
        #     return self.visit(ctx.forStmt())
        # elif ctx.whileStmt():
        #     return self.visit(ctx.whileStmt())
        # elif ctx.doWhileStmt():
        #     return self.visit(ctx.doWhileStmt())
        # elif ctx.breakStmt():
        #     return self.visit(ctx.breakStmt())
        # elif ctx.continueStmt():
        #     return self.visit(ctx.continueStmt())
        # elif ctx.returnStmt():
        #     return self.visit(ctx.returnStmt())
        # elif ctx.callStmt():
        #     return self.visit(ctx.callStmt())
        # elif ctx.blockStmt():
        #     return self.visit(ctx.blockStmt())
        return self.visitChildren(ctx)

    # assignStmt: lhs ASSIGN expression SEMI;
    def visitAssignStmt(self, ctx: MT22Parser.AssignStmtContext):
        lhs = self.visit(ctx.lhs())
        expression = self.visit(ctx.expression())
        return AssignStmt(lhs, expression)

    # lhs: IDENTIFIER | IDENTIFIER LSB expressionListNonnull RSB;
    def visitLhs(self, ctx: MT22Parser.LhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.IDENTIFIER().getText())
        identifier = Id(ctx.IDENTIFIER().getText())
        expressionList = self.visit(ctx.expressionListNonnull())
        return ArrayCell(identifier, expressionList)

    # ifStmt: IF expression statement (ELSE statement)?;
    def visitIfStmt(self, ctx: MT22Parser.IfStmtContext):
        expression = self.visit(ctx.expression())
        if ctx.ELSE():
            tstmt = self.visit(ctx.statement(0))
            fstmt = self.visit(ctx.statement(1))
            return IfStmt(expression, tstmt, fstmt)
        stmt = self.visit(ctx.statement(0))
        return IfStmt(expression, stmt)
    
    # forStmt: FOR LP initExpr COMMA conditionExpr COMMA updateExpr RP statement;
    def visitForStmt(self, ctx: MT22Parser.ForStmtContext):
        return ForStmt(
            self.visit(ctx.initExpr()),
            self.visit(ctx.conditionExpr()),
            self.visit(ctx.updateExpr()),
            self.visit(ctx.statement())
        )

    # initExpr: IDENTIFIER ASSIGN expression;    
    def visitInitExpr(self, ctx: MT22Parser.InitExprContext):
        return AssignStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expression()))

    # conditionExpr: expression (EQUAL | NOTEQUAL | LESSTHAN | GREATERTHAN | LESSEQUAL | GREATEREQUAL) expression;
    def visitConditionExpr(self, ctx: MT22Parser.ConditionExprContext):
        operator = ''
        if ctx.EQUAL():
            operator = ctx.EQUAL().getText()
        elif ctx.NOTEQUAL():
            operator = ctx.NOTEQUAL().getText()
        elif ctx.LESSTHAN():
            operator = ctx.LESSTHAN().getText()
        elif ctx.GREATERTHAN():
            operator = ctx.GREATERTHAN().getText()
        elif ctx.LESSEQUAL():
            operator = ctx.LESSEQUAL().getText()
        elif ctx.GREATEREQUAL():
            operator = ctx.GREATEREQUAL().getText()

        expression0 = self.visit(ctx.expression(0))
        expression1 = self.visit(ctx.expression(1))
        return BinExpr(operator, expression0, expression1)

    # updateExpr: expression;
    def visitUpdateExpr(self, ctx: MT22Parser.UpdateExprContext):
        return self.visit(ctx.expression())
    
    # whileStmt: WHILE expression statement;
    def visitWhileStmt(self, ctx: MT22Parser.WhileStmtContext):
        return WhileStmt(self.visit(ctx.expression()), self.visit(ctx.statement()))

    # doWhileStmt: DO blockStmt WHILE expression SEMI;
    def visitDoWhileStmt(self, ctx: MT22Parser.DoWhileStmtContext):
        return DoWhileStmt(self.visit(ctx.expression()), self.visit(ctx.blockStmt()))

    # breakStmt: BREAK SEMI;
    def visitBreakStmt(self, ctx: MT22Parser.BreakStmtContext):
        return BreakStmt()

    # continueStmt: CONTINUE SEMI;
    def visitContinueStmt(self, ctx: MT22Parser.ContinueStmtContext):
        return ContinueStmt()

    # returnStmt: RETURN (expression | ) SEMI;
    def visitReturnStmt(self, ctx: MT22Parser.ReturnStmtContext):
        return ReturnStmt(self.visit(ctx.expression()) if ctx.expression() else None)
    
    # callStmt: (specialFunc SEMI) | (IDENTIFIER LP expressionListNullable RP SEMI);
    def visitCallStmt(self, ctx: MT22Parser.CallStmtContext):
        if ctx.getChildCount() == 2:
            identifier, args = self.visit(ctx.specialFunc())
            if args is None:
                return CallStmt(identifier, [])
            if isinstance(args, list):
                return CallStmt(identifier, args)
            return CallStmt(identifier, [args])
        identifier = ctx.IDENTIFIER().getText()
        expressionList = self.visit(ctx.expressionListNullable())
        return CallStmt(identifier, expressionList)

    # blockStmt: LB blockBody RB | EMPTYBLOCK;
    def visitBlockStmt(self, ctx: MT22Parser.BlockStmtContext):
        if ctx.getChildCount() == 1:
            return BlockStmt([])
        # blockBody can be either a list of statements or a list of vardecls
        #  but in case of vardecls, it is already a list of vardecls, so now it is a list of lists (nested list)

        def flatten(lst):
            result = []
            for element in lst:
                if isinstance(element, list):
                    result.extend(flatten(element))
                else:
                    result.append(element)
            return result
        
        return BlockStmt(flatten(self.visit(ctx.blockBody())))
    
    # blockBody: stmtsOrVardecls | ;
    def visitBlockBody(self, ctx: MT22Parser.BlockBodyContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.stmtsOrVardecls())
    
    # stmtsOrVardecls: stmtOrVardecl stmtsOrVardecls | stmtOrVardecl;
    def visitStmtsOrVardecls(self, ctx: MT22Parser.StmtsOrVardeclsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.stmtOrVardecl())]
        return [self.visit(ctx.stmtOrVardecl())] + self.visit(ctx.stmtsOrVardecls())
    
    # stmtOrVardecl: statement | vardecl;
    def visitStmtOrVardecl(self, ctx: MT22Parser.StmtOrVardeclContext):
        return self.visitChildren(ctx)
    
    # statementList: statement statementList | statement;
    def visitStatementList(self, ctx: MT22Parser.StatementListContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.statement())]
        return [self.visit(ctx.statement())] + self.visit(ctx.statementList())
    
    # vardeclList: vardecl vardeclList | vardecl;
    def visitVardeclList(self, ctx: MT22Parser.VardeclListContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.vardecl())]
        return [self.visit(ctx.vardecl())] + self.visit(ctx.vardeclList())
    
    # functionCall: specialFunc | IDENTIFIER LP expressionListNullable RP;
    def visitFunctionCall(self, ctx: MT22Parser.FunctionCallContext):
        if ctx.getChildCount() == 1:
            identifier, args = self.visit(ctx.specialFunc())
            if args is None:
                return FuncCall(identifier, [])
            if isinstance(args, list):
                return FuncCall(identifier, args)
            return FuncCall(identifier, [args])
        identifier = ctx.IDENTIFIER().getText()
        expressionList = self.visit(ctx.expressionListNullable())
        return FuncCall(identifier, expressionList)
    
    # functionCallList: functionCall COMMA functionCallList | functionCall;
    def visitFunctionCallList(self, ctx: MT22Parser.FunctionCallListContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.functionCall())]
        return [self.visit(ctx.functionCall())] + self.visit(ctx.functionCallList())
    
    # specialFunc: readInteger | printInteger | readFloat | writeFloat | printBoolean | readString | printString | superFunction | preventDefault;
    def visitSpecialFunc(self, ctx: MT22Parser.SpecialFuncContext):
        return self.visitChildren(ctx)
    
    # readInteger: READINTEGER LP RP;
    def visitReadInteger(self, ctx: MT22Parser.ReadIntegerContext):
        return ctx.READINTEGER().getText(), None
    
    # printInteger: PRINTINTEGER LP expression RP;
    def visitPrintInteger(self, ctx: MT22Parser.PrintIntegerContext):
        return ctx.PRINTINTEGER().getText(), self.visit(ctx.expression())
    
    # readFloat: READFLOAT LP RP;
    def visitReadFloat(self, ctx: MT22Parser.ReadFloatContext):
        return ctx.READFLOAT().getText(), None
    
    # writeFloat: WRITEFLOAT LP expression RP;
    def visitWriteFloat(self, ctx: MT22Parser.WriteFloatContext):
        return ctx.WRITEFLOAT().getText(), self.visit(ctx.expression())
    
    # readBoolean: READBOOLEAN LP RP;
    def visitReadBoolean(self, ctx: MT22Parser.ReadBooleanContext):
        return ctx.READBOOLEAN().getText(), None
    
    # printBoolean: PRINTBOOLEAN LP expression RP;
    def visitPrintBoolean(self, ctx: MT22Parser.PrintBooleanContext):
        return ctx.PRINTBOOLEAN().getText(), self.visit(ctx.expression())
    
    # readString: READSTRING LP RP;
    def visitReadString(self, ctx: MT22Parser.ReadStringContext):
        return ctx.READSTRING().getText(), None
    
    # printString: PRINTSTRING LP expression RP;
    def visitPrintString(self, ctx: MT22Parser.PrintStringContext):
        return ctx.PRINTSTRING().getText(), self.visit(ctx.expression())

    # superFunction: SUPER LP expressionListNonnull RP;
    def visitSuperFunction(self, ctx: MT22Parser.SuperFunctionContext):
        return ctx.SUPER().getText(), self.visit(ctx.expressionListNonnull())
    
    # preventDefault: PREVENTDEFAULT LP RP;
    def visitPreventDefault(self,ctx:MT22Parser.PreventDefaultContext):
        return ctx.PREVENTDEFAULT().getText(), None