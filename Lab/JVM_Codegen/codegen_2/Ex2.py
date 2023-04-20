def visitId(self, ctx, o):
    sym = list(filter(lambda x: x.name == ctx.name, o.sym))[0]
    if o.isLeft:
        if type(sym.value) is Index:
            code = self.emit.emitWRITEVAR(
                ctx.name, sym.mtype, sym.value.value, o.frame)
        else:
            code = self.emit.emitPUTSTATIC(
                sym.value.value + "." + sym.name, sym.mtype, o.frame)
    else:
        if type(sym.value) is Index:
            code = self.emit.emitREADVAR(
                ctx.name, sym.mtype, sym.value.value, o.frame)
        else:
            code = self.emit.emitGETSTATIC(
                sym.value.value + "." + sym.name, sym.mtype, o.frame)
    return code, sym.mtype
