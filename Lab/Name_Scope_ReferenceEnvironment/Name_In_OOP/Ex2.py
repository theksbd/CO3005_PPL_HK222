class GetENV(Visitor):

    def visitProgram(self, ctx: Program, o: object):
        o = []
        for decl in ctx.decl:
            o += [self.visit(decl, o)]
        return o

    def visitClassDecl(self, ctx: ClassDecl, o: object):
        env = []
        for mem in ctx.mem:
            env = self.visit(mem, env)
        return (ctx.name, ctx.parent, env)

    def visitVarDecl(self, ctx: VarDecl, o: object):
        for decl in o:
            if decl.name == ctx.name:
                raise RedeclaredField(ctx.name)
        o += [ctx]
        return o

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        for decl in o:
            if decl.name == ctx.name:
                raise RedeclaredMethod(ctx.name)
        o += [ctx]
        return o


class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o: object):
        o = GetENV().visit(ctx)
        for class_decl in ctx.decl:
            self.visit(class_decl, o)

    def visitClassDecl(self, ctx: ClassDecl, o: object):
        for mem in ctx.mem:
            if type(mem) is FuncDecl:
                self.visit(mem, o)

    def visitVarDecl(self, ctx: VarDecl, o: object):
        for decl in o:
            if decl.name == ctx.name:
                raise RedeclaredField(ctx.name)
        return o + [ctx]

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        local = ctx.param + ctx.body[0]
        for expr in body[1]:
            self.visit(expr, (local, o))

    def visitIntType(self, ctx: IntType, o: object): pass

    def visitFloatType(self, ctx: FloatType, o: object): pass

    def visitClassType(self, ctx: ClassType, o: object): pass

    def visitIntLit(self, ctx: IntLit, o: object): pass

    def visitId(self, ctx: Id, o: object):
        for decl in o:
            if decl.name == ctx.name:
                return decl.typ
        raise UndeclaredIdentifier(ctx.name)

    def visitFieldAccess(self, ctx: FieldAccess, o: object):
        typ = self.visit(ctx.exp, o) # m.a -> ClassType(x)
        if type(typ) is ClassType:
            # Look up in o[1] if there is a class with name x and field a in x
            type_info = None
            found = False
            for class_decl in o[1]:
                if typ.name == class_decl[0]:
                    type_info = class_decl
                    found = True
                    break
            # Not exist, raise UndeclaredClass
            if not found:
                raise UndeclaredClass(typ.name)
            for mem in type_info[2]:
                if mem.name == ctx.field:
                    return mem.typ
            raise UndeclaredField(ctx.field)