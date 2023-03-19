import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_305(self):
        input = """x, y, z: integer = 1, 2, foo(3);
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, FuncCall(foo, [IntegerLit(3)]))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_306(self):
        input = """main: function void () {
            printInteger(4);
            a, b: integer = 1, 2;
            foo(a, b);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4)), VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), CallStmt(foo, Id(a), Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_307(self):
        input = """main: function void () {
            a, b: integer = 1, 2;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_308(self):
        input = """main: function void () {
            printInteger(4);
            readInteger();
            writeFloat(a);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4)), CallStmt(readInteger, ), CallStmt(writeFloat, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
    
    def test_309(self):
        input = """main: function void () {
            a: integer;
            a = 5;
            foo(a);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), IntegerLit(5)), CallStmt(foo, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_310(self):
        input = """main: function void () {
            super(foo(a, b));
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(super, FuncCall(foo, [Id(a), Id(b)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))   
        
    def test_311(self):
        input = """main: function void () {
            for(i = 0, i < 10, i + 1) {
                a = 5;
                foo(a);
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(5)), CallStmt(foo, Id(a))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_311(self):
        input = """main: function void () {
            while(i < 10) {
                a: integer = 5;
                for(i = 0, i < foo(a, 1), i + 1) {
                    b: integer = foo(a, 1);
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([VarDecl(a, IntegerType, IntegerLit(5)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(foo, [Id(a), IntegerLit(1)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(b, IntegerType, FuncCall(foo, [Id(a), IntegerLit(1)]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_312(self):
        input = """main: function void () {
            x: float = 0.0;
            y: float = 1.0;
            while (x < 1.0) {
                if (x < 0.5) {
                    x = x + 0.1;
                    y = y * 2;
                } else {
                    x = x + 0.2;
                    y = y + 1;
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(0.0)), VarDecl(y, FloatType, FloatLit(1.0)), WhileStmt(BinExpr(<, Id(x), FloatLit(1.0)), BlockStmt([IfStmt(BinExpr(<, Id(x), FloatLit(0.5)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), FloatLit(0.1))), AssignStmt(Id(y), BinExpr(*, Id(y), IntegerLit(2)))]), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), FloatLit(0.2))), AssignStmt(Id(y), BinExpr(+, Id(y), IntegerLit(1)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_313(self):
        input = """main: function void () {
            i: integer;
            arr: array[10] of integer;
            for(i = 0, i < 10, i + 1) {
                arr[i] = i * i;
            }
            for(i = 9, i >= 0, i - 1) {
                printInteger(arr[i]);
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(arr, ArrayType([10], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(Id(arr), [Id(i)]), BinExpr(*, Id(i), Id(i)))])), ForStmt(AssignStmt(Id(i), IntegerLit(9)), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, ArrayCell(Id(arr), [Id(i)]))]))]))
])"""

        self.assertTrue(TestAST.test(input, expect, 313))

    def test_314(self):
        input = """main: function void () {
            if (a == b) {
                c = a + b;
            } else {
                c = a - b;
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(b)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(a), Id(b)))]), BlockStmt([AssignStmt(Id(c), BinExpr(-, Id(a), Id(b)))]))]))
])"""

        self.assertTrue(TestAST.test(input, expect, 314))

    def test_315(self):
        input = """main: function void () {
            a: boolean = true;
            do {
                i: integer;
                var: array[10] of integer;
                for(i = 0, i < 10, i + 1) {
                    var[i] = i * i;
                }
                while(i > 0) {
                    printInteger(var[i]);
                    i = i - 1;
                }
                if (i == 0) {
                    a = false;
                }
            } while (a == true);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, BooleanLit(True)), DoWhileStmt(BinExpr(==, Id(a), BooleanLit(True)), BlockStmt([VarDecl(i, IntegerType), VarDecl(var, ArrayType([10], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(Id(var), [Id(i)]), BinExpr(*, Id(i), Id(i)))])), WhileStmt(BinExpr(>, Id(i), IntegerLit(0)), BlockStmt([CallStmt(printInteger, ArrayCell(Id(var), [Id(i)])), AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))])), IfStmt(BinExpr(==, Id(i), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), BooleanLit(False))]))]))]))
])"""

        self.assertTrue(TestAST.test(input, expect, 315))

    def test_316(self):
        input = """main: function void () {
            while (a == true) {
                continue;
            }
            while (a == true) {
                break;
            }
            while (a == true) {
                return;
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(a), BooleanLit(True)), BlockStmt([ContinueStmt()])), WhileStmt(BinExpr(==, Id(a), BooleanLit(True)), BlockStmt([BreakStmt()])), WhileStmt(BinExpr(==, Id(a), BooleanLit(True)), BlockStmt([ReturnStmt()]))]))
])"""

        self.assertTrue(TestAST.test(input, expect, 316))