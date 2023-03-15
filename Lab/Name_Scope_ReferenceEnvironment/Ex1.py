class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o: object):
        o = []
        for decl in ctx.decl:
            self.visit(decl, o)

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        o += [ctx.name]

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        o += [ctx.name]

    def visitIntType(self, ctx: IntType, o: object): pass

    def visitFloatType(self, ctx: FloatType, o: object): pass

    def visitIntLit(self, ctx: IntLit, o: object): pass
