def visitBinExpr(self, ctx, o):
    e1c, e1t = self.visit(ctx.e1, o)
    e2c, e2t = self.visit(ctx.e2, o)
    if ctx.op in ['+', '-']:
        code = self.emit.emitADDOP(ctx.op, IntType(), o.frame)
        typ = IntType()
    elif ctx.op in ['*', '/']:
        code = self.emit.emitMULOP(ctx.op, IntType(), o.frame)
        typ = IntType()
    elif ctx.op in ['+.', '-.']:
        code = self.emit.emitADDOP(ctx.op, FloatType(), o.frame)
        typ = FloatType()
    elif ctx.op in ['*.', '/.']:
        code = self.emit.emitMULOP(ctx.op, FloatType(), o.frame)
        typ = FloatType()

    return e1c + e2c + code, typ
