def visitBinExpr(self, ctx, o):
    e1c, e1t = self.visit(ctx.e1, o)
    e2c, e2t = self.visit(ctx.e2, o)

    if type(e1t) is type(e2t):
        typ = e1t
    elif type(e1t) is IntType and type(e2t) is FloatType:
        e1c += self.emit.emitI2F(o.frame)
        typ = e2t
    else:
        e2c += self.emit.emitI2F(o.frame)
        typ = e1t

    if ctx.op in ['+', '-']:
        op = self.emit.emitADDOP(ctx.op, typ, o.frame)
    elif ctx.op in ['*']:
        op = self.emit.emitMULOP(ctx.op, typ, o.frame)
    elif ctx.op in ['/']:
        if type(e1t) is IntType and type(e2t) is IntType:
            e1c += self.emit.emitI2F(o.frame)
            e2c += self.emit.emitI2F(o.frame)
            typ = FloatType()
        op = self.emit.emitMULOP(ctx.op, typ, o.frame)
    else:
        op = self.emit.emitREOP(ctx.op, typ, o.frame)

    return e1c + e2c + op, typ
