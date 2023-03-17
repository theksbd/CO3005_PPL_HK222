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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u02b8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3")
        buf.write("+\3+\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3;\3;\3;\3;\7;\u01db\n;\f;\16")
        buf.write(";\u01de\13;\3<\3<\3<\3<\7<\u01e4\n<\f<\16<\u01e7\13<\3")
        buf.write("<\3<\3<\3=\3=\3>\3>\3?\3?\5?\u01f2\n?\3@\3@\3A\3A\3B\3")
        buf.write("B\3B\7B\u01fb\nB\fB\16B\u01fe\13B\3B\3B\6B\u0202\nB\r")
        buf.write("B\16B\u0203\7B\u0206\nB\fB\16B\u0209\13B\5B\u020b\nB\3")
        buf.write("C\3C\7C\u020f\nC\fC\16C\u0212\13C\3D\3D\3E\3E\5E\u0218")
        buf.write("\nE\3E\6E\u021b\nE\rE\16E\u021c\3F\3F\3F\3F\3F\3G\3G\3")
        buf.write("G\3G\3G\3G\3H\3H\3H\3I\3I\3I\3J\3J\3J\3J\3J\3J\7J\u0236")
        buf.write("\nJ\fJ\16J\u0239\13J\3J\3J\3J\3K\3K\3K\5K\u0241\nK\3L")
        buf.write("\3L\3L\3L\3L\5L\u0248\nL\3M\3M\3M\3M\3M\5M\u024f\nM\3")
        buf.write("N\3N\3N\3N\3N\5N\u0256\nN\3O\3O\5O\u025a\nO\3O\3O\3P\3")
        buf.write("P\3P\3Q\3Q\3Q\5Q\u0264\nQ\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\5")
        buf.write("Q\u026f\nQ\3Q\3Q\3R\3R\5R\u0275\nR\3S\3S\3S\3S\7S\u027b")
        buf.write("\nS\fS\16S\u027e\13S\3S\3S\3S\3T\3T\5T\u0285\nT\3T\3T")
        buf.write("\3U\3U\5U\u028b\nU\3U\3U\3U\7U\u0290\nU\fU\16U\u0293\13")
        buf.write("U\3V\6V\u0296\nV\rV\16V\u0297\3V\3V\3W\3W\3W\3W\7W\u02a0")
        buf.write("\nW\fW\16W\u02a3\13W\3W\5W\u02a6\nW\3W\3W\3X\3X\3X\3X")
        buf.write("\7X\u02ae\nX\fX\16X\u02b1\13X\3X\3X\3X\3Y\3Y\3Y\5\u01e5")
        buf.write("\u0237\u02a1\2Z\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m8o9q:s;u\2w\2y\2{\2}\2\177\2\u0081\2\u0083\2")
        buf.write("\u0085\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091")
        buf.write("\2\u0093\2\u0095\2\u0097\2\u0099\2\u009b\2\u009d<\u009f")
        buf.write("=\u00a1>\u00a3?\u00a5@\u00a7A\u00a9B\u00abC\u00adD\u00af")
        buf.write("E\u00b1F\3\2\16\4\2\f\f\17\17\3\2C\\\3\2c|\3\2\62;\3\2")
        buf.write("\63;\4\2--//\4\2GGgg\n\2$$))^^ddhhppttvv\5\2\f\f$$^^\5")
        buf.write("\2\13\f\17\17\"\"\4\2$$^^\4\3\f\f\17\17\2\u02ca\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2")
        buf.write("\2\2\2s\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af")
        buf.write("\3\2\2\2\2\u00b1\3\2\2\2\3\u00b3\3\2\2\2\5\u00b6\3\2\2")
        buf.write("\2\7\u00bb\3\2\2\2\t\u00c1\3\2\2\2\13\u00c9\3\2\2\2\r")
        buf.write("\u00cc\3\2\2\2\17\u00d1\3\2\2\2\21\u00d7\3\2\2\2\23\u00db")
        buf.write("\3\2\2\2\25\u00e4\3\2\2\2\27\u00e7\3\2\2\2\31\u00ef\3")
        buf.write("\2\2\2\33\u00f6\3\2\2\2\35\u00fd\3\2\2\2\37\u0103\3\2")
        buf.write("\2\2!\u0108\3\2\2\2#\u010c\3\2\2\2%\u0115\3\2\2\2\'\u0118")
        buf.write("\3\2\2\2)\u0120\3\2\2\2+\u0126\3\2\2\2-\u0132\3\2\2\2")
        buf.write("/\u013f\3\2\2\2\61\u0149\3\2\2\2\63\u0154\3\2\2\2\65\u0160")
        buf.write("\3\2\2\2\67\u016d\3\2\2\29\u0178\3\2\2\2;\u0184\3\2\2")
        buf.write("\2=\u018a\3\2\2\2?\u0199\3\2\2\2A\u019b\3\2\2\2C\u019d")
        buf.write("\3\2\2\2E\u019f\3\2\2\2G\u01a1\3\2\2\2I\u01a3\3\2\2\2")
        buf.write("K\u01a5\3\2\2\2M\u01a8\3\2\2\2O\u01ab\3\2\2\2Q\u01ae\3")
        buf.write("\2\2\2S\u01b1\3\2\2\2U\u01b3\3\2\2\2W\u01b6\3\2\2\2Y\u01b8")
        buf.write("\3\2\2\2[\u01bb\3\2\2\2]\u01be\3\2\2\2_\u01c0\3\2\2\2")
        buf.write("a\u01c2\3\2\2\2c\u01c4\3\2\2\2e\u01c6\3\2\2\2g\u01c8\3")
        buf.write("\2\2\2i\u01ca\3\2\2\2k\u01cc\3\2\2\2m\u01ce\3\2\2\2o\u01d0")
        buf.write("\3\2\2\2q\u01d2\3\2\2\2s\u01d4\3\2\2\2u\u01d6\3\2\2\2")
        buf.write("w\u01df\3\2\2\2y\u01eb\3\2\2\2{\u01ed\3\2\2\2}\u01f1\3")
        buf.write("\2\2\2\177\u01f3\3\2\2\2\u0081\u01f5\3\2\2\2\u0083\u020a")
        buf.write("\3\2\2\2\u0085\u020c\3\2\2\2\u0087\u0213\3\2\2\2\u0089")
        buf.write("\u0215\3\2\2\2\u008b\u021e\3\2\2\2\u008d\u0223\3\2\2\2")
        buf.write("\u008f\u0229\3\2\2\2\u0091\u022c\3\2\2\2\u0093\u022f\3")
        buf.write("\2\2\2\u0095\u0240\3\2\2\2\u0097\u0247\3\2\2\2\u0099\u024e")
        buf.write("\3\2\2\2\u009b\u0255\3\2\2\2\u009d\u0259\3\2\2\2\u009f")
        buf.write("\u025d\3\2\2\2\u00a1\u026e\3\2\2\2\u00a3\u0274\3\2\2\2")
        buf.write("\u00a5\u0276\3\2\2\2\u00a7\u0282\3\2\2\2\u00a9\u028a\3")
        buf.write("\2\2\2\u00ab\u0295\3\2\2\2\u00ad\u029b\3\2\2\2\u00af\u02a9")
        buf.write("\3\2\2\2\u00b1\u02b5\3\2\2\2\u00b3\u00b4\7}\2\2\u00b4")
        buf.write("\u00b5\7\177\2\2\u00b5\4\3\2\2\2\u00b6\u00b7\7c\2\2\u00b7")
        buf.write("\u00b8\7w\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba\7q\2\2\u00ba")
        buf.write("\6\3\2\2\2\u00bb\u00bc\7d\2\2\u00bc\u00bd\7t\2\2\u00bd")
        buf.write("\u00be\7g\2\2\u00be\u00bf\7c\2\2\u00bf\u00c0\7m\2\2\u00c0")
        buf.write("\b\3\2\2\2\u00c1\u00c2\7d\2\2\u00c2\u00c3\7q\2\2\u00c3")
        buf.write("\u00c4\7q\2\2\u00c4\u00c5\7n\2\2\u00c5\u00c6\7g\2\2\u00c6")
        buf.write("\u00c7\7c\2\2\u00c7\u00c8\7p\2\2\u00c8\n\3\2\2\2\u00c9")
        buf.write("\u00ca\7f\2\2\u00ca\u00cb\7q\2\2\u00cb\f\3\2\2\2\u00cc")
        buf.write("\u00cd\7g\2\2\u00cd\u00ce\7n\2\2\u00ce\u00cf\7u\2\2\u00cf")
        buf.write("\u00d0\7g\2\2\u00d0\16\3\2\2\2\u00d1\u00d2\7h\2\2\u00d2")
        buf.write("\u00d3\7n\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5\7c\2\2\u00d5")
        buf.write("\u00d6\7v\2\2\u00d6\20\3\2\2\2\u00d7\u00d8\7h\2\2\u00d8")
        buf.write("\u00d9\7q\2\2\u00d9\u00da\7t\2\2\u00da\22\3\2\2\2\u00db")
        buf.write("\u00dc\7h\2\2\u00dc\u00dd\7w\2\2\u00dd\u00de\7p\2\2\u00de")
        buf.write("\u00df\7e\2\2\u00df\u00e0\7v\2\2\u00e0\u00e1\7k\2\2\u00e1")
        buf.write("\u00e2\7q\2\2\u00e2\u00e3\7p\2\2\u00e3\24\3\2\2\2\u00e4")
        buf.write("\u00e5\7k\2\2\u00e5\u00e6\7h\2\2\u00e6\26\3\2\2\2\u00e7")
        buf.write("\u00e8\7k\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea\7v\2\2\u00ea")
        buf.write("\u00eb\7g\2\2\u00eb\u00ec\7i\2\2\u00ec\u00ed\7g\2\2\u00ed")
        buf.write("\u00ee\7t\2\2\u00ee\30\3\2\2\2\u00ef\u00f0\7t\2\2\u00f0")
        buf.write("\u00f1\7g\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7w\2\2\u00f3")
        buf.write("\u00f4\7t\2\2\u00f4\u00f5\7p\2\2\u00f5\32\3\2\2\2\u00f6")
        buf.write("\u00f7\7u\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9\7t\2\2\u00f9")
        buf.write("\u00fa\7k\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc\7i\2\2\u00fc")
        buf.write("\34\3\2\2\2\u00fd\u00fe\7y\2\2\u00fe\u00ff\7j\2\2\u00ff")
        buf.write("\u0100\7k\2\2\u0100\u0101\7n\2\2\u0101\u0102\7g\2\2\u0102")
        buf.write("\36\3\2\2\2\u0103\u0104\7x\2\2\u0104\u0105\7q\2\2\u0105")
        buf.write("\u0106\7k\2\2\u0106\u0107\7f\2\2\u0107 \3\2\2\2\u0108")
        buf.write("\u0109\7q\2\2\u0109\u010a\7w\2\2\u010a\u010b\7v\2\2\u010b")
        buf.write("\"\3\2\2\2\u010c\u010d\7e\2\2\u010d\u010e\7q\2\2\u010e")
        buf.write("\u010f\7p\2\2\u010f\u0110\7v\2\2\u0110\u0111\7k\2\2\u0111")
        buf.write("\u0112\7p\2\2\u0112\u0113\7w\2\2\u0113\u0114\7g\2\2\u0114")
        buf.write("$\3\2\2\2\u0115\u0116\7q\2\2\u0116\u0117\7h\2\2\u0117")
        buf.write("&\3\2\2\2\u0118\u0119\7k\2\2\u0119\u011a\7p\2\2\u011a")
        buf.write("\u011b\7j\2\2\u011b\u011c\7g\2\2\u011c\u011d\7t\2\2\u011d")
        buf.write("\u011e\7k\2\2\u011e\u011f\7v\2\2\u011f(\3\2\2\2\u0120")
        buf.write("\u0121\7c\2\2\u0121\u0122\7t\2\2\u0122\u0123\7t\2\2\u0123")
        buf.write("\u0124\7c\2\2\u0124\u0125\7{\2\2\u0125*\3\2\2\2\u0126")
        buf.write("\u0127\7t\2\2\u0127\u0128\7g\2\2\u0128\u0129\7c\2\2\u0129")
        buf.write("\u012a\7f\2\2\u012a\u012b\7K\2\2\u012b\u012c\7p\2\2\u012c")
        buf.write("\u012d\7v\2\2\u012d\u012e\7g\2\2\u012e\u012f\7i\2\2\u012f")
        buf.write("\u0130\7g\2\2\u0130\u0131\7t\2\2\u0131,\3\2\2\2\u0132")
        buf.write("\u0133\7r\2\2\u0133\u0134\7t\2\2\u0134\u0135\7k\2\2\u0135")
        buf.write("\u0136\7p\2\2\u0136\u0137\7v\2\2\u0137\u0138\7K\2\2\u0138")
        buf.write("\u0139\7p\2\2\u0139\u013a\7v\2\2\u013a\u013b\7g\2\2\u013b")
        buf.write("\u013c\7i\2\2\u013c\u013d\7g\2\2\u013d\u013e\7t\2\2\u013e")
        buf.write(".\3\2\2\2\u013f\u0140\7t\2\2\u0140\u0141\7g\2\2\u0141")
        buf.write("\u0142\7c\2\2\u0142\u0143\7f\2\2\u0143\u0144\7H\2\2\u0144")
        buf.write("\u0145\7n\2\2\u0145\u0146\7q\2\2\u0146\u0147\7c\2\2\u0147")
        buf.write("\u0148\7v\2\2\u0148\60\3\2\2\2\u0149\u014a\7y\2\2\u014a")
        buf.write("\u014b\7t\2\2\u014b\u014c\7k\2\2\u014c\u014d\7v\2\2\u014d")
        buf.write("\u014e\7g\2\2\u014e\u014f\7H\2\2\u014f\u0150\7n\2\2\u0150")
        buf.write("\u0151\7q\2\2\u0151\u0152\7c\2\2\u0152\u0153\7v\2\2\u0153")
        buf.write("\62\3\2\2\2\u0154\u0155\7t\2\2\u0155\u0156\7g\2\2\u0156")
        buf.write("\u0157\7c\2\2\u0157\u0158\7f\2\2\u0158\u0159\7D\2\2\u0159")
        buf.write("\u015a\7q\2\2\u015a\u015b\7q\2\2\u015b\u015c\7n\2\2\u015c")
        buf.write("\u015d\7g\2\2\u015d\u015e\7c\2\2\u015e\u015f\7p\2\2\u015f")
        buf.write("\64\3\2\2\2\u0160\u0161\7r\2\2\u0161\u0162\7t\2\2\u0162")
        buf.write("\u0163\7k\2\2\u0163\u0164\7p\2\2\u0164\u0165\7v\2\2\u0165")
        buf.write("\u0166\7D\2\2\u0166\u0167\7q\2\2\u0167\u0168\7q\2\2\u0168")
        buf.write("\u0169\7n\2\2\u0169\u016a\7g\2\2\u016a\u016b\7c\2\2\u016b")
        buf.write("\u016c\7p\2\2\u016c\66\3\2\2\2\u016d\u016e\7t\2\2\u016e")
        buf.write("\u016f\7g\2\2\u016f\u0170\7c\2\2\u0170\u0171\7f\2\2\u0171")
        buf.write("\u0172\7U\2\2\u0172\u0173\7v\2\2\u0173\u0174\7t\2\2\u0174")
        buf.write("\u0175\7k\2\2\u0175\u0176\7p\2\2\u0176\u0177\7i\2\2\u0177")
        buf.write("8\3\2\2\2\u0178\u0179\7r\2\2\u0179\u017a\7t\2\2\u017a")
        buf.write("\u017b\7k\2\2\u017b\u017c\7p\2\2\u017c\u017d\7v\2\2\u017d")
        buf.write("\u017e\7U\2\2\u017e\u017f\7v\2\2\u017f\u0180\7t\2\2\u0180")
        buf.write("\u0181\7k\2\2\u0181\u0182\7p\2\2\u0182\u0183\7i\2\2\u0183")
        buf.write(":\3\2\2\2\u0184\u0185\7u\2\2\u0185\u0186\7w\2\2\u0186")
        buf.write("\u0187\7r\2\2\u0187\u0188\7g\2\2\u0188\u0189\7t\2\2\u0189")
        buf.write("<\3\2\2\2\u018a\u018b\7r\2\2\u018b\u018c\7t\2\2\u018c")
        buf.write("\u018d\7g\2\2\u018d\u018e\7x\2\2\u018e\u018f\7g\2\2\u018f")
        buf.write("\u0190\7p\2\2\u0190\u0191\7v\2\2\u0191\u0192\7F\2\2\u0192")
        buf.write("\u0193\7g\2\2\u0193\u0194\7h\2\2\u0194\u0195\7c\2\2\u0195")
        buf.write("\u0196\7w\2\2\u0196\u0197\7n\2\2\u0197\u0198\7v\2\2\u0198")
        buf.write(">\3\2\2\2\u0199\u019a\7-\2\2\u019a@\3\2\2\2\u019b\u019c")
        buf.write("\7/\2\2\u019cB\3\2\2\2\u019d\u019e\7,\2\2\u019eD\3\2\2")
        buf.write("\2\u019f\u01a0\7\61\2\2\u01a0F\3\2\2\2\u01a1\u01a2\7\'")
        buf.write("\2\2\u01a2H\3\2\2\2\u01a3\u01a4\7#\2\2\u01a4J\3\2\2\2")
        buf.write("\u01a5\u01a6\7(\2\2\u01a6\u01a7\7(\2\2\u01a7L\3\2\2\2")
        buf.write("\u01a8\u01a9\7~\2\2\u01a9\u01aa\7~\2\2\u01aaN\3\2\2\2")
        buf.write("\u01ab\u01ac\7?\2\2\u01ac\u01ad\7?\2\2\u01adP\3\2\2\2")
        buf.write("\u01ae\u01af\7#\2\2\u01af\u01b0\7?\2\2\u01b0R\3\2\2\2")
        buf.write("\u01b1\u01b2\7>\2\2\u01b2T\3\2\2\2\u01b3\u01b4\7>\2\2")
        buf.write("\u01b4\u01b5\7?\2\2\u01b5V\3\2\2\2\u01b6\u01b7\7@\2\2")
        buf.write("\u01b7X\3\2\2\2\u01b8\u01b9\7@\2\2\u01b9\u01ba\7?\2\2")
        buf.write("\u01baZ\3\2\2\2\u01bb\u01bc\7<\2\2\u01bc\u01bd\7<\2\2")
        buf.write("\u01bd\\\3\2\2\2\u01be\u01bf\7*\2\2\u01bf^\3\2\2\2\u01c0")
        buf.write("\u01c1\7+\2\2\u01c1`\3\2\2\2\u01c2\u01c3\7]\2\2\u01c3")
        buf.write("b\3\2\2\2\u01c4\u01c5\7_\2\2\u01c5d\3\2\2\2\u01c6\u01c7")
        buf.write("\7\60\2\2\u01c7f\3\2\2\2\u01c8\u01c9\7.\2\2\u01c9h\3\2")
        buf.write("\2\2\u01ca\u01cb\7=\2\2\u01cbj\3\2\2\2\u01cc\u01cd\7<")
        buf.write("\2\2\u01cdl\3\2\2\2\u01ce\u01cf\7}\2\2\u01cfn\3\2\2\2")
        buf.write("\u01d0\u01d1\7\177\2\2\u01d1p\3\2\2\2\u01d2\u01d3\7?\2")
        buf.write("\2\u01d3r\3\2\2\2\u01d4\u01d5\7$\2\2\u01d5t\3\2\2\2\u01d6")
        buf.write("\u01d7\7\61\2\2\u01d7\u01d8\7\61\2\2\u01d8\u01dc\3\2\2")
        buf.write("\2\u01d9\u01db\n\2\2\2\u01da\u01d9\3\2\2\2\u01db\u01de")
        buf.write("\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd")
        buf.write("v\3\2\2\2\u01de\u01dc\3\2\2\2\u01df\u01e0\7\61\2\2\u01e0")
        buf.write("\u01e1\7,\2\2\u01e1\u01e5\3\2\2\2\u01e2\u01e4\13\2\2\2")
        buf.write("\u01e3\u01e2\3\2\2\2\u01e4\u01e7\3\2\2\2\u01e5\u01e6\3")
        buf.write("\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01e8\3\2\2\2\u01e7\u01e5")
        buf.write("\3\2\2\2\u01e8\u01e9\7,\2\2\u01e9\u01ea\7\61\2\2\u01ea")
        buf.write("x\3\2\2\2\u01eb\u01ec\t\3\2\2\u01ecz\3\2\2\2\u01ed\u01ee")
        buf.write("\t\4\2\2\u01ee|\3\2\2\2\u01ef\u01f2\5y=\2\u01f0\u01f2")
        buf.write("\5{>\2\u01f1\u01ef\3\2\2\2\u01f1\u01f0\3\2\2\2\u01f2~")
        buf.write("\3\2\2\2\u01f3\u01f4\7a\2\2\u01f4\u0080\3\2\2\2\u01f5")
        buf.write("\u01f6\t\5\2\2\u01f6\u0082\3\2\2\2\u01f7\u020b\7\62\2")
        buf.write("\2\u01f8\u01fc\t\6\2\2\u01f9\u01fb\5\u0081A\2\u01fa\u01f9")
        buf.write("\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc")
        buf.write("\u01fd\3\2\2\2\u01fd\u0207\3\2\2\2\u01fe\u01fc\3\2\2\2")
        buf.write("\u01ff\u0201\5\177@\2\u0200\u0202\5\u0081A\2\u0201\u0200")
        buf.write("\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0201\3\2\2\2\u0203")
        buf.write("\u0204\3\2\2\2\u0204\u0206\3\2\2\2\u0205\u01ff\3\2\2\2")
        buf.write("\u0206\u0209\3\2\2\2\u0207\u0205\3\2\2\2\u0207\u0208\3")
        buf.write("\2\2\2\u0208\u020b\3\2\2\2\u0209\u0207\3\2\2\2\u020a\u01f7")
        buf.write("\3\2\2\2\u020a\u01f8\3\2\2\2\u020b\u0084\3\2\2\2\u020c")
        buf.write("\u0210\7\60\2\2\u020d\u020f\5\u0081A\2\u020e\u020d\3\2")
        buf.write("\2\2\u020f\u0212\3\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211")
        buf.write("\3\2\2\2\u0211\u0086\3\2\2\2\u0212\u0210\3\2\2\2\u0213")
        buf.write("\u0214\t\7\2\2\u0214\u0088\3\2\2\2\u0215\u0217\t\b\2\2")
        buf.write("\u0216\u0218\5\u0087D\2\u0217\u0216\3\2\2\2\u0217\u0218")
        buf.write("\3\2\2\2\u0218\u021a\3\2\2\2\u0219\u021b\5\u0081A\2\u021a")
        buf.write("\u0219\3\2\2\2\u021b\u021c\3\2\2\2\u021c\u021a\3\2\2\2")
        buf.write("\u021c\u021d\3\2\2\2\u021d\u008a\3\2\2\2\u021e\u021f\7")
        buf.write("v\2\2\u021f\u0220\7t\2\2\u0220\u0221\7w\2\2\u0221\u0222")
        buf.write("\7g\2\2\u0222\u008c\3\2\2\2\u0223\u0224\7h\2\2\u0224\u0225")
        buf.write("\7c\2\2\u0225\u0226\7n\2\2\u0226\u0227\7u\2\2\u0227\u0228")
        buf.write("\7g\2\2\u0228\u008e\3\2\2\2\u0229\u022a\7^\2\2\u022a\u022b")
        buf.write("\n\t\2\2\u022b\u0090\3\2\2\2\u022c\u022d\7^\2\2\u022d")
        buf.write("\u022e\t\t\2\2\u022e\u0092\3\2\2\2\u022f\u0230\7^\2\2")
        buf.write("\u0230\u0231\7$\2\2\u0231\u0237\3\2\2\2\u0232\u0236\n")
        buf.write("\n\2\2\u0233\u0236\5\u0093J\2\u0234\u0236\5\u0091I\2\u0235")
        buf.write("\u0232\3\2\2\2\u0235\u0233\3\2\2\2\u0235\u0234\3\2\2\2")
        buf.write("\u0236\u0239\3\2\2\2\u0237\u0238\3\2\2\2\u0237\u0235\3")
        buf.write("\2\2\2\u0238\u023a\3\2\2\2\u0239\u0237\3\2\2\2\u023a\u023b")
        buf.write("\7^\2\2\u023b\u023c\7$\2\2\u023c\u0094\3\2\2\2\u023d\u0241")
        buf.write("\5\u0097L\2\u023e\u0241\5\u0099M\2\u023f\u0241\5\u009b")
        buf.write("N\2\u0240\u023d\3\2\2\2\u0240\u023e\3\2\2\2\u0240\u023f")
        buf.write("\3\2\2\2\u0241\u0096\3\2\2\2\u0242\u0243\5\u009fP\2\u0243")
        buf.write("\u0244\5g\64\2\u0244\u0245\5\u0097L\2\u0245\u0248\3\2")
        buf.write("\2\2\u0246\u0248\5\u009fP\2\u0247\u0242\3\2\2\2\u0247")
        buf.write("\u0246\3\2\2\2\u0248\u0098\3\2\2\2\u0249\u024a\5\u00a1")
        buf.write("Q\2\u024a\u024b\5g\64\2\u024b\u024c\5\u0099M\2\u024c\u024f")
        buf.write("\3\2\2\2\u024d\u024f\5\u00a1Q\2\u024e\u0249\3\2\2\2\u024e")
        buf.write("\u024d\3\2\2\2\u024f\u009a\3\2\2\2\u0250\u0251\5\u00a5")
        buf.write("S\2\u0251\u0252\5g\64\2\u0252\u0253\5\u009bN\2\u0253\u0256")
        buf.write("\3\2\2\2\u0254\u0256\5\u00a5S\2\u0255\u0250\3\2\2\2\u0255")
        buf.write("\u0254\3\2\2\2\u0256\u009c\3\2\2\2\u0257\u025a\5u;\2\u0258")
        buf.write("\u025a\5w<\2\u0259\u0257\3\2\2\2\u0259\u0258\3\2\2\2\u025a")
        buf.write("\u025b\3\2\2\2\u025b\u025c\bO\2\2\u025c\u009e\3\2\2\2")
        buf.write("\u025d\u025e\5\u0083B\2\u025e\u025f\bP\3\2\u025f\u00a0")
        buf.write("\3\2\2\2\u0260\u0261\5\u0083B\2\u0261\u0263\5\u0085C\2")
        buf.write("\u0262\u0264\5\u0089E\2\u0263\u0262\3\2\2\2\u0263\u0264")
        buf.write("\3\2\2\2\u0264\u026f\3\2\2\2\u0265\u0266\5\u0083B\2\u0266")
        buf.write("\u0267\5\u0089E\2\u0267\u026f\3\2\2\2\u0268\u0269\5\u0083")
        buf.write("B\2\u0269\u026a\5\u0085C\2\u026a\u026f\3\2\2\2\u026b\u026c")
        buf.write("\5\u0085C\2\u026c\u026d\5\u0089E\2\u026d\u026f\3\2\2\2")
        buf.write("\u026e\u0260\3\2\2\2\u026e\u0265\3\2\2\2\u026e\u0268\3")
        buf.write("\2\2\2\u026e\u026b\3\2\2\2\u026f\u0270\3\2\2\2\u0270\u0271")
        buf.write("\bQ\4\2\u0271\u00a2\3\2\2\2\u0272\u0275\5\u008bF\2\u0273")
        buf.write("\u0275\5\u008dG\2\u0274\u0272\3\2\2\2\u0274\u0273\3\2")
        buf.write("\2\2\u0275\u00a4\3\2\2\2\u0276\u027c\5s:\2\u0277\u027b")
        buf.write("\5\u0091I\2\u0278\u027b\n\n\2\2\u0279\u027b\5\u0093J\2")
        buf.write("\u027a\u0277\3\2\2\2\u027a\u0278\3\2\2\2\u027a\u0279\3")
        buf.write("\2\2\2\u027b\u027e\3\2\2\2\u027c\u027a\3\2\2\2\u027c\u027d")
        buf.write("\3\2\2\2\u027d\u027f\3\2\2\2\u027e\u027c\3\2\2\2\u027f")
        buf.write("\u0280\5s:\2\u0280\u0281\bS\5\2\u0281\u00a6\3\2\2\2\u0282")
        buf.write("\u0284\5m\67\2\u0283\u0285\5\u0095K\2\u0284\u0283\3\2")
        buf.write("\2\2\u0284\u0285\3\2\2\2\u0285\u0286\3\2\2\2\u0286\u0287")
        buf.write("\5o8\2\u0287\u00a8\3\2\2\2\u0288\u028b\5}?\2\u0289\u028b")
        buf.write("\5\177@\2\u028a\u0288\3\2\2\2\u028a\u0289\3\2\2\2\u028b")
        buf.write("\u0291\3\2\2\2\u028c\u0290\5}?\2\u028d\u0290\5\177@\2")
        buf.write("\u028e\u0290\5\u0081A\2\u028f\u028c\3\2\2\2\u028f\u028d")
        buf.write("\3\2\2\2\u028f\u028e\3\2\2\2\u0290\u0293\3\2\2\2\u0291")
        buf.write("\u028f\3\2\2\2\u0291\u0292\3\2\2\2\u0292\u00aa\3\2\2\2")
        buf.write("\u0293\u0291\3\2\2\2\u0294\u0296\t\13\2\2\u0295\u0294")
        buf.write("\3\2\2\2\u0296\u0297\3\2\2\2\u0297\u0295\3\2\2\2\u0297")
        buf.write("\u0298\3\2\2\2\u0298\u0299\3\2\2\2\u0299\u029a\bV\2\2")
        buf.write("\u029a\u00ac\3\2\2\2\u029b\u02a1\5s:\2\u029c\u02a0\n\f")
        buf.write("\2\2\u029d\u02a0\5\u0093J\2\u029e\u02a0\5\u0091I\2\u029f")
        buf.write("\u029c\3\2\2\2\u029f\u029d\3\2\2\2\u029f\u029e\3\2\2\2")
        buf.write("\u02a0\u02a3\3\2\2\2\u02a1\u02a2\3\2\2\2\u02a1\u029f\3")
        buf.write("\2\2\2\u02a2\u02a5\3\2\2\2\u02a3\u02a1\3\2\2\2\u02a4\u02a6")
        buf.write("\t\r\2\2\u02a5\u02a4\3\2\2\2\u02a6\u02a7\3\2\2\2\u02a7")
        buf.write("\u02a8\bW\6\2\u02a8\u00ae\3\2\2\2\u02a9\u02af\5s:\2\u02aa")
        buf.write("\u02ae\n\f\2\2\u02ab\u02ae\5\u0093J\2\u02ac\u02ae\5\u0091")
        buf.write("I\2\u02ad\u02aa\3\2\2\2\u02ad\u02ab\3\2\2\2\u02ad\u02ac")
        buf.write("\3\2\2\2\u02ae\u02b1\3\2\2\2\u02af\u02ad\3\2\2\2\u02af")
        buf.write("\u02b0\3\2\2\2\u02b0\u02b2\3\2\2\2\u02b1\u02af\3\2\2\2")
        buf.write("\u02b2\u02b3\5\u008fH\2\u02b3\u02b4\bX\7\2\u02b4\u00b0")
        buf.write("\3\2\2\2\u02b5\u02b6\13\2\2\2\u02b6\u02b7\bY\b\2\u02b7")
        buf.write("\u00b2\3\2\2\2#\2\u01dc\u01e5\u01f1\u01fc\u0203\u0207")
        buf.write("\u020a\u0210\u0217\u021c\u0235\u0237\u0240\u0247\u024e")
        buf.write("\u0255\u0259\u0263\u026e\u0274\u027a\u027c\u0284\u028a")
        buf.write("\u028f\u0291\u0297\u029f\u02a1\u02a5\u02ad\u02af\t\b\2")
        buf.write("\2\3P\2\3Q\3\3S\4\3W\5\3X\6\3Y\7")
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
    DOUBLE_QUOTE = 57
    COMMENT = 58
    INTEGER_LIT = 59
    FLOAT_LIT = 60
    BOOLEAN_LIT = 61
    STRING_LIT = 62
    ARRAY_LIT = 63
    IDENTIFIER = 64
    WS = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67
    ERROR_CHAR = 68

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
            "'.'", "','", "';'", "':'", "'{'", "'}'", "'='", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", 
            "IF", "INTEGER", "RETURN", "STRING", "WHILE", "VOID", "OUT", 
            "CONTINUE", "OF", "INHERIT", "ARRAY", "READINTEGER", "PRINTINTEGER", 
            "READFLOAT", "WRITEFLOAT", "READBOOLEAN", "PRINTBOOLEAN", "READSTRING", 
            "PRINTSTRING", "SUPER", "PREVENTDEFAULT", "ADD", "MINUS", "MUL", 
            "DIV", "MODUL", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS_THAN", 
            "LESS_EQUAL", "GREATER_THAN", "GREATER_EQUAL", "DOUBLE_COLON", 
            "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", "LB", 
            "RB", "ASSIGN", "DOUBLE_QUOTE", "COMMENT", "INTEGER_LIT", "FLOAT_LIT", 
            "BOOLEAN_LIT", "STRING_LIT", "ARRAY_LIT", "IDENTIFIER", "WS", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
                  "READINTEGER", "PRINTINTEGER", "READFLOAT", "WRITEFLOAT", 
                  "READBOOLEAN", "PRINTBOOLEAN", "READSTRING", "PRINTSTRING", 
                  "SUPER", "PREVENTDEFAULT", "ADD", "MINUS", "MUL", "DIV", 
                  "MODUL", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS_THAN", 
                  "LESS_EQUAL", "GREATER_THAN", "GREATER_EQUAL", "DOUBLE_COLON", 
                  "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", 
                  "LB", "RB", "ASSIGN", "DOUBLE_QUOTE", "CPPCOMMENT", "CCOMMENT", 
                  "UPPERCASE", "LOWERCASE", "LETTER", "UNDERSCORE", "DIGIT", 
                  "INTPART", "FRACPART", "SIGN", "EXPPART", "TRUE", "FALSE", 
                  "NOTESC", "ESC", "CHAR", "EXPS", "INTS", "FLOATS", "STRINGS", 
                  "COMMENT", "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", 
                  "STRING_LIT", "ARRAY_LIT", "IDENTIFIER", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[78] = self.INTEGER_LIT_action 
            actions[79] = self.FLOAT_LIT_action 
            actions[81] = self.STRING_LIT_action 
            actions[85] = self.UNCLOSE_STRING_action 
            actions[86] = self.ILLEGAL_ESCAPE_action 
            actions[87] = self.ERROR_CHAR_action 
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
     


