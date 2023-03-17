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
        buf.write("\u0216\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\6\2\u0082\n\2\r\2")
        buf.write("\16\2\u0083\3\2\3\2\3\3\3\3\5\3\u008a\n\3\3\4\3\4\5\4")
        buf.write("\u008e\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("\u009a\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00a3\n\6\3")
        buf.write("\7\3\7\3\7\3\7\5\7\u00a9\n\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\5\b\u00b2\n\b\3\b\3\b\3\t\5\t\u00b7\n\t\3\t\5\t\u00ba")
        buf.write("\n\t\3\t\3\t\3\t\3\t\5\t\u00c0\n\t\3\n\3\n\3\n\3\n\5\n")
        buf.write("\u00c6\n\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5")
        buf.write("\f\u00d2\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00dd")
        buf.write("\n\r\3\16\3\16\5\16\u00e1\n\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u00e8\n\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\22\3\22\3\22\3\22\5\22\u00f8\n\22\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\5\24\u0103\n")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\5\25\u010a\n\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\7\26\u0112\n\26\f\26\16\26\u0115")
        buf.write("\13\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u011d\n\27\f")
        buf.write("\27\16\27\u0120\13\27\3\30\3\30\3\30\3\30\3\30\3\30\7")
        buf.write("\30\u0128\n\30\f\30\16\30\u012b\13\30\3\31\3\31\3\31\5")
        buf.write("\31\u0130\n\31\3\32\3\32\3\32\5\32\u0135\n\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\5\33\u013d\n\33\3\34\3\34\3\34\3")
        buf.write("\34\3\34\5\34\u0144\n\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u014d\n\35\3\36\3\36\5\36\u0151\n\36\3\37\3")
        buf.write("\37\3\37\3\37\3\37\5\37\u0158\n\37\3 \3 \3 \3 \3 \5 \u015f")
        buf.write("\n \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u016b\n!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\5#\u0178\n#\3$\3$\3$\3")
        buf.write("$\3$\5$\u017f\n$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3")
        buf.write("&\3&\3\'\3\'\3\'\3\'\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3*")
        buf.write("\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\5-\u01a8\n-\3-\3-\3.\3")
        buf.write(".\5.\u01ae\n.\3.\3.\3/\3/\3/\3/\3/\5/\u01b7\n/\3\60\3")
        buf.write("\60\3\60\3\60\5\60\u01bd\n\60\3\61\3\61\5\61\u01c1\n\61")
        buf.write("\3\62\3\62\3\62\3\62\5\62\u01c7\n\62\3\63\3\63\3\63\3")
        buf.write("\63\5\63\u01cd\n\63\3\64\3\64\3\64\3\64\3\64\3\64\5\64")
        buf.write("\u01d5\n\64\3\65\3\65\3\65\3\65\3\65\5\65\u01dc\n\65\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u01e7")
        buf.write("\n\66\3\67\3\67\3\67\3\67\38\38\38\38\38\39\39\39\39\3")
        buf.write(":\3:\3:\3:\3:\3;\3;\3;\3;\3<\3<\3<\3<\3<\3=\3=\3=\3=\3")
        buf.write(">\3>\3>\3>\3>\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\2\5*,.A\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\2\7\7\2\4\4\6")
        buf.write("\6\t\t\r\r\17\17\3\2).\3\2\'(\3\2!\"\3\2#%\2\u0219\2\u0081")
        buf.write("\3\2\2\2\4\u0089\3\2\2\2\6\u008d\3\2\2\2\b\u0099\3\2\2")
        buf.write("\2\n\u00a2\3\2\2\2\f\u00a4\3\2\2\2\16\u00ad\3\2\2\2\20")
        buf.write("\u00b6\3\2\2\2\22\u00c5\3\2\2\2\24\u00c7\3\2\2\2\26\u00c9")
        buf.write("\3\2\2\2\30\u00dc\3\2\2\2\32\u00e0\3\2\2\2\34\u00e7\3")
        buf.write("\2\2\2\36\u00e9\3\2\2\2 \u00ec\3\2\2\2\"\u00f7\3\2\2\2")
        buf.write("$\u00f9\3\2\2\2&\u0102\3\2\2\2(\u0109\3\2\2\2*\u010b\3")
        buf.write("\2\2\2,\u0116\3\2\2\2.\u0121\3\2\2\2\60\u012f\3\2\2\2")
        buf.write("\62\u0134\3\2\2\2\64\u013c\3\2\2\2\66\u0143\3\2\2\28\u014c")
        buf.write("\3\2\2\2:\u0150\3\2\2\2<\u0157\3\2\2\2>\u015e\3\2\2\2")
        buf.write("@\u016a\3\2\2\2B\u016c\3\2\2\2D\u0177\3\2\2\2F\u0179\3")
        buf.write("\2\2\2H\u0180\3\2\2\2J\u018a\3\2\2\2L\u018e\3\2\2\2N\u0192")
        buf.write("\3\2\2\2P\u0194\3\2\2\2R\u0198\3\2\2\2T\u019e\3\2\2\2")
        buf.write("V\u01a1\3\2\2\2X\u01a4\3\2\2\2Z\u01ad\3\2\2\2\\\u01b6")
        buf.write("\3\2\2\2^\u01bc\3\2\2\2`\u01c0\3\2\2\2b\u01c6\3\2\2\2")
        buf.write("d\u01cc\3\2\2\2f\u01d4\3\2\2\2h\u01db\3\2\2\2j\u01e6\3")
        buf.write("\2\2\2l\u01e8\3\2\2\2n\u01ec\3\2\2\2p\u01f1\3\2\2\2r\u01f5")
        buf.write("\3\2\2\2t\u01fa\3\2\2\2v\u01fe\3\2\2\2x\u0203\3\2\2\2")
        buf.write("z\u0207\3\2\2\2|\u020c\3\2\2\2~\u0211\3\2\2\2\u0080\u0082")
        buf.write("\5\4\3\2\u0081\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083")
        buf.write("\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0085\3\2\2\2")
        buf.write("\u0085\u0086\7\2\2\3\u0086\3\3\2\2\2\u0087\u008a\5\6\4")
        buf.write("\2\u0088\u008a\5\26\f\2\u0089\u0087\3\2\2\2\u0089\u0088")
        buf.write("\3\2\2\2\u008a\5\3\2\2\2\u008b\u008e\5\b\5\2\u008c\u008e")
        buf.write("\5\16\b\2\u008d\u008b\3\2\2\2\u008d\u008c\3\2\2\2\u008e")
        buf.write("\7\3\2\2\2\u008f\u0090\7B\2\2\u0090\u0091\7\65\2\2\u0091")
        buf.write("\u0092\5\n\6\2\u0092\u0093\7\65\2\2\u0093\u0094\5&\24")
        buf.write("\2\u0094\u0095\7\66\2\2\u0095\u009a\3\2\2\2\u0096\u0097")
        buf.write("\5\f\7\2\u0097\u0098\7\66\2\2\u0098\u009a\3\2\2\2\u0099")
        buf.write("\u008f\3\2\2\2\u0099\u0096\3\2\2\2\u009a\t\3\2\2\2\u009b")
        buf.write("\u009c\7B\2\2\u009c\u009d\7\65\2\2\u009d\u009e\5\n\6\2")
        buf.write("\u009e\u009f\7\65\2\2\u009f\u00a0\5&\24\2\u00a0\u00a3")
        buf.write("\3\2\2\2\u00a1\u00a3\5\f\7\2\u00a2\u009b\3\2\2\2\u00a2")
        buf.write("\u00a1\3\2\2\2\u00a3\13\3\2\2\2\u00a4\u00a5\7B\2\2\u00a5")
        buf.write("\u00a8\7\67\2\2\u00a6\u00a9\5\24\13\2\u00a7\u00a9\5 \21")
        buf.write("\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00aa")
        buf.write("\3\2\2\2\u00aa\u00ab\7:\2\2\u00ab\u00ac\5&\24\2\u00ac")
        buf.write("\r\3\2\2\2\u00ad\u00ae\5\22\n\2\u00ae\u00b1\7\67\2\2\u00af")
        buf.write("\u00b2\5\24\13\2\u00b0\u00b2\5 \21\2\u00b1\u00af\3\2\2")
        buf.write("\2\u00b1\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4")
        buf.write("\7\66\2\2\u00b4\17\3\2\2\2\u00b5\u00b7\7\25\2\2\u00b6")
        buf.write("\u00b5\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b9\3\2\2\2")
        buf.write("\u00b8\u00ba\7\22\2\2\u00b9\u00b8\3\2\2\2\u00b9\u00ba")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\7B\2\2\u00bc")
        buf.write("\u00bf\7\67\2\2\u00bd\u00c0\5\24\13\2\u00be\u00c0\5 \21")
        buf.write("\2\u00bf\u00bd\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0\21\3")
        buf.write("\2\2\2\u00c1\u00c2\7B\2\2\u00c2\u00c3\7\65\2\2\u00c3\u00c6")
        buf.write("\5\22\n\2\u00c4\u00c6\7B\2\2\u00c5\u00c1\3\2\2\2\u00c5")
        buf.write("\u00c4\3\2\2\2\u00c6\23\3\2\2\2\u00c7\u00c8\t\2\2\2\u00c8")
        buf.write("\25\3\2\2\2\u00c9\u00ca\7B\2\2\u00ca\u00cb\7\67\2\2\u00cb")
        buf.write("\u00cc\7\13\2\2\u00cc\u00cd\5\30\r\2\u00cd\u00ce\7\60")
        buf.write("\2\2\u00ce\u00cf\5\32\16\2\u00cf\u00d1\7\61\2\2\u00d0")
        buf.write("\u00d2\5\36\20\2\u00d1\u00d0\3\2\2\2\u00d1\u00d2\3\2\2")
        buf.write("\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\5@!\2\u00d4\27\3\2")
        buf.write("\2\2\u00d5\u00dd\7\6\2\2\u00d6\u00dd\7\r\2\2\u00d7\u00dd")
        buf.write("\7\t\2\2\u00d8\u00dd\7\17\2\2\u00d9\u00dd\7\21\2\2\u00da")
        buf.write("\u00dd\7\4\2\2\u00db\u00dd\5 \21\2\u00dc\u00d5\3\2\2\2")
        buf.write("\u00dc\u00d6\3\2\2\2\u00dc\u00d7\3\2\2\2\u00dc\u00d8\3")
        buf.write("\2\2\2\u00dc\u00d9\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00db")
        buf.write("\3\2\2\2\u00dd\31\3\2\2\2\u00de\u00e1\5\34\17\2\u00df")
        buf.write("\u00e1\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00df\3\2\2\2")
        buf.write("\u00e1\33\3\2\2\2\u00e2\u00e3\5\20\t\2\u00e3\u00e4\7\65")
        buf.write("\2\2\u00e4\u00e5\5\34\17\2\u00e5\u00e8\3\2\2\2\u00e6\u00e8")
        buf.write("\5\20\t\2\u00e7\u00e2\3\2\2\2\u00e7\u00e6\3\2\2\2\u00e8")
        buf.write("\35\3\2\2\2\u00e9\u00ea\7\25\2\2\u00ea\u00eb\7B\2\2\u00eb")
        buf.write("\37\3\2\2\2\u00ec\u00ed\7\26\2\2\u00ed\u00ee\7\62\2\2")
        buf.write("\u00ee\u00ef\5\"\22\2\u00ef\u00f0\7\63\2\2\u00f0\u00f1")
        buf.write("\7\24\2\2\u00f1\u00f2\5\24\13\2\u00f2!\3\2\2\2\u00f3\u00f4")
        buf.write("\7=\2\2\u00f4\u00f5\7\65\2\2\u00f5\u00f8\5\"\22\2\u00f6")
        buf.write("\u00f8\7=\2\2\u00f7\u00f3\3\2\2\2\u00f7\u00f6\3\2\2\2")
        buf.write("\u00f8#\3\2\2\2\u00f9\u00fa\78\2\2\u00fa\u00fb\5> \2\u00fb")
        buf.write("\u00fc\79\2\2\u00fc%\3\2\2\2\u00fd\u00fe\5(\25\2\u00fe")
        buf.write("\u00ff\7/\2\2\u00ff\u0100\5(\25\2\u0100\u0103\3\2\2\2")
        buf.write("\u0101\u0103\5(\25\2\u0102\u00fd\3\2\2\2\u0102\u0101\3")
        buf.write("\2\2\2\u0103\'\3\2\2\2\u0104\u0105\5*\26\2\u0105\u0106")
        buf.write("\t\3\2\2\u0106\u0107\5*\26\2\u0107\u010a\3\2\2\2\u0108")
        buf.write("\u010a\5*\26\2\u0109\u0104\3\2\2\2\u0109\u0108\3\2\2\2")
        buf.write("\u010a)\3\2\2\2\u010b\u010c\b\26\1\2\u010c\u010d\5,\27")
        buf.write("\2\u010d\u0113\3\2\2\2\u010e\u010f\f\4\2\2\u010f\u0110")
        buf.write("\t\4\2\2\u0110\u0112\5,\27\2\u0111\u010e\3\2\2\2\u0112")
        buf.write("\u0115\3\2\2\2\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2\2")
        buf.write("\u0114+\3\2\2\2\u0115\u0113\3\2\2\2\u0116\u0117\b\27\1")
        buf.write("\2\u0117\u0118\5.\30\2\u0118\u011e\3\2\2\2\u0119\u011a")
        buf.write("\f\4\2\2\u011a\u011b\t\5\2\2\u011b\u011d\5.\30\2\u011c")
        buf.write("\u0119\3\2\2\2\u011d\u0120\3\2\2\2\u011e\u011c\3\2\2\2")
        buf.write("\u011e\u011f\3\2\2\2\u011f-\3\2\2\2\u0120\u011e\3\2\2")
        buf.write("\2\u0121\u0122\b\30\1\2\u0122\u0123\5\60\31\2\u0123\u0129")
        buf.write("\3\2\2\2\u0124\u0125\f\4\2\2\u0125\u0126\t\6\2\2\u0126")
        buf.write("\u0128\5\60\31\2\u0127\u0124\3\2\2\2\u0128\u012b\3\2\2")
        buf.write("\2\u0129\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a/\3\2")
        buf.write("\2\2\u012b\u0129\3\2\2\2\u012c\u012d\7&\2\2\u012d\u0130")
        buf.write("\5\60\31\2\u012e\u0130\5\62\32\2\u012f\u012c\3\2\2\2\u012f")
        buf.write("\u012e\3\2\2\2\u0130\61\3\2\2\2\u0131\u0132\7\"\2\2\u0132")
        buf.write("\u0135\5\62\32\2\u0133\u0135\5\64\33\2\u0134\u0131\3\2")
        buf.write("\2\2\u0134\u0133\3\2\2\2\u0135\63\3\2\2\2\u0136\u0137")
        buf.write("\7B\2\2\u0137\u0138\7\62\2\2\u0138\u0139\5> \2\u0139\u013a")
        buf.write("\7\63\2\2\u013a\u013d\3\2\2\2\u013b\u013d\5\66\34\2\u013c")
        buf.write("\u0136\3\2\2\2\u013c\u013b\3\2\2\2\u013d\65\3\2\2\2\u013e")
        buf.write("\u013f\7\60\2\2\u013f\u0140\5&\24\2\u0140\u0141\7\61\2")
        buf.write("\2\u0141\u0144\3\2\2\2\u0142\u0144\58\35\2\u0143\u013e")
        buf.write("\3\2\2\2\u0143\u0142\3\2\2\2\u0144\67\3\2\2\2\u0145\u014d")
        buf.write("\7=\2\2\u0146\u014d\7>\2\2\u0147\u014d\7?\2\2\u0148\u014d")
        buf.write("\7@\2\2\u0149\u014d\7B\2\2\u014a\u014d\5f\64\2\u014b\u014d")
        buf.write("\5$\23\2\u014c\u0145\3\2\2\2\u014c\u0146\3\2\2\2\u014c")
        buf.write("\u0147\3\2\2\2\u014c\u0148\3\2\2\2\u014c\u0149\3\2\2\2")
        buf.write("\u014c\u014a\3\2\2\2\u014c\u014b\3\2\2\2\u014d9\3\2\2")
        buf.write("\2\u014e\u0151\5<\37\2\u014f\u0151\3\2\2\2\u0150\u014e")
        buf.write("\3\2\2\2\u0150\u014f\3\2\2\2\u0151;\3\2\2\2\u0152\u0153")
        buf.write("\5&\24\2\u0153\u0154\7\65\2\2\u0154\u0155\5<\37\2\u0155")
        buf.write("\u0158\3\2\2\2\u0156\u0158\5&\24\2\u0157\u0152\3\2\2\2")
        buf.write("\u0157\u0156\3\2\2\2\u0158=\3\2\2\2\u0159\u015a\5&\24")
        buf.write("\2\u015a\u015b\7\65\2\2\u015b\u015c\5> \2\u015c\u015f")
        buf.write("\3\2\2\2\u015d\u015f\5&\24\2\u015e\u0159\3\2\2\2\u015e")
        buf.write("\u015d\3\2\2\2\u015f?\3\2\2\2\u0160\u016b\5B\"\2\u0161")
        buf.write("\u016b\5F$\2\u0162\u016b\5H%\2\u0163\u016b\5P)\2\u0164")
        buf.write("\u016b\5R*\2\u0165\u016b\5T+\2\u0166\u016b\5V,\2\u0167")
        buf.write("\u016b\5X-\2\u0168\u016b\5Z.\2\u0169\u016b\5\\/\2\u016a")
        buf.write("\u0160\3\2\2\2\u016a\u0161\3\2\2\2\u016a\u0162\3\2\2\2")
        buf.write("\u016a\u0163\3\2\2\2\u016a\u0164\3\2\2\2\u016a\u0165\3")
        buf.write("\2\2\2\u016a\u0166\3\2\2\2\u016a\u0167\3\2\2\2\u016a\u0168")
        buf.write("\3\2\2\2\u016a\u0169\3\2\2\2\u016bA\3\2\2\2\u016c\u016d")
        buf.write("\5D#\2\u016d\u016e\7:\2\2\u016e\u016f\5&\24\2\u016f\u0170")
        buf.write("\7\66\2\2\u0170C\3\2\2\2\u0171\u0178\7B\2\2\u0172\u0173")
        buf.write("\7B\2\2\u0173\u0174\7\62\2\2\u0174\u0175\5> \2\u0175\u0176")
        buf.write("\7\63\2\2\u0176\u0178\3\2\2\2\u0177\u0171\3\2\2\2\u0177")
        buf.write("\u0172\3\2\2\2\u0178E\3\2\2\2\u0179\u017a\7\f\2\2\u017a")
        buf.write("\u017b\5&\24\2\u017b\u017e\5@!\2\u017c\u017d\7\b\2\2\u017d")
        buf.write("\u017f\5@!\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f")
        buf.write("G\3\2\2\2\u0180\u0181\7\n\2\2\u0181\u0182\7\60\2\2\u0182")
        buf.write("\u0183\5J&\2\u0183\u0184\7\65\2\2\u0184\u0185\5L\'\2\u0185")
        buf.write("\u0186\7\65\2\2\u0186\u0187\5N(\2\u0187\u0188\7\61\2\2")
        buf.write("\u0188\u0189\5@!\2\u0189I\3\2\2\2\u018a\u018b\7B\2\2\u018b")
        buf.write("\u018c\7:\2\2\u018c\u018d\5&\24\2\u018dK\3\2\2\2\u018e")
        buf.write("\u018f\5&\24\2\u018f\u0190\t\3\2\2\u0190\u0191\5&\24\2")
        buf.write("\u0191M\3\2\2\2\u0192\u0193\5&\24\2\u0193O\3\2\2\2\u0194")
        buf.write("\u0195\7\20\2\2\u0195\u0196\5&\24\2\u0196\u0197\5@!\2")
        buf.write("\u0197Q\3\2\2\2\u0198\u0199\7\7\2\2\u0199\u019a\5\\/\2")
        buf.write("\u019a\u019b\7\20\2\2\u019b\u019c\5&\24\2\u019c\u019d")
        buf.write("\7\66\2\2\u019dS\3\2\2\2\u019e\u019f\7\5\2\2\u019f\u01a0")
        buf.write("\7\66\2\2\u01a0U\3\2\2\2\u01a1\u01a2\7\23\2\2\u01a2\u01a3")
        buf.write("\7\66\2\2\u01a3W\3\2\2\2\u01a4\u01a7\7\16\2\2\u01a5\u01a8")
        buf.write("\5&\24\2\u01a6\u01a8\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7")
        buf.write("\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa\7\66\2")
        buf.write("\2\u01aaY\3\2\2\2\u01ab\u01ae\5f\64\2\u01ac\u01ae\5j\66")
        buf.write("\2\u01ad\u01ab\3\2\2\2\u01ad\u01ac\3\2\2\2\u01ae\u01af")
        buf.write("\3\2\2\2\u01af\u01b0\7\66\2\2\u01b0[\3\2\2\2\u01b1\u01b2")
        buf.write("\78\2\2\u01b2\u01b3\5^\60\2\u01b3\u01b4\79\2\2\u01b4\u01b7")
        buf.write("\3\2\2\2\u01b5\u01b7\7\3\2\2\u01b6\u01b1\3\2\2\2\u01b6")
        buf.write("\u01b5\3\2\2\2\u01b7]\3\2\2\2\u01b8\u01b9\5`\61\2\u01b9")
        buf.write("\u01ba\5^\60\2\u01ba\u01bd\3\2\2\2\u01bb\u01bd\3\2\2\2")
        buf.write("\u01bc\u01b8\3\2\2\2\u01bc\u01bb\3\2\2\2\u01bd_\3\2\2")
        buf.write("\2\u01be\u01c1\5b\62\2\u01bf\u01c1\5d\63\2\u01c0\u01be")
        buf.write("\3\2\2\2\u01c0\u01bf\3\2\2\2\u01c1a\3\2\2\2\u01c2\u01c3")
        buf.write("\5@!\2\u01c3\u01c4\5b\62\2\u01c4\u01c7\3\2\2\2\u01c5\u01c7")
        buf.write("\5@!\2\u01c6\u01c2\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7c")
        buf.write("\3\2\2\2\u01c8\u01c9\5\6\4\2\u01c9\u01ca\5d\63\2\u01ca")
        buf.write("\u01cd\3\2\2\2\u01cb\u01cd\5\6\4\2\u01cc\u01c8\3\2\2\2")
        buf.write("\u01cc\u01cb\3\2\2\2\u01cde\3\2\2\2\u01ce\u01cf\7B\2\2")
        buf.write("\u01cf\u01d0\7\60\2\2\u01d0\u01d1\5:\36\2\u01d1\u01d2")
        buf.write("\7\61\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d5\5j\66\2\u01d4")
        buf.write("\u01ce\3\2\2\2\u01d4\u01d3\3\2\2\2\u01d5g\3\2\2\2\u01d6")
        buf.write("\u01d7\5f\64\2\u01d7\u01d8\7\65\2\2\u01d8\u01d9\5h\65")
        buf.write("\2\u01d9\u01dc\3\2\2\2\u01da\u01dc\5f\64\2\u01db\u01d6")
        buf.write("\3\2\2\2\u01db\u01da\3\2\2\2\u01dci\3\2\2\2\u01dd\u01e7")
        buf.write("\5l\67\2\u01de\u01e7\5n8\2\u01df\u01e7\5p9\2\u01e0\u01e7")
        buf.write("\5r:\2\u01e1\u01e7\5v<\2\u01e2\u01e7\5x=\2\u01e3\u01e7")
        buf.write("\5z>\2\u01e4\u01e7\5|?\2\u01e5\u01e7\5~@\2\u01e6\u01dd")
        buf.write("\3\2\2\2\u01e6\u01de\3\2\2\2\u01e6\u01df\3\2\2\2\u01e6")
        buf.write("\u01e0\3\2\2\2\u01e6\u01e1\3\2\2\2\u01e6\u01e2\3\2\2\2")
        buf.write("\u01e6\u01e3\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e5\3")
        buf.write("\2\2\2\u01e7k\3\2\2\2\u01e8\u01e9\7\27\2\2\u01e9\u01ea")
        buf.write("\7\60\2\2\u01ea\u01eb\7\61\2\2\u01ebm\3\2\2\2\u01ec\u01ed")
        buf.write("\7\30\2\2\u01ed\u01ee\7\60\2\2\u01ee\u01ef\5&\24\2\u01ef")
        buf.write("\u01f0\7\61\2\2\u01f0o\3\2\2\2\u01f1\u01f2\7\31\2\2\u01f2")
        buf.write("\u01f3\7\60\2\2\u01f3\u01f4\7\61\2\2\u01f4q\3\2\2\2\u01f5")
        buf.write("\u01f6\7\32\2\2\u01f6\u01f7\7\60\2\2\u01f7\u01f8\5&\24")
        buf.write("\2\u01f8\u01f9\7\61\2\2\u01f9s\3\2\2\2\u01fa\u01fb\7\33")
        buf.write("\2\2\u01fb\u01fc\7\60\2\2\u01fc\u01fd\7\61\2\2\u01fdu")
        buf.write("\3\2\2\2\u01fe\u01ff\7\34\2\2\u01ff\u0200\7\60\2\2\u0200")
        buf.write("\u0201\5&\24\2\u0201\u0202\7\61\2\2\u0202w\3\2\2\2\u0203")
        buf.write("\u0204\7\35\2\2\u0204\u0205\7\60\2\2\u0205\u0206\7\61")
        buf.write("\2\2\u0206y\3\2\2\2\u0207\u0208\7\36\2\2\u0208\u0209\7")
        buf.write("\60\2\2\u0209\u020a\5&\24\2\u020a\u020b\7\61\2\2\u020b")
        buf.write("{\3\2\2\2\u020c\u020d\7\37\2\2\u020d\u020e\7\60\2\2\u020e")
        buf.write("\u020f\5> \2\u020f\u0210\7\61\2\2\u0210}\3\2\2\2\u0211")
        buf.write("\u0212\7 \2\2\u0212\u0213\7\60\2\2\u0213\u0214\7\61\2")
        buf.write("\2\u0214\177\3\2\2\2,\u0083\u0089\u008d\u0099\u00a2\u00a8")
        buf.write("\u00b1\u00b6\u00b9\u00bf\u00c5\u00d1\u00dc\u00e0\u00e7")
        buf.write("\u00f7\u0102\u0109\u0113\u011e\u0129\u012f\u0134\u013c")
        buf.write("\u0143\u014c\u0150\u0157\u015e\u016a\u0177\u017e\u01a7")
        buf.write("\u01ad\u01b6\u01bc\u01c0\u01c6\u01cc\u01d4\u01db\u01e6")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{}'", "'auto'", "'break'", "'boolean'", 
                     "'do'", "'else'", "'float'", "'for'", "'function'", 
                     "'if'", "'integer'", "'return'", "'string'", "'while'", 
                     "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
                     "'array'", "'readInteger'", "'printInteger'", "'readFloat'", 
                     "'writeFloat'", "'readBoolean'", "'printBoolean'", 
                     "'readString'", "'printString'", "'super'", "'preventDefault'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
                     "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", 
                     "'{'", "'}'", "'='", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "AUTO", "BREAK", "BOOLEAN", 
                      "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
                      "RETURN", "STRING", "WHILE", "VOID", "OUT", "CONTINUE", 
                      "OF", "INHERIT", "ARRAY", "READINTEGER", "PRINTINTEGER", 
                      "READFLOAT", "WRITEFLOAT", "READBOOLEAN", "PRINTBOOLEAN", 
                      "READSTRING", "PRINTSTRING", "SUPER", "PREVENTDEFAULT", 
                      "ADD", "MINUS", "MUL", "DIV", "MODUL", "NOT", "AND", 
                      "OR", "EQUAL", "NOTEQUAL", "LESSTHAN", "LESSEQUAL", 
                      "GREATERTHAN", "GREATEREQUAL", "DOUBLECOLON", "LP", 
                      "RP", "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", 
                      "LB", "RB", "ASSIGN", "DOUBLEQUOTE", "COMMENT", "INTEGERLIT", 
                      "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "ARRAYLIT", 
                      "IDENTIFIER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

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
    RULE_arraytype = 15
    RULE_dimensions = 16
    RULE_arrayLit = 17
    RULE_expression = 18
    RULE_expr1 = 19
    RULE_expr2 = 20
    RULE_expr3 = 21
    RULE_expr4 = 22
    RULE_expr5 = 23
    RULE_expr6 = 24
    RULE_expr7 = 25
    RULE_expr8 = 26
    RULE_factor = 27
    RULE_expressionListNullable = 28
    RULE_expressionPrime = 29
    RULE_expressionListNonnull = 30
    RULE_statement = 31
    RULE_assignStmt = 32
    RULE_lhs = 33
    RULE_ifStmt = 34
    RULE_forStmt = 35
    RULE_initExpr = 36
    RULE_conditionExpr = 37
    RULE_updateExpr = 38
    RULE_whileStmt = 39
    RULE_doWhileStmt = 40
    RULE_breakStmt = 41
    RULE_continueStmt = 42
    RULE_returnStmt = 43
    RULE_callStmt = 44
    RULE_blockStmt = 45
    RULE_stmtsOrVardecls = 46
    RULE_stmtOrVardecl = 47
    RULE_statementList = 48
    RULE_vardeclList = 49
    RULE_functionCall = 50
    RULE_functionCallList = 51
    RULE_specialFunc = 52
    RULE_readInteger = 53
    RULE_printInteger = 54
    RULE_readFloat = 55
    RULE_writeFloat = 56
    RULE_readBoolean = 57
    RULE_printBoolean = 58
    RULE_readString = 59
    RULE_printString = 60
    RULE_superFunction = 61
    RULE_preventDefault = 62

    ruleNames =  [ "program", "decls", "vardecl", "vardeclAssign", "vardeclAssignment", 
                   "vardeclAssignBaseCase", "vardeclNoAssign", "parameter", 
                   "identifierList", "typ", "funcdecl", "returnType", "parameterList", 
                   "parameterPrime", "inheritanceSubpart", "arraytype", 
                   "dimensions", "arrayLit", "expression", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "expr8", 
                   "factor", "expressionListNullable", "expressionPrime", 
                   "expressionListNonnull", "statement", "assignStmt", "lhs", 
                   "ifStmt", "forStmt", "initExpr", "conditionExpr", "updateExpr", 
                   "whileStmt", "doWhileStmt", "breakStmt", "continueStmt", 
                   "returnStmt", "callStmt", "blockStmt", "stmtsOrVardecls", 
                   "stmtOrVardecl", "statementList", "vardeclList", "functionCall", 
                   "functionCallList", "specialFunc", "readInteger", "printInteger", 
                   "readFloat", "writeFloat", "readBoolean", "printBoolean", 
                   "readString", "printString", "superFunction", "preventDefault" ]

    EOF = Token.EOF
    T__0=1
    AUTO=2
    BREAK=3
    BOOLEAN=4
    DO=5
    ELSE=6
    FLOAT=7
    FOR=8
    FUNCTION=9
    IF=10
    INTEGER=11
    RETURN=12
    STRING=13
    WHILE=14
    VOID=15
    OUT=16
    CONTINUE=17
    OF=18
    INHERIT=19
    ARRAY=20
    READINTEGER=21
    PRINTINTEGER=22
    READFLOAT=23
    WRITEFLOAT=24
    READBOOLEAN=25
    PRINTBOOLEAN=26
    READSTRING=27
    PRINTSTRING=28
    SUPER=29
    PREVENTDEFAULT=30
    ADD=31
    MINUS=32
    MUL=33
    DIV=34
    MODUL=35
    NOT=36
    AND=37
    OR=38
    EQUAL=39
    NOTEQUAL=40
    LESSTHAN=41
    LESSEQUAL=42
    GREATERTHAN=43
    GREATEREQUAL=44
    DOUBLECOLON=45
    LP=46
    RP=47
    LSB=48
    RSB=49
    DOT=50
    COMMA=51
    SEMI=52
    COLON=53
    LB=54
    RB=55
    ASSIGN=56
    DOUBLEQUOTE=57
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
            self.state = 127 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 126
                self.decls()
                self.state = 129 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MT22Parser.IDENTIFIER):
                    break

            self.state = 131
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
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
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
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.vardeclAssign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
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


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def vardeclAssignBaseCase(self):
            return self.getTypedRuleContext(MT22Parser.VardeclAssignBaseCaseContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardeclAssign




    def vardeclAssign(self):

        localctx = MT22Parser.VardeclAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardeclAssign)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(MT22Parser.IDENTIFIER)
                self.state = 142
                self.match(MT22Parser.COMMA)
                self.state = 143
                self.vardeclAssignment()
                self.state = 144
                self.match(MT22Parser.COMMA)
                self.state = 145
                self.expression()
                self.state = 146
                self.match(MT22Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.vardeclAssignBaseCase()
                self.state = 149
                self.match(MT22Parser.SEMI)
                pass


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
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.match(MT22Parser.IDENTIFIER)
                self.state = 154
                self.match(MT22Parser.COMMA)
                self.state = 155
                self.vardeclAssignment()
                self.state = 156
                self.match(MT22Parser.COMMA)
                self.state = 157
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
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


        def arraytype(self):
            return self.getTypedRuleContext(MT22Parser.ArraytypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardeclAssignBaseCase




    def vardeclAssignBaseCase(self):

        localctx = MT22Parser.VardeclAssignBaseCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardeclAssignBaseCase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(MT22Parser.IDENTIFIER)
            self.state = 163
            self.match(MT22Parser.COLON)
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.AUTO, MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.state = 164
                self.typ()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.state = 165
                self.arraytype()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 168
            self.match(MT22Parser.ASSIGN)
            self.state = 169
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


        def arraytype(self):
            return self.getTypedRuleContext(MT22Parser.ArraytypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardeclNoAssign




    def vardeclNoAssign(self):

        localctx = MT22Parser.VardeclNoAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vardeclNoAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.identifierList()
            self.state = 172
            self.match(MT22Parser.COLON)
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.AUTO, MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.state = 173
                self.typ()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.state = 174
                self.arraytype()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 177
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


        def arraytype(self):
            return self.getTypedRuleContext(MT22Parser.ArraytypeContext,0)


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
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 179
                self.match(MT22Parser.INHERIT)


            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 182
                self.match(MT22Parser.OUT)


            self.state = 185
            self.match(MT22Parser.IDENTIFIER)
            self.state = 186
            self.match(MT22Parser.COLON)
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.AUTO, MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.state = 187
                self.typ()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.state = 188
                self.arraytype()
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
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(MT22Parser.IDENTIFIER)
                self.state = 192
                self.match(MT22Parser.COMMA)
                self.state = 193
                self.identifierList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
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
            self.state = 197
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

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


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
            self.state = 199
            self.match(MT22Parser.IDENTIFIER)
            self.state = 200
            self.match(MT22Parser.COLON)
            self.state = 201
            self.match(MT22Parser.FUNCTION)
            self.state = 202
            self.returnType()
            self.state = 203
            self.match(MT22Parser.LP)
            self.state = 204
            self.parameterList()
            self.state = 205
            self.match(MT22Parser.RP)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 206
                self.inheritanceSubpart()


            self.state = 209
            self.statement()
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

        def arraytype(self):
            return self.getTypedRuleContext(MT22Parser.ArraytypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_returnType




    def returnType(self):

        localctx = MT22Parser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_returnType)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(MT22Parser.BOOLEAN)
                pass
            elif token in [MT22Parser.INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(MT22Parser.INTEGER)
                pass
            elif token in [MT22Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.match(MT22Parser.FLOAT)
                pass
            elif token in [MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 214
                self.match(MT22Parser.STRING)
                pass
            elif token in [MT22Parser.VOID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 215
                self.match(MT22Parser.VOID)
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 6)
                self.state = 216
                self.match(MT22Parser.AUTO)
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 7)
                self.state = 217
                self.arraytype()
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
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT, MT22Parser.INHERIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
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
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.parameter()
                self.state = 225
                self.match(MT22Parser.COMMA)
                self.state = 226
                self.parameterPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
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
            self.state = 231
            self.match(MT22Parser.INHERIT)
            self.state = 232
            self.match(MT22Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):
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

        def typ(self):
            return self.getTypedRuleContext(MT22Parser.TypContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arraytype




    def arraytype(self):

        localctx = MT22Parser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(MT22Parser.ARRAY)
            self.state = 235
            self.match(MT22Parser.LSB)
            self.state = 236
            self.dimensions()
            self.state = 237
            self.match(MT22Parser.RSB)
            self.state = 238
            self.match(MT22Parser.OF)
            self.state = 239
            self.typ()
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
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(MT22Parser.INTEGERLIT)
                self.state = 242
                self.match(MT22Parser.COMMA)
                self.state = 243
                self.dimensions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(MT22Parser.INTEGERLIT)
                pass


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
        self.enterRule(localctx, 34, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(MT22Parser.LB)
            self.state = 248
            self.expressionListNonnull()
            self.state = 249
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
        self.enterRule(localctx, 36, self.RULE_expression)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.expr1()
                self.state = 252
                self.match(MT22Parser.DOUBLECOLON)
                self.state = 253
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
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
        self.enterRule(localctx, 38, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.expr2(0)
                self.state = 259
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUAL) | (1 << MT22Parser.NOTEQUAL) | (1 << MT22Parser.LESSTHAN) | (1 << MT22Parser.LESSEQUAL) | (1 << MT22Parser.GREATERTHAN) | (1 << MT22Parser.GREATEREQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 260
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 268
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 269
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AND or _la==MT22Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 270
                    self.expr3(0) 
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 284
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 279
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 280
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADD or _la==MT22Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 281
                    self.expr4(0) 
                self.state = 286
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 295
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 290
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 291
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MUL) | (1 << MT22Parser.DIV) | (1 << MT22Parser.MODUL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 292
                    self.expr5() 
                self.state = 297
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        self.enterRule(localctx, 46, self.RULE_expr5)
        try:
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(MT22Parser.NOT)
                self.state = 299
                self.expr5()
                pass
            elif token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.MINUS, MT22Parser.LP, MT22Parser.LB, MT22Parser.INTEGERLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLEANLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
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
        self.enterRule(localctx, 48, self.RULE_expr6)
        try:
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.match(MT22Parser.MINUS)
                self.state = 304
                self.expr6()
                pass
            elif token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.LP, MT22Parser.LB, MT22Parser.INTEGERLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLEANLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
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
        self.enterRule(localctx, 50, self.RULE_expr7)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.match(MT22Parser.IDENTIFIER)
                self.state = 309
                self.match(MT22Parser.LSB)
                self.state = 310
                self.expressionListNonnull()
                self.state = 311
                self.match(MT22Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
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
        self.enterRule(localctx, 52, self.RULE_expr8)
        try:
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(MT22Parser.LP)
                self.state = 317
                self.expression()
                self.state = 318
                self.match(MT22Parser.RP)
                pass
            elif token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.LB, MT22Parser.INTEGERLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLEANLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
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
        self.enterRule(localctx, 54, self.RULE_factor)
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(MT22Parser.INTEGERLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.match(MT22Parser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 325
                self.match(MT22Parser.BOOLEANLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 326
                self.match(MT22Parser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 327
                self.match(MT22Parser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 328
                self.functionCall()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 329
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
        self.enterRule(localctx, 56, self.RULE_expressionListNullable)
        try:
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.MINUS, MT22Parser.NOT, MT22Parser.LP, MT22Parser.LB, MT22Parser.INTEGERLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLEANLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
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
        self.enterRule(localctx, 58, self.RULE_expressionPrime)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.expression()
                self.state = 337
                self.match(MT22Parser.COMMA)
                self.state = 338
                self.expressionPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
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
        self.enterRule(localctx, 60, self.RULE_expressionListNonnull)
        try:
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.expression()
                self.state = 344
                self.match(MT22Parser.COMMA)
                self.state = 345
                self.expressionListNonnull()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
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
        self.enterRule(localctx, 62, self.RULE_statement)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.assignStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.ifStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 352
                self.forStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 353
                self.whileStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 354
                self.doWhileStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 355
                self.breakStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 356
                self.continueStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 357
                self.returnStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 358
                self.callStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 359
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
        self.enterRule(localctx, 64, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.lhs()
            self.state = 363
            self.match(MT22Parser.ASSIGN)
            self.state = 364
            self.expression()
            self.state = 365
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
        self.enterRule(localctx, 66, self.RULE_lhs)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.match(MT22Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.match(MT22Parser.IDENTIFIER)
                self.state = 369
                self.match(MT22Parser.LSB)
                self.state = 370
                self.expressionListNonnull()
                self.state = 371
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
        self.enterRule(localctx, 68, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(MT22Parser.IF)
            self.state = 376
            self.expression()
            self.state = 377
            self.statement()
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 378
                self.match(MT22Parser.ELSE)
                self.state = 379
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
        self.enterRule(localctx, 70, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(MT22Parser.FOR)
            self.state = 383
            self.match(MT22Parser.LP)
            self.state = 384
            self.initExpr()
            self.state = 385
            self.match(MT22Parser.COMMA)
            self.state = 386
            self.conditionExpr()
            self.state = 387
            self.match(MT22Parser.COMMA)
            self.state = 388
            self.updateExpr()
            self.state = 389
            self.match(MT22Parser.RP)
            self.state = 390
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
        self.enterRule(localctx, 72, self.RULE_initExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(MT22Parser.IDENTIFIER)
            self.state = 393
            self.match(MT22Parser.ASSIGN)
            self.state = 394
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
        self.enterRule(localctx, 74, self.RULE_conditionExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.expression()
            self.state = 397
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUAL) | (1 << MT22Parser.NOTEQUAL) | (1 << MT22Parser.LESSTHAN) | (1 << MT22Parser.LESSEQUAL) | (1 << MT22Parser.GREATERTHAN) | (1 << MT22Parser.GREATEREQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 398
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
        self.enterRule(localctx, 76, self.RULE_updateExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
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
        self.enterRule(localctx, 78, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(MT22Parser.WHILE)
            self.state = 403
            self.expression()
            self.state = 404
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
        self.enterRule(localctx, 80, self.RULE_doWhileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(MT22Parser.DO)
            self.state = 407
            self.blockStmt()
            self.state = 408
            self.match(MT22Parser.WHILE)
            self.state = 409
            self.expression()
            self.state = 410
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
        self.enterRule(localctx, 82, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(MT22Parser.BREAK)
            self.state = 413
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
        self.enterRule(localctx, 84, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(MT22Parser.CONTINUE)
            self.state = 416
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
        self.enterRule(localctx, 86, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(MT22Parser.RETURN)
            self.state = 421
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.MINUS, MT22Parser.NOT, MT22Parser.LP, MT22Parser.LB, MT22Parser.INTEGERLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLEANLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.state = 419
                self.expression()
                pass
            elif token in [MT22Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 423
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

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def functionCall(self):
            return self.getTypedRuleContext(MT22Parser.FunctionCallContext,0)


        def specialFunc(self):
            return self.getTypedRuleContext(MT22Parser.SpecialFuncContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_callStmt




    def callStmt(self):

        localctx = MT22Parser.CallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_callStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 425
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 426
                self.specialFunc()
                pass


            self.state = 429
            self.match(MT22Parser.SEMI)
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

        def stmtsOrVardecls(self):
            return self.getTypedRuleContext(MT22Parser.StmtsOrVardeclsContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_blockStmt




    def blockStmt(self):

        localctx = MT22Parser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_blockStmt)
        try:
            self.state = 436
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.match(MT22Parser.LB)
                self.state = 432
                self.stmtsOrVardecls()
                self.state = 433
                self.match(MT22Parser.RB)
                pass
            elif token in [MT22Parser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.match(MT22Parser.T__0)
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
        self.enterRule(localctx, 92, self.RULE_stmtsOrVardecls)
        try:
            self.state = 442
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.T__0, MT22Parser.BREAK, MT22Parser.DO, MT22Parser.FOR, MT22Parser.IF, MT22Parser.RETURN, MT22Parser.WHILE, MT22Parser.CONTINUE, MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.LB, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.stmtOrVardecl()
                self.state = 439
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


    class StmtOrVardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(MT22Parser.StatementListContext,0)


        def vardeclList(self):
            return self.getTypedRuleContext(MT22Parser.VardeclListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmtOrVardecl




    def stmtOrVardecl(self):

        localctx = MT22Parser.StmtOrVardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_stmtOrVardecl)
        try:
            self.state = 446
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.statementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.vardeclList()
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
        self.enterRule(localctx, 96, self.RULE_statementList)
        try:
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.statement()
                self.state = 449
                self.statementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
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
        self.enterRule(localctx, 98, self.RULE_vardeclList)
        try:
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.vardecl()
                self.state = 455
                self.vardeclList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
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

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expressionListNullable(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionListNullableContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def specialFunc(self):
            return self.getTypedRuleContext(MT22Parser.SpecialFuncContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functionCall




    def functionCall(self):

        localctx = MT22Parser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_functionCall)
        try:
            self.state = 466
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.match(MT22Parser.IDENTIFIER)
                self.state = 461
                self.match(MT22Parser.LP)
                self.state = 462
                self.expressionListNullable()
                self.state = 463
                self.match(MT22Parser.RP)
                pass
            elif token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                self.specialFunc()
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
        self.enterRule(localctx, 102, self.RULE_functionCallList)
        try:
            self.state = 473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 468
                self.functionCall()
                self.state = 469
                self.match(MT22Parser.COMMA)
                self.state = 470
                self.functionCallList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 472
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
        self.enterRule(localctx, 104, self.RULE_specialFunc)
        try:
            self.state = 484
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.READINTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
                self.readInteger()
                pass
            elif token in [MT22Parser.PRINTINTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 476
                self.printInteger()
                pass
            elif token in [MT22Parser.READFLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 477
                self.readFloat()
                pass
            elif token in [MT22Parser.WRITEFLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 478
                self.writeFloat()
                pass
            elif token in [MT22Parser.PRINTBOOLEAN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 479
                self.printBoolean()
                pass
            elif token in [MT22Parser.READSTRING]:
                self.enterOuterAlt(localctx, 6)
                self.state = 480
                self.readString()
                pass
            elif token in [MT22Parser.PRINTSTRING]:
                self.enterOuterAlt(localctx, 7)
                self.state = 481
                self.printString()
                pass
            elif token in [MT22Parser.SUPER]:
                self.enterOuterAlt(localctx, 8)
                self.state = 482
                self.superFunction()
                pass
            elif token in [MT22Parser.PREVENTDEFAULT]:
                self.enterOuterAlt(localctx, 9)
                self.state = 483
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
        self.enterRule(localctx, 106, self.RULE_readInteger)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(MT22Parser.READINTEGER)
            self.state = 487
            self.match(MT22Parser.LP)
            self.state = 488
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
        self.enterRule(localctx, 108, self.RULE_printInteger)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.match(MT22Parser.PRINTINTEGER)
            self.state = 491
            self.match(MT22Parser.LP)
            self.state = 492
            self.expression()
            self.state = 493
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
        self.enterRule(localctx, 110, self.RULE_readFloat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(MT22Parser.READFLOAT)
            self.state = 496
            self.match(MT22Parser.LP)
            self.state = 497
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
        self.enterRule(localctx, 112, self.RULE_writeFloat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(MT22Parser.WRITEFLOAT)
            self.state = 500
            self.match(MT22Parser.LP)
            self.state = 501
            self.expression()
            self.state = 502
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
        self.enterRule(localctx, 114, self.RULE_readBoolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(MT22Parser.READBOOLEAN)
            self.state = 505
            self.match(MT22Parser.LP)
            self.state = 506
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
        self.enterRule(localctx, 116, self.RULE_printBoolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(MT22Parser.PRINTBOOLEAN)
            self.state = 509
            self.match(MT22Parser.LP)
            self.state = 510
            self.expression()
            self.state = 511
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
        self.enterRule(localctx, 118, self.RULE_readString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(MT22Parser.READSTRING)
            self.state = 514
            self.match(MT22Parser.LP)
            self.state = 515
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
        self.enterRule(localctx, 120, self.RULE_printString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(MT22Parser.PRINTSTRING)
            self.state = 518
            self.match(MT22Parser.LP)
            self.state = 519
            self.expression()
            self.state = 520
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
        self.enterRule(localctx, 122, self.RULE_superFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            self.match(MT22Parser.SUPER)
            self.state = 523
            self.match(MT22Parser.LP)
            self.state = 524
            self.expressionListNonnull()
            self.state = 525
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
        self.enterRule(localctx, 124, self.RULE_preventDefault)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(MT22Parser.PREVENTDEFAULT)
            self.state = 528
            self.match(MT22Parser.LP)
            self.state = 529
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
        self._predicates[20] = self.expr2_sempred
        self._predicates[21] = self.expr3_sempred
        self._predicates[22] = self.expr4_sempred
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
         




