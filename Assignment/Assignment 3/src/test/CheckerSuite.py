import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_0(self):
        input = """f : integer = "abc";"""
        expect = "Type mismatch in Variable Declaration: VarDecl(f, IntegerType, StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_1(self):
        input = """
        x: integer = 3;
        y: auto;
        main: function void(){}
    """

        expect = "Invalid Variable: y"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_2(self):
        input = """
        x: integer = 3;
        y: auto = x;
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_3(self):
        input = """
        x: integer = 3;
        y: float = 3.100;
        z: auto = y + x;
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_4(self):
        input = """
        x: boolean;
        y: auto = 3.100;
        z: auto = y + x;
        main: function void(){}
    """

        expect = "Type mismatch in expression: BinExpr(+, Id(y), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_5(self):
        input = """
        x: string = "Hello";
        y: auto = x == "World";
        main: function void(){}
    """

        expect = "Type mismatch in expression: BinExpr(==, Id(x), StringLit(World))"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_6(self):
        input = """
        isTrue: function boolean(x: boolean) {
            return x;
        }
        x: boolean = false;
        y: auto = isTrue(x);
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_7(self):
        input = """
            main: function void() {
                do {
                    x: integer = "hoang";
                }
                while(x > 1);
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, StringLit(hoang))"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_8(self):
        input = """
        x: integer = 100;
        y: auto = x != 5;
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_9(self):
        input = """
            main: function void() {
                a: integer = 1;
                a: integer = 2;
            }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_10(self):
        input = """
        x: integer = -100;
        y: integer = -x;
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_11(self):
        input = """
        y: integer =  true || (true && false);
        main: function void(){}
    """

        expect = "Type mismatch in expression: VarDecl(y, IntegerType, BinExpr(||, BooleanLit(True), BinExpr(&&, BooleanLit(True), BooleanLit(False))))"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_12(self):
        input = """
        x: integer = -100_999;
        y: float = x;
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_13(self):
        input = """
            main: function void(){
                a: auto = 22;
                b: integer = V + 1.0;
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, BinExpr(+, Id(a), FloatLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_14(self):
        input = """
        a : array [2] of integer;
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_15(self):
        input = """
        a : array [2] of integer = {-1.0, 3.0};
        main: function void(){}
    """

        expect = "Type mismatch in statement: VarDecl(a, ArrayType([2], IntegerType), ArrayLit([UnExpr(-, FloatLit(1.0)), FloatLit(3.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 415))

        def test_16(self):
            input = """
        a : array [2] of integer = {-1, 3};
        main: function void(){}
    """

            expect = "[]"
            self.assertTrue(TestChecker.test(input, expect, 416))

    def test_17(self):
        input = """
        a: array [2] of integer = {1, 2};
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_18(self):
        input = """
        b: array [2, 3] of integer = {{}, {}};
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_19(self):
        input = """
        c: array [2, 3] of integer = {{1}, {1, 2, 3}};
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_20(self):
        input = """
        d: array [2, 3, 5] of integer = {{{1, 3, 4}, {5, 6}, {}}, {{1}, {2}, {1}}};
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_21(self):
        input = """
        e: array [2, 3] of integer = {{1.0}, {1, 2, 3}};
        main: function void(){}
    """

        expect = "Type mismatch in statement: VarDecl(e, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([FloatLit(1.0)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_22(self):
        input = """
        f: array [2, 3] of integer = {{1, 1}, {1.0, 2, 3}};
        main: function void(){}
    """

        expect = "Illegal array literal: ArrayLit([FloatLit(1.0), IntegerLit(2), IntegerLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_23(self):
        input = """
            x, y, z: integer = 1, 2, 3;
            a: array [3, 2] of integer = {{x + z}, {y, z}};
            main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_24(self):
        input = """
        // c : integer = 1;
        c : array [1] of integer = {1};
        b : integer = 10;
        // a : array [2, 2] of integer = {{3, c[0.1 + 3]}, {b, 199}};
        a : array [2, 2] of integer = {{3, c[1 + 3, 3 + 4]}, {b, 199}};
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_25(self):
        input = """
        a3 : array [2, 2] of boolean = {{3.3, 3.5}, {123.1, 199.10}};
        main: function void(){}
    """

        expect = "Type mismatch in statement: VarDecl(a3, ArrayType([2, 2], BooleanType), ArrayLit([ArrayLit([FloatLit(3.3), FloatLit(3.5)]), ArrayLit([FloatLit(123.1), FloatLit(199.1)])]))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_26(self):
        input = """
        a2 : array [2, 2] of integer = {{3.3, 3.5}, {123.1, 199.10}};
        main: function void(){}
    """

        expect = "Type mismatch in statement: VarDecl(a2, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([FloatLit(3.3), FloatLit(3.5)]), ArrayLit([FloatLit(123.1), FloatLit(199.1)])]))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_27(self):
        input = """
        a : array [2, 2] of float = {{3, 3}, {123, 199}};
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_28(self):
        input = """
        a : array [2, 2] of float = {{3, 3}, {123, 199, 123}, {123}};
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_29(self):
        input = r"""
        a: array [2, 2] of float = {false};
        main: function void(){}"""

        expect = "Type mismatch in statement: VarDecl(a, ArrayType([2, 2], FloatType), ArrayLit([BooleanLit(False)]))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_30(self):
        input = """main: function void(){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_31(self):
        input = r"""fact: function integer (n : integer) {}"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_32(self):
        input = """
        fact : function integer (n : integer) {}
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_33(self):
        input = """
        fact : function integer (n : integer, n : float) {}
        main: function void(){}
    """

        expect = "Redeclared Parameter: n"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_34(self):
        input = """
        fact : function integer (n : integer) {}
        fact : function float () {}
        main: function void(){}
    """

        expect = "Redeclared Function: fact"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_35(self):
        input = """
        x: float = 3.0;
        fact : function integer (n : integer) {
            x: integer = 3;
            x: boolean = false;
        }
        main: function void(){}
    """

        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_36(self):
        input = """
        x: float = 3.0;
        fact : function integer (n : integer) {
            x: integer = 3;
            y: float = 3.100;
            z: auto = y + x;

            c : array [1] of integer = {1};
            b : integer = 10;
            a : array [2, 2] of integer = {{3, c[1 + 3]}, {b, 199}};
        }
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_37(self):
        input = """
        x: float = 3.0;
        fact : function integer (n : integer) {
            if (n == 10) {}
            else {
            }
        }
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_38(self):
        input = """
        x: float = 3.0;
        fact : function integer (n : integer) {
            if (n + 10) {}
            else {
            }
        }
        main: function void(){}
    """

        expect = "Type mismatch in statement: IfStmt(BinExpr(+, Id(n), IntegerLit(10)), BlockStmt([]), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_39(self):
        input = """
        x: float = 3.0;
        a : array [2] of integer;
        fact : function integer (n : integer) {
            n = n + 10;
            a[0] = 1239;
        }
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_40(self):
        input = """
        x: float = 3.0;
        a : array [2] of integer;
        foo: function auto(){}
        fact : function integer (n : integer) {
            b: float;
            n = b + 1;
        }
        main: function void(){}
    """

        expect = "Type mismatch in statement: AssignStmt(Id(n), BinExpr(+, Id(b), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_41(self):
        input = """
        a : array [2] of integer;
        // foo: function auto(){}
        foo: function auto(x: integer){}
        // foo1: function auto(y: float){}
        fact : function integer (n : integer) {
            foo: float = 3.0;
            b: integer;
            // n1: float = foo(foo(1)); // foo(int)
            // n1: float = foo(1) + foo1(foo(100)); // foo: float foo1: float
            // n1: float = foo(1) + 1; // foo: int
            //n1: float = !foo(1) + 1; // TypeMisMatch
            n1: boolean = -foo(1) == true;
            // n1: float = -foo(1) + 1; // foo: float
        }
        main: function void(){}
    """

        expect = "Type mismatch in expression: UnExpr(-, FuncCall(foo, [IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_42(self):
        input = """
        foo: function auto(x: integer){}
        foo1: function auto(x: float){}
        fact : function integer (n : integer) {
            // b: integer = 99;
            // b = foo(100); // foo: int
            // foo(19) = b // don't have this

            a : array [2] of integer;
            a[1] = (foo1(foo(1900)) + 1);
            // a[0] = 19;
            // a[2] = 10.1231;
            // a[2] = false;

            // foo: float = 3.0;
            // foo = foo(100);

            // n1: float = foo(foo(1)); // foo(int)
            // n1: float = foo(1) + foo1(foo(100)); // foo: float foo1: float
            // n1: float = foo(1) + 1; // foo: int
            //n1: float = !foo(1) + 1; // TypeMisMatch
            // n1: boolean = -foo(1) == true;
            // n1: float = -foo(1) + 1; // foo: float
        }
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_43(self):
        input = """
            main1: function void(b: string) {
                a: string = "hoang";
                b: integer = a[1];
            }
            main: function void(){}
        """
        expect = "Type mismatch in expression: ArrayCell(a, [IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_44(self):
        input = """
        // foo: function auto(){}
        // foo1: function auto(y: boolean){}
        foo2: function boolean(i: integer){}
        /*fact : function integer () {
            // a : array [2] of integer;
            // i: float = 3;
        }*/
        main: function void(){

            // i: integer = 3;
            // for (i = 123, i > 8, i + 1){}

            for (i = 123, i > 8, foo2(1)){}
            // for (i = 123, i > 8, i + 1.4){}
        }
    """

        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(123)), BinExpr(>, Id(i), IntegerLit(8)), FuncCall(foo2, [IntegerLit(1)]), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_45(self):
        input = """
        foo2: function auto(i: integer){
            return 1;
        }

        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_46(self):
        input = """
            foo: function string() {return "hoang";}
            main: function void(){
                v: string = foo();
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_47(self):
        input = """

        x: integer;
        foo1: function integer(inherit x: float){}

        foo2: function float(inherit y: float) inherit foo1{
            super(10);
            z: float = 10.1;
            return 1;
        }
        foo3: function float(out z: float) inherit foo2{
            preventDefault();
            y: integer = 10;
            printInteger(1);
            return 1.123;
        }

        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_48(self):
        input = """

        x: integer;
        foo1: function integer(inherit x: float){}
        foo2: function float(inherit y: float){
            super(10);
            z: float = 10.1;
            return 1;
        }
        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "Invalid statement in function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_49(self):
        input = """

        x: integer;
        foo1: function integer(){}

        foo2: function float(inherit y: float) inherit foo1{
            // super();
            // preventDefault();
            z: float = 10.1;
            return 1;
        }

        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_50(self):
        input = """
        x: integer;
        foo1: function integer(y: integer){}

        foo2: function float(inherit y: float) inherit foo1{
            super(10, 1.0);
            z: float = 10.1;
            return 1;
        }

        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "Invalid statement in function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_51(self):
        input = """

        x: integer;
        foo1: function integer(inherit y: integer){}

        foo2: function float(inherit y: float) inherit foo1{
            super(10);
            z: float = 10.1;
            return 1;
        }

        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "Redeclared Parameter: y"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_52(self):
        input = """

            x: integer;
            foo1: function integer(inherit y: integer){}

            foo2: function float(inherit z: float) inherit foo1{
                super(10);
                y: float = 10.1;
                return 1;
            }

            main: function void(){
                x: integer = readInteger();
            }
        """

        expect = "Redeclared Variable: y"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_53(self):
        input = """

        x: integer;
        foo1: function integer(inherit y: integer){}

        foo2: function float(inherit z: float) inherit foo1{
            preventDefault();
            y: float = 10.1;
            return 1;
        }

        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_54(self):
        input = """

        x: integer;
        foo1: function integer(inherit y: integer){}

        foo2: function float(inherit z: float) inherit foo1{
            preventDefault(1, 2, 3);
            y: float = 10.1;
            return 1;
        }

        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "Invalid statement in function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_55(self):
        input = """

        x: integer;
        foo1: function auto(){}

        foo2: function float(inherit z: float) inherit foo1{
            super(1);
            y: float = 10.1;
            return 1;
        }

        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "Invalid statement in function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_56(self):
        input = """
            x: integer = 65;
            fact: function integer (n: integer) {
                if (n == 0) return 1;
                else return n * fact(n - 1);
            }
            inc: function void(out n: integer, delta: integer) {
                n = n + delta;
            }
            main: function void() {
                delta: integer = fact(3);
                inc(x, delta);
                printInteger(x);
            }
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_57(self):
        input = """
            main: function void(){
                a: float = v;
                v: integer = 3;
            }
        """
        expect = "Undeclared Identifier: v"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_58(self):
        input = """
        main: function void() {
            x: array[4, 10, 10] of integer = {1, 2, 3, 4};
            for (i = 1, i < 100, i+1) {
                if (i % 2 == 0) {
                    while(true){
                        x[i, 0, 1] = i;
                        break;
                    }
                    do{
                        continue;
                    }while(true);
                    continue;
                    break;
                } else {
                    x[0, i] = i + 1;
                }
                break;
            }
            break;
        }
    """

        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_59(self):
        input = """
        main: function void(args: integer, argv: array[100] of string) {}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_60(self):
        input = """
        isPalindrome: function boolean(strs: array[100] of string, strSize: integer) {
          for (i = 0, i < strSize / 2, i+1) {
            if (strs[i] != strs[strSize-i-1]) {
              return false;
            }
          }
          return true;
        }
        main: function void() {
            strs   : array [5] of string = {"hello", "world", "!!!", "", "test\n"};

            if(isPalindrome(strs, 5)) printString("Correct!!!");
            else printString("Wrong!!!");
        }
    """

        expect = "Type mismatch in expression: BinExpr(!=, ArrayCell(strs, [Id(i)]), ArrayCell(strs, [BinExpr(-, BinExpr(-, Id(strSize), Id(i)), IntegerLit(1))]))"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_61(self):
        input = """
        isPalindrome: function boolean(strs: array[100] of integer, strSize: integer) {
          for (i = 0, i < strSize / 2, i+1) {
            if (strs[i] != strs[strSize-i-1]) {
              return false;
            }
          }
          return true;
        }
        main: function void() {
            strs   : array [5] of integer = {1, 2, 3, 4 ,5};

            if(isPalindrome(strs, 5)) printString("Correct!!!");
            else printString("Wrong!!!");
        }
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_62(self):
        input = """
        isPalindrome: function boolean(strs: array[100] of integer, strSize: integer) {
          for (i = 0, i < strSize / 2, i+1) {
            if (strs[i] != strs[strSize-i-1]) {
              return false;
            }
          }
          return 10.123;
        }
        main: function void() {}
    """

        expect = "Type mismatch in statement: ReturnStmt(FloatLit(10.123))"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_63(self):
        input = """
        calculateSumIterative: function integer(n: integer) {
            sum: integer = 0;
            for (i = 1, i <= n, i+1) {
                sum = sum + i;
            }
            return sum;
        }
        calculateSumRecursive: function integer(n: integer) {
            if (n == 1) {
                return 1;
            }
            return n + calculateSumRecursive(n - 1);
        }
        main: function void() {}
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_64(self):
        input = """
        n : integer = 10;
        binarySearch: function integer(n: integer, x: integer, arr: array[100] of integer, pos: integer) {
            if (pos > n) {
                return -1;
            }
            mid: integer = (pos + n) / 2;
            if (arr[mid] == x) {
                return mid;
            }
            if (arr[mid] > x) {
                return binarySearch(mid - 1, x, arr, pos);
            }
            return binarySearch(n, x, arr, mid + 1);
        }
        main: function void() {
            arr: array [5] of integer = {1, 91, 0, -100, 100};
            printInteger(binarySearch(n, 10, arr, 0));
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_65(self):
        input = """
        findMax: function integer(n: integer, arr: array[100] of integer) {
            max: integer = arr[0];
            for (i = 1, i < n, i+1) {
                if (arr[i] > max) {
                    max = arr[i];
                }
            }
            return max;
        }
        main: function void() {
            arr: array [5] of integer = {1, 100, 1000, 0, -1000};
            printInteger(findMax(5, arr));
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_66(self):
        input = """
        findMin: function integer(n: integer, arr: array[100] of integer) {
            min: integer = arr[0];
            for (i = 1, i < n, i+1) {
                if (arr[i] < min) {
                    min = arr[i];
                }
            }
            return min;
        }
        main: function void() {
            arr: array [5] of integer = {1, 100, 1000, 0, -1000};
            printInteger(findMin(5, arr));
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_67(self):
        input = """
        binarySearch: function integer(arr: array[100] of integer, left: integer, right: integer, x: integer) {
          if (right >= left) {
            mid:integer = left + (right - left) / 2;
            if (arr[mid] == x)
              return mid;
            if (arr[mid] > x)
              return binarySearch(arr, left, mid - 1, x);
            return binarySearch(arr, mid + 1, right, x);
          }
          return -1;
        }
        main: function void() {
            arr   : array [5] of integer = {1, 91, 0, -100, 100};
            binarySearch(arr, 0, 4, 0);
        }
    """
        expect = "Type mismatch in statement: CallStmt(binarySearch, Id(arr), IntegerLit(0), IntegerLit(4), IntegerLit(0))"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_68(self):
        input = """
            main: function void() {
                j: boolean = false;
                for (i = 1, i < 100, i+1) {
                    j : integer = 0;
                    j = true;
                }
            }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(j), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_69(self):
        input = """
        main: function void() {
            for (i = 1, i < 100, i+1) {
                j : integer = 0;
                while (j < 200) {
                    if (i + j >= 20) {
                        break;
                    } else {
                     j = j + 1;
                    }
                }
            }
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_70(self):
        input = """
        x :  integer = 1;
        main: function void(out x: integer) {
            for (i = 1, i < 100, i+1) {
                for (j = 1, j < 200, j+1) {
                    if (i + j >= 2) {
                        foo(2, x + 1);
                    }
                }
            }
        }
    """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_71(self):
        input = """
        x :  integer = 1;
        foo: function auto(x: integer, y: float){}
        main: function void(out x: integer) {
            for (i = 1, i < 100, i+1) {
                for (j = 1, j < 200, j+1) {
                    if (i + j >= 2) {
                        foo(2, x + 1);
                    }
                }
            }
        }
    """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_72(self):
        input = """
        x :  integer = 1;
        foo: function auto(x: integer, y: float){}
        main: function void() {
            for (i = 1, i < 100, i+1) {
                for (j = 1, j < 200, j+1) {
                    if (i + j >= 2) {
                        foo(2, x + 1);
                    }
                }
            }
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_73(self):
        input = """
            checkElementsUniqueness: function auto (arr: array[100] of integer, n: integer) {
              if ((n > 1000) || (n < 0))
                return 1;
              for (i = 0, i < n - 1, i+1) {
                for (j = i + 1, j < n, j+1) {
                  if (arr[i] == arr[j])
                    return false;
                }
              }
              return true;
            }

            main: function void() {
                arr   : array [6] of integer = {1, 91, 0, -100, 100, 200};
                if (checkElementsUniqueness(arr, 6)) printString("Correct!");
                else printString("Wrong!");
            }
        """
        expect = "Type mismatch in statement: ReturnStmt(BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_74(self):
        input = """
        checkElementsUniqueness: function auto (arr: array[100] of integer, n: integer) {
          if ((n > 1000) || (n < 0))
            return true;
          for (i = 0, i < n - 1, i+1) {
            for (j = i + 1, j < n, j+1) {
              if (arr[i] == arr[j])
                return false;
            }
          }
          return true;
        }

        main: function void() {
            arr   : array [6] of integer = {1, 91, 0, -100, 100, 200};
            if (checkElementsUniqueness(arr, 6)) printString("Correct!");
            else printString("Wrong!");
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_75(self):
        input = """
        a : integer = 2;
        main: function void() {
            do{
                c = c + 1;
            }
            while (a==c);
        }
    """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_76(self):
        input = """
        foo: function string (a: string, b: float) {
            c : integer = 2;
            d: float = c + 1;
            f : array [5] of string;
            f[1] = d + 2.5;
            return f[1];
        }
        main: function void() {}
    """
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(f, [IntegerLit(1)]), BinExpr(+, Id(d), FloatLit(2.5)))"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_77(self):
        input = """
        foo: function string (a: string, b: float) {
            c : integer = 2;
            d: float = c + 1;
            f : array [5] of string;
            return f[1];
        }
        bar: function void (inherit out a: integer, inherit out b: string) inherit foo {
            super("Hello", 123);
            for (i = 1, i < 10, i + 1)
            {
                writeFloat(a);
            }
            if (a==2)
                return;
            else
                break;
        }
        main: function void() {}
    """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_78(self):
        input = """
        foo: function string (a: string, b: float) {
            c : integer = 2;
            d: float = c + 1;
            f : array [5] of string;
            return f[1];
        }
        bar: function void (inherit out a: integer, inherit out b: string) inherit foo {
            super("Hello", 123);
            for (i = 1, i < 10, i + 1)
            {
                writeFloat(a);
            }
            if (a==2)
                return;
            printString(foo("Hello", 1.2312));
        }
        main: function void() {}
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_79(self):
        input = """
        inc: function auto(a: integer, b: float)
        {
            a = -1 + -2 + -3;
            b = a + a / b + a;
            while (a!=0)
                a = a - 1;
            return a;
            do
            {
                a = b + 1;
            }
            while (a==true);
        }
        main: function void() {
        }
    """
        expect = "Type mismatch in statement: AssignStmt(Id(a), BinExpr(+, Id(b), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_80(self):
        input = """
        inc: function auto(a: integer, b: float)
        {
            a = -1 + -2 + -3;
            b = a + a / b + a;
            while (a!=0)
                a = a - 1;
            do
            {
                return b;
            }
            while (a==true);

            return a;
        }
        main: function void() {
        }
    """
        expect = "Type mismatch in expression: BinExpr(==, Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_81(self):
        input = """
        inc: function auto(a: integer, b: float)
        {
            a = -1 + -2 + -3;
            b = a + a / b + a;
            while (a!=0)
                a = a - 1;
            do
            {
                return b;
            }
            while (a==102);

            return a;
        }
        main: function void() {
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_82(self):
        input = """
        inc: function auto(a: integer, b: float)
        {
            a = -1 + -2 + -3;
            b = a + a / b + a;
            while (a!=0)
                a = a - 1;
            do
            {
                return a;
            }
            while (a==102);
            return b;
        }
        main: function void() {
        }
    """
        expect = "Type mismatch in statement: ReturnStmt(Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_83(self):
        input = """
        count: function boolean(n: integer)
        {
            i: integer;
            c: integer = 0;
            for (i=1,i<n,i+1)
                if (n%i==0)
                    c = c + 1;
            if (c == 2)
                return true;
            else
                return false;
        }
        main: function void() {
            n : integer;
            printString("Input n:");
            readInteger(n);
            if (count(n) == true)
                print("n is prime number");
            else
                print("n is not prime number");
        }
    """
        expect = "Type mismatch in statement: CallStmt(readInteger, Id(n))"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_84(self):
        input = """
        count: function boolean(n: integer)
        {
            i: integer;
            c: integer = 0;
            for (i=1,i<n,i+1)
                if (n%i==0)
                    c = c + 1;
            if (c == 2)
                return true;
            else
                return false;
        }
        main: function void() {
            n : integer;
            printString("Input n:");
            n = readInteger();
            if (count(n) == true)
                printString("n is prime number");
            else
                printString("n is not prime number");
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_85(self):
        input = """
        s : string;
        random: function string(n: integer)
        {
            i: integer;
            s = "";
            for (i = 0,i < n,i+1)
                s = s + randomChar();
            return s;
        }
        main: function void() {}
    """
        expect = "Undeclared Function: randomChar"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_86(self):
        input = """
        s : string;
        random: function string(n: integer)
        {
            i: integer;
            s = "";
            for (i = 0,i < n,i+1)
                s = s + readString();
            return s;
        }
        main: function void() {}
    """
        expect = "Type mismatch in expression: BinExpr(+, Id(s), FuncCall(readString, []))"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_87(self):
        input = """
        s : string;
        random: function string(n: integer)
        {
            i: integer;
            s = "";
            for (i = 0,i < n,i+1)
                s = s::readString();
            return s;
        }
        main: function void() {
            n : integer;
            printString("Input n:");
            n = readInteger();
            printString("The random string length n is "::random(n));
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_88(self):
        input = """
        a,b: array[10] of integer;
        swap: function void(out a: array[10] of integer, out b: array[10] of integer, n: integer)
        {
            if (n>10)
                return;
            else
            {
                temp,i : integer;
                for (i=0,i<n,i+1)
                {
                    temp=a[i];
                    a[i]=b[i];
                    b[i]=temp;
                }
            }
        }
        main: function void() {
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_89(self):
        input = """
            foo3: function auto(inherit i: integer, a: float) {}
            foo2: function auto(inherit b: float, a: float) inherit foo3 {
                super(true, 1.0);
            }
            main: function void(){
                foo2(foo1(1.0), 1);
            }
            """
        expect = "Invalid statement in function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_90(self):
        input = """
        foo3: function auto(inherit i: integer, a: float) {}
        foo2: function auto(inherit b: float, a: float) inherit foo3 {
            super(1, 1.0);
            c: integer = 1;
        }
        foo1: function integer(inherit c: float) inherit foo2 {
            super(1, 1.0);
            i: integer = 2;
            return 1;
        }

        main: function void(){
            foo2(foo1(1.0), 1);
        }
            """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_91(self):
        input = """
            foo2: function auto() {}
            foo1: function integer(inherit c: float) inherit foo2 {
                printInteger(super(1.0, 1.0));
                i: integer = 2;
                return 1;
            }

            main: function void(){
                foo2(foo1(1.0), 1);
            }
            """
        expect = "Type mismatch in expression: FuncCall(super, [FloatLit(1.0), FloatLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_92(self):
        input = """
            main: function void() {
                x: array[4, 10, 10] of integer;
                for (i = 1, i < 100, i+1) {
                    if (i % 2 == 0) {
                        x[i, 0, 1] = i;
                    } else {
                        x[0, i] = i + 1;
                    }
                    for(j = 1, j < 100, j+1) {
                        continue;
                    }
                    while(true) {continue;}
                    break;
                }
            }
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_93(self):
        input = """
            foo: function auto(out n: integer, delta: integer) {
                n = n + delta;
            }
            main: function void() {
                x: integer = 2;
                for (i = 1, i < 100, i+1) {
                    foo(x + 1, foo(i + 1, foo(x + 2, 1)));
                }
            }
            """
        expect = "Type mismatch in expression: FuncCall(foo, [BinExpr(+, Id(i), IntegerLit(1)), FuncCall(foo, [BinExpr(+, Id(x), IntegerLit(2)), IntegerLit(1)])])"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_94(self):
        input = """
            x: array[0, 100] of integer;
            inc: function auto(out n: integer, delta: integer) {
                n = n + delta;
            }
            main: function void() {
                delta: integer = 1;
                i: integer = 1;
                if (x[i, 0] > inc(x[0, i])) {
                    x[i, 0] = i;
                } else {
                    x[0, i] = i + 1;
                }
            }
            """
        expect = "Type mismatch in expression: FuncCall(inc, [ArrayCell(x, [IntegerLit(0), Id(i)])])"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_95(self):
        input = """
            main: function void(){
                y: auto = y:
                x: auto = y != 1;
                z: int;
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_96(self):
        input = """
            x: integer;
            a: array [10] of integer;
            inc: function auto(out n: integer, delta: integer) {
                n = n + delta;
            }
            main: function void() {
                delta: integer = 1;
                delta = inc(delta, x);
            }
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_97(self):
        input = """
            x: integer;
            jump: function integer(inherit nums: array[100] of integer, size: integer){
              minjump: integer = size - 1;
              return minjump;
            }

            jump_: function float(inherit z: float) inherit jump {
                preventDefault();
                y: float = 10.1;
                return nums[0];
            }

            main: function void(){
            }
        """

        expect = "Undeclared Identifier: nums"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_98(self):
        input = """
            x: integer;
            inherit out  y: integer
            main: function void() {
            }
            """
        expect = "Invalid Parameter: y"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_99(self):
        input = """
            main: function void(){
                x, y: auto = x, y;
                z: integer = (x + 1)+y;
                y = 100.0;
            }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(y), FloatLit(100.0))"
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_100(self):
        input = """
        foo: function string (a: string, b: float) {
            c : integer = 2;
            d: float = c + 1;
            f : array [5] of string;
            return f[1];
        }
        bar: function void (inherit out a: float, inherit out b: string) inherit foo {
            super("Hello", 123);
            for (i = 1, i < 10, i + 1)
            {
                writeFloat(a);
            }
            if (a==2)
                return;
            else
                break;
        }
        main: function void() {}
    """
        expect = "Type mismatch in expression: BinExpr(==, Id(a), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 500))
