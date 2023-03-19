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
        input = """main: function void() {
            r,s : integer;
            r = 2.0;
            a,b : array [5] of integer;
            s = r * r * myPi;
            a[0] = s;
            do {
                writeInt(i);
                i = i + 1;
            } while (i < 10);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 612))

    def test_11(self):
        input = """main: function void() {
            while (i < 10) {
                writeInt(i);
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 611))

    def test_10(self):
        input = """main: function void() {
        for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 610))

    def test_9(self):
        input = """main: function void() {
            if (n == 0) return 1;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 609))

    def test_8(self):
        input = """main: function void() {
                a, b: float = foo(2 + x, 4.0 / y), bar(x);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 608))

    def test_1(self):
        input = """main: function void() {
            x: array [5] of integer = {1, 2, 3, 4, 5};
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 601))

    def test_2(self):
        input = """main: function void() {
            x: array [5] of float = {1, 2, 3, 4, 5};
            writeFloat(x[0]);
            readFloat();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 602))

    def test_3(self):
        input = """main: function void () { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 603))

    def test_4(self):
        input = """main: function void() {
            a, b, c: integer = 3, 4, 6;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 604))

    def test_6(self):
        input = """main: function void() {
            x: integer = fact(3);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 606))

    def test_7(self):
        input = """main: function void() {
        x: integer = 65;
        while (x > 0) {
            x = x - 1;
            y: integer = 65;
            while (y > 0) {
                y = y - 1;
            }
        }
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

    def test_23(self):
        input = """main: function void() {
            readInteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 623))

    def test_24(self):
        input = """main: function void() {
            printInteger(foo(5));
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 624))

    def test_25(self):
        input = """main: function void() {
            foo(2);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 625))