def visitAssign(self, ctx, o):
    rc, rt = self.visit(ctx.rhs, Access(o.frame, o.sym, False))
    self.emit.printout(rc)
    lc, lt = self.visit(ctx.lhs, Access(o.frame, o.sym, True))
    self.emit.printout(lc)
