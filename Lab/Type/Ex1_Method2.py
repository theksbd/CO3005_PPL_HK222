class Type(ABC): pass
class IntType(Type): pass
class FloatType(Type): pass
class BoolType(Type): pass

class StaticCheck(Visitor):

    def visitBinOp(self, ctx:BinOp, o):
        e1t = self.visit(ctx.e1, o)
        e2t = self.visit(ctx.e2, o)

        if ctx.op in ['+', '-', '*']:
            if type(e1t) is BoolType or type(e2t) is BoolType:
                raise TypeMismatchInExpression(ctx)
            if type(e1t) is FloatType or type(e2t) is FloatType:
                return FloatType()
            return IntType()
        elif ctx.op in ['/']:
            if type(e1t) is BoolType or type(e2t) is BoolType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        elif ctx.op in ['!', '&&', '||']:
            if type(e2t) is not BoolType or type(e2t) is not BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        elif ctx.op in ['>', '<', '==', '!=']:
            if e1t != e2t:
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitUnOp(self, ctx:UnOp, o):
        et = self.visit(ctx.e, o)
        if ctx.op in ['-']:
            if type(et) is BoolType:
                raise TypeMismatchInExpression(ctx)
            return et
        elif ctx.op in ['!']:
            if type(et) is not BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitIntLit(self, ctx:IntLit, o): return IntType()

    def visitFloatLit(self, ctx, o): return FloatType()

    def visitBoolLit(self, ctx,o): return BoolType()