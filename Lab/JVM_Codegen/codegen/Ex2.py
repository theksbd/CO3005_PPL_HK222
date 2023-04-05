def visitFloatLiteral(self, ctx, o):
    code = self.emit.emitPUSHFCONST(str(ctx.value), o.frame)
    return code, FloatType()
