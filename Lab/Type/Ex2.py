class Type(ABC):
    pass


class IntType(Type):
    pass


class FloatType(Type):
    pass


class BoolType(Type):
    pass


class StaticCheck(Visitor):
    def visitProgram(self, ctx: Program, o):
        o = []
        for decl in ctx.decl:
            self.visit(decl, o)
        self.visit(ctx.exp, o)

    def visitVarDecl(self, ctx: VarDecl, o):
        if ctx.name in o:
            raise UndeclaredIdentifier(ctx.name)
        o += [ctx]

    def visitIntType(self, ctx: IntType, o): pass

    def visitFloatType(self, ctx: FloatType, o): pass

    def visitBoolType(self, ctx: BoolType, o): pass

    def visitBinOp(self, ctx: BinOp, o):
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
            if not type(e2t) is BoolType or not type(e2t) is BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        elif ctx.op in ['>', '<', '==', '!=']:
            if e1t != e2t:
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitUnOp(self, ctx: UnOp, o):
        et = self.visit(ctx.e, o)
        if ctx.op in ['-']:
            if type(et) is BoolType:
                raise TypeMismatchInExpression(ctx)
            return et
        elif ctx.op in ['!']:
            if not type(et) is BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitIntLit(self, ctx: IntLit, o): return IntType()

    def visitFloatLit(self, ctx, o): return FloatType()

    def visitBoolLit(self, ctx, o): return BoolType()

    def visitId(self, ctx, o):
        for decl in o:
            if decl.name == ctx.name:
                return decl.typ
        raise UndeclaredIdentifier(ctx.name)
