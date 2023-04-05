class StaticCheck(Visitor):

    def visitBinOp(self, ctx:BinOp, o):
        e1t = self.visit(ctx.e1, o)
        e2t = self.visit(ctx.e2, o)

        if ctx.op in ['+', '-', '*']:
            if e1t == 3 or e2t == 3:
                raise TypeMismatchInExpression(ctx)
            if e1t == 2 or e2t == 2:
                return 2
            return 1
        elif ctx.op in ['/']:
            if e1t == 3 or e2t == 3:
                raise TypeMismatchInExpression(ctx)
            return 2
        elif ctx.op in ['!', '&&', '||']:
            if e1t != 3 or e2t != 3:
                raise TypeMismatchInExpression(ctx)
            return 3
        elif ctx.op in ['>', '<', '==', '!=']:
            if e1t != e2t:
                raise TypeMismatchInExpression(ctx)
            return 3

    def visitUnOp(self, ctx:UnOp, o):
        et = self.visit(ctx.e, o)
        if ctx.op in ['-']:
            if et == 3:
                raise TypeMismatchInExpression(ctx)
            return et
        elif ctx.op in ['!']:
            if et != 3:
                raise TypeMismatchInExpression(ctx)
            return 3

    def visitIntLit(self, ctx:IntLit, o): return 1 

    def visitFloatLit(self, ctx, o): return 2

    def visitBoolLit(self, ctx,o): return 3