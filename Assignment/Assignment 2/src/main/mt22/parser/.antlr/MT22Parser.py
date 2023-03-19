# Generated from e:\Bo\Subjects\Principles of Programming Languages\222\Assignment\Assignment 2\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u021c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\6\2\u0086")
        buf.write("\n\2\r\2\16\2\u0087\3\2\3\2\3\3\3\3\5\3\u008e\n\3\3\4")
        buf.write("\3\4\5\4\u0092\n\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\5\6\u009e\n\6\3\7\3\7\3\7\3\7\5\7\u00a4\n\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\5\b\u00ad\n\b\3\b\3\b\3\t\5\t\u00b2")
        buf.write("\n\t\3\t\5\t\u00b5\n\t\3\t\3\t\3\t\3\t\5\t\u00bb\n\t\3")
        buf.write("\n\3\n\3\n\3\n\5\n\u00c1\n\n\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\5\f\u00cd\n\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\5\r\u00d8\n\r\3\16\3\16\5\16\u00dc\n\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\5\17\u00e3\n\17\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u00f3\n\22\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\5\25\u0100\n\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\5\26\u0107\n\26\3\27\3\27\3\27\3\27\3\27\3\27\7")
        buf.write("\27\u010f\n\27\f\27\16\27\u0112\13\27\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\7\30\u011a\n\30\f\30\16\30\u011d\13\30\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\7\31\u0125\n\31\f\31\16\31")
        buf.write("\u0128\13\31\3\32\3\32\3\32\5\32\u012d\n\32\3\33\3\33")
        buf.write("\3\33\5\33\u0132\n\33\3\34\3\34\3\34\3\34\3\34\3\34\5")
        buf.write("\34\u013a\n\34\3\35\3\35\3\35\3\35\3\35\5\35\u0141\n\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u014a\n\36\3")
        buf.write("\37\3\37\5\37\u014e\n\37\3 \3 \3 \3 \3 \5 \u0155\n \3")
        buf.write("!\3!\3!\3!\3!\5!\u015c\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\5\"\u0168\n\"\3#\3#\3#\3#\3#\3$\3$\3$\3$")
        buf.write("\3$\3$\5$\u0175\n$\3%\3%\3%\3%\3%\5%\u017c\n%\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)")
        buf.write("\3)\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3")
        buf.write(".\3.\3.\5.\u01a5\n.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3/\5")
        buf.write("/\u01b2\n/\3\60\3\60\3\60\3\60\3\60\5\60\u01b9\n\60\3")
        buf.write("\61\3\61\5\61\u01bd\n\61\3\62\3\62\3\62\3\62\5\62\u01c3")
        buf.write("\n\62\3\63\3\63\5\63\u01c7\n\63\3\64\3\64\3\64\3\64\5")
        buf.write("\64\u01cd\n\64\3\65\3\65\3\65\3\65\5\65\u01d3\n\65\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\5\66\u01db\n\66\3\67\3\67\3")
        buf.write("\67\3\67\3\67\5\67\u01e2\n\67\38\38\38\38\38\38\38\38")
        buf.write("\38\58\u01ed\n8\39\39\39\39\3:\3:\3:\3:\3:\3;\3;\3;\3")
        buf.write(";\3<\3<\3<\3<\3<\3=\3=\3=\3=\3>\3>\3>\3>\3>\3?\3?\3?\3")
        buf.write("?\3@\3@\3@\3@\3@\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\2\5,.\60")
        buf.write("C\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\2\b\7\2\3\3\5\5\b\b\f\f\16\16\6\2\5\5\b\b\f\f\16\16\3")
        buf.write("\2(-\3\2&\'\3\2 !\3\2\"$\2\u021d\2\u0085\3\2\2\2\4\u008d")
        buf.write("\3\2\2\2\6\u0091\3\2\2\2\b\u0093\3\2\2\2\n\u009d\3\2\2")
        buf.write("\2\f\u009f\3\2\2\2\16\u00a8\3\2\2\2\20\u00b1\3\2\2\2\22")
        buf.write("\u00c0\3\2\2\2\24\u00c2\3\2\2\2\26\u00c4\3\2\2\2\30\u00d7")
        buf.write("\3\2\2\2\32\u00db\3\2\2\2\34\u00e2\3\2\2\2\36\u00e4\3")
        buf.write("\2\2\2 \u00e7\3\2\2\2\"\u00f2\3\2\2\2$\u00f4\3\2\2\2&")
        buf.write("\u00f6\3\2\2\2(\u00ff\3\2\2\2*\u0106\3\2\2\2,\u0108\3")
        buf.write("\2\2\2.\u0113\3\2\2\2\60\u011e\3\2\2\2\62\u012c\3\2\2")
        buf.write("\2\64\u0131\3\2\2\2\66\u0139\3\2\2\28\u0140\3\2\2\2:\u0149")
        buf.write("\3\2\2\2<\u014d\3\2\2\2>\u0154\3\2\2\2@\u015b\3\2\2\2")
        buf.write("B\u0167\3\2\2\2D\u0169\3\2\2\2F\u0174\3\2\2\2H\u0176\3")
        buf.write("\2\2\2J\u017d\3\2\2\2L\u0187\3\2\2\2N\u018b\3\2\2\2P\u018f")
        buf.write("\3\2\2\2R\u0191\3\2\2\2T\u0195\3\2\2\2V\u019b\3\2\2\2")
        buf.write("X\u019e\3\2\2\2Z\u01a1\3\2\2\2\\\u01b1\3\2\2\2^\u01b8")
        buf.write("\3\2\2\2`\u01bc\3\2\2\2b\u01c2\3\2\2\2d\u01c6\3\2\2\2")
        buf.write("f\u01cc\3\2\2\2h\u01d2\3\2\2\2j\u01da\3\2\2\2l\u01e1\3")
        buf.write("\2\2\2n\u01ec\3\2\2\2p\u01ee\3\2\2\2r\u01f2\3\2\2\2t\u01f7")
        buf.write("\3\2\2\2v\u01fb\3\2\2\2x\u0200\3\2\2\2z\u0204\3\2\2\2")
        buf.write("|\u0209\3\2\2\2~\u020d\3\2\2\2\u0080\u0212\3\2\2\2\u0082")
        buf.write("\u0217\3\2\2\2\u0084\u0086\5\4\3\2\u0085\u0084\3\2\2\2")
        buf.write("\u0086\u0087\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3")
        buf.write("\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\7\2\2\3\u008a\3")
        buf.write("\3\2\2\2\u008b\u008e\5\6\4\2\u008c\u008e\5\26\f\2\u008d")
        buf.write("\u008b\3\2\2\2\u008d\u008c\3\2\2\2\u008e\5\3\2\2\2\u008f")
        buf.write("\u0092\5\b\5\2\u0090\u0092\5\16\b\2\u0091\u008f\3\2\2")
        buf.write("\2\u0091\u0090\3\2\2\2\u0092\7\3\2\2\2\u0093\u0094\5\n")
        buf.write("\6\2\u0094\u0095\7\65\2\2\u0095\t\3\2\2\2\u0096\u0097")
        buf.write("\7B\2\2\u0097\u0098\7\64\2\2\u0098\u0099\5\n\6\2\u0099")
        buf.write("\u009a\7\64\2\2\u009a\u009b\5(\25\2\u009b\u009e\3\2\2")
        buf.write("\2\u009c\u009e\5\f\7\2\u009d\u0096\3\2\2\2\u009d\u009c")
        buf.write("\3\2\2\2\u009e\13\3\2\2\2\u009f\u00a0\7B\2\2\u00a0\u00a3")
        buf.write("\7\66\2\2\u00a1\u00a4\5\24\13\2\u00a2\u00a4\5 \21\2\u00a3")
        buf.write("\u00a1\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2")
        buf.write("\u00a5\u00a6\79\2\2\u00a6\u00a7\5(\25\2\u00a7\r\3\2\2")
        buf.write("\2\u00a8\u00a9\5\22\n\2\u00a9\u00ac\7\66\2\2\u00aa\u00ad")
        buf.write("\5\24\13\2\u00ab\u00ad\5 \21\2\u00ac\u00aa\3\2\2\2\u00ac")
        buf.write("\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\7\65\2")
        buf.write("\2\u00af\17\3\2\2\2\u00b0\u00b2\7\24\2\2\u00b1\u00b0\3")
        buf.write("\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b4\3\2\2\2\u00b3\u00b5")
        buf.write("\7\21\2\2\u00b4\u00b3\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5")
        buf.write("\u00b6\3\2\2\2\u00b6\u00b7\7B\2\2\u00b7\u00ba\7\66\2\2")
        buf.write("\u00b8\u00bb\5\24\13\2\u00b9\u00bb\5 \21\2\u00ba\u00b8")
        buf.write("\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\21\3\2\2\2\u00bc\u00bd")
        buf.write("\7B\2\2\u00bd\u00be\7\64\2\2\u00be\u00c1\5\22\n\2\u00bf")
        buf.write("\u00c1\7B\2\2\u00c0\u00bc\3\2\2\2\u00c0\u00bf\3\2\2\2")
        buf.write("\u00c1\23\3\2\2\2\u00c2\u00c3\t\2\2\2\u00c3\25\3\2\2\2")
        buf.write("\u00c4\u00c5\7B\2\2\u00c5\u00c6\7\66\2\2\u00c6\u00c7\7")
        buf.write("\n\2\2\u00c7\u00c8\5\30\r\2\u00c8\u00c9\7/\2\2\u00c9\u00ca")
        buf.write("\5\32\16\2\u00ca\u00cc\7\60\2\2\u00cb\u00cd\5\36\20\2")
        buf.write("\u00cc\u00cb\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\3")
        buf.write("\2\2\2\u00ce\u00cf\5^\60\2\u00cf\27\3\2\2\2\u00d0\u00d8")
        buf.write("\7\5\2\2\u00d1\u00d8\7\f\2\2\u00d2\u00d8\7\b\2\2\u00d3")
        buf.write("\u00d8\7\16\2\2\u00d4\u00d8\7\20\2\2\u00d5\u00d8\7\3\2")
        buf.write("\2\u00d6\u00d8\5 \21\2\u00d7\u00d0\3\2\2\2\u00d7\u00d1")
        buf.write("\3\2\2\2\u00d7\u00d2\3\2\2\2\u00d7\u00d3\3\2\2\2\u00d7")
        buf.write("\u00d4\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d6\3\2\2\2")
        buf.write("\u00d8\31\3\2\2\2\u00d9\u00dc\5\34\17\2\u00da\u00dc\3")
        buf.write("\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00da\3\2\2\2\u00dc\33")
        buf.write("\3\2\2\2\u00dd\u00de\5\20\t\2\u00de\u00df\7\64\2\2\u00df")
        buf.write("\u00e0\5\34\17\2\u00e0\u00e3\3\2\2\2\u00e1\u00e3\5\20")
        buf.write("\t\2\u00e2\u00dd\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3\35")
        buf.write("\3\2\2\2\u00e4\u00e5\7\24\2\2\u00e5\u00e6\7B\2\2\u00e6")
        buf.write("\37\3\2\2\2\u00e7\u00e8\7\25\2\2\u00e8\u00e9\7\61\2\2")
        buf.write("\u00e9\u00ea\5\"\22\2\u00ea\u00eb\7\62\2\2\u00eb\u00ec")
        buf.write("\7\23\2\2\u00ec\u00ed\5$\23\2\u00ed!\3\2\2\2\u00ee\u00ef")
        buf.write("\7=\2\2\u00ef\u00f0\7\64\2\2\u00f0\u00f3\5\"\22\2\u00f1")
        buf.write("\u00f3\7=\2\2\u00f2\u00ee\3\2\2\2\u00f2\u00f1\3\2\2\2")
        buf.write("\u00f3#\3\2\2\2\u00f4\u00f5\t\3\2\2\u00f5%\3\2\2\2\u00f6")
        buf.write("\u00f7\7\67\2\2\u00f7\u00f8\5@!\2\u00f8\u00f9\78\2\2\u00f9")
        buf.write("\'\3\2\2\2\u00fa\u00fb\5*\26\2\u00fb\u00fc\7.\2\2\u00fc")
        buf.write("\u00fd\5*\26\2\u00fd\u0100\3\2\2\2\u00fe\u0100\5*\26\2")
        buf.write("\u00ff\u00fa\3\2\2\2\u00ff\u00fe\3\2\2\2\u0100)\3\2\2")
        buf.write("\2\u0101\u0102\5,\27\2\u0102\u0103\t\4\2\2\u0103\u0104")
        buf.write("\5,\27\2\u0104\u0107\3\2\2\2\u0105\u0107\5,\27\2\u0106")
        buf.write("\u0101\3\2\2\2\u0106\u0105\3\2\2\2\u0107+\3\2\2\2\u0108")
        buf.write("\u0109\b\27\1\2\u0109\u010a\5.\30\2\u010a\u0110\3\2\2")
        buf.write("\2\u010b\u010c\f\4\2\2\u010c\u010d\t\5\2\2\u010d\u010f")
        buf.write("\5.\30\2\u010e\u010b\3\2\2\2\u010f\u0112\3\2\2\2\u0110")
        buf.write("\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111-\3\2\2\2\u0112")
        buf.write("\u0110\3\2\2\2\u0113\u0114\b\30\1\2\u0114\u0115\5\60\31")
        buf.write("\2\u0115\u011b\3\2\2\2\u0116\u0117\f\4\2\2\u0117\u0118")
        buf.write("\t\6\2\2\u0118\u011a\5\60\31\2\u0119\u0116\3\2\2\2\u011a")
        buf.write("\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2")
        buf.write("\u011c/\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u011f\b\31\1")
        buf.write("\2\u011f\u0120\5\62\32\2\u0120\u0126\3\2\2\2\u0121\u0122")
        buf.write("\f\4\2\2\u0122\u0123\t\7\2\2\u0123\u0125\5\62\32\2\u0124")
        buf.write("\u0121\3\2\2\2\u0125\u0128\3\2\2\2\u0126\u0124\3\2\2\2")
        buf.write("\u0126\u0127\3\2\2\2\u0127\61\3\2\2\2\u0128\u0126\3\2")
        buf.write("\2\2\u0129\u012a\7%\2\2\u012a\u012d\5\62\32\2\u012b\u012d")
        buf.write("\5\64\33\2\u012c\u0129\3\2\2\2\u012c\u012b\3\2\2\2\u012d")
        buf.write("\63\3\2\2\2\u012e\u012f\7!\2\2\u012f\u0132\5\64\33\2\u0130")
        buf.write("\u0132\5\66\34\2\u0131\u012e\3\2\2\2\u0131\u0130\3\2\2")
        buf.write("\2\u0132\65\3\2\2\2\u0133\u0134\7B\2\2\u0134\u0135\7\61")
        buf.write("\2\2\u0135\u0136\5@!\2\u0136\u0137\7\62\2\2\u0137\u013a")
        buf.write("\3\2\2\2\u0138\u013a\58\35\2\u0139\u0133\3\2\2\2\u0139")
        buf.write("\u0138\3\2\2\2\u013a\67\3\2\2\2\u013b\u013c\7/\2\2\u013c")
        buf.write("\u013d\5(\25\2\u013d\u013e\7\60\2\2\u013e\u0141\3\2\2")
        buf.write("\2\u013f\u0141\5:\36\2\u0140\u013b\3\2\2\2\u0140\u013f")
        buf.write("\3\2\2\2\u01419\3\2\2\2\u0142\u014a\7=\2\2\u0143\u014a")
        buf.write("\7>\2\2\u0144\u014a\7?\2\2\u0145\u014a\7@\2\2\u0146\u014a")
        buf.write("\7B\2\2\u0147\u014a\5j\66\2\u0148\u014a\5&\24\2\u0149")
        buf.write("\u0142\3\2\2\2\u0149\u0143\3\2\2\2\u0149\u0144\3\2\2\2")
        buf.write("\u0149\u0145\3\2\2\2\u0149\u0146\3\2\2\2\u0149\u0147\3")
        buf.write("\2\2\2\u0149\u0148\3\2\2\2\u014a;\3\2\2\2\u014b\u014e")
        buf.write("\5> \2\u014c\u014e\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014c")
        buf.write("\3\2\2\2\u014e=\3\2\2\2\u014f\u0150\5(\25\2\u0150\u0151")
        buf.write("\7\64\2\2\u0151\u0152\5> \2\u0152\u0155\3\2\2\2\u0153")
        buf.write("\u0155\5(\25\2\u0154\u014f\3\2\2\2\u0154\u0153\3\2\2\2")
        buf.write("\u0155?\3\2\2\2\u0156\u0157\5(\25\2\u0157\u0158\7\64\2")
        buf.write("\2\u0158\u0159\5@!\2\u0159\u015c\3\2\2\2\u015a\u015c\5")
        buf.write("(\25\2\u015b\u0156\3\2\2\2\u015b\u015a\3\2\2\2\u015cA")
        buf.write("\3\2\2\2\u015d\u0168\5D#\2\u015e\u0168\5H%\2\u015f\u0168")
        buf.write("\5J&\2\u0160\u0168\5R*\2\u0161\u0168\5T+\2\u0162\u0168")
        buf.write("\5V,\2\u0163\u0168\5X-\2\u0164\u0168\5Z.\2\u0165\u0168")
        buf.write("\5\\/\2\u0166\u0168\5^\60\2\u0167\u015d\3\2\2\2\u0167")
        buf.write("\u015e\3\2\2\2\u0167\u015f\3\2\2\2\u0167\u0160\3\2\2\2")
        buf.write("\u0167\u0161\3\2\2\2\u0167\u0162\3\2\2\2\u0167\u0163\3")
        buf.write("\2\2\2\u0167\u0164\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0166")
        buf.write("\3\2\2\2\u0168C\3\2\2\2\u0169\u016a\5F$\2\u016a\u016b")
        buf.write("\79\2\2\u016b\u016c\5(\25\2\u016c\u016d\7\65\2\2\u016d")
        buf.write("E\3\2\2\2\u016e\u0175\7B\2\2\u016f\u0170\7B\2\2\u0170")
        buf.write("\u0171\7\61\2\2\u0171\u0172\5@!\2\u0172\u0173\7\62\2\2")
        buf.write("\u0173\u0175\3\2\2\2\u0174\u016e\3\2\2\2\u0174\u016f\3")
        buf.write("\2\2\2\u0175G\3\2\2\2\u0176\u0177\7\13\2\2\u0177\u0178")
        buf.write("\5(\25\2\u0178\u017b\5B\"\2\u0179\u017a\7\7\2\2\u017a")
        buf.write("\u017c\5B\"\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017cI\3\2\2\2\u017d\u017e\7\t\2\2\u017e\u017f\7/\2\2")
        buf.write("\u017f\u0180\5L\'\2\u0180\u0181\7\64\2\2\u0181\u0182\5")
        buf.write("N(\2\u0182\u0183\7\64\2\2\u0183\u0184\5P)\2\u0184\u0185")
        buf.write("\7\60\2\2\u0185\u0186\5B\"\2\u0186K\3\2\2\2\u0187\u0188")
        buf.write("\7B\2\2\u0188\u0189\79\2\2\u0189\u018a\5(\25\2\u018aM")
        buf.write("\3\2\2\2\u018b\u018c\5(\25\2\u018c\u018d\t\4\2\2\u018d")
        buf.write("\u018e\5(\25\2\u018eO\3\2\2\2\u018f\u0190\5(\25\2\u0190")
        buf.write("Q\3\2\2\2\u0191\u0192\7\17\2\2\u0192\u0193\5(\25\2\u0193")
        buf.write("\u0194\5B\"\2\u0194S\3\2\2\2\u0195\u0196\7\6\2\2\u0196")
        buf.write("\u0197\5^\60\2\u0197\u0198\7\17\2\2\u0198\u0199\5(\25")
        buf.write("\2\u0199\u019a\7\65\2\2\u019aU\3\2\2\2\u019b\u019c\7\4")
        buf.write("\2\2\u019c\u019d\7\65\2\2\u019dW\3\2\2\2\u019e\u019f\7")
        buf.write("\22\2\2\u019f\u01a0\7\65\2\2\u01a0Y\3\2\2\2\u01a1\u01a4")
        buf.write("\7\r\2\2\u01a2\u01a5\5(\25\2\u01a3\u01a5\3\2\2\2\u01a4")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2")
        buf.write("\u01a6\u01a7\7\65\2\2\u01a7[\3\2\2\2\u01a8\u01a9\5n8\2")
        buf.write("\u01a9\u01aa\7\65\2\2\u01aa\u01b2\3\2\2\2\u01ab\u01ac")
        buf.write("\7B\2\2\u01ac\u01ad\7/\2\2\u01ad\u01ae\5<\37\2\u01ae\u01af")
        buf.write("\7\60\2\2\u01af\u01b0\7\65\2\2\u01b0\u01b2\3\2\2\2\u01b1")
        buf.write("\u01a8\3\2\2\2\u01b1\u01ab\3\2\2\2\u01b2]\3\2\2\2\u01b3")
        buf.write("\u01b4\7\67\2\2\u01b4\u01b5\5`\61\2\u01b5\u01b6\78\2\2")
        buf.write("\u01b6\u01b9\3\2\2\2\u01b7\u01b9\7;\2\2\u01b8\u01b3\3")
        buf.write("\2\2\2\u01b8\u01b7\3\2\2\2\u01b9_\3\2\2\2\u01ba\u01bd")
        buf.write("\5b\62\2\u01bb\u01bd\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bb\3\2\2\2\u01bda\3\2\2\2\u01be\u01bf\5d\63\2\u01bf")
        buf.write("\u01c0\5b\62\2\u01c0\u01c3\3\2\2\2\u01c1\u01c3\5d\63\2")
        buf.write("\u01c2\u01be\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3c\3\2\2")
        buf.write("\2\u01c4\u01c7\5B\"\2\u01c5\u01c7\5\6\4\2\u01c6\u01c4")
        buf.write("\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7e\3\2\2\2\u01c8\u01c9")
        buf.write("\5B\"\2\u01c9\u01ca\5f\64\2\u01ca\u01cd\3\2\2\2\u01cb")
        buf.write("\u01cd\5B\"\2\u01cc\u01c8\3\2\2\2\u01cc\u01cb\3\2\2\2")
        buf.write("\u01cdg\3\2\2\2\u01ce\u01cf\5\6\4\2\u01cf\u01d0\5h\65")
        buf.write("\2\u01d0\u01d3\3\2\2\2\u01d1\u01d3\5\6\4\2\u01d2\u01ce")
        buf.write("\3\2\2\2\u01d2\u01d1\3\2\2\2\u01d3i\3\2\2\2\u01d4\u01db")
        buf.write("\5n8\2\u01d5\u01d6\7B\2\2\u01d6\u01d7\7/\2\2\u01d7\u01d8")
        buf.write("\5<\37\2\u01d8\u01d9\7\60\2\2\u01d9\u01db\3\2\2\2\u01da")
        buf.write("\u01d4\3\2\2\2\u01da\u01d5\3\2\2\2\u01dbk\3\2\2\2\u01dc")
        buf.write("\u01dd\5j\66\2\u01dd\u01de\7\64\2\2\u01de\u01df\5l\67")
        buf.write("\2\u01df\u01e2\3\2\2\2\u01e0\u01e2\5j\66\2\u01e1\u01dc")
        buf.write("\3\2\2\2\u01e1\u01e0\3\2\2\2\u01e2m\3\2\2\2\u01e3\u01ed")
        buf.write("\5p9\2\u01e4\u01ed\5r:\2\u01e5\u01ed\5t;\2\u01e6\u01ed")
        buf.write("\5v<\2\u01e7\u01ed\5z>\2\u01e8\u01ed\5|?\2\u01e9\u01ed")
        buf.write("\5~@\2\u01ea\u01ed\5\u0080A\2\u01eb\u01ed\5\u0082B\2\u01ec")
        buf.write("\u01e3\3\2\2\2\u01ec\u01e4\3\2\2\2\u01ec\u01e5\3\2\2\2")
        buf.write("\u01ec\u01e6\3\2\2\2\u01ec\u01e7\3\2\2\2\u01ec\u01e8\3")
        buf.write("\2\2\2\u01ec\u01e9\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01eb")
        buf.write("\3\2\2\2\u01edo\3\2\2\2\u01ee\u01ef\7\26\2\2\u01ef\u01f0")
        buf.write("\7/\2\2\u01f0\u01f1\7\60\2\2\u01f1q\3\2\2\2\u01f2\u01f3")
        buf.write("\7\27\2\2\u01f3\u01f4\7/\2\2\u01f4\u01f5\5(\25\2\u01f5")
        buf.write("\u01f6\7\60\2\2\u01f6s\3\2\2\2\u01f7\u01f8\7\30\2\2\u01f8")
        buf.write("\u01f9\7/\2\2\u01f9\u01fa\7\60\2\2\u01fau\3\2\2\2\u01fb")
        buf.write("\u01fc\7\31\2\2\u01fc\u01fd\7/\2\2\u01fd\u01fe\5(\25\2")
        buf.write("\u01fe\u01ff\7\60\2\2\u01ffw\3\2\2\2\u0200\u0201\7\32")
        buf.write("\2\2\u0201\u0202\7/\2\2\u0202\u0203\7\60\2\2\u0203y\3")
        buf.write("\2\2\2\u0204\u0205\7\33\2\2\u0205\u0206\7/\2\2\u0206\u0207")
        buf.write("\5(\25\2\u0207\u0208\7\60\2\2\u0208{\3\2\2\2\u0209\u020a")
        buf.write("\7\34\2\2\u020a\u020b\7/\2\2\u020b\u020c\7\60\2\2\u020c")
        buf.write("}\3\2\2\2\u020d\u020e\7\35\2\2\u020e\u020f\7/\2\2\u020f")
        buf.write("\u0210\5(\25\2\u0210\u0211\7\60\2\2\u0211\177\3\2\2\2")
        buf.write("\u0212\u0213\7\36\2\2\u0213\u0214\7/\2\2\u0214\u0215\5")
        buf.write("@!\2\u0215\u0216\7\60\2\2\u0216\u0081\3\2\2\2\u0217\u0218")
        buf.write("\7\37\2\2\u0218\u0219\7/\2\2\u0219\u021a\7\60\2\2\u021a")
        buf.write("\u0083\3\2\2\2,\u0087\u008d\u0091\u009d\u00a3\u00ac\u00b1")
        buf.write("\u00b4\u00ba\u00c0\u00cc\u00d7\u00db\u00e2\u00f2\u00ff")
        buf.write("\u0106\u0110\u011b\u0126\u012c\u0131\u0139\u0140\u0149")
        buf.write("\u014d\u0154\u015b\u0167\u0174\u017b\u01a4\u01b1\u01b8")
        buf.write("\u01bc\u01c2\u01c6\u01cc\u01d2\u01da\u01e1\u01ec")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'auto'", "'break'", "'boolean'", "'do'", 
                     "'else'", "'float'", "'for'", "'function'", "'if'", 
                     "'integer'", "'return'", "'string'", "'while'", "'void'", 
                     "'out'", "'continue'", "'of'", "'inherit'", "'array'", 
                     "'readInteger'", "'printInteger'", "'readFloat'", "'writeFloat'", 
                     "'readBoolean'", "'printBoolean'", "'readString'", 
                     "'printString'", "'super'", "'preventDefault'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
                     "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", 
                     "'{'", "'}'", "'='", "'\"'", "'{}'" ]

    symbolicNames = [ "<INVALID>", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
                      "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", 
                      "STRING", "WHILE", "VOID", "OUT", "CONTINUE", "OF", 
                      "INHERIT", "ARRAY", "READINTEGER", "PRINTINTEGER", 
                      "READFLOAT", "WRITEFLOAT", "READBOOLEAN", "PRINTBOOLEAN", 
                      "READSTRING", "PRINTSTRING", "SUPER", "PREVENTDEFAULT", 
                      "ADD", "MINUS", "MUL", "DIV", "MODUL", "NOT", "AND", 
                      "OR", "EQUAL", "NOTEQUAL", "LESSTHAN", "LESSEQUAL", 
                      "GREATERTHAN", "GREATEREQUAL", "DOUBLECOLON", "LP", 
                      "RP", "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", 
                      "LB", "RB", "ASSIGN", "DOUBLEQUOTE", "EMPTYBLOCK", 
                      "COMMENT", "INTEGERLIT", "FLOATLIT", "BOOLEANLIT", 
                      "STRINGLIT", "ARRAYLIT", "IDENTIFIER", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_vardecl = 2
    RULE_vardeclAssign = 3
    RULE_vardeclAssignment = 4
    RULE_vardeclAssignBaseCase = 5
    RULE_vardeclNoAssign = 6
    RULE_parameter = 7
    RULE_identifierList = 8
    RULE_typ = 9
    RULE_funcdecl = 10
    RULE_returnType = 11
    RULE_parameterList = 12
    RULE_parameterPrime = 13
    RULE_inheritanceSubpart = 14
    RULE_arrayType = 15
    RULE_dimensions = 16
    RULE_elementTyp = 17
    RULE_arrayLit = 18
    RULE_expression = 19
    RULE_expr1 = 20
    RULE_expr2 = 21
    RULE_expr3 = 22
    RULE_expr4 = 23
    RULE_expr5 = 24
    RULE_expr6 = 25
    RULE_expr7 = 26
    RULE_expr8 = 27
    RULE_factor = 28
    RULE_expressionListNullable = 29
    RULE_expressionPrime = 30
    RULE_expressionListNonnull = 31
    RULE_statement = 32
    RULE_assignStmt = 33
    RULE_lhs = 34
    RULE_ifStmt = 35
    RULE_forStmt = 36
    RULE_initExpr = 37
    RULE_conditionExpr = 38
    RULE_updateExpr = 39
    RULE_whileStmt = 40
    RULE_doWhileStmt = 41
    RULE_breakStmt = 42
    RULE_continueStmt = 43
    RULE_returnStmt = 44
    RULE_callStmt = 45
    RULE_blockStmt = 46
    RULE_blockBody = 47
    RULE_stmtsOrVardecls = 48
    RULE_stmtOrVardecl = 49
    RULE_statementList = 50
    RULE_vardeclList = 51
    RULE_functionCall = 52
    RULE_functionCallList = 53
    RULE_specialFunc = 54
    RULE_readInteger = 55
    RULE_printInteger = 56
    RULE_readFloat = 57
    RULE_writeFloat = 58
    RULE_readBoolean = 59
    RULE_printBoolean = 60
    RULE_readString = 61
    RULE_printString = 62
    RULE_superFunction = 63
    RULE_preventDefault = 64

    ruleNames =  [ "program", "decls", "vardecl", "vardeclAssign", "vardeclAssignment", 
                   "vardeclAssignBaseCase", "vardeclNoAssign", "parameter", 
                   "identifierList", "typ", "funcdecl", "returnType", "parameterList", 
                   "parameterPrime", "inheritanceSubpart", "arrayType", 
                   "dimensions", "elementTyp", "arrayLit", "expression", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "expr8", "factor", "expressionListNullable", 
                   "expressionPrime", "expressionListNonnull", "statement", 
                   "assignStmt", "lhs", "ifStmt", "forStmt", "initExpr", 
                   "conditionExpr", "updateExpr", "whileStmt", "doWhileStmt", 
                   "breakStmt", "continueStmt", "returnStmt", "callStmt", 
                   "blockStmt", "blockBody", "stmtsOrVardecls", "stmtOrVardecl", 
                   "statementList", "vardeclList", "functionCall", "functionCallList", 
                   "specialFunc", "readInteger", "printInteger", "readFloat", 
                   "writeFloat", "readBoolean", "printBoolean", "readString", 
                   "printString", "superFunction", "preventDefault" ]

    EOF = Token.EOF
    AUTO=1
    BREAK=2
    BOOLEAN=3
    DO=4
    ELSE=5
    FLOAT=6
    FOR=7
    FUNCTION=8
    IF=9
    INTEGER=10
    RETURN=11
    STRING=12
    WHILE=13
    VOID=14
    OUT=15
    CONTINUE=16
    OF=17
    INHERIT=18
    ARRAY=19
    READINTEGER=20
    PRINTINTEGER=21
    READFLOAT=22
    WRITEFLOAT=23
    READBOOLEAN=24
    PRINTBOOLEAN=25
    READSTRING=26
    PRINTSTRING=27
    SUPER=28
    PREVENTDEFAULT=29
    ADD=30
    MINUS=31
    MUL=32
    DIV=33
    MODUL=34
    NOT=35
    AND=36
    OR=37
    EQUAL=38
    NOTEQUAL=39
    LESSTHAN=40
    LESSEQUAL=41
    GREATERTHAN=42
    GREATEREQUAL=43
    DOUBLECOLON=44
    LP=45
    RP=46
    LSB=47
    RSB=48
    DOT=49
    COMMA=50
    SEMI=51
    COLON=52
    LB=53
    RB=54
    ASSIGN=55
    DOUBLEQUOTE=56
    EMPTYBLOCK=57
    COMMENT=58
    INTEGERLIT=59
    FLOATLIT=60
    BOOLEANLIT=61
    STRINGLIT=62
    ARRAYLIT=63
    IDENTIFIER=64
    WS=65
    UNCLOSE_STRING=66
    ILLEGAL_ESCAPE=67
    ERROR_CHAR=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def decls(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.DeclsContext)
            else:
                return self.getTypedRuleContext(MT22Parser.DeclsContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 130
                self.decls()
                self.state = 133 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MT22Parser.IDENTIFIER):
                    break

            self.state = 135
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MT22Parser.FuncdeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decls




    def decls(self):

        localctx = MT22Parser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardeclAssign(self):
            return self.getTypedRuleContext(MT22Parser.VardeclAssignContext,0)


        def vardeclNoAssign(self):
            return self.getTypedRuleContext(MT22Parser.VardeclNoAssignContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardecl




    def vardecl(self):

        localctx = MT22Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.vardeclAssign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.vardeclNoAssign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardeclAssignment(self):
            return self.getTypedRuleContext(MT22Parser.VardeclAssignmentContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_vardeclAssign




    def vardeclAssign(self):

        localctx = MT22Parser.VardeclAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardeclAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.vardeclAssignment()
            self.state = 146
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def vardeclAssignment(self):
            return self.getTypedRuleContext(MT22Parser.VardeclAssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def vardeclAssignBaseCase(self):
            return self.getTypedRuleContext(MT22Parser.VardeclAssignBaseCaseContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardeclAssignment




    def vardeclAssignment(self):

        localctx = MT22Parser.VardeclAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardeclAssignment)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.match(MT22Parser.IDENTIFIER)
                self.state = 149
                self.match(MT22Parser.COMMA)
                self.state = 150
                self.vardeclAssignment()
                self.state = 151
                self.match(MT22Parser.COMMA)
                self.state = 152
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.vardeclAssignBaseCase()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclAssignBaseCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def typ(self):
            return self.getTypedRuleContext(MT22Parser.TypContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MT22Parser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardeclAssignBaseCase




    def vardeclAssignBaseCase(self):

        localctx = MT22Parser.VardeclAssignBaseCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardeclAssignBaseCase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(MT22Parser.IDENTIFIER)
            self.state = 158
            self.match(MT22Parser.COLON)
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.AUTO, MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.state = 159
                self.typ()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.state = 160
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 163
            self.match(MT22Parser.ASSIGN)
            self.state = 164
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclNoAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(MT22Parser.IdentifierListContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def typ(self):
            return self.getTypedRuleContext(MT22Parser.TypContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MT22Parser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardeclNoAssign




    def vardeclNoAssign(self):

        localctx = MT22Parser.VardeclNoAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vardeclNoAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.identifierList()
            self.state = 167
            self.match(MT22Parser.COLON)
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.AUTO, MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.state = 168
                self.typ()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.state = 169
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 172
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(MT22Parser.TypContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MT22Parser.ArrayTypeContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_parameter




    def parameter(self):

        localctx = MT22Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 174
                self.match(MT22Parser.INHERIT)


            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 177
                self.match(MT22Parser.OUT)


            self.state = 180
            self.match(MT22Parser.IDENTIFIER)
            self.state = 181
            self.match(MT22Parser.COLON)
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.AUTO, MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.state = 182
                self.typ()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.state = 183
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def identifierList(self):
            return self.getTypedRuleContext(MT22Parser.IdentifierListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_identifierList




    def identifierList(self):

        localctx = MT22Parser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_identifierList)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.match(MT22Parser.IDENTIFIER)
                self.state = 187
                self.match(MT22Parser.COMMA)
                self.state = 188
                self.identifierList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.match(MT22Parser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_typ




    def typ(self):

        localctx = MT22Parser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.AUTO) | (1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def returnType(self):
            return self.getTypedRuleContext(MT22Parser.ReturnTypeContext,0)


        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def parameterList(self):
            return self.getTypedRuleContext(MT22Parser.ParameterListContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockStmtContext,0)


        def inheritanceSubpart(self):
            return self.getTypedRuleContext(MT22Parser.InheritanceSubpartContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_funcdecl




    def funcdecl(self):

        localctx = MT22Parser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(MT22Parser.IDENTIFIER)
            self.state = 195
            self.match(MT22Parser.COLON)
            self.state = 196
            self.match(MT22Parser.FUNCTION)
            self.state = 197
            self.returnType()
            self.state = 198
            self.match(MT22Parser.LP)
            self.state = 199
            self.parameterList()
            self.state = 200
            self.match(MT22Parser.RP)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 201
                self.inheritanceSubpart()


            self.state = 204
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def arrayType(self):
            return self.getTypedRuleContext(MT22Parser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_returnType




    def returnType(self):

        localctx = MT22Parser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_returnType)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.match(MT22Parser.BOOLEAN)
                pass
            elif token in [MT22Parser.INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.match(MT22Parser.INTEGER)
                pass
            elif token in [MT22Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                self.match(MT22Parser.FLOAT)
                pass
            elif token in [MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 209
                self.match(MT22Parser.STRING)
                pass
            elif token in [MT22Parser.VOID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 210
                self.match(MT22Parser.VOID)
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 6)
                self.state = 211
                self.match(MT22Parser.AUTO)
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 7)
                self.state = 212
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterPrime(self):
            return self.getTypedRuleContext(MT22Parser.ParameterPrimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_parameterList




    def parameterList(self):

        localctx = MT22Parser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameterList)
        try:
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT, MT22Parser.INHERIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.parameterPrime()
                pass
            elif token in [MT22Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(MT22Parser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def parameterPrime(self):
            return self.getTypedRuleContext(MT22Parser.ParameterPrimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_parameterPrime




    def parameterPrime(self):

        localctx = MT22Parser.ParameterPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameterPrime)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.parameter()
                self.state = 220
                self.match(MT22Parser.COMMA)
                self.state = 221
                self.parameterPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InheritanceSubpartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_inheritanceSubpart




    def inheritanceSubpart(self):

        localctx = MT22Parser.InheritanceSubpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_inheritanceSubpart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(MT22Parser.INHERIT)
            self.state = 227
            self.match(MT22Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def dimensions(self):
            return self.getTypedRuleContext(MT22Parser.DimensionsContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def elementTyp(self):
            return self.getTypedRuleContext(MT22Parser.ElementTypContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arrayType




    def arrayType(self):

        localctx = MT22Parser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(MT22Parser.ARRAY)
            self.state = 230
            self.match(MT22Parser.LSB)
            self.state = 231
            self.dimensions()
            self.state = 232
            self.match(MT22Parser.RSB)
            self.state = 233
            self.match(MT22Parser.OF)
            self.state = 234
            self.elementTyp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGERLIT(self):
            return self.getToken(MT22Parser.INTEGERLIT, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def dimensions(self):
            return self.getTypedRuleContext(MT22Parser.DimensionsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_dimensions




    def dimensions(self):

        localctx = MT22Parser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_dimensions)
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(MT22Parser.INTEGERLIT)
                self.state = 237
                self.match(MT22Parser.COMMA)
                self.state = 238
                self.dimensions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(MT22Parser.INTEGERLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementTypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_elementTyp




    def elementTyp(self):

        localctx = MT22Parser.ElementTypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_elementTyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expressionListNonnull(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionListNonnullContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arrayLit




    def arrayLit(self):

        localctx = MT22Parser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(MT22Parser.LB)
            self.state = 245
            self.expressionListNonnull()
            self.state = 246
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr1Context,i)


        def DOUBLECOLON(self):
            return self.getToken(MT22Parser.DOUBLECOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression




    def expression(self):

        localctx = MT22Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expression)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.expr1()
                self.state = 249
                self.match(MT22Parser.DOUBLECOLON)
                self.state = 250
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr2Context,i)


        def EQUAL(self):
            return self.getToken(MT22Parser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(MT22Parser.NOTEQUAL, 0)

        def LESSTHAN(self):
            return self.getToken(MT22Parser.LESSTHAN, 0)

        def GREATERTHAN(self):
            return self.getToken(MT22Parser.GREATERTHAN, 0)

        def LESSEQUAL(self):
            return self.getToken(MT22Parser.LESSEQUAL, 0)

        def GREATEREQUAL(self):
            return self.getToken(MT22Parser.GREATEREQUAL, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr1




    def expr1(self):

        localctx = MT22Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.expr2(0)
                self.state = 256
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUAL) | (1 << MT22Parser.NOTEQUAL) | (1 << MT22Parser.LESSTHAN) | (1 << MT22Parser.LESSEQUAL) | (1 << MT22Parser.GREATERTHAN) | (1 << MT22Parser.GREATEREQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 257
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MT22Parser.Expr2Context,0)


        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 270
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 265
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 266
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AND or _la==MT22Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 267
                    self.expr3(0) 
                self.state = 272
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def ADD(self):
            return self.getToken(MT22Parser.ADD, 0)

        def MINUS(self):
            return self.getToken(MT22Parser.MINUS, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 281
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 276
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 277
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADD or _la==MT22Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 278
                    self.expr4(0) 
                self.state = 283
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def MUL(self):
            return self.getToken(MT22Parser.MUL, 0)

        def DIV(self):
            return self.getToken(MT22Parser.DIV, 0)

        def MODUL(self):
            return self.getToken(MT22Parser.MODUL, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 292
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 287
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 288
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MUL) | (1 << MT22Parser.DIV) | (1 << MT22Parser.MODUL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 289
                    self.expr5() 
                self.state = 294
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr5




    def expr5(self):

        localctx = MT22Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr5)
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.match(MT22Parser.NOT)
                self.state = 296
                self.expr5()
                pass
            elif token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.MINUS, MT22Parser.LP, MT22Parser.LB, MT22Parser.INTEGERLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLEANLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(MT22Parser.MINUS, 0)

        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(MT22Parser.Expr7Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr6




    def expr6(self):

        localctx = MT22Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr6)
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(MT22Parser.MINUS)
                self.state = 301
                self.expr6()
                pass
            elif token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.LP, MT22Parser.LB, MT22Parser.INTEGERLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLEANLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def expressionListNonnull(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionListNonnullContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def expr8(self):
            return self.getTypedRuleContext(MT22Parser.Expr8Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr7




    def expr7(self):

        localctx = MT22Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr7)
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.match(MT22Parser.IDENTIFIER)
                self.state = 306
                self.match(MT22Parser.LSB)
                self.state = 307
                self.expressionListNonnull()
                self.state = 308
                self.match(MT22Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.expr8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def factor(self):
            return self.getTypedRuleContext(MT22Parser.FactorContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr8




    def expr8(self):

        localctx = MT22Parser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr8)
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.match(MT22Parser.LP)
                self.state = 314
                self.expression()
                self.state = 315
                self.match(MT22Parser.RP)
                pass
            elif token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.LB, MT22Parser.INTEGERLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLEANLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.factor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGERLIT(self):
            return self.getToken(MT22Parser.INTEGERLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MT22Parser.FLOATLIT, 0)

        def BOOLEANLIT(self):
            return self.getToken(MT22Parser.BOOLEANLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MT22Parser.STRINGLIT, 0)

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def functionCall(self):
            return self.getTypedRuleContext(MT22Parser.FunctionCallContext,0)


        def arrayLit(self):
            return self.getTypedRuleContext(MT22Parser.ArrayLitContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_factor




    def factor(self):

        localctx = MT22Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_factor)
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.match(MT22Parser.INTEGERLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.match(MT22Parser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
                self.match(MT22Parser.BOOLEANLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 323
                self.match(MT22Parser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 324
                self.match(MT22Parser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 325
                self.functionCall()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 326
                self.arrayLit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListNullableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionPrime(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionPrimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expressionListNullable




    def expressionListNullable(self):

        localctx = MT22Parser.ExpressionListNullableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expressionListNullable)
        try:
            self.state = 331
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.MINUS, MT22Parser.NOT, MT22Parser.LP, MT22Parser.LB, MT22Parser.INTEGERLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLEANLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.expressionPrime()
                pass
            elif token in [MT22Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def expressionPrime(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionPrimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expressionPrime




    def expressionPrime(self):

        localctx = MT22Parser.ExpressionPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expressionPrime)
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.expression()
                self.state = 334
                self.match(MT22Parser.COMMA)
                self.state = 335
                self.expressionPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListNonnullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def expressionListNonnull(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionListNonnullContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expressionListNonnull




    def expressionListNonnull(self):

        localctx = MT22Parser.ExpressionListNonnullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expressionListNonnull)
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.expression()
                self.state = 341
                self.match(MT22Parser.COMMA)
                self.state = 342
                self.expressionListNonnull()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStmt(self):
            return self.getTypedRuleContext(MT22Parser.AssignStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(MT22Parser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(MT22Parser.ForStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(MT22Parser.WhileStmtContext,0)


        def doWhileStmt(self):
            return self.getTypedRuleContext(MT22Parser.DoWhileStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(MT22Parser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(MT22Parser.ContinueStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(MT22Parser.ReturnStmtContext,0)


        def callStmt(self):
            return self.getTypedRuleContext(MT22Parser.CallStmtContext,0)


        def blockStmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockStmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statement




    def statement(self):

        localctx = MT22Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_statement)
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.assignStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.ifStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 349
                self.forStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 350
                self.whileStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 351
                self.doWhileStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 352
                self.breakStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 353
                self.continueStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 354
                self.returnStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 355
                self.callStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 356
                self.blockStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MT22Parser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assignStmt




    def assignStmt(self):

        localctx = MT22Parser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.lhs()
            self.state = 360
            self.match(MT22Parser.ASSIGN)
            self.state = 361
            self.expression()
            self.state = 362
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def expressionListNonnull(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionListNonnullContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_lhs




    def lhs(self):

        localctx = MT22Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_lhs)
        try:
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.match(MT22Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.match(MT22Parser.IDENTIFIER)
                self.state = 366
                self.match(MT22Parser.LSB)
                self.state = 367
                self.expressionListNonnull()
                self.state = 368
                self.match(MT22Parser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_ifStmt




    def ifStmt(self):

        localctx = MT22Parser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(MT22Parser.IF)
            self.state = 373
            self.expression()
            self.state = 374
            self.statement()
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 375
                self.match(MT22Parser.ELSE)
                self.state = 376
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def initExpr(self):
            return self.getTypedRuleContext(MT22Parser.InitExprContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def conditionExpr(self):
            return self.getTypedRuleContext(MT22Parser.ConditionExprContext,0)


        def updateExpr(self):
            return self.getTypedRuleContext(MT22Parser.UpdateExprContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_forStmt




    def forStmt(self):

        localctx = MT22Parser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(MT22Parser.FOR)
            self.state = 380
            self.match(MT22Parser.LP)
            self.state = 381
            self.initExpr()
            self.state = 382
            self.match(MT22Parser.COMMA)
            self.state = 383
            self.conditionExpr()
            self.state = 384
            self.match(MT22Parser.COMMA)
            self.state = 385
            self.updateExpr()
            self.state = 386
            self.match(MT22Parser.RP)
            self.state = 387
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_initExpr




    def initExpr(self):

        localctx = MT22Parser.InitExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_initExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(MT22Parser.IDENTIFIER)
            self.state = 390
            self.match(MT22Parser.ASSIGN)
            self.state = 391
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExpressionContext,i)


        def EQUAL(self):
            return self.getToken(MT22Parser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(MT22Parser.NOTEQUAL, 0)

        def LESSTHAN(self):
            return self.getToken(MT22Parser.LESSTHAN, 0)

        def GREATERTHAN(self):
            return self.getToken(MT22Parser.GREATERTHAN, 0)

        def LESSEQUAL(self):
            return self.getToken(MT22Parser.LESSEQUAL, 0)

        def GREATEREQUAL(self):
            return self.getToken(MT22Parser.GREATEREQUAL, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_conditionExpr




    def conditionExpr(self):

        localctx = MT22Parser.ConditionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_conditionExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.expression()
            self.state = 394
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUAL) | (1 << MT22Parser.NOTEQUAL) | (1 << MT22Parser.LESSTHAN) | (1 << MT22Parser.LESSEQUAL) | (1 << MT22Parser.GREATERTHAN) | (1 << MT22Parser.GREATEREQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 395
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_updateExpr




    def updateExpr(self):

        localctx = MT22Parser.UpdateExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_updateExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_whileStmt




    def whileStmt(self):

        localctx = MT22Parser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(MT22Parser.WHILE)
            self.state = 400
            self.expression()
            self.state = 401
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockStmtContext,0)


        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_doWhileStmt




    def doWhileStmt(self):

        localctx = MT22Parser.DoWhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_doWhileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(MT22Parser.DO)
            self.state = 404
            self.blockStmt()
            self.state = 405
            self.match(MT22Parser.WHILE)
            self.state = 406
            self.expression()
            self.state = 407
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MT22Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_breakStmt




    def breakStmt(self):

        localctx = MT22Parser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(MT22Parser.BREAK)
            self.state = 410
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MT22Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continueStmt




    def continueStmt(self):

        localctx = MT22Parser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(MT22Parser.CONTINUE)
            self.state = 413
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_returnStmt




    def returnStmt(self):

        localctx = MT22Parser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(MT22Parser.RETURN)
            self.state = 418
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.MINUS, MT22Parser.NOT, MT22Parser.LP, MT22Parser.LB, MT22Parser.INTEGERLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLEANLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.state = 416
                self.expression()
                pass
            elif token in [MT22Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 420
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def specialFunc(self):
            return self.getTypedRuleContext(MT22Parser.SpecialFuncContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expressionListNullable(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionListNullableContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_callStmt




    def callStmt(self):

        localctx = MT22Parser.CallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_callStmt)
        try:
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.specialFunc()
                self.state = 423
                self.match(MT22Parser.SEMI)
                pass
            elif token in [MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.match(MT22Parser.IDENTIFIER)
                self.state = 426
                self.match(MT22Parser.LP)
                self.state = 427
                self.expressionListNullable()
                self.state = 428
                self.match(MT22Parser.RP)
                self.state = 429
                self.match(MT22Parser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def blockBody(self):
            return self.getTypedRuleContext(MT22Parser.BlockBodyContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def EMPTYBLOCK(self):
            return self.getToken(MT22Parser.EMPTYBLOCK, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_blockStmt




    def blockStmt(self):

        localctx = MT22Parser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_blockStmt)
        try:
            self.state = 438
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.match(MT22Parser.LB)
                self.state = 434
                self.blockBody()
                self.state = 435
                self.match(MT22Parser.RB)
                pass
            elif token in [MT22Parser.EMPTYBLOCK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.match(MT22Parser.EMPTYBLOCK)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtsOrVardecls(self):
            return self.getTypedRuleContext(MT22Parser.StmtsOrVardeclsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_blockBody




    def blockBody(self):

        localctx = MT22Parser.BlockBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_blockBody)
        try:
            self.state = 442
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BREAK, MT22Parser.DO, MT22Parser.FOR, MT22Parser.IF, MT22Parser.RETURN, MT22Parser.WHILE, MT22Parser.CONTINUE, MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.LB, MT22Parser.EMPTYBLOCK, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.stmtsOrVardecls()
                pass
            elif token in [MT22Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsOrVardeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtOrVardecl(self):
            return self.getTypedRuleContext(MT22Parser.StmtOrVardeclContext,0)


        def stmtsOrVardecls(self):
            return self.getTypedRuleContext(MT22Parser.StmtsOrVardeclsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmtsOrVardecls




    def stmtsOrVardecls(self):

        localctx = MT22Parser.StmtsOrVardeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_stmtsOrVardecls)
        try:
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.stmtOrVardecl()
                self.state = 445
                self.stmtsOrVardecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.stmtOrVardecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtOrVardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmtOrVardecl




    def stmtOrVardecl(self):

        localctx = MT22Parser.StmtOrVardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_stmtOrVardecl)
        try:
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.vardecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def statementList(self):
            return self.getTypedRuleContext(MT22Parser.StatementListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statementList




    def statementList(self):

        localctx = MT22Parser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_statementList)
        try:
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.statement()
                self.state = 455
                self.statementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def vardeclList(self):
            return self.getTypedRuleContext(MT22Parser.VardeclListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardeclList




    def vardeclList(self):

        localctx = MT22Parser.VardeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_vardeclList)
        try:
            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.vardecl()
                self.state = 461
                self.vardeclList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.vardecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def specialFunc(self):
            return self.getTypedRuleContext(MT22Parser.SpecialFuncContext,0)


        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expressionListNullable(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionListNullableContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_functionCall




    def functionCall(self):

        localctx = MT22Parser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_functionCall)
        try:
            self.state = 472
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.specialFunc()
                pass
            elif token in [MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 467
                self.match(MT22Parser.IDENTIFIER)
                self.state = 468
                self.match(MT22Parser.LP)
                self.state = 469
                self.expressionListNullable()
                self.state = 470
                self.match(MT22Parser.RP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(MT22Parser.FunctionCallContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def functionCallList(self):
            return self.getTypedRuleContext(MT22Parser.FunctionCallListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functionCallList




    def functionCallList(self):

        localctx = MT22Parser.FunctionCallListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_functionCallList)
        try:
            self.state = 479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.functionCall()
                self.state = 475
                self.match(MT22Parser.COMMA)
                self.state = 476
                self.functionCallList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecialFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def readInteger(self):
            return self.getTypedRuleContext(MT22Parser.ReadIntegerContext,0)


        def printInteger(self):
            return self.getTypedRuleContext(MT22Parser.PrintIntegerContext,0)


        def readFloat(self):
            return self.getTypedRuleContext(MT22Parser.ReadFloatContext,0)


        def writeFloat(self):
            return self.getTypedRuleContext(MT22Parser.WriteFloatContext,0)


        def printBoolean(self):
            return self.getTypedRuleContext(MT22Parser.PrintBooleanContext,0)


        def readString(self):
            return self.getTypedRuleContext(MT22Parser.ReadStringContext,0)


        def printString(self):
            return self.getTypedRuleContext(MT22Parser.PrintStringContext,0)


        def superFunction(self):
            return self.getTypedRuleContext(MT22Parser.SuperFunctionContext,0)


        def preventDefault(self):
            return self.getTypedRuleContext(MT22Parser.PreventDefaultContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_specialFunc




    def specialFunc(self):

        localctx = MT22Parser.SpecialFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_specialFunc)
        try:
            self.state = 490
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.READINTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 481
                self.readInteger()
                pass
            elif token in [MT22Parser.PRINTINTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
                self.printInteger()
                pass
            elif token in [MT22Parser.READFLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 483
                self.readFloat()
                pass
            elif token in [MT22Parser.WRITEFLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 484
                self.writeFloat()
                pass
            elif token in [MT22Parser.PRINTBOOLEAN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 485
                self.printBoolean()
                pass
            elif token in [MT22Parser.READSTRING]:
                self.enterOuterAlt(localctx, 6)
                self.state = 486
                self.readString()
                pass
            elif token in [MT22Parser.PRINTSTRING]:
                self.enterOuterAlt(localctx, 7)
                self.state = 487
                self.printString()
                pass
            elif token in [MT22Parser.SUPER]:
                self.enterOuterAlt(localctx, 8)
                self.state = 488
                self.superFunction()
                pass
            elif token in [MT22Parser.PREVENTDEFAULT]:
                self.enterOuterAlt(localctx, 9)
                self.state = 489
                self.preventDefault()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadIntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READINTEGER(self):
            return self.getToken(MT22Parser.READINTEGER, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readInteger




    def readInteger(self):

        localctx = MT22Parser.ReadIntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_readInteger)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(MT22Parser.READINTEGER)
            self.state = 493
            self.match(MT22Parser.LP)
            self.state = 494
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintIntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTINTEGER(self):
            return self.getToken(MT22Parser.PRINTINTEGER, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printInteger




    def printInteger(self):

        localctx = MT22Parser.PrintIntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_printInteger)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.match(MT22Parser.PRINTINTEGER)
            self.state = 497
            self.match(MT22Parser.LP)
            self.state = 498
            self.expression()
            self.state = 499
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadFloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READFLOAT(self):
            return self.getToken(MT22Parser.READFLOAT, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readFloat




    def readFloat(self):

        localctx = MT22Parser.ReadFloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_readFloat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(MT22Parser.READFLOAT)
            self.state = 502
            self.match(MT22Parser.LP)
            self.state = 503
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteFloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITEFLOAT(self):
            return self.getToken(MT22Parser.WRITEFLOAT, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_writeFloat




    def writeFloat(self):

        localctx = MT22Parser.WriteFloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_writeFloat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(MT22Parser.WRITEFLOAT)
            self.state = 506
            self.match(MT22Parser.LP)
            self.state = 507
            self.expression()
            self.state = 508
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadBooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READBOOLEAN(self):
            return self.getToken(MT22Parser.READBOOLEAN, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readBoolean




    def readBoolean(self):

        localctx = MT22Parser.ReadBooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_readBoolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(MT22Parser.READBOOLEAN)
            self.state = 511
            self.match(MT22Parser.LP)
            self.state = 512
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintBooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTBOOLEAN(self):
            return self.getToken(MT22Parser.PRINTBOOLEAN, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printBoolean




    def printBoolean(self):

        localctx = MT22Parser.PrintBooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_printBoolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(MT22Parser.PRINTBOOLEAN)
            self.state = 515
            self.match(MT22Parser.LP)
            self.state = 516
            self.expression()
            self.state = 517
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READSTRING(self):
            return self.getToken(MT22Parser.READSTRING, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readString




    def readString(self):

        localctx = MT22Parser.ReadStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_readString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(MT22Parser.READSTRING)
            self.state = 520
            self.match(MT22Parser.LP)
            self.state = 521
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTSTRING(self):
            return self.getToken(MT22Parser.PRINTSTRING, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printString




    def printString(self):

        localctx = MT22Parser.PrintStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_printString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(MT22Parser.PRINTSTRING)
            self.state = 524
            self.match(MT22Parser.LP)
            self.state = 525
            self.expression()
            self.state = 526
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUPER(self):
            return self.getToken(MT22Parser.SUPER, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expressionListNonnull(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionListNonnullContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_superFunction




    def superFunction(self):

        localctx = MT22Parser.SuperFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_superFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.match(MT22Parser.SUPER)
            self.state = 529
            self.match(MT22Parser.LP)
            self.state = 530
            self.expressionListNonnull()
            self.state = 531
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreventDefaultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREVENTDEFAULT(self):
            return self.getToken(MT22Parser.PREVENTDEFAULT, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_preventDefault




    def preventDefault(self):

        localctx = MT22Parser.PreventDefaultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_preventDefault)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.match(MT22Parser.PREVENTDEFAULT)
            self.state = 534
            self.match(MT22Parser.LP)
            self.state = 535
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.expr2_sempred
        self._predicates[22] = self.expr3_sempred
        self._predicates[23] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




