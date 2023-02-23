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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u0220\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(")
        buf.write("\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3")
        buf.write("\60\3\60\7\60\u014e\n\60\f\60\16\60\u0151\13\60\3\61\3")
        buf.write("\61\3\61\3\61\7\61\u0157\n\61\f\61\16\61\u015a\13\61\3")
        buf.write("\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\5\64\u0165")
        buf.write("\n\64\3\65\3\65\3\66\3\66\3\67\3\67\3\67\7\67\u016e\n")
        buf.write("\67\f\67\16\67\u0171\13\67\3\67\3\67\6\67\u0175\n\67\r")
        buf.write("\67\16\67\u0176\7\67\u0179\n\67\f\67\16\67\u017c\13\67")
        buf.write("\5\67\u017e\n\67\38\38\78\u0182\n8\f8\168\u0185\138\3")
        buf.write("9\39\3:\3:\5:\u018b\n:\3:\6:\u018e\n:\r:\16:\u018f\3;")
        buf.write("\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3=\3=\3=\3>\3>\3>\3>\7")
        buf.write(">\u01a4\n>\f>\16>\u01a7\13>\3>\3>\3>\3?\3?\3?\5?\u01af")
        buf.write("\n?\3@\3@\3@\3@\3@\5@\u01b6\n@\3A\3A\3A\3A\3A\5A\u01bd")
        buf.write("\nA\3B\3B\3B\3B\3B\5B\u01c4\nB\3C\3C\5C\u01c8\nC\3C\3")
        buf.write("C\3D\3D\3D\3E\3E\3E\5E\u01d2\nE\3E\3E\3E\3E\3E\3E\3E\3")
        buf.write("E\3E\5E\u01dd\nE\3E\3E\3F\3F\5F\u01e3\nF\3G\3G\3G\3G\7")
        buf.write("G\u01e9\nG\fG\16G\u01ec\13G\3G\3G\3G\3H\3H\5H\u01f3\n")
        buf.write("H\3H\3H\3I\3I\5I\u01f9\nI\3I\3I\3I\7I\u01fe\nI\fI\16I")
        buf.write("\u0201\13I\3J\6J\u0204\nJ\rJ\16J\u0205\3J\3J\3K\3K\3K")
        buf.write("\7K\u020d\nK\fK\16K\u0210\13K\3K\3K\3L\3L\7L\u0216\nL")
        buf.write("\fL\16L\u0219\13L\3L\3L\3L\3M\3M\3M\6\u0158\u01a5\u020e")
        buf.write("\u0217\2N\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\2a\2c\2e\2g\2i\2k\2m\2o")
        buf.write("\2q\2s\2u\2w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\61")
        buf.write("\u0087\62\u0089\63\u008b\64\u008d\65\u008f\66\u0091\67")
        buf.write("\u00938\u00959\u0097:\u0099;\3\2\r\4\2\f\f\17\17\3\2C")
        buf.write("\\\3\2c|\3\2\62;\3\2\63;\4\2--//\4\2GGgg\t\2))^^ddhhp")
        buf.write("pttvv\6\2\f\f\17\17$$^^\5\2\13\f\17\17\"\"\4\2$$^^\2\u022f")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2")
        buf.write("\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\3\u009b\3\2\2\2\5\u009e\3\2\2\2\7\u00a3")
        buf.write("\3\2\2\2\t\u00a9\3\2\2\2\13\u00b1\3\2\2\2\r\u00b4\3\2")
        buf.write("\2\2\17\u00b9\3\2\2\2\21\u00bf\3\2\2\2\23\u00c3\3\2\2")
        buf.write("\2\25\u00cc\3\2\2\2\27\u00cf\3\2\2\2\31\u00d7\3\2\2\2")
        buf.write("\33\u00de\3\2\2\2\35\u00e5\3\2\2\2\37\u00eb\3\2\2\2!\u00f0")
        buf.write("\3\2\2\2#\u00f4\3\2\2\2%\u00fd\3\2\2\2\'\u0100\3\2\2\2")
        buf.write(")\u0108\3\2\2\2+\u010e\3\2\2\2-\u0110\3\2\2\2/\u0112\3")
        buf.write("\2\2\2\61\u0114\3\2\2\2\63\u0116\3\2\2\2\65\u0118\3\2")
        buf.write("\2\2\67\u011a\3\2\2\29\u011d\3\2\2\2;\u0120\3\2\2\2=\u0123")
        buf.write("\3\2\2\2?\u0126\3\2\2\2A\u0128\3\2\2\2C\u012b\3\2\2\2")
        buf.write("E\u012d\3\2\2\2G\u0130\3\2\2\2I\u0133\3\2\2\2K\u0135\3")
        buf.write("\2\2\2M\u0137\3\2\2\2O\u0139\3\2\2\2Q\u013b\3\2\2\2S\u013d")
        buf.write("\3\2\2\2U\u013f\3\2\2\2W\u0141\3\2\2\2Y\u0143\3\2\2\2")
        buf.write("[\u0145\3\2\2\2]\u0147\3\2\2\2_\u0149\3\2\2\2a\u0152\3")
        buf.write("\2\2\2c\u015e\3\2\2\2e\u0160\3\2\2\2g\u0164\3\2\2\2i\u0166")
        buf.write("\3\2\2\2k\u0168\3\2\2\2m\u017d\3\2\2\2o\u017f\3\2\2\2")
        buf.write("q\u0186\3\2\2\2s\u0188\3\2\2\2u\u0191\3\2\2\2w\u0196\3")
        buf.write("\2\2\2y\u019c\3\2\2\2{\u019f\3\2\2\2}\u01ae\3\2\2\2\177")
        buf.write("\u01b5\3\2\2\2\u0081\u01bc\3\2\2\2\u0083\u01c3\3\2\2\2")
        buf.write("\u0085\u01c7\3\2\2\2\u0087\u01cb\3\2\2\2\u0089\u01dc\3")
        buf.write("\2\2\2\u008b\u01e2\3\2\2\2\u008d\u01e4\3\2\2\2\u008f\u01f0")
        buf.write("\3\2\2\2\u0091\u01f8\3\2\2\2\u0093\u0203\3\2\2\2\u0095")
        buf.write("\u0209\3\2\2\2\u0097\u0217\3\2\2\2\u0099\u021d\3\2\2\2")
        buf.write("\u009b\u009c\7}\2\2\u009c\u009d\7\177\2\2\u009d\4\3\2")
        buf.write("\2\2\u009e\u009f\7c\2\2\u009f\u00a0\7w\2\2\u00a0\u00a1")
        buf.write("\7v\2\2\u00a1\u00a2\7q\2\2\u00a2\6\3\2\2\2\u00a3\u00a4")
        buf.write("\7d\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6\7g\2\2\u00a6\u00a7")
        buf.write("\7c\2\2\u00a7\u00a8\7m\2\2\u00a8\b\3\2\2\2\u00a9\u00aa")
        buf.write("\7d\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad")
        buf.write("\7n\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7c\2\2\u00af\u00b0")
        buf.write("\7p\2\2\u00b0\n\3\2\2\2\u00b1\u00b2\7f\2\2\u00b2\u00b3")
        buf.write("\7q\2\2\u00b3\f\3\2\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6")
        buf.write("\7n\2\2\u00b6\u00b7\7u\2\2\u00b7\u00b8\7g\2\2\u00b8\16")
        buf.write("\3\2\2\2\u00b9\u00ba\7h\2\2\u00ba\u00bb\7n\2\2\u00bb\u00bc")
        buf.write("\7q\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be\7v\2\2\u00be\20")
        buf.write("\3\2\2\2\u00bf\u00c0\7h\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2")
        buf.write("\7t\2\2\u00c2\22\3\2\2\2\u00c3\u00c4\7h\2\2\u00c4\u00c5")
        buf.write("\7w\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7e\2\2\u00c7\u00c8")
        buf.write("\7v\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb")
        buf.write("\7p\2\2\u00cb\24\3\2\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce")
        buf.write("\7h\2\2\u00ce\26\3\2\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4")
        buf.write("\7i\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6\7t\2\2\u00d6\30")
        buf.write("\3\2\2\2\u00d7\u00d8\7t\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da")
        buf.write("\7v\2\2\u00da\u00db\7w\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd")
        buf.write("\7p\2\2\u00dd\32\3\2\2\2\u00de\u00df\7u\2\2\u00df\u00e0")
        buf.write("\7v\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3")
        buf.write("\7p\2\2\u00e3\u00e4\7i\2\2\u00e4\34\3\2\2\2\u00e5\u00e6")
        buf.write("\7y\2\2\u00e6\u00e7\7j\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9")
        buf.write("\7n\2\2\u00e9\u00ea\7g\2\2\u00ea\36\3\2\2\2\u00eb\u00ec")
        buf.write("\7x\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef")
        buf.write("\7f\2\2\u00ef \3\2\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2")
        buf.write("\7w\2\2\u00f2\u00f3\7v\2\2\u00f3\"\3\2\2\2\u00f4\u00f5")
        buf.write("\7e\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8")
        buf.write("\7v\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb")
        buf.write("\7w\2\2\u00fb\u00fc\7g\2\2\u00fc$\3\2\2\2\u00fd\u00fe")
        buf.write("\7q\2\2\u00fe\u00ff\7h\2\2\u00ff&\3\2\2\2\u0100\u0101")
        buf.write("\7k\2\2\u0101\u0102\7p\2\2\u0102\u0103\7j\2\2\u0103\u0104")
        buf.write("\7g\2\2\u0104\u0105\7t\2\2\u0105\u0106\7k\2\2\u0106\u0107")
        buf.write("\7v\2\2\u0107(\3\2\2\2\u0108\u0109\7c\2\2\u0109\u010a")
        buf.write("\7t\2\2\u010a\u010b\7t\2\2\u010b\u010c\7c\2\2\u010c\u010d")
        buf.write("\7{\2\2\u010d*\3\2\2\2\u010e\u010f\7-\2\2\u010f,\3\2\2")
        buf.write("\2\u0110\u0111\7/\2\2\u0111.\3\2\2\2\u0112\u0113\7,\2")
        buf.write("\2\u0113\60\3\2\2\2\u0114\u0115\7\61\2\2\u0115\62\3\2")
        buf.write("\2\2\u0116\u0117\7\'\2\2\u0117\64\3\2\2\2\u0118\u0119")
        buf.write("\7#\2\2\u0119\66\3\2\2\2\u011a\u011b\7(\2\2\u011b\u011c")
        buf.write("\7(\2\2\u011c8\3\2\2\2\u011d\u011e\7~\2\2\u011e\u011f")
        buf.write("\7~\2\2\u011f:\3\2\2\2\u0120\u0121\7?\2\2\u0121\u0122")
        buf.write("\7?\2\2\u0122<\3\2\2\2\u0123\u0124\7#\2\2\u0124\u0125")
        buf.write("\7?\2\2\u0125>\3\2\2\2\u0126\u0127\7>\2\2\u0127@\3\2\2")
        buf.write("\2\u0128\u0129\7>\2\2\u0129\u012a\7?\2\2\u012aB\3\2\2")
        buf.write("\2\u012b\u012c\7@\2\2\u012cD\3\2\2\2\u012d\u012e\7@\2")
        buf.write("\2\u012e\u012f\7?\2\2\u012fF\3\2\2\2\u0130\u0131\7<\2")
        buf.write("\2\u0131\u0132\7<\2\2\u0132H\3\2\2\2\u0133\u0134\7*\2")
        buf.write("\2\u0134J\3\2\2\2\u0135\u0136\7+\2\2\u0136L\3\2\2\2\u0137")
        buf.write("\u0138\7]\2\2\u0138N\3\2\2\2\u0139\u013a\7_\2\2\u013a")
        buf.write("P\3\2\2\2\u013b\u013c\7\60\2\2\u013cR\3\2\2\2\u013d\u013e")
        buf.write("\7.\2\2\u013eT\3\2\2\2\u013f\u0140\7=\2\2\u0140V\3\2\2")
        buf.write("\2\u0141\u0142\7<\2\2\u0142X\3\2\2\2\u0143\u0144\7}\2")
        buf.write("\2\u0144Z\3\2\2\2\u0145\u0146\7\177\2\2\u0146\\\3\2\2")
        buf.write("\2\u0147\u0148\7?\2\2\u0148^\3\2\2\2\u0149\u014a\7\61")
        buf.write("\2\2\u014a\u014b\7\61\2\2\u014b\u014f\3\2\2\2\u014c\u014e")
        buf.write("\n\2\2\2\u014d\u014c\3\2\2\2\u014e\u0151\3\2\2\2\u014f")
        buf.write("\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150`\3\2\2\2\u0151")
        buf.write("\u014f\3\2\2\2\u0152\u0153\7\61\2\2\u0153\u0154\7,\2\2")
        buf.write("\u0154\u0158\3\2\2\2\u0155\u0157\13\2\2\2\u0156\u0155")
        buf.write("\3\2\2\2\u0157\u015a\3\2\2\2\u0158\u0159\3\2\2\2\u0158")
        buf.write("\u0156\3\2\2\2\u0159\u015b\3\2\2\2\u015a\u0158\3\2\2\2")
        buf.write("\u015b\u015c\7,\2\2\u015c\u015d\7\61\2\2\u015db\3\2\2")
        buf.write("\2\u015e\u015f\t\3\2\2\u015fd\3\2\2\2\u0160\u0161\t\4")
        buf.write("\2\2\u0161f\3\2\2\2\u0162\u0165\5c\62\2\u0163\u0165\5")
        buf.write("e\63\2\u0164\u0162\3\2\2\2\u0164\u0163\3\2\2\2\u0165h")
        buf.write("\3\2\2\2\u0166\u0167\7a\2\2\u0167j\3\2\2\2\u0168\u0169")
        buf.write("\t\5\2\2\u0169l\3\2\2\2\u016a\u017e\7\62\2\2\u016b\u016f")
        buf.write("\t\6\2\2\u016c\u016e\5k\66\2\u016d\u016c\3\2\2\2\u016e")
        buf.write("\u0171\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170\u017a\3\2\2\2\u0171\u016f\3\2\2\2\u0172\u0174\5")
        buf.write("i\65\2\u0173\u0175\5k\66\2\u0174\u0173\3\2\2\2\u0175\u0176")
        buf.write("\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177")
        buf.write("\u0179\3\2\2\2\u0178\u0172\3\2\2\2\u0179\u017c\3\2\2\2")
        buf.write("\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017e\3")
        buf.write("\2\2\2\u017c\u017a\3\2\2\2\u017d\u016a\3\2\2\2\u017d\u016b")
        buf.write("\3\2\2\2\u017en\3\2\2\2\u017f\u0183\7\60\2\2\u0180\u0182")
        buf.write("\5k\66\2\u0181\u0180\3\2\2\2\u0182\u0185\3\2\2\2\u0183")
        buf.write("\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184p\3\2\2\2\u0185")
        buf.write("\u0183\3\2\2\2\u0186\u0187\t\7\2\2\u0187r\3\2\2\2\u0188")
        buf.write("\u018a\t\b\2\2\u0189\u018b\5q9\2\u018a\u0189\3\2\2\2\u018a")
        buf.write("\u018b\3\2\2\2\u018b\u018d\3\2\2\2\u018c\u018e\5k\66\2")
        buf.write("\u018d\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u018d\3")
        buf.write("\2\2\2\u018f\u0190\3\2\2\2\u0190t\3\2\2\2\u0191\u0192")
        buf.write("\7v\2\2\u0192\u0193\7t\2\2\u0193\u0194\7w\2\2\u0194\u0195")
        buf.write("\7g\2\2\u0195v\3\2\2\2\u0196\u0197\7h\2\2\u0197\u0198")
        buf.write("\7c\2\2\u0198\u0199\7n\2\2\u0199\u019a\7u\2\2\u019a\u019b")
        buf.write("\7g\2\2\u019bx\3\2\2\2\u019c\u019d\7^\2\2\u019d\u019e")
        buf.write("\t\t\2\2\u019ez\3\2\2\2\u019f\u01a0\7^\2\2\u01a0\u01a1")
        buf.write("\7$\2\2\u01a1\u01a5\3\2\2\2\u01a2\u01a4\13\2\2\2\u01a3")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a6\3\2\2\2")
        buf.write("\u01a5\u01a3\3\2\2\2\u01a6\u01a8\3\2\2\2\u01a7\u01a5\3")
        buf.write("\2\2\2\u01a8\u01a9\7^\2\2\u01a9\u01aa\7$\2\2\u01aa|\3")
        buf.write("\2\2\2\u01ab\u01af\5\177@\2\u01ac\u01af\5\u0081A\2\u01ad")
        buf.write("\u01af\5\u0083B\2\u01ae\u01ab\3\2\2\2\u01ae\u01ac\3\2")
        buf.write("\2\2\u01ae\u01ad\3\2\2\2\u01af~\3\2\2\2\u01b0\u01b1\5")
        buf.write("\u0087D\2\u01b1\u01b2\5S*\2\u01b2\u01b3\5\177@\2\u01b3")
        buf.write("\u01b6\3\2\2\2\u01b4\u01b6\5\u0087D\2\u01b5\u01b0\3\2")
        buf.write("\2\2\u01b5\u01b4\3\2\2\2\u01b6\u0080\3\2\2\2\u01b7\u01b8")
        buf.write("\5\u0089E\2\u01b8\u01b9\5S*\2\u01b9\u01ba\5\u0081A\2\u01ba")
        buf.write("\u01bd\3\2\2\2\u01bb\u01bd\5\u0089E\2\u01bc\u01b7\3\2")
        buf.write("\2\2\u01bc\u01bb\3\2\2\2\u01bd\u0082\3\2\2\2\u01be\u01bf")
        buf.write("\5\u008dG\2\u01bf\u01c0\5S*\2\u01c0\u01c1\5\u0083B\2\u01c1")
        buf.write("\u01c4\3\2\2\2\u01c2\u01c4\5\u008dG\2\u01c3\u01be\3\2")
        buf.write("\2\2\u01c3\u01c2\3\2\2\2\u01c4\u0084\3\2\2\2\u01c5\u01c8")
        buf.write("\5_\60\2\u01c6\u01c8\5a\61\2\u01c7\u01c5\3\2\2\2\u01c7")
        buf.write("\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca\bC\2\2")
        buf.write("\u01ca\u0086\3\2\2\2\u01cb\u01cc\5m\67\2\u01cc\u01cd\b")
        buf.write("D\3\2\u01cd\u0088\3\2\2\2\u01ce\u01cf\5m\67\2\u01cf\u01d1")
        buf.write("\5o8\2\u01d0\u01d2\5s:\2\u01d1\u01d0\3\2\2\2\u01d1\u01d2")
        buf.write("\3\2\2\2\u01d2\u01dd\3\2\2\2\u01d3\u01d4\5m\67\2\u01d4")
        buf.write("\u01d5\5s:\2\u01d5\u01dd\3\2\2\2\u01d6\u01d7\5m\67\2\u01d7")
        buf.write("\u01d8\5o8\2\u01d8\u01dd\3\2\2\2\u01d9\u01da\5o8\2\u01da")
        buf.write("\u01db\5s:\2\u01db\u01dd\3\2\2\2\u01dc\u01ce\3\2\2\2\u01dc")
        buf.write("\u01d3\3\2\2\2\u01dc\u01d6\3\2\2\2\u01dc\u01d9\3\2\2\2")
        buf.write("\u01dd\u01de\3\2\2\2\u01de\u01df\bE\4\2\u01df\u008a\3")
        buf.write("\2\2\2\u01e0\u01e3\5u;\2\u01e1\u01e3\5w<\2\u01e2\u01e0")
        buf.write("\3\2\2\2\u01e2\u01e1\3\2\2\2\u01e3\u008c\3\2\2\2\u01e4")
        buf.write("\u01ea\7$\2\2\u01e5\u01e9\5y=\2\u01e6\u01e9\n\n\2\2\u01e7")
        buf.write("\u01e9\5{>\2\u01e8\u01e5\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8")
        buf.write("\u01e7\3\2\2\2\u01e9\u01ec\3\2\2\2\u01ea\u01e8\3\2\2\2")
        buf.write("\u01ea\u01eb\3\2\2\2\u01eb\u01ed\3\2\2\2\u01ec\u01ea\3")
        buf.write("\2\2\2\u01ed\u01ee\7$\2\2\u01ee\u01ef\bG\5\2\u01ef\u008e")
        buf.write("\3\2\2\2\u01f0\u01f2\5Y-\2\u01f1\u01f3\5}?\2\u01f2\u01f1")
        buf.write("\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4")
        buf.write("\u01f5\5[.\2\u01f5\u0090\3\2\2\2\u01f6\u01f9\5g\64\2\u01f7")
        buf.write("\u01f9\5i\65\2\u01f8\u01f6\3\2\2\2\u01f8\u01f7\3\2\2\2")
        buf.write("\u01f9\u01ff\3\2\2\2\u01fa\u01fe\5g\64\2\u01fb\u01fe\5")
        buf.write("i\65\2\u01fc\u01fe\5k\66\2\u01fd\u01fa\3\2\2\2\u01fd\u01fb")
        buf.write("\3\2\2\2\u01fd\u01fc\3\2\2\2\u01fe\u0201\3\2\2\2\u01ff")
        buf.write("\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0092\3\2\2\2")
        buf.write("\u0201\u01ff\3\2\2\2\u0202\u0204\t\13\2\2\u0203\u0202")
        buf.write("\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0203\3\2\2\2\u0205")
        buf.write("\u0206\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0208\bJ\2\2")
        buf.write("\u0208\u0094\3\2\2\2\u0209\u020e\7$\2\2\u020a\u020d\n")
        buf.write("\f\2\2\u020b\u020d\5{>\2\u020c\u020a\3\2\2\2\u020c\u020b")
        buf.write("\3\2\2\2\u020d\u0210\3\2\2\2\u020e\u020f\3\2\2\2\u020e")
        buf.write("\u020c\3\2\2\2\u020f\u0211\3\2\2\2\u0210\u020e\3\2\2\2")
        buf.write("\u0211\u0212\bK\6\2\u0212\u0096\3\2\2\2\u0213\u0216\n")
        buf.write("\f\2\2\u0214\u0216\5{>\2\u0215\u0213\3\2\2\2\u0215\u0214")
        buf.write("\3\2\2\2\u0216\u0219\3\2\2\2\u0217\u0218\3\2\2\2\u0217")
        buf.write("\u0215\3\2\2\2\u0218\u021a\3\2\2\2\u0219\u0217\3\2\2\2")
        buf.write("\u021a\u021b\7$\2\2\u021b\u021c\bL\7\2\u021c\u0098\3\2")
        buf.write("\2\2\u021d\u021e\13\2\2\2\u021e\u021f\bM\b\2\u021f\u009a")
        buf.write("\3\2\2\2!\2\u014f\u0158\u0164\u016f\u0176\u017a\u017d")
        buf.write("\u0183\u018a\u018f\u01a5\u01ae\u01b5\u01bc\u01c3\u01c7")
        buf.write("\u01d1\u01dc\u01e2\u01e8\u01ea\u01f2\u01f8\u01fd\u01ff")
        buf.write("\u0205\u020c\u020e\u0215\u0217\t\b\2\2\3D\2\3E\3\3G\4")
        buf.write("\3K\5\3L\6\3M\7")
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
    ADD = 21
    MINUS = 22
    MUL = 23
    DIV = 24
    MODUL = 25
    NOT = 26
    AND = 27
    OR = 28
    EQUAL = 29
    NOT_EQUAL = 30
    LESS_THAN = 31
    LESS_EQUAL = 32
    GREATER_THAN = 33
    GREATER_EQUAL = 34
    DOUBLE_COLON = 35
    LP = 36
    RP = 37
    LSB = 38
    RSB = 39
    DOT = 40
    COMMA = 41
    SEMI = 42
    COLON = 43
    LB = 44
    RB = 45
    ASSIGN = 46
    COMMENT = 47
    INTEGER_LIT = 48
    FLOAT_LIT = 49
    BOOLEAN_LIT = 50
    STRING_LIT = 51
    ARRAY_LIT = 52
    IDENTIFIER = 53
    WS = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    ERROR_CHAR = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{}'", "'auto'", "'break'", "'boolean'", "'do'", "'else'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'while'", "'void'", "'out'", "'continue'", "'of'", 
            "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
            "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'::'", "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", 
            "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", 
            "IF", "INTEGER", "RETURN", "STRING", "WHILE", "VOID", "OUT", 
            "CONTINUE", "OF", "INHERIT", "ARRAY", "ADD", "MINUS", "MUL", 
            "DIV", "MODUL", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS_THAN", 
            "LESS_EQUAL", "GREATER_THAN", "GREATER_EQUAL", "DOUBLE_COLON", 
            "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", "LB", 
            "RB", "ASSIGN", "COMMENT", "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", 
            "STRING_LIT", "ARRAY_LIT", "IDENTIFIER", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
                  "ADD", "MINUS", "MUL", "DIV", "MODUL", "NOT", "AND", "OR", 
                  "EQUAL", "NOT_EQUAL", "LESS_THAN", "LESS_EQUAL", "GREATER_THAN", 
                  "GREATER_EQUAL", "DOUBLE_COLON", "LP", "RP", "LSB", "RSB", 
                  "DOT", "COMMA", "SEMI", "COLON", "LB", "RB", "ASSIGN", 
                  "CPPCOMMENT", "CCOMMENT", "UPPERCASE", "LOWERCASE", "LETTER", 
                  "UNDERSCORE", "DIGIT", "INTPART", "FRACPART", "SIGN", 
                  "EXPPART", "TRUE", "FALSE", "ESC", "CHAR", "EXPS", "INTS", 
                  "FLOATS", "STRINGS", "COMMENT", "INTEGER_LIT", "FLOAT_LIT", 
                  "BOOLEAN_LIT", "STRING_LIT", "ARRAY_LIT", "IDENTIFIER", 
                  "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[66] = self.INTEGER_LIT_action 
            actions[67] = self.FLOAT_LIT_action 
            actions[69] = self.STRING_LIT_action 
            actions[73] = self.UNCLOSE_STRING_action 
            actions[74] = self.ILLEGAL_ESCAPE_action 
            actions[75] = self.ERROR_CHAR_action 
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
             self.text = self.text[1:-1] 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


