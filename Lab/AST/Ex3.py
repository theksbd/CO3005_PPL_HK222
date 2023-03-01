class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx: MPParser.ProgramContext):
        return Program(self.visit(ctx.vardecls()))

    def visitVardecls(self, ctx: MPParser.VardeclsContext):
        vardecl = self.visit(ctx.vardecl())  # List of Vardecl
        vardecltail = self.visit(ctx.vardecltail())  # List of Vardecl
        return vardecl + vardecltail

    def visitVardecltail(self, ctx: MPParser.VardecltailContext):
        if ctx.getChildCount() == 2:
            vardecl = self.visit(ctx.vardecl())  # List of Vardecl
            vardecltail = self.visit(ctx.vardecltail())  # List of Vardecl
            return vardecl + vardecltail
        return []

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        typ = self.visit(ctx.mptype())
        ids = self.visit(ctx.ids())
        return list(map(lambda x: VarDecl(x, typ), ids))

    def visitMptype(self, ctx: MPParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    def visitIds(self, ctx: MPParser.IdsContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        ids = self.visit(ctx.ids())  # list of ID
        x = Id(ctx.ID().getText())
        return [x] + ids
