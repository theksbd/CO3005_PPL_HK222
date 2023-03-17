import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_comment_1(self):
        input = "/* A C-style comment */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 101))

    def test_comment_2(self):
        input = "// A C++ style comment"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 102))

    def test_comment_3(self):
        input = "//abc//abc \n abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 103))

    def test_comment_4(self):
        input = "/*//*/"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 104))

    def test_comment_5(self):
        input = "/**/*/"
        expect = "*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 105))

    def test_comment_6(self):
        input = "// abc \n xyz"
        expect = "xyz,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 106))

    def test_comment_7(self):
        input = "/*aabbcsda\taaw*/"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 107))

    def test_literals_integer_1(self):
        input = "1_72"
        expect = "172,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 201))

    def test_literals_integer_2(self):
        input = "1_234_567"
        expect = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 202))

    def test_literals_integer_3(self):
        input = "1_123"
        expect = "1123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 203))

    def test_literals_integer_4(self):
        input = "201"
        expect = "201,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 204))

    def test_literals_integer_5(self):
        input = "123_92_213_21"
        expect = "1239221321,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 205))

    def test_literals_float_1(self):
        input = "2.01"
        expect = "2.01,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 301))

    def test_literals_float_2(self):
        input = "1.234"
        expect = "1.234,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 302))

    def test_literals_float_3(self):
        input = "1_234.567"
        expect = "1234.567,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 303))

    def test_literals_float_4(self):
        input = "7E-10"
        expect = "7E-10,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 304))

    def test_literals_float_5(self):
        input = "0.123e3"
        expect = "0.123e3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 305))

    def test_literals_float_6(self):
        input = "0.023e321"
        expect = "0.023e321,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 306))

    def test_literals_float_7(self):
        input = "0.00203e301"
        expect = "0.00203e301,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 307))

    def test_literals_string_1(self):
        input = """ "He asked me: \\\"Where is John?\\\"" """
        expect = """He asked me: \\\"Where is John?\\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 401))

    def test_literals_string_2(self):
        input = """ "I\'m Hoang" """
        expect = """I\'m Hoang,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 402))

    def test_literals_string_3(self):
        input = """ "I\'m Hoang" """
        expect = """I\'m Hoang,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 403))

    def test_literals_string_4(self):
        input = """ "I\'m Hoang" """
        expect = """I\'m Hoang,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 404))

    def test_literals_string_5(self):
        input = """ "I\'m Hoang" """
        expect = """I\'m Hoang,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 405))

    def test_literals_string_6(self):
        input = """ "I\'m Hoang \n" """
        expect = """Unclosed String: I\'m Hoang """
        self.assertTrue(TestLexer.test(input, expect, 406))

    def test_literals_string_7(self):
        input = "\"This is string containing tab \t \""
        expect = "This is string containing tab \t ,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 407))

    def test_literals_string_8(self):
        input = """ "He asked me: \\"Where is John?\\"" """
        expect = "He asked me: \"Where is John?\",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 408))

    def test_literals_string_9(self):
        input = """ "Im Hoang" """
        expect = """Im Hoang,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 409))

    def test_literals_string_9(self):
        input = "\"\""
        expect = ",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 410))

    def test_literals_array_1(self):
        self.assertTrue(TestLexer.test("""{1}""", """{1},<EOF>""", 501))

    def test_literals_array_2(self):
        self.assertTrue(TestLexer.test(
            """{"Hanoi","Tokyo","London"}""", """{"Hanoi","Tokyo","London"},<EOF>""", 502))

    def test_literals_array_3(self):
        self.assertTrue(TestLexer.test(
            """{1,5,7,12}""", """{1,5,7,12},<EOF>""", 503))

    def test_random_1(self):
        input = """1.234e-10"""
        expect = """1.234e-10,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 601))

    def test_random_2(self):
        input = "if x > y then x = x + 1 else x = x - 1"
        expect = "if,x,>,y,then,x,=,x,+,1,else,x,=,x,-,1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 602))

    def test_random_3(self):
        input = """ "Hello World" """
        expect = """Hello World,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 603))

    def test_random_4(self):
        input = """ "Hello World\n" """
        expect = """Unclosed String: Hello World"""
        self.assertTrue(TestLexer.test(input, expect, 604))

    def test_random_5(self):
        input = """ // "Hello World" """
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 605))

    def test_random_6(self):
        input = """ /* "Hello World" */"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 606))

    def test_random_7(self):
        input = "/* Hello */ World */"
        expect = "World,*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 607))

    def test_random_8(self):
        input = "// Hello\tW orld \r hello"
        expect = "hello,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 608))

    def test_random_9(self):
        input = """ 1_23e+4_56 """
        expect = """123e+4,_56,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 609))

    def test_random_10(self):
        input = """ 123_456 """
        expect = """123456,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 610))

    def test_random_11(self):
        input = """ 123_456_1.23e+456 """
        expect = """1234561.23e+456,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 611))

    def test_random_12(self):
        input = """theksbd"""
        expect = """theksbd,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 612))

    def test_random_13(self):
        input = """theksbd_"""
        expect = """theksbd_,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 613))

    def test_random_14(self):
        input = """theksbd_123"""
        expect = """theksbd_123,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 614))

    def test_random_15(self):
        input = """theksbd_123_"""
        expect = """theksbd_123_,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 615))

    def test_random_16(self):
        input = """_theksbd_123_123"""
        expect = """_theksbd_123_123,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 616))

    def test_random_17(self):
        input = """Theksbd_123_123_"""
        expect = """Theksbd_123_123_,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 617))

    def test_random_18(self):
        input = """theksbd@123"""
        expect = """theksbd,Error Token @"""
        self.assertTrue(TestLexer.test(input, expect, 618))

    def test_random_19(self):
        input = """/**/"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 619))

    def test_random_20(self):
        input = """/*theksbd*/ 123 is my password"""
        expect = """123,is,my,password,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 620))

    def test_random_21(self):
        input = """/*theksbd*/ 123 is my password /*theksbd*/"""
        expect = """123,is,my,password,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 621))

    def test_random_22(self):
        input = """a = 1 + 2 * 3 + 4 * 5;"""
        expect = """a,=,1,+,2,*,3,+,4,*,5,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 622))

    def test_random_23(self):
        input = """for (i = 0, i < 10, i + 1) { print(i); }"""
        expect = """for,(,i,=,0,,,i,<,10,,,i,+,1,),{,print,(,i,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 623))

    def test_random_24(self):
        input = """While (i < 10) { i = i + 1; }"""
        expect = """While,(,i,<,10,),{,i,=,i,+,1,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 624))

    def test_random_25(self):
        input = """if (i < 10) { i = i + 1; }"""
        expect = """if,(,i,<,10,),{,i,=,i,+,1,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 625))

    def test_random_26(self):
        input = """do { i = i + 1; } While (i < 10);"""
        expect = """do,{,i,=,i,+,1,;,},While,(,i,<,10,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 626))

    def test_random_27(self):
        input = """break;"""
        expect = """break,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 627))

    def test_random_28(self):
        input = """continue;"""
        expect = """continue,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 628))

    def test_random_29(self):
        input = """return foo(a + 6);"""
        expect = """return,foo,(,a,+,6,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 629))

    def test_random_30(self):
        input = """return i + 1;"""
        expect = """return,i,+,1,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 630))

    def test_random_31(self):
        input = """foo(2.3);"""
        expect = """foo,(,2.3,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 631))

    def test_random_32(self):
        input = """foo(2.3e-4);"""
        expect = """foo,(,2.3e-4,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 632))

    def test_random_33(self):
        input = """foo(x + y/5 + bar(z));"""
        expect = """foo,(,x,+,y,/,5,+,bar,(,z,),),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 633))

    def test_random_34(self):
        input = """foo(2 + 3);"""
        expect = """foo,(,2,+,3,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 634))

    def test_random_35(self):
        input = """a = a + 1;"""
        expect = """a,=,a,+,1,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 635))

    def test_random_36(self):
        input = """{}"""
        expect = """{,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 636))

    def test_random_37(self):
        input = """{ return a;}"""
        expect = """{,return,a,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 637))

    def test_random_38(self):
        input = """{ return foo(x); }"""
        expect = """{,return,foo,(,x,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 638))

    def test_random_39(self):
        input = """{ continue; }"""
        expect = """{,continue,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 639))

    def test_random_40(self):
        input = """{ break; }"""
        expect = """{,break,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 640))

    def test_random_41(self):
        input = """/* This is a\nmulti-line comment\n*/ Hello"""
        expect = """Hello,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 641))

    def test_random_42(self):
        input = """/* This is a\nmulti-line comment\n*/ Hello /* This is a\nmulti-line comment\n*/"""
        expect = """Hello,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 642))

    def test_random_43(self):
        input = """/* This is a\nmulti-line comment\n*/ Hello /* This is a\nmulti-line comment\n*/ 123"""
        expect = """Hello,123,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 643))

    def test_random_44(self):
        input = """for (i = 0, i < 10, i + 1) { 
            print(i); 
            // This is a comment
            }"""
        expect = """for,(,i,=,0,,,i,<,10,,,i,+,1,),{,print,(,i,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 644))

    def test_random_45(self):
        input = """for (i = 0, i < 10, i + 1) { 
            print(i); 
            /* This is a comment */
            }"""
        expect = """for,(,i,=,0,,,i,<,10,,,i,+,1,),{,print,(,i,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 645))

    def test_random_46(self):
        input = """for (i = 0, i < 10, i + 1) { 
            print(i); 
            /* This is a comment 
            This is a comment 
            This is a comment
            This is a comment
            */
            }"""
        expect = """for,(,i,=,0,,,i,<,10,,,i,+,1,),{,print,(,i,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 646))

    def test_random_47(self):
        input = """while (i < 10) {
            /* This is a comment 
            This is a comment 
            This is a comment
            This is a comment
            */
            }"""
        expect = """while,(,i,<,10,),{,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 647))

    def test_random_48(self):
        input = """do {
            /* This is a comment 
            This is a comment 
            This is a comment
            This is a comment
            */
            } While (i < 10);"""
        expect = """do,{,},While,(,i,<,10,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 648))

    def test_random_49(self):
        input = """return foo(a + 6 /* a */);"""
        expect = """return,foo,(,a,+,6,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 649))

    def test_random_50(self):
        input = """ = """
        expect = """=,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 650))

    def test_random_51(self):
        input = """ + """
        expect = """+,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 651))

    def test_random_52(self):
        input = """ + -  * /"""
        expect = """+,-,*,/,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 652))

    def test_random_53(self):
        input = """ + -  * / %"""
        expect = """+,-,*,/,%,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 653))

    def test_random_54(self):
        input = """if (a == 1) {
            a = 2;
            }"""
        expect = """if,(,a,==,1,),{,a,=,2,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 654))

    def test_random_55(self):
        input = """if (a == 1) {
            a = 2;
            } else {
            a = 3;
            }"""
        expect = """if,(,a,==,1,),{,a,=,2,;,},else,{,a,=,3,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 655))

    def test_random_56(self):
        input = """if (a == 1) {
            a = 2;
            // This is a comment
            } else {
            a = 3;
            }"""
        expect = """if,(,a,==,1,),{,a,=,2,;,},else,{,a,=,3,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 656))

    def test_random_57(self):
        input = """if (a == 1) {
            a = 2;
            /* This is a comment */
            } else {
            a = 3;
            }"""
        expect = """if,(,a,==,1,),{,a,=,2,;,},else,{,a,=,3,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 657))

    def test_random_58(self):
        input = """if (a == 1) {
            a = 2;
            /* This is a comment 
            This is a comment 
            This is a comment
            This is a comment
            */
            } else {
            a = 3;
            }"""
        expect = """if,(,a,==,1,),{,a,=,2,;,},else,{,a,=,3,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 658))

    def test_random_59(self):
        input = """if (a == 1) {
            a = 2;
            /* This is a comment 
            This is a comment 
            This is a comment
            This is a comment
            */
            } else {
            a = 3;
            // This is a comment
            }"""
        expect = """if,(,a,==,1,),{,a,=,2,;,},else,{,a,=,3,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 659))

    def test_random_60(self):
        input = """if (a == 1) {
            a = 2;
            /* This is a comment 
            This is a comment 
            This is a comment
            This is a comment
            */
            } else {
            a = 3;
            /* This is a comment */
            }"""
        expect = """if,(,a,==,1,),{,a,=,2,;,},else,{,a,=,3,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 660))

    def test_random_61(self):
        input = """if (a == 1) {
            a = 2;
            /* This is a comment 
            This is a comment 
            This is a comment
            This is a comment
            */
            } else {
            a = 3;
            /* This is a comment 
            This is a comment 
            This is a comment
            This is a comment
            */
            }"""
        expect = """if,(,a,==,1,),{,a,=,2,;,},else,{,a,=,3,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 661))

    def test_random_62(self):
        input = """8 more tests"""
        expect = """8,more,tests,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 662))

    def test_random_63(self):
        input = """//8 more tests"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 663))

    def test_random_64(self):
        input = """/*8 more tests*/ if (test == 7) { return a; }"""
        expect = """if,(,test,==,7,),{,return,a,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 664))

    def test_random_65(self):
        input = """/*8 more tests*/ while (test == 7) { return a; }"""
        expect = """while,(,test,==,7,),{,return,a,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 665))

    def test_random_66(self):
        input = """(a + b) * c;"""
        expect = """(,a,+,b,),*,c,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 666))

    def test_random_67(self):
        input = """for (i = 0; i < 10; i = i + 1) {
            a = a + 1;
            }"""
        expect = """for,(,i,=,0,;,i,<,10,;,i,=,i,+,1,),{,a,=,a,+,1,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 667))

    def test_random_68(self):
        input = """for (i = 0; i < 10; i = i + 1) {
            //a = a + 1;
            }"""
        expect = """for,(,i,=,0,;,i,<,10,;,i,=,i,+,1,),{,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 668))

    def test_random_69(self):
        input = """ "This is a string """
        expect = """Unclosed String: This is a string """
        self.assertTrue(TestLexer.test(input, expect, 669))
