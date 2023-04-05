class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o: object):
        o = []
        for decl in ctx.decl:
            o + self.visit(decl, o)
        return o

    def visitClassDecl(self, ctx: ClassDecl, o: object):
        env = []
        for decl in ctx.mem:
            env = self.visit(decl, env)
        return o + [(ctx.name, ctx.parent, env)]

    def visitVarDecl(self, ctx: VarDecl, o: object):
        for decl in o:
            if decl.name == ctx.name:
                raise RedeclaredField(ctx.name)
        return o + [ctx]

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        for decl in o:
            if decl.name == ctx.name:
                raise RedeclaredMethod(ctx.name)
        return o + [ctx]

    def visitIntType(self, ctx: IntType, o: object): pass

    def visitFloatType(self, ctx: FloatType, o: object): pass

    def visitClassType(self, ctx: ClassType, o: object): pass

    def visitIntLit(self, ctx: IntLit, o: object): pass

    def visitId(self, ctx: Id, o: object): pass

    def visitFieldAccess(self, ctx: FieldAccess, o: object): pass
