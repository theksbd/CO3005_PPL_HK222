# Extend the contents of classes Exp, BinExp, UnExp, IntLit, FloatLit such that they can response to printPrefix() message to return the string corresponding to the expression in prefix format. Note that, unary operator +/- is printed as +./-. in prefix format and there is a space after each operator or operand. For example, when receiving message printPrefix(), the object expressing the expression -4 + 3 * 2 will return the string "+ -. 4 * 3 2 "
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


x1 = IntLit(1)
x2 = FloatLit(2.0)
x3 = BinExp(x1, '+', x1)
x4 = UnExp('-', x1)
x5 = BinExp(x4, '+', BinExp(IntLit(4), '*', IntLit(2)))

print(x5.printPrefix())
