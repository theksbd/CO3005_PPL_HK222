# As in the previous question, when a task is added into expression classes, new methods are added into these classes. Please change the way these classes are implemented in such a way that these classes do not change their contents when new tasks are added into these classes:

# - Define class Eval to calculate the value of an expression.

# - Define class PrintPrefix to return the string corresponding to the expression in prefix format.

# All arithmetic classes in previous questions have just been defined as follows:

# class Exp(ABC):pass
# class BinExp(Exp):
#     def __init__(self,o1,op,o2):
#         self.left = o1
#         self.op = op
#         self.right = o2
# class UnExp(Exp):
#     def __init__(self,op,o1):
#         self.op = op
#         self.operand = o1
# class IntLit(Exp):
#     def __init__(self,v):
#         self.value = v
# class FloatLit(Exp):
#     def __init__(self,v):
#         self.value = v
# Let v1, v2 be an object of Eval, PrintPrefix and x be an object expressing an expression, v1.visit(x1) will return the value of the expression x and v2.visit(x) will return the expression in prefix format.

# For testing, given some following objects:

# x1 = IntLit(1)
# x2 = FloatLit(2.0)
# x3 = BinExp(x1,"+",x1)
# x4 = UnExp("-",x1)
# x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))
# Hint: use type(), isinstance() to find out the type of x when implementing this exercise.
class Exp:
    pass


class BinExp(Exp):
    def __init__(self, o1, op, o2):
        self.o1 = o1
        self.o2 = o2
        self.op = op

    def eval(self):
        e1 = self.o1.eval()
        e2 = self.o2.eval()
        if self.op == '+':
            return e1 + e2
        elif self.op == '-':
            return e1 - e2
        elif self.op == '*':
            return e1 * e2
        return e1 / e2

    def printPrefix(self):
        e1 = self.o1.printPrefix()
        e2 = self.o2.printPrefix()
        return self.op + ' ' + e1 + ' ' + e2


class UnExp(Exp):
    def __init__(self, op, o):
        self.op = op
        self.o = o

    def eval(self):
        e = self.o.eval()
        if self.op == '-':
            return -e
        return e

    def printPrefix(self):
        e = self.o.printPrefix()
        return self.op + '. ' + e


class IntLit(Exp):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return self.val

    def printPrefix(self):
        return str(self.val)


class FloatLit(Exp):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return self.val

    def printPrefix(self):
        return str(self.val)


class Eval:
    def visit(self, ctx: Exp):
        if type(ctx) is IntLit or type(ctx) is FloatLit:
            return ctx.val
        elif type(ctx) is BinExp:
            o1 = self.visit(ctx.o1)
            o2 = self.visit(ctx.o2)
            if ctx.op == '+':
                return o1 + o2
            elif ctx.op == '-':
                return o1 - o2
            elif ctx.op == '*':
                return o1 * o2
            return o1 / o2
        elif type(ctx) is UnExp:
            o = self.visit(ctx.o)
            return -o if ctx.op == '-' else o


class PrintPrefix:
    def visit(self, ctx: Exp):
        if type(ctx) is IntLit or type(ctx) is FloatLit:
            return str(ctx.val)
        elif type(ctx) is BinExp:
            o1 = self.visit(ctx.o1)
            o2 = self.visit(ctx.o2)
            return ctx.op + ' ' + o1 + ' ' + o2
        elif type(ctx) is UnExp:
            o = self.visit(ctx.o)
            return ctx.op + '. ' + o


class PrintPostfix:
    def visit(self, ctx: Exp):
        if type(ctx) is IntLit or type(ctx) is FloatLit:
            return str(ctx.value)
        elif type(ctx) is BinExp:
            o1 = self.visit(ctx.o1)
            o2 = self.visit(ctx.o2)
            return o1 + ' ' + o2 + ' ' + ctx.op
        elif type(ctx) is UnExp:
            o = self.visit(ctx.o)
            return o + ' ' + ctx.op + '.'
