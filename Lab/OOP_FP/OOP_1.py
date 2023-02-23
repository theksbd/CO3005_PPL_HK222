# To express an arithmetic expression, there are 5 following classes:

# Exp: general arithmetic expression

# BinExp: an arithmetic expression that contains one binary operators (+,-,*,/) and two operands. To construct a BinExp object, you must pass parameters: first operand, operator, second operand, respectively.

# UnExp: an arithmetic expression that contains one unary operator (+,-) and one operand. To construct a UnExp object, you must pass the operator first.

# IntLit: an arithmetic expression that contains one integer number

# FloatLit: an arithmetic expression that contains one floating point number

# Define these classes in Python (their parents, attributes, methods) such that their objects can response to eval() message by returning the value of the expression. For example, let object x express the arithmetic expression 3 + 4 * 2.0, x.eval() must return 11.0

# In this exercise, we use:

# x1 = IntLit(1)

# x2 = FloatLit(2.0)

# x3 = BinExp(x1,"+",x1)

# x4 = UnExp("-",x1)

# x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))

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


class UnExp(Exp):
    def __init__(self, op, o):
        self.op = op
        self.o = o

    def eval(self):
        e = self.o.eval()
        if self.op == '-':
            return -e
        return e


class IntLit(Exp):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return self.val


class FloatLit(Exp):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return self.val


x1 = IntLit(1)
x2 = FloatLit(2.0)
x3 = BinExp(x1, '+', x1)
x4 = UnExp('-', x1)
x5 = BinExp(x4, '+', BinExp(IntLit(4), '*', 2))

print(x5.eval())
