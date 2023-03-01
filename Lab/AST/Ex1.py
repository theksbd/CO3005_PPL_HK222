class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx: MPParser.ProgramContext):
        return self.visit(ctx.vardecls()) + 1

    def visitVardecls(self, ctx: MPParser.VardeclsContext):
        vardecl = self.visit(ctx.vardecl())
        vardecltail = self.visit(ctx.vardecltail())
        return vardecl + vardecltail

    def visitVardecltail(self, ctx: MPParser.VardecltailContext):
        if ctx.getChildCount() == 0:
            return 0
        else:
            vardecl = self.visit(ctx.vardecl())
            vardecltail = self.visit(ctx.vardecltail())
            return vardecl + vardecltail

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        typ = self.visit(ctx.mptype())
        ids = self.visit(ctx.ids())
        return typ + ids + 1

    def visitMptype(self, ctx: MPParser.MptypeContext):
        return 1

    def visitIds(self, ctx: MPParser.IdsContext):
        if ctx.getChildCount() == 1:
            return 1
        else:
            return 2 + self.visit(ctx.ids())
