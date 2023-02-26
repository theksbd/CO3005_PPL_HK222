# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u02b4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%")
        buf.write("\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3:\3:\7:\u01d7\n:\f:\16:\u01da")
        buf.write("\13:\3;\3;\3;\3;\7;\u01e0\n;\f;\16;\u01e3\13;\3;\3;\3")
        buf.write(";\3<\3<\3=\3=\3>\3>\5>\u01ee\n>\3?\3?\3@\3@\3A\3A\3A\7")
        buf.write("A\u01f7\nA\fA\16A\u01fa\13A\3A\3A\6A\u01fe\nA\rA\16A\u01ff")
        buf.write("\7A\u0202\nA\fA\16A\u0205\13A\5A\u0207\nA\3B\3B\7B\u020b")
        buf.write("\nB\fB\16B\u020e\13B\3C\3C\3D\3D\5D\u0214\nD\3D\6D\u0217")
        buf.write("\nD\rD\16D\u0218\3E\3E\3E\3E\3E\3F\3F\3F\3F\3F\3F\3G\3")
        buf.write("G\3G\3H\3H\3H\3I\3I\3I\3I\3I\3I\7I\u0232\nI\fI\16I\u0235")
        buf.write("\13I\3I\3I\3I\3J\3J\3J\5J\u023d\nJ\3K\3K\3K\3K\3K\5K\u0244")
        buf.write("\nK\3L\3L\3L\3L\3L\5L\u024b\nL\3M\3M\3M\3M\3M\5M\u0252")
        buf.write("\nM\3N\3N\5N\u0256\nN\3N\3N\3O\3O\3O\3P\3P\3P\5P\u0260")
        buf.write("\nP\3P\3P\3P\3P\3P\3P\3P\3P\3P\5P\u026b\nP\3P\3P\3Q\3")
        buf.write("Q\5Q\u0271\nQ\3R\3R\3R\3R\7R\u0277\nR\fR\16R\u027a\13")
        buf.write("R\3R\3R\3R\3S\3S\5S\u0281\nS\3S\3S\3T\3T\5T\u0287\nT\3")
        buf.write("T\3T\3T\7T\u028c\nT\fT\16T\u028f\13T\3U\6U\u0292\nU\r")
        buf.write("U\16U\u0293\3U\3U\3V\3V\3V\3V\7V\u029c\nV\fV\16V\u029f")
        buf.write("\13V\3V\5V\u02a2\nV\3V\3V\3W\3W\3W\3W\7W\u02aa\nW\fW\16")
        buf.write("W\u02ad\13W\3W\3W\3W\3X\3X\3X\5\u01e1\u0233\u029d\2Y\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s\2u\2")
        buf.write("w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097")
        buf.write("\2\u0099\2\u009b;\u009d<\u009f=\u00a1>\u00a3?\u00a5@\u00a7")
        buf.write("A\u00a9B\u00abC\u00adD\u00afE\3\2\16\4\2\f\f\17\17\3\2")
        buf.write("C\\\3\2c|\3\2\62;\3\2\63;\4\2--//\4\2GGgg\n\2$$))^^dd")
        buf.write("hhppttvv\5\2\f\f$$^^\5\2\13\f\17\17\"\"\4\2$$^^\4\3\f")
        buf.write("\f\17\17\2\u02c6\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5")
        buf.write("\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2")
        buf.write("\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\3\u00b1\3\2\2\2\5\u00b4")
        buf.write("\3\2\2\2\7\u00b9\3\2\2\2\t\u00bf\3\2\2\2\13\u00c7\3\2")
        buf.write("\2\2\r\u00ca\3\2\2\2\17\u00cf\3\2\2\2\21\u00d5\3\2\2\2")
        buf.write("\23\u00d9\3\2\2\2\25\u00e2\3\2\2\2\27\u00e5\3\2\2\2\31")
        buf.write("\u00ed\3\2\2\2\33\u00f4\3\2\2\2\35\u00fb\3\2\2\2\37\u0101")
        buf.write("\3\2\2\2!\u0106\3\2\2\2#\u010a\3\2\2\2%\u0113\3\2\2\2")
        buf.write("\'\u0116\3\2\2\2)\u011e\3\2\2\2+\u0124\3\2\2\2-\u0130")
        buf.write("\3\2\2\2/\u013d\3\2\2\2\61\u0147\3\2\2\2\63\u0152\3\2")
        buf.write("\2\2\65\u015e\3\2\2\2\67\u016b\3\2\2\29\u0176\3\2\2\2")
        buf.write(";\u0182\3\2\2\2=\u0188\3\2\2\2?\u0197\3\2\2\2A\u0199\3")
        buf.write("\2\2\2C\u019b\3\2\2\2E\u019d\3\2\2\2G\u019f\3\2\2\2I\u01a1")
        buf.write("\3\2\2\2K\u01a3\3\2\2\2M\u01a6\3\2\2\2O\u01a9\3\2\2\2")
        buf.write("Q\u01ac\3\2\2\2S\u01af\3\2\2\2U\u01b1\3\2\2\2W\u01b4\3")
        buf.write("\2\2\2Y\u01b6\3\2\2\2[\u01b9\3\2\2\2]\u01bc\3\2\2\2_\u01be")
        buf.write("\3\2\2\2a\u01c0\3\2\2\2c\u01c2\3\2\2\2e\u01c4\3\2\2\2")
        buf.write("g\u01c6\3\2\2\2i\u01c8\3\2\2\2k\u01ca\3\2\2\2m\u01cc\3")
        buf.write("\2\2\2o\u01ce\3\2\2\2q\u01d0\3\2\2\2s\u01d2\3\2\2\2u\u01db")
        buf.write("\3\2\2\2w\u01e7\3\2\2\2y\u01e9\3\2\2\2{\u01ed\3\2\2\2")
        buf.write("}\u01ef\3\2\2\2\177\u01f1\3\2\2\2\u0081\u0206\3\2\2\2")
        buf.write("\u0083\u0208\3\2\2\2\u0085\u020f\3\2\2\2\u0087\u0211\3")
        buf.write("\2\2\2\u0089\u021a\3\2\2\2\u008b\u021f\3\2\2\2\u008d\u0225")
        buf.write("\3\2\2\2\u008f\u0228\3\2\2\2\u0091\u022b\3\2\2\2\u0093")
        buf.write("\u023c\3\2\2\2\u0095\u0243\3\2\2\2\u0097\u024a\3\2\2\2")
        buf.write("\u0099\u0251\3\2\2\2\u009b\u0255\3\2\2\2\u009d\u0259\3")
        buf.write("\2\2\2\u009f\u026a\3\2\2\2\u00a1\u0270\3\2\2\2\u00a3\u0272")
        buf.write("\3\2\2\2\u00a5\u027e\3\2\2\2\u00a7\u0286\3\2\2\2\u00a9")
        buf.write("\u0291\3\2\2\2\u00ab\u0297\3\2\2\2\u00ad\u02a5\3\2\2\2")
        buf.write("\u00af\u02b1\3\2\2\2\u00b1\u00b2\7}\2\2\u00b2\u00b3\7")
        buf.write("\177\2\2\u00b3\4\3\2\2\2\u00b4\u00b5\7c\2\2\u00b5\u00b6")
        buf.write("\7w\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8\7q\2\2\u00b8\6")
        buf.write("\3\2\2\2\u00b9\u00ba\7d\2\2\u00ba\u00bb\7t\2\2\u00bb\u00bc")
        buf.write("\7g\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be\7m\2\2\u00be\b")
        buf.write("\3\2\2\2\u00bf\u00c0\7d\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2")
        buf.write("\7q\2\2\u00c2\u00c3\7n\2\2\u00c3\u00c4\7g\2\2\u00c4\u00c5")
        buf.write("\7c\2\2\u00c5\u00c6\7p\2\2\u00c6\n\3\2\2\2\u00c7\u00c8")
        buf.write("\7f\2\2\u00c8\u00c9\7q\2\2\u00c9\f\3\2\2\2\u00ca\u00cb")
        buf.write("\7g\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd\7u\2\2\u00cd\u00ce")
        buf.write("\7g\2\2\u00ce\16\3\2\2\2\u00cf\u00d0\7h\2\2\u00d0\u00d1")
        buf.write("\7n\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3\7c\2\2\u00d3\u00d4")
        buf.write("\7v\2\2\u00d4\20\3\2\2\2\u00d5\u00d6\7h\2\2\u00d6\u00d7")
        buf.write("\7q\2\2\u00d7\u00d8\7t\2\2\u00d8\22\3\2\2\2\u00d9\u00da")
        buf.write("\7h\2\2\u00da\u00db\7w\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd")
        buf.write("\7e\2\2\u00dd\u00de\7v\2\2\u00de\u00df\7k\2\2\u00df\u00e0")
        buf.write("\7q\2\2\u00e0\u00e1\7p\2\2\u00e1\24\3\2\2\2\u00e2\u00e3")
        buf.write("\7k\2\2\u00e3\u00e4\7h\2\2\u00e4\26\3\2\2\2\u00e5\u00e6")
        buf.write("\7k\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9")
        buf.write("\7g\2\2\u00e9\u00ea\7i\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec")
        buf.write("\7t\2\2\u00ec\30\3\2\2\2\u00ed\u00ee\7t\2\2\u00ee\u00ef")
        buf.write("\7g\2\2\u00ef\u00f0\7v\2\2\u00f0\u00f1\7w\2\2\u00f1\u00f2")
        buf.write("\7t\2\2\u00f2\u00f3\7p\2\2\u00f3\32\3\2\2\2\u00f4\u00f5")
        buf.write("\7u\2\2\u00f5\u00f6\7v\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8")
        buf.write("\7k\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa\7i\2\2\u00fa\34")
        buf.write("\3\2\2\2\u00fb\u00fc\7y\2\2\u00fc\u00fd\7j\2\2\u00fd\u00fe")
        buf.write("\7k\2\2\u00fe\u00ff\7n\2\2\u00ff\u0100\7g\2\2\u0100\36")
        buf.write("\3\2\2\2\u0101\u0102\7x\2\2\u0102\u0103\7q\2\2\u0103\u0104")
        buf.write("\7k\2\2\u0104\u0105\7f\2\2\u0105 \3\2\2\2\u0106\u0107")
        buf.write("\7q\2\2\u0107\u0108\7w\2\2\u0108\u0109\7v\2\2\u0109\"")
        buf.write("\3\2\2\2\u010a\u010b\7e\2\2\u010b\u010c\7q\2\2\u010c\u010d")
        buf.write("\7p\2\2\u010d\u010e\7v\2\2\u010e\u010f\7k\2\2\u010f\u0110")
        buf.write("\7p\2\2\u0110\u0111\7w\2\2\u0111\u0112\7g\2\2\u0112$\3")
        buf.write("\2\2\2\u0113\u0114\7q\2\2\u0114\u0115\7h\2\2\u0115&\3")
        buf.write("\2\2\2\u0116\u0117\7k\2\2\u0117\u0118\7p\2\2\u0118\u0119")
        buf.write("\7j\2\2\u0119\u011a\7g\2\2\u011a\u011b\7t\2\2\u011b\u011c")
        buf.write("\7k\2\2\u011c\u011d\7v\2\2\u011d(\3\2\2\2\u011e\u011f")
        buf.write("\7c\2\2\u011f\u0120\7t\2\2\u0120\u0121\7t\2\2\u0121\u0122")
        buf.write("\7c\2\2\u0122\u0123\7{\2\2\u0123*\3\2\2\2\u0124\u0125")
        buf.write("\7t\2\2\u0125\u0126\7g\2\2\u0126\u0127\7c\2\2\u0127\u0128")
        buf.write("\7f\2\2\u0128\u0129\7K\2\2\u0129\u012a\7p\2\2\u012a\u012b")
        buf.write("\7v\2\2\u012b\u012c\7g\2\2\u012c\u012d\7i\2\2\u012d\u012e")
        buf.write("\7g\2\2\u012e\u012f\7t\2\2\u012f,\3\2\2\2\u0130\u0131")
        buf.write("\7r\2\2\u0131\u0132\7t\2\2\u0132\u0133\7k\2\2\u0133\u0134")
        buf.write("\7p\2\2\u0134\u0135\7v\2\2\u0135\u0136\7K\2\2\u0136\u0137")
        buf.write("\7p\2\2\u0137\u0138\7v\2\2\u0138\u0139\7g\2\2\u0139\u013a")
        buf.write("\7i\2\2\u013a\u013b\7g\2\2\u013b\u013c\7t\2\2\u013c.\3")
        buf.write("\2\2\2\u013d\u013e\7t\2\2\u013e\u013f\7g\2\2\u013f\u0140")
        buf.write("\7c\2\2\u0140\u0141\7f\2\2\u0141\u0142\7H\2\2\u0142\u0143")
        buf.write("\7n\2\2\u0143\u0144\7q\2\2\u0144\u0145\7c\2\2\u0145\u0146")
        buf.write("\7v\2\2\u0146\60\3\2\2\2\u0147\u0148\7y\2\2\u0148\u0149")
        buf.write("\7t\2\2\u0149\u014a\7k\2\2\u014a\u014b\7v\2\2\u014b\u014c")
        buf.write("\7g\2\2\u014c\u014d\7H\2\2\u014d\u014e\7n\2\2\u014e\u014f")
        buf.write("\7q\2\2\u014f\u0150\7c\2\2\u0150\u0151\7v\2\2\u0151\62")
        buf.write("\3\2\2\2\u0152\u0153\7t\2\2\u0153\u0154\7g\2\2\u0154\u0155")
        buf.write("\7c\2\2\u0155\u0156\7f\2\2\u0156\u0157\7D\2\2\u0157\u0158")
        buf.write("\7q\2\2\u0158\u0159\7q\2\2\u0159\u015a\7n\2\2\u015a\u015b")
        buf.write("\7g\2\2\u015b\u015c\7c\2\2\u015c\u015d\7p\2\2\u015d\64")
        buf.write("\3\2\2\2\u015e\u015f\7r\2\2\u015f\u0160\7t\2\2\u0160\u0161")
        buf.write("\7k\2\2\u0161\u0162\7p\2\2\u0162\u0163\7v\2\2\u0163\u0164")
        buf.write("\7D\2\2\u0164\u0165\7q\2\2\u0165\u0166\7q\2\2\u0166\u0167")
        buf.write("\7n\2\2\u0167\u0168\7g\2\2\u0168\u0169\7c\2\2\u0169\u016a")
        buf.write("\7p\2\2\u016a\66\3\2\2\2\u016b\u016c\7t\2\2\u016c\u016d")
        buf.write("\7g\2\2\u016d\u016e\7c\2\2\u016e\u016f\7f\2\2\u016f\u0170")
        buf.write("\7U\2\2\u0170\u0171\7v\2\2\u0171\u0172\7t\2\2\u0172\u0173")
        buf.write("\7k\2\2\u0173\u0174\7p\2\2\u0174\u0175\7i\2\2\u01758\3")
        buf.write("\2\2\2\u0176\u0177\7r\2\2\u0177\u0178\7t\2\2\u0178\u0179")
        buf.write("\7k\2\2\u0179\u017a\7p\2\2\u017a\u017b\7v\2\2\u017b\u017c")
        buf.write("\7U\2\2\u017c\u017d\7v\2\2\u017d\u017e\7t\2\2\u017e\u017f")
        buf.write("\7k\2\2\u017f\u0180\7p\2\2\u0180\u0181\7i\2\2\u0181:\3")
        buf.write("\2\2\2\u0182\u0183\7u\2\2\u0183\u0184\7w\2\2\u0184\u0185")
        buf.write("\7r\2\2\u0185\u0186\7g\2\2\u0186\u0187\7t\2\2\u0187<\3")
        buf.write("\2\2\2\u0188\u0189\7r\2\2\u0189\u018a\7t\2\2\u018a\u018b")
        buf.write("\7g\2\2\u018b\u018c\7x\2\2\u018c\u018d\7g\2\2\u018d\u018e")
        buf.write("\7p\2\2\u018e\u018f\7v\2\2\u018f\u0190\7F\2\2\u0190\u0191")
        buf.write("\7g\2\2\u0191\u0192\7h\2\2\u0192\u0193\7c\2\2\u0193\u0194")
        buf.write("\7w\2\2\u0194\u0195\7n\2\2\u0195\u0196\7v\2\2\u0196>\3")
        buf.write("\2\2\2\u0197\u0198\7-\2\2\u0198@\3\2\2\2\u0199\u019a\7")
        buf.write("/\2\2\u019aB\3\2\2\2\u019b\u019c\7,\2\2\u019cD\3\2\2\2")
        buf.write("\u019d\u019e\7\61\2\2\u019eF\3\2\2\2\u019f\u01a0\7\'\2")
        buf.write("\2\u01a0H\3\2\2\2\u01a1\u01a2\7#\2\2\u01a2J\3\2\2\2\u01a3")
        buf.write("\u01a4\7(\2\2\u01a4\u01a5\7(\2\2\u01a5L\3\2\2\2\u01a6")
        buf.write("\u01a7\7~\2\2\u01a7\u01a8\7~\2\2\u01a8N\3\2\2\2\u01a9")
        buf.write("\u01aa\7?\2\2\u01aa\u01ab\7?\2\2\u01abP\3\2\2\2\u01ac")
        buf.write("\u01ad\7#\2\2\u01ad\u01ae\7?\2\2\u01aeR\3\2\2\2\u01af")
        buf.write("\u01b0\7>\2\2\u01b0T\3\2\2\2\u01b1\u01b2\7>\2\2\u01b2")
        buf.write("\u01b3\7?\2\2\u01b3V\3\2\2\2\u01b4\u01b5\7@\2\2\u01b5")
        buf.write("X\3\2\2\2\u01b6\u01b7\7@\2\2\u01b7\u01b8\7?\2\2\u01b8")
        buf.write("Z\3\2\2\2\u01b9\u01ba\7<\2\2\u01ba\u01bb\7<\2\2\u01bb")
        buf.write("\\\3\2\2\2\u01bc\u01bd\7*\2\2\u01bd^\3\2\2\2\u01be\u01bf")
        buf.write("\7+\2\2\u01bf`\3\2\2\2\u01c0\u01c1\7]\2\2\u01c1b\3\2\2")
        buf.write("\2\u01c2\u01c3\7_\2\2\u01c3d\3\2\2\2\u01c4\u01c5\7\60")
        buf.write("\2\2\u01c5f\3\2\2\2\u01c6\u01c7\7.\2\2\u01c7h\3\2\2\2")
        buf.write("\u01c8\u01c9\7=\2\2\u01c9j\3\2\2\2\u01ca\u01cb\7<\2\2")
        buf.write("\u01cbl\3\2\2\2\u01cc\u01cd\7}\2\2\u01cdn\3\2\2\2\u01ce")
        buf.write("\u01cf\7\177\2\2\u01cfp\3\2\2\2\u01d0\u01d1\7?\2\2\u01d1")
        buf.write("r\3\2\2\2\u01d2\u01d3\7\61\2\2\u01d3\u01d4\7\61\2\2\u01d4")
        buf.write("\u01d8\3\2\2\2\u01d5\u01d7\n\2\2\2\u01d6\u01d5\3\2\2\2")
        buf.write("\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3")
        buf.write("\2\2\2\u01d9t\3\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01dc")
        buf.write("\7\61\2\2\u01dc\u01dd\7,\2\2\u01dd\u01e1\3\2\2\2\u01de")
        buf.write("\u01e0\13\2\2\2\u01df\u01de\3\2\2\2\u01e0\u01e3\3\2\2")
        buf.write("\2\u01e1\u01e2\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e4")
        buf.write("\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e4\u01e5\7,\2\2\u01e5")
        buf.write("\u01e6\7\61\2\2\u01e6v\3\2\2\2\u01e7\u01e8\t\3\2\2\u01e8")
        buf.write("x\3\2\2\2\u01e9\u01ea\t\4\2\2\u01eaz\3\2\2\2\u01eb\u01ee")
        buf.write("\5w<\2\u01ec\u01ee\5y=\2\u01ed\u01eb\3\2\2\2\u01ed\u01ec")
        buf.write("\3\2\2\2\u01ee|\3\2\2\2\u01ef\u01f0\7a\2\2\u01f0~\3\2")
        buf.write("\2\2\u01f1\u01f2\t\5\2\2\u01f2\u0080\3\2\2\2\u01f3\u0207")
        buf.write("\7\62\2\2\u01f4\u01f8\t\6\2\2\u01f5\u01f7\5\177@\2\u01f6")
        buf.write("\u01f5\3\2\2\2\u01f7\u01fa\3\2\2\2\u01f8\u01f6\3\2\2\2")
        buf.write("\u01f8\u01f9\3\2\2\2\u01f9\u0203\3\2\2\2\u01fa\u01f8\3")
        buf.write("\2\2\2\u01fb\u01fd\5}?\2\u01fc\u01fe\5\177@\2\u01fd\u01fc")
        buf.write("\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff")
        buf.write("\u0200\3\2\2\2\u0200\u0202\3\2\2\2\u0201\u01fb\3\2\2\2")
        buf.write("\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2\u0203\u0204\3")
        buf.write("\2\2\2\u0204\u0207\3\2\2\2\u0205\u0203\3\2\2\2\u0206\u01f3")
        buf.write("\3\2\2\2\u0206\u01f4\3\2\2\2\u0207\u0082\3\2\2\2\u0208")
        buf.write("\u020c\7\60\2\2\u0209\u020b\5\177@\2\u020a\u0209\3\2\2")
        buf.write("\2\u020b\u020e\3\2\2\2\u020c\u020a\3\2\2\2\u020c\u020d")
        buf.write("\3\2\2\2\u020d\u0084\3\2\2\2\u020e\u020c\3\2\2\2\u020f")
        buf.write("\u0210\t\7\2\2\u0210\u0086\3\2\2\2\u0211\u0213\t\b\2\2")
        buf.write("\u0212\u0214\5\u0085C\2\u0213\u0212\3\2\2\2\u0213\u0214")
        buf.write("\3\2\2\2\u0214\u0216\3\2\2\2\u0215\u0217\5\177@\2\u0216")
        buf.write("\u0215\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u0216\3\2\2\2")
        buf.write("\u0218\u0219\3\2\2\2\u0219\u0088\3\2\2\2\u021a\u021b\7")
        buf.write("v\2\2\u021b\u021c\7t\2\2\u021c\u021d\7w\2\2\u021d\u021e")
        buf.write("\7g\2\2\u021e\u008a\3\2\2\2\u021f\u0220\7h\2\2\u0220\u0221")
        buf.write("\7c\2\2\u0221\u0222\7n\2\2\u0222\u0223\7u\2\2\u0223\u0224")
        buf.write("\7g\2\2\u0224\u008c\3\2\2\2\u0225\u0226\7^\2\2\u0226\u0227")
        buf.write("\n\t\2\2\u0227\u008e\3\2\2\2\u0228\u0229\7^\2\2\u0229")
        buf.write("\u022a\t\t\2\2\u022a\u0090\3\2\2\2\u022b\u022c\7^\2\2")
        buf.write("\u022c\u022d\7$\2\2\u022d\u0233\3\2\2\2\u022e\u0232\n")
        buf.write("\n\2\2\u022f\u0232\5\u0091I\2\u0230\u0232\5\u008fH\2\u0231")
        buf.write("\u022e\3\2\2\2\u0231\u022f\3\2\2\2\u0231\u0230\3\2\2\2")
        buf.write("\u0232\u0235\3\2\2\2\u0233\u0234\3\2\2\2\u0233\u0231\3")
        buf.write("\2\2\2\u0234\u0236\3\2\2\2\u0235\u0233\3\2\2\2\u0236\u0237")
        buf.write("\7^\2\2\u0237\u0238\7$\2\2\u0238\u0092\3\2\2\2\u0239\u023d")
        buf.write("\5\u0095K\2\u023a\u023d\5\u0097L\2\u023b\u023d\5\u0099")
        buf.write("M\2\u023c\u0239\3\2\2\2\u023c\u023a\3\2\2\2\u023c\u023b")
        buf.write("\3\2\2\2\u023d\u0094\3\2\2\2\u023e\u023f\5\u009dO\2\u023f")
        buf.write("\u0240\5g\64\2\u0240\u0241\5\u0095K\2\u0241\u0244\3\2")
        buf.write("\2\2\u0242\u0244\5\u009dO\2\u0243\u023e\3\2\2\2\u0243")
        buf.write("\u0242\3\2\2\2\u0244\u0096\3\2\2\2\u0245\u0246\5\u009f")
        buf.write("P\2\u0246\u0247\5g\64\2\u0247\u0248\5\u0097L\2\u0248\u024b")
        buf.write("\3\2\2\2\u0249\u024b\5\u009fP\2\u024a\u0245\3\2\2\2\u024a")
        buf.write("\u0249\3\2\2\2\u024b\u0098\3\2\2\2\u024c\u024d\5\u00a3")
        buf.write("R\2\u024d\u024e\5g\64\2\u024e\u024f\5\u0099M\2\u024f\u0252")
        buf.write("\3\2\2\2\u0250\u0252\5\u00a3R\2\u0251\u024c\3\2\2\2\u0251")
        buf.write("\u0250\3\2\2\2\u0252\u009a\3\2\2\2\u0253\u0256\5s:\2\u0254")
        buf.write("\u0256\5u;\2\u0255\u0253\3\2\2\2\u0255\u0254\3\2\2\2\u0256")
        buf.write("\u0257\3\2\2\2\u0257\u0258\bN\2\2\u0258\u009c\3\2\2\2")
        buf.write("\u0259\u025a\5\u0081A\2\u025a\u025b\bO\3\2\u025b\u009e")
        buf.write("\3\2\2\2\u025c\u025d\5\u0081A\2\u025d\u025f\5\u0083B\2")
        buf.write("\u025e\u0260\5\u0087D\2\u025f\u025e\3\2\2\2\u025f\u0260")
        buf.write("\3\2\2\2\u0260\u026b\3\2\2\2\u0261\u0262\5\u0081A\2\u0262")
        buf.write("\u0263\5\u0087D\2\u0263\u026b\3\2\2\2\u0264\u0265\5\u0081")
        buf.write("A\2\u0265\u0266\5\u0083B\2\u0266\u026b\3\2\2\2\u0267\u0268")
        buf.write("\5\u0083B\2\u0268\u0269\5\u0087D\2\u0269\u026b\3\2\2\2")
        buf.write("\u026a\u025c\3\2\2\2\u026a\u0261\3\2\2\2\u026a\u0264\3")
        buf.write("\2\2\2\u026a\u0267\3\2\2\2\u026b\u026c\3\2\2\2\u026c\u026d")
        buf.write("\bP\4\2\u026d\u00a0\3\2\2\2\u026e\u0271\5\u0089E\2\u026f")
        buf.write("\u0271\5\u008bF\2\u0270\u026e\3\2\2\2\u0270\u026f\3\2")
        buf.write("\2\2\u0271\u00a2\3\2\2\2\u0272\u0278\7$\2\2\u0273\u0277")
        buf.write("\5\u008fH\2\u0274\u0277\n\n\2\2\u0275\u0277\5\u0091I\2")
        buf.write("\u0276\u0273\3\2\2\2\u0276\u0274\3\2\2\2\u0276\u0275\3")
        buf.write("\2\2\2\u0277\u027a\3\2\2\2\u0278\u0276\3\2\2\2\u0278\u0279")
        buf.write("\3\2\2\2\u0279\u027b\3\2\2\2\u027a\u0278\3\2\2\2\u027b")
        buf.write("\u027c\7$\2\2\u027c\u027d\bR\5\2\u027d\u00a4\3\2\2\2\u027e")
        buf.write("\u0280\5m\67\2\u027f\u0281\5\u0093J\2\u0280\u027f\3\2")
        buf.write("\2\2\u0280\u0281\3\2\2\2\u0281\u0282\3\2\2\2\u0282\u0283")
        buf.write("\5o8\2\u0283\u00a6\3\2\2\2\u0284\u0287\5{>\2\u0285\u0287")
        buf.write("\5}?\2\u0286\u0284\3\2\2\2\u0286\u0285\3\2\2\2\u0287\u028d")
        buf.write("\3\2\2\2\u0288\u028c\5{>\2\u0289\u028c\5}?\2\u028a\u028c")
        buf.write("\5\177@\2\u028b\u0288\3\2\2\2\u028b\u0289\3\2\2\2\u028b")
        buf.write("\u028a\3\2\2\2\u028c\u028f\3\2\2\2\u028d\u028b\3\2\2\2")
        buf.write("\u028d\u028e\3\2\2\2\u028e\u00a8\3\2\2\2\u028f\u028d\3")
        buf.write("\2\2\2\u0290\u0292\t\13\2\2\u0291\u0290\3\2\2\2\u0292")
        buf.write("\u0293\3\2\2\2\u0293\u0291\3\2\2\2\u0293\u0294\3\2\2\2")
        buf.write("\u0294\u0295\3\2\2\2\u0295\u0296\bU\2\2\u0296\u00aa\3")
        buf.write("\2\2\2\u0297\u029d\7$\2\2\u0298\u029c\n\f\2\2\u0299\u029c")
        buf.write("\5\u0091I\2\u029a\u029c\5\u008fH\2\u029b\u0298\3\2\2\2")
        buf.write("\u029b\u0299\3\2\2\2\u029b\u029a\3\2\2\2\u029c\u029f\3")
        buf.write("\2\2\2\u029d\u029e\3\2\2\2\u029d\u029b\3\2\2\2\u029e\u02a1")
        buf.write("\3\2\2\2\u029f\u029d\3\2\2\2\u02a0\u02a2\t\r\2\2\u02a1")
        buf.write("\u02a0\3\2\2\2\u02a2\u02a3\3\2\2\2\u02a3\u02a4\bV\6\2")
        buf.write("\u02a4\u00ac\3\2\2\2\u02a5\u02ab\7$\2\2\u02a6\u02aa\n")
        buf.write("\f\2\2\u02a7\u02aa\5\u0091I\2\u02a8\u02aa\5\u008fH\2\u02a9")
        buf.write("\u02a6\3\2\2\2\u02a9\u02a7\3\2\2\2\u02a9\u02a8\3\2\2\2")
        buf.write("\u02aa\u02ad\3\2\2\2\u02ab\u02a9\3\2\2\2\u02ab\u02ac\3")
        buf.write("\2\2\2\u02ac\u02ae\3\2\2\2\u02ad\u02ab\3\2\2\2\u02ae\u02af")
        buf.write("\5\u008dG\2\u02af\u02b0\bW\7\2\u02b0\u00ae\3\2\2\2\u02b1")
        buf.write("\u02b2\13\2\2\2\u02b2\u02b3\bX\b\2\u02b3\u00b0\3\2\2\2")
        buf.write("#\2\u01d8\u01e1\u01ed\u01f8\u01ff\u0203\u0206\u020c\u0213")
        buf.write("\u0218\u0231\u0233\u023c\u0243\u024a\u0251\u0255\u025f")
        buf.write("\u026a\u0270\u0276\u0278\u0280\u0286\u028b\u028d\u0293")
        buf.write("\u029b\u029d\u02a1\u02a9\u02ab\t\b\2\2\3O\2\3P\3\3R\4")
        buf.write("\3V\5\3W\6\3X\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    AUTO = 2
    BREAK = 3
    BOOLEAN = 4
    DO = 5
    ELSE = 6
    FLOAT = 7
    FOR = 8
    FUNCTION = 9
    IF = 10
    INTEGER = 11
    RETURN = 12
    STRING = 13
    WHILE = 14
    VOID = 15
    OUT = 16
    CONTINUE = 17
    OF = 18
    INHERIT = 19
    ARRAY = 20
    READINTEGER = 21
    PRINTINTEGER = 22
    READFLOAT = 23
    WRITEFLOAT = 24
    READBOOLEAN = 25
    PRINTBOOLEAN = 26
    READSTRING = 27
    PRINTSTRING = 28
    SUPER = 29
    PREVENTDEFAULT = 30
    ADD = 31
    MINUS = 32
    MUL = 33
    DIV = 34
    MODUL = 35
    NOT = 36
    AND = 37
    OR = 38
    EQUAL = 39
    NOT_EQUAL = 40
    LESS_THAN = 41
    LESS_EQUAL = 42
    GREATER_THAN = 43
    GREATER_EQUAL = 44
    DOUBLE_COLON = 45
    LP = 46
    RP = 47
    LSB = 48
    RSB = 49
    DOT = 50
    COMMA = 51
    SEMI = 52
    COLON = 53
    LB = 54
    RB = 55
    ASSIGN = 56
    COMMENT = 57
    INTEGER_LIT = 58
    FLOAT_LIT = 59
    BOOLEAN_LIT = 60
    STRING_LIT = 61
    ARRAY_LIT = 62
    IDENTIFIER = 63
    WS = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66
    ERROR_CHAR = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{}'", "'auto'", "'break'", "'boolean'", "'do'", "'else'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'while'", "'void'", "'out'", "'continue'", "'of'", 
            "'inherit'", "'array'", "'readInteger'", "'printInteger'", "'readFloat'", 
            "'writeFloat'", "'readBoolean'", "'printBoolean'", "'readString'", 
            "'printString'", "'super'", "'preventDefault'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", 
            "'.'", "','", "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", 
            "IF", "INTEGER", "RETURN", "STRING", "WHILE", "VOID", "OUT", 
            "CONTINUE", "OF", "INHERIT", "ARRAY", "READINTEGER", "PRINTINTEGER", 
            "READFLOAT", "WRITEFLOAT", "READBOOLEAN", "PRINTBOOLEAN", "READSTRING", 
            "PRINTSTRING", "SUPER", "PREVENTDEFAULT", "ADD", "MINUS", "MUL", 
            "DIV", "MODUL", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS_THAN", 
            "LESS_EQUAL", "GREATER_THAN", "GREATER_EQUAL", "DOUBLE_COLON", 
            "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", "LB", 
            "RB", "ASSIGN", "COMMENT", "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", 
            "STRING_LIT", "ARRAY_LIT", "IDENTIFIER", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
                  "READINTEGER", "PRINTINTEGER", "READFLOAT", "WRITEFLOAT", 
                  "READBOOLEAN", "PRINTBOOLEAN", "READSTRING", "PRINTSTRING", 
                  "SUPER", "PREVENTDEFAULT", "ADD", "MINUS", "MUL", "DIV", 
                  "MODUL", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS_THAN", 
                  "LESS_EQUAL", "GREATER_THAN", "GREATER_EQUAL", "DOUBLE_COLON", 
                  "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", 
                  "LB", "RB", "ASSIGN", "CPPCOMMENT", "CCOMMENT", "UPPERCASE", 
                  "LOWERCASE", "LETTER", "UNDERSCORE", "DIGIT", "INTPART", 
                  "FRACPART", "SIGN", "EXPPART", "TRUE", "FALSE", "NOTESC", 
                  "ESC", "CHAR", "EXPS", "INTS", "FLOATS", "STRINGS", "COMMENT", 
                  "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", 
                  "ARRAY_LIT", "IDENTIFIER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[77] = self.INTEGER_LIT_action 
            actions[78] = self.FLOAT_LIT_action 
            actions[80] = self.STRING_LIT_action 
            actions[84] = self.UNCLOSE_STRING_action 
            actions[85] = self.ILLEGAL_ESCAPE_action 
            actions[86] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGER_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.text = self.text.replace("_","") 
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             self.text = self.text.replace("_","") 
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             self.text = str(self.text[1:-1]) 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		raise UncloseString(self.text[1:]) if self.text[len(self.text)-1] != '\n' and self.text[len(self.text)-1] != '\r' else UncloseString(self.text[1:-1])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


