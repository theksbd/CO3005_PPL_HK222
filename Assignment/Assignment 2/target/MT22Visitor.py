# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decls.
    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardeclAssign.
    def visitVardeclAssign(self, ctx:MT22Parser.VardeclAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardeclAssignment.
    def visitVardeclAssignment(self, ctx:MT22Parser.VardeclAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardeclAssignBaseCase.
    def visitVardeclAssignBaseCase(self, ctx:MT22Parser.VardeclAssignBaseCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardeclNoAssign.
    def visitVardeclNoAssign(self, ctx:MT22Parser.VardeclNoAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifierList.
    def visitIdentifierList(self, ctx:MT22Parser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnType.
    def visitReturnType(self, ctx:MT22Parser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameterList.
    def visitParameterList(self, ctx:MT22Parser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameterPrime.
    def visitParameterPrime(self, ctx:MT22Parser.ParameterPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#inheritanceSubpart.
    def visitInheritanceSubpart(self, ctx:MT22Parser.InheritanceSubpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraytype.
    def visitArraytype(self, ctx:MT22Parser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensions.
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayLit.
    def visitArrayLit(self, ctx:MT22Parser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr8.
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#factor.
    def visitFactor(self, ctx:MT22Parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expressionListNullable.
    def visitExpressionListNullable(self, ctx:MT22Parser.ExpressionListNullableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expressionPrime.
    def visitExpressionPrime(self, ctx:MT22Parser.ExpressionPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expressionListNonnull.
    def visitExpressionListNonnull(self, ctx:MT22Parser.ExpressionListNonnullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignStmt.
    def visitAssignStmt(self, ctx:MT22Parser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifStmt.
    def visitIfStmt(self, ctx:MT22Parser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forStmt.
    def visitForStmt(self, ctx:MT22Parser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#initExpr.
    def visitInitExpr(self, ctx:MT22Parser.InitExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#conditionExpr.
    def visitConditionExpr(self, ctx:MT22Parser.ConditionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#updateExpr.
    def visitUpdateExpr(self, ctx:MT22Parser.UpdateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whileStmt.
    def visitWhileStmt(self, ctx:MT22Parser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#doWhileStmt.
    def visitDoWhileStmt(self, ctx:MT22Parser.DoWhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakStmt.
    def visitBreakStmt(self, ctx:MT22Parser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continueStmt.
    def visitContinueStmt(self, ctx:MT22Parser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnStmt.
    def visitReturnStmt(self, ctx:MT22Parser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callStmt.
    def visitCallStmt(self, ctx:MT22Parser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockStmt.
    def visitBlockStmt(self, ctx:MT22Parser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmtsOrVardecls.
    def visitStmtsOrVardecls(self, ctx:MT22Parser.StmtsOrVardeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmtOrVardecl.
    def visitStmtOrVardecl(self, ctx:MT22Parser.StmtOrVardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statementList.
    def visitStatementList(self, ctx:MT22Parser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardeclList.
    def visitVardeclList(self, ctx:MT22Parser.VardeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionCall.
    def visitFunctionCall(self, ctx:MT22Parser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionCallList.
    def visitFunctionCallList(self, ctx:MT22Parser.FunctionCallListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#specialFunc.
    def visitSpecialFunc(self, ctx:MT22Parser.SpecialFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readInteger.
    def visitReadInteger(self, ctx:MT22Parser.ReadIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printInteger.
    def visitPrintInteger(self, ctx:MT22Parser.PrintIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readFloat.
    def visitReadFloat(self, ctx:MT22Parser.ReadFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#writeFloat.
    def visitWriteFloat(self, ctx:MT22Parser.WriteFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readBoolean.
    def visitReadBoolean(self, ctx:MT22Parser.ReadBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printBoolean.
    def visitPrintBoolean(self, ctx:MT22Parser.PrintBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readString.
    def visitReadString(self, ctx:MT22Parser.ReadStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printString.
    def visitPrintString(self, ctx:MT22Parser.PrintStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#superFunction.
    def visitSuperFunction(self, ctx:MT22Parser.SuperFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#preventDefault.
    def visitPreventDefault(self, ctx:MT22Parser.PreventDefaultContext):
        return self.visitChildren(ctx)



del MT22Parser