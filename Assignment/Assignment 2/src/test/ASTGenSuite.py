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

    def test_317(self):
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

        self.assertTrue(TestAST.test(input, expect, 317))

    def test_318(self):
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

        self.assertTrue(TestAST.test(input, expect, 318))

    def test_319(self):
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

        self.assertTrue(TestAST.test(input, expect, 319))

    def test_320(self):
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

        self.assertTrue(TestAST.test(input, expect, 320))

    def test_321(self):
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

        self.assertTrue(TestAST.test(input, expect, 321))

    def test_322(self):
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

        self.assertTrue(TestAST.test(input, expect, 322))

    def test_323(self):
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

        self.assertTrue(TestAST.test(input, expect, 323))

    def test_324(self):
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

        self.assertTrue(TestAST.test(input, expect, 324))

    def test_325(self):
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

        self.assertTrue(TestAST.test(input, expect, 325))

    def test_326(self):
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

        self.assertTrue(TestAST.test(input, expect, 326))

    def test_327(self):
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

        self.assertTrue(TestAST.test(input, expect, 327))

    def test_328(self):
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

        self.assertTrue(TestAST.test(input, expect, 328))

    def test_329(self):
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

        self.assertTrue(TestAST.test(input, expect, 329))
    def test_330(self):
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

        self.assertTrue(TestAST.test(input, expect, 330))
    def test_331(self):
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

        self.assertTrue(TestAST.test(input, expect, 331))

    def test_332(self):
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

        self.assertTrue(TestAST.test(input, expect, 332))

    def test_333(self):
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

        self.assertTrue(TestAST.test(input, expect, 333))

    def test_334(self):
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

        self.assertTrue(TestAST.test(input, expect, 334))

    def test_335(self):
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

        self.assertTrue(TestAST.test(input, expect, 335))

    def test_336(self):
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

        self.assertTrue(TestAST.test(input, expect, 336))

    def test_337(self):
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

        self.assertTrue(TestAST.test(input, expect, 337))

    def test_338(self):
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

        self.assertTrue(TestAST.test(input, expect, 338))

    def test_339(self):
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

        self.assertTrue(TestAST.test(input, expect, 339))

    def test_340(self):
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

        self.assertTrue(TestAST.test(input, expect, 340))

    def test_341(self):
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

        self.assertTrue(TestAST.test(input, expect, 340))

    def test_341(self):
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

        self.assertTrue(TestAST.test(input, expect, 341))

    def test_342(self):
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

        self.assertTrue(TestAST.test(input, expect, 342))

    def test_343(self):
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

        self.assertTrue(TestAST.test(input, expect, 343))

    def test_344(self):
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

        self.assertTrue(TestAST.test(input, expect, 344))

    def test_345(self):
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

        self.assertTrue(TestAST.test(input, expect, 345))

    def test_346(self):
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

        self.assertTrue(TestAST.test(input, expect, 346))

    def test_347(self):
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

        self.assertTrue(TestAST.test(input, expect, 347))

    def test_348(self):
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

        self.assertTrue(TestAST.test(input, expect, 348))

    def test_349(self):
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

        self.assertTrue(TestAST.test(input, expect, 349))

    def test_350(self):
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

        self.assertTrue(TestAST.test(input, expect, 350))

    def test_351(self):
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

        self.assertTrue(TestAST.test(input, expect, 351))

    def test_352(self):
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

        self.assertTrue(TestAST.test(input, expect, 352))

    def test_353(self):
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

        self.assertTrue(TestAST.test(input, expect, 353))

    def test_354(self):
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

        self.assertTrue(TestAST.test(input, expect, 354))

    def test_355(self):
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

        self.assertTrue(TestAST.test(input, expect, 355))

    def test_356(self):
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

        self.assertTrue(TestAST.test(input, expect, 356))

    def test_357(self):
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

        self.assertTrue(TestAST.test(input, expect, 357))

    def test_358(self):
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

        self.assertTrue(TestAST.test(input, expect, 358))

    def test_359(self):
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

        self.assertTrue(TestAST.test(input, expect, 359))

    def test_360(self):
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

        self.assertTrue(TestAST.test(input, expect, 360))

    def test_361(self):
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

        self.assertTrue(TestAST.test(input, expect, 361))

    def test_362(self):
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

        self.assertTrue(TestAST.test(input, expect, 362))

    def test_363(self):
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

        self.assertTrue(TestAST.test(input, expect, 363))

    def test_364(self):
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

        self.assertTrue(TestAST.test(input, expect, 364))

    def test_365(self):
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

        self.assertTrue(TestAST.test(input, expect, 365))

    def test_366(self):
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

        self.assertTrue(TestAST.test(input, expect, 366))

    def test_367(self):
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

        self.assertTrue(TestAST.test(input, expect, 367))

    def test_368(self):
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

        self.assertTrue(TestAST.test(input, expect, 368))

    def test_369(self):
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

        self.assertTrue(TestAST.test(input, expect, 369))

    def test_370(self):
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

        self.assertTrue(TestAST.test(input, expect, 370))

    def test_371(self):
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

        self.assertTrue(TestAST.test(input, expect, 371))

    def test_372(self):
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

        self.assertTrue(TestAST.test(input, expect, 372))

    def test_373(self):
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

        self.assertTrue(TestAST.test(input, expect, 373))

    def test_374(self):
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

        self.assertTrue(TestAST.test(input, expect, 374))

    def test_375(self):
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

        self.assertTrue(TestAST.test(input, expect, 375))

    def test_376(self):
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

        self.assertTrue(TestAST.test(input, expect, 376))

    def test_377(self):
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

        self.assertTrue(TestAST.test(input, expect, 377))

    def test_378(self):
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

        self.assertTrue(TestAST.test(input, expect, 378))

    def test_379(self):
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

        self.assertTrue(TestAST.test(input, expect, 379))

    def test_380(self):
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

        self.assertTrue(TestAST.test(input, expect, 380))

    def test_381(self):
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

        self.assertTrue(TestAST.test(input, expect, 381))

    def test_382(self):
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

        self.assertTrue(TestAST.test(input, expect, 382))

    def test_383(self):
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

        self.assertTrue(TestAST.test(input, expect, 383))

    def test_384(self):
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

        self.assertTrue(TestAST.test(input, expect, 384))

    def test_385(self):
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

        self.assertTrue(TestAST.test(input, expect, 385))

    def test_386(self):
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

        self.assertTrue(TestAST.test(input, expect, 386))

    def test_387(self):
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

        self.assertTrue(TestAST.test(input, expect, 387))

    def test_388(self):
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

        self.assertTrue(TestAST.test(input, expect, 388))

    def test_389(self):
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

        self.assertTrue(TestAST.test(input, expect, 389))

    def test_390(self):
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

        self.assertTrue(TestAST.test(input, expect, 390))

    def test_391(self):
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

        self.assertTrue(TestAST.test(input, expect, 391))

    def test_392(self):
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

        self.assertTrue(TestAST.test(input, expect, 392))

    def test_393(self):
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

        self.assertTrue(TestAST.test(input, expect, 393))

    def test_394(self):
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

        self.assertTrue(TestAST.test(input, expect, 394))

    def test_395(self):
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

        self.assertTrue(TestAST.test(input, expect, 395))

    def test_396(self):
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

        self.assertTrue(TestAST.test(input, expect, 396))

    def test_397(self):
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

        self.assertTrue(TestAST.test(input, expect, 397))

    def test_398(self):
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

        self.assertTrue(TestAST.test(input, expect, 398))

    def test_399(self):
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

        self.assertTrue(TestAST.test(input, expect, 399))