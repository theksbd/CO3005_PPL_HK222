# import unittest
# from TestUtils import TestParser


# class ParserSuite(unittest.TestCase):
#     def test_simple_program(self):
#         """Simple program: int main() {} """
#         input = """main: function void() {}"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 201))
import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_13(self):
        input = """main: function void() {
            r,s : integer;
            r = 2.0;
            a,b : array [5] of integer;
            s = r * r * myPi;
            a[0] = s;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 613))

    def test_12(self):
        input = """do {
                    writeInt(i);
                    i = i + 1;
                } while (i < 10);"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 612))

    def test_11(self):
        input = """while (i < 10) {
                    writeInt(i);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 611))

    def test_10(self):
        input = """for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 610))

    def test_9(self):
        input = """if (n == 0) return 1;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 609))

    def test_8(self):
        input = """a, b: float = foo(2 + x, 4.0 / y), bar(x);"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 608))

    def test_1(self):
        input = """array [5] of integer"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 601))

    def test_2(self):
        input = """fact: function integer (n : integer) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 602))

    def test_3(self):
        input = """main: function void () {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 603))

    def test_4(self):
        input = """a, b, c: integer = 3, 4, 6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 604))

    def test_5(self):
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 605))

    def test_6(self):
        input = """x: integer = fact(3);"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 606))

    def test_7(self):
        input = """x: integer = 65;
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
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 607))

    def test_14(self):
        input = """main: function void() {
            a,b : array [5] of integer;
            a[0] = s;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 614))

    def test_15(self):
        input = """main: function integer() {
            a,b : array [5] of integer;
            a[0] = s;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 615))

    def test_16(self):
        input = """main: function integer() {
            a,b : array [5] of integer;
            a[0] = s;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 616))

    def test_17(self):
        input = """main: function integer() {
            a,b : array [5] of integer;
            a[0] = s;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 617))

    def test_18(self):
        input = """main: function integer() {
            a,b : array [5] of integer;
            a[0] = s;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 618))

    def test_19(self):
        input = """main: function integer() {
            a,b : array [5] of integer;
            a[0] = s;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 619))

    def test_20(self):
        input = """main: function integer() {
            a,b : array [5] of integer;
            a[0] = s;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 620))

    def test_21(self):
        input = """main: function integer() {
            a,b : array [5] of integer;
            a[0] = s;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 621))

    def test_22(self):
        input = """main: function integer() {
            a,b : array [5] of integer;
            a[0] = s;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 622))
