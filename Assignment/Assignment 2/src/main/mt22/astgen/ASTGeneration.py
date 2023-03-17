from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
# from functools import reduce

# # Functional Programming
# def flatten(lst):
#     return list(reduce(lambda total, curr: total + curr, lst, []))

class ASTGeneration(MT22Visitor):
    # program: decls+ EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program([])
    
    # decls: vardecl | funcdecl;

    # vardecl: vardeclAssign | vardeclNoAssign;

    # vardeclAssign: IDENTIFIER COMMA vardeclAssignment COMMA expression SEMI | vardeclAssignBaseCase SEMI;
    
    # vardeclAssignment: IDENTIFIER COMMA vardeclAssignment COMMA expression | vardeclAssignBaseCase;
    
    # vardeclAssignBaseCase: IDENTIFIER COLON (typ | arraytype) ASSIGN expression;

    # vardeclNoAssign: identifierList COLON (typ | arraytype) SEMI;

    # parameter: INHERIT? OUT? IDENTIFIER COLON (typ | arraytype);
    
    # identifierList: IDENTIFIER COMMA identifierList | IDENTIFIER;
    
    # typ: BOOLEAN | INTEGER | FLOAT | STRING | AUTO;
    
    # funcdecl: IDENTIFIER COLON FUNCTION returnType LP parameterList RP inheritanceSubpart? statement;

    # returnType: BOOLEAN | INTEGER | FLOAT | STRING | VOID | AUTO | arraytype;

    # parameterList: parameterPrime | ;

    # parameterPrime: parameter COMMA parameterPrime | parameter;

    # inheritanceSubpart: INHERIT IDENTIFIER;
    
    # arraytype: ARRAY LSB dimensions RSB OF typ;

    # dimensions: INTEGERLIT COMMA dimensions | INTEGERLIT;

    # arrayLit: LB expressionListNonnull RB;
    
    # expression: expr1 DOUBLECOLON expr1 | expr1;
    
    # expr1: expr2 (EQUAL | NOTEQUAL | LESSTHAN | GREATERTHAN | LESSEQUAL | GREATEREQUAL) expr2 | expr2;
    
    # expr2: expr2 (AND | OR) expr3 | expr3;
    
    # expr3: expr3 (ADD | MINUS) expr4 | expr4;
    
    # expr4: expr4 (MUL | DIV | MODUL) expr5 | expr5;
    
    # expr5: NOT expr5 | expr6;
    
    # expr6: MINUS expr6 | expr7;
    
    # expr7: IDENTIFIER LSB expressionListNonnull RSB | expr8;

    # expr8: LP expression RP | factor;

    # factor: INTEGERLIT | FLOATLIT | BOOLEANLIT | STRINGLIT | IDENTIFIER | functionCall | arrayLit;
    
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
        identifier = ctx.IDENTIFIER().getText()
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
        operator = '=='
        if ctx.NOTEQUAL():
            operator = '!='
        elif ctx.LESSTHAN():
            operator = '<'
        elif ctx.GREATERTHAN():
            operator = '>'
        elif ctx.LESSEQUAL():
            operator = '<='
        elif ctx.GREATEREQUAL():
            operator = '>='

        return BinExpr(operator, self.visit(ctx.expression(0)), self.visit(ctx.expression(1)))

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
    
    # callStmt: (functionCall | specialFunc) SEMI;
    def visitCallStmt(self, ctx: MT22Parser.CallStmtContext):
        if ctx.specialFunc():
            identifier, args = self.visit(ctx.specialFunc())
            if args is None:
                return CallStmt(identifier, [])
            if isinstance(args, list):
                return CallStmt(identifier, args)
            return CallStmt(identifier, [args])
        functionCall = self.visit(ctx.functionCall())
        return CallStmt(functionCall.name, functionCall.args)
        
    
    # blockStmt: LB stmtsOrVardecls RB | '{}';
    def visitBlockStmt(self, ctx: MT22Parser.BlockStmtContext):
        if ctx.getChildCount() == 1:
            return BlockStmt([])
        return BlockStmt(self.visit(ctx.stmtsOrVardecls()))
    
    # stmtsOrVardecls: stmtOrVardecl stmtsOrVardecls | ;
    def visitStmtsOrVardecls(self, ctx: MT22Parser.StmtsOrVardeclsContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.stmtOrVardecl())] + self.visit(ctx.stmtsOrVardecls())
    
    # stmtOrVardecl: statementList | vardeclList;
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
    
    # functionCall: IDENTIFIER LP expressionListNullable RP | specialFunc;
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
        return ctx.SUPERFUNCTION().getText(), self.visit(ctx.expressionListNonnull())
    
    # preventDefault: PREVENTDEFAULT LP RP;
    def visitPreventDefault(self,ctx:MT22Parser.PreventDefaultContext):
        return ctx.PREVENTDEFAULT().getText(), None