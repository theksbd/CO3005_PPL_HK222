# Code gen for while else statement in python
def visitWhileElse(self, ctx, o):
    o.enterLoop()

    # Get BREAKLABEL and CONTINUELABEL
    BREAKLABEL = o.frame.getBreakLabel()
    CONTINUELABEL = o.frame.getContinueLabel()

    # Place CONTINUELABEL here for repeating while statement
    code = self.emit.emitLABEL(CONTINUELABEL, o.frame)
    self.emit.printout(code)

    # Code gen for expr
    er, et = self.visit(ctx.expr, Access(o.frame, o.sym, False))
    self.emit.printout(er)

    # Jump to BREAKLABEL if False
    code = self.emit.emitIFFALSE(BREAKLABEL, o.frame)
    self.emit.printout(code)

    # Code gen for stmt
    self.visit(ctx.stmt, o)

    # Jump to CONTINUELABEL to repeat while statement
    code = self.emit.emitGOTO(CONTINUELABEL, o.frame)
    self.emit.printout(code)

    # Place BREAKLABEL here for upcoming jump
    code = self.emit.emitLABEL(BREAKLABEL, o.frame)
    self.emit.printout(code)

    # Code gen for else statement
    self.visit(ctx.elseStmt, o)

    o.exitLoop()
