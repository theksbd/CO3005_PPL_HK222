def visitIf(self, ctx, o):
    # Code gen for expr
    ec, et = self.visit(ctx.expr, Access(o.frame, o.sym, False))
    self.emit.printout(ec)

    # Jump to FLABEL if False
    FLABEL = o.frame.getNewLabel()
    code = self.emit.emitIFFALSE(FLABEL, o.frame)
    self.emit.printout(code)

    # Code gen for true statement
    self.visit(ctx.tstmt, o)

    # Jump to ELABEL to finish if else statement
    ELABEL = o.frame.getNewLabel()
    code = self.emit.emitGOTO(ELABEL, o.frame)
    self.emit.printout(code)

    if ctx.estmt:
        # Place FLABEL here for upcoming jump
        code = self.emit.emitLABEL(FLABEL, o.frame)
        self.emit.printout(code)

        # Code gen for else statement
        self.visit(ctx.estmt, o)

    # Place ELABEL here for upcoming jump
    code = self.emit.emitLABEL(ELABEL, o.frame)
    self.emit.printout(code)
