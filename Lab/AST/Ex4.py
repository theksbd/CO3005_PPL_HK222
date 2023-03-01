from functools import *


class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):
        return Program(reduce(lambda prev, curr: prev + self.visit(curr), ctx.vardecl(), []))

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        mptype = self.visit(ctx.mptype())
        ids = self.visit(ctx.ids())
        res = list(map(lambda x: VarDecl(x, mptype), ids))
        return res

    def visitMptype(self, ctx: MPParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    def visitIds(self, ctx: MPParser.IdsContext):
        res = list(map(lambda x: Id(x.getText()), ctx.ID()))
        return res
