class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o: object):
        o = []
        for decl in ctx.decl:
            self.visit(decl, o)

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        o += [ctx.name]

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        o += [ctx.name]

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name)
        o += [ctx.name]

        env = []
        for decl in ctx.param:
            self.visit(decl, env)
        for decl in ctx.body:
            self.visit(decl, env)

    def visitIntType(self, ctx: IntType, o: object): pass

    def visitFloatType(self, ctx: FloatType, o: object): pass

    def visitIntLit(self, ctx: IntLit, o: object): pass
