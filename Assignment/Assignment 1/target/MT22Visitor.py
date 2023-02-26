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


    # Visit a parse tree produced by MT22Parser#var_decl.
    def visitVar_decl(self, ctx:MT22Parser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifier_list.
    def visitIdentifier_list(self, ctx:MT22Parser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_value_list.
    def visitAssign_value_list(self, ctx:MT22Parser.Assign_value_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_func_call.
    def visitAssign_func_call(self, ctx:MT22Parser.Assign_func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#value_list.
    def visitValue_list(self, ctx:MT22Parser.Value_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#value_list_type_int.
    def visitValue_list_type_int(self, ctx:MT22Parser.Value_list_type_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#value_list_type_float.
    def visitValue_list_type_float(self, ctx:MT22Parser.Value_list_type_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#value_list_type_string.
    def visitValue_list_type_string(self, ctx:MT22Parser.Value_list_type_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#value_list_type_boolean.
    def visitValue_list_type_boolean(self, ctx:MT22Parser.Value_list_type_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_array.
    def visitAssign_array(self, ctx:MT22Parser.Assign_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_decl.
    def visitFunc_decl(self, ctx:MT22Parser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_type.
    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter_list.
    def visitParameter_list(self, ctx:MT22Parser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter_prime.
    def visitParameter_prime(self, ctx:MT22Parser.Parameter_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#inheritance_subpart.
    def visitInheritance_subpart(self, ctx:MT22Parser.Inheritance_subpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensions.
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
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


    # Visit a parse tree produced by MT22Parser#expression_list.
    def visitExpression_list(self, ctx:MT22Parser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_prime.
    def visitExpression_prime(self, ctx:MT22Parser.Expression_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalar_variable.
    def visitScalar_variable(self, ctx:MT22Parser.Scalar_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_expr.
    def visitInit_expr(self, ctx:MT22Parser.Init_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#condition_expr.
    def visitCondition_expr(self, ctx:MT22Parser.Condition_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#update_expr.
    def visitUpdate_expr(self, ctx:MT22Parser.Update_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmts_or_var_decls.
    def visitStmts_or_var_decls(self, ctx:MT22Parser.Stmts_or_var_declsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt_or_var_decl.
    def visitStmt_or_var_decl(self, ctx:MT22Parser.Stmt_or_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement_list.
    def visitStatement_list(self, ctx:MT22Parser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_decl_list.
    def visitVar_decl_list(self, ctx:MT22Parser.Var_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_call.
    def visitFunction_call(self, ctx:MT22Parser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_list.
    def visitExp_list(self, ctx:MT22Parser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_prime.
    def visitExp_prime(self, ctx:MT22Parser.Exp_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_call_list.
    def visitFunction_call_list(self, ctx:MT22Parser.Function_call_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#special_func.
    def visitSpecial_func(self, ctx:MT22Parser.Special_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_integer.
    def visitRead_integer(self, ctx:MT22Parser.Read_integerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#print_integer.
    def visitPrint_integer(self, ctx:MT22Parser.Print_integerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_float.
    def visitRead_float(self, ctx:MT22Parser.Read_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#write_float.
    def visitWrite_float(self, ctx:MT22Parser.Write_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_boolean.
    def visitRead_boolean(self, ctx:MT22Parser.Read_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#print_boolean.
    def visitPrint_boolean(self, ctx:MT22Parser.Print_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_string.
    def visitRead_string(self, ctx:MT22Parser.Read_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#print_string.
    def visitPrint_string(self, ctx:MT22Parser.Print_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#super_.
    def visitSuper_(self, ctx:MT22Parser.Super_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#prevent_default.
    def visitPrevent_default(self, ctx:MT22Parser.Prevent_defaultContext):
        return self.visitChildren(ctx)



del MT22Parser