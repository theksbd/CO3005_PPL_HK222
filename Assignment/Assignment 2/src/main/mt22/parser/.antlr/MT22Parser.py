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
        buf.write("\u0211\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\6\2\u0084\n")
        buf.write("\2\r\2\16\2\u0085\3\2\3\2\3\3\3\3\5\3\u008c\n\3\3\4\3")
        buf.write("\4\5\4\u0090\n\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\5\6\u009c\n\6\3\7\3\7\3\7\3\7\5\7\u00a2\n\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\5\b\u00ab\n\b\3\b\3\b\3\t\5\t\u00b0")
        buf.write("\n\t\3\t\5\t\u00b3\n\t\3\t\3\t\3\t\3\t\5\t\u00b9\n\t\3")
        buf.write("\n\3\n\3\n\3\n\5\n\u00bf\n\n\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\5\f\u00cb\n\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\5\r\u00d6\n\r\3\16\3\16\5\16\u00da\n\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\5\17\u00e1\n\17\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u00f1\n\22\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\5\25\u00fe\n\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\5\26\u0105\n\26\3\27\3\27\3\27\3\27\3\27\3\27\7")
        buf.write("\27\u010d\n\27\f\27\16\27\u0110\13\27\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\7\30\u0118\n\30\f\30\16\30\u011b\13\30\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\7\31\u0123\n\31\f\31\16\31")
        buf.write("\u0126\13\31\3\32\3\32\3\32\5\32\u012b\n\32\3\33\3\33")
        buf.write("\3\33\5\33\u0130\n\33\3\34\3\34\3\34\3\34\3\34\3\34\5")
        buf.write("\34\u0138\n\34\3\35\3\35\3\35\3\35\3\35\5\35\u013f\n\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0148\n\36\3")
        buf.write("\37\3\37\5\37\u014c\n\37\3 \3 \3 \3 \3 \5 \u0153\n \3")
        buf.write("!\3!\3!\3!\3!\5!\u015a\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\5\"\u0166\n\"\3#\3#\3#\3#\3#\3$\3$\3$\3$")
        buf.write("\3$\3$\5$\u0173\n$\3%\3%\3%\3%\3%\5%\u017a\n%\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)")
        buf.write("\3)\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3")
        buf.write(".\3.\3.\5.\u01a3\n.\3.\3.\3/\3/\5/\u01a9\n/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\60\3\60\5\60\u01b2\n\60\3\61\3\61\3\61\3")
        buf.write("\61\5\61\u01b8\n\61\3\62\3\62\5\62\u01bc\n\62\3\63\3\63")
        buf.write("\3\63\3\63\5\63\u01c2\n\63\3\64\3\64\3\64\3\64\5\64\u01c8")
        buf.write("\n\64\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u01d0\n\65\3")
        buf.write("\66\3\66\3\66\3\66\3\66\5\66\u01d7\n\66\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u01e2\n\67\38\38\3")
        buf.write("8\38\39\39\39\39\39\3:\3:\3:\3:\3;\3;\3;\3;\3;\3<\3<\3")
        buf.write("<\3<\3=\3=\3=\3=\3=\3>\3>\3>\3>\3?\3?\3?\3?\3?\3@\3@\3")
        buf.write("@\3@\3@\3A\3A\3A\3A\3A\2\5,.\60B\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnprtvxz|~\u0080\2\b\7\2\4\4\6\6\t\t\r\r")
        buf.write("\17\17\6\2\6\6\t\t\r\r\17\17\3\2).\3\2\'(\3\2!\"\3\2#")
        buf.write("%\2\u0212\2\u0083\3\2\2\2\4\u008b\3\2\2\2\6\u008f\3\2")
        buf.write("\2\2\b\u0091\3\2\2\2\n\u009b\3\2\2\2\f\u009d\3\2\2\2\16")
        buf.write("\u00a6\3\2\2\2\20\u00af\3\2\2\2\22\u00be\3\2\2\2\24\u00c0")
        buf.write("\3\2\2\2\26\u00c2\3\2\2\2\30\u00d5\3\2\2\2\32\u00d9\3")
        buf.write("\2\2\2\34\u00e0\3\2\2\2\36\u00e2\3\2\2\2 \u00e5\3\2\2")
        buf.write("\2\"\u00f0\3\2\2\2$\u00f2\3\2\2\2&\u00f4\3\2\2\2(\u00fd")
        buf.write("\3\2\2\2*\u0104\3\2\2\2,\u0106\3\2\2\2.\u0111\3\2\2\2")
        buf.write("\60\u011c\3\2\2\2\62\u012a\3\2\2\2\64\u012f\3\2\2\2\66")
        buf.write("\u0137\3\2\2\28\u013e\3\2\2\2:\u0147\3\2\2\2<\u014b\3")
        buf.write("\2\2\2>\u0152\3\2\2\2@\u0159\3\2\2\2B\u0165\3\2\2\2D\u0167")
        buf.write("\3\2\2\2F\u0172\3\2\2\2H\u0174\3\2\2\2J\u017b\3\2\2\2")
        buf.write("L\u0185\3\2\2\2N\u0189\3\2\2\2P\u018d\3\2\2\2R\u018f\3")
        buf.write("\2\2\2T\u0193\3\2\2\2V\u0199\3\2\2\2X\u019c\3\2\2\2Z\u019f")
        buf.write("\3\2\2\2\\\u01a8\3\2\2\2^\u01b1\3\2\2\2`\u01b7\3\2\2\2")
        buf.write("b\u01bb\3\2\2\2d\u01c1\3\2\2\2f\u01c7\3\2\2\2h\u01cf\3")
        buf.write("\2\2\2j\u01d6\3\2\2\2l\u01e1\3\2\2\2n\u01e3\3\2\2\2p\u01e7")
        buf.write("\3\2\2\2r\u01ec\3\2\2\2t\u01f0\3\2\2\2v\u01f5\3\2\2\2")
        buf.write("x\u01f9\3\2\2\2z\u01fe\3\2\2\2|\u0202\3\2\2\2~\u0207\3")
        buf.write("\2\2\2\u0080\u020c\3\2\2\2\u0082\u0084\5\4\3\2\u0083\u0082")
        buf.write("\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0083\3\2\2\2\u0085")
        buf.write("\u0086\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\7\2\2\3")
        buf.write("\u0088\3\3\2\2\2\u0089\u008c\5\6\4\2\u008a\u008c\5\26")
        buf.write("\f\2\u008b\u0089\3\2\2\2\u008b\u008a\3\2\2\2\u008c\5\3")
        buf.write("\2\2\2\u008d\u0090\5\b\5\2\u008e\u0090\5\16\b\2\u008f")
        buf.write("\u008d\3\2\2\2\u008f\u008e\3\2\2\2\u0090\7\3\2\2\2\u0091")
        buf.write("\u0092\5\n\6\2\u0092\u0093\7\66\2\2\u0093\t\3\2\2\2\u0094")
        buf.write("\u0095\7B\2\2\u0095\u0096\7\65\2\2\u0096\u0097\5\n\6\2")
        buf.write("\u0097\u0098\7\65\2\2\u0098\u0099\5(\25\2\u0099\u009c")
        buf.write("\3\2\2\2\u009a\u009c\5\f\7\2\u009b\u0094\3\2\2\2\u009b")
        buf.write("\u009a\3\2\2\2\u009c\13\3\2\2\2\u009d\u009e\7B\2\2\u009e")
        buf.write("\u00a1\7\67\2\2\u009f\u00a2\5\24\13\2\u00a0\u00a2\5 \21")
        buf.write("\2\u00a1\u009f\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\u00a4\7:\2\2\u00a4\u00a5\5(\25\2\u00a5")
        buf.write("\r\3\2\2\2\u00a6\u00a7\5\22\n\2\u00a7\u00aa\7\67\2\2\u00a8")
        buf.write("\u00ab\5\24\13\2\u00a9\u00ab\5 \21\2\u00aa\u00a8\3\2\2")
        buf.write("\2\u00aa\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad")
        buf.write("\7\66\2\2\u00ad\17\3\2\2\2\u00ae\u00b0\7\25\2\2\u00af")
        buf.write("\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b2\3\2\2\2")
        buf.write("\u00b1\u00b3\7\22\2\2\u00b2\u00b1\3\2\2\2\u00b2\u00b3")
        buf.write("\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\7B\2\2\u00b5")
        buf.write("\u00b8\7\67\2\2\u00b6\u00b9\5\24\13\2\u00b7\u00b9\5 \21")
        buf.write("\2\u00b8\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\21\3")
        buf.write("\2\2\2\u00ba\u00bb\7B\2\2\u00bb\u00bc\7\65\2\2\u00bc\u00bf")
        buf.write("\5\22\n\2\u00bd\u00bf\7B\2\2\u00be\u00ba\3\2\2\2\u00be")
        buf.write("\u00bd\3\2\2\2\u00bf\23\3\2\2\2\u00c0\u00c1\t\2\2\2\u00c1")
        buf.write("\25\3\2\2\2\u00c2\u00c3\7B\2\2\u00c3\u00c4\7\67\2\2\u00c4")
        buf.write("\u00c5\7\13\2\2\u00c5\u00c6\5\30\r\2\u00c6\u00c7\7\60")
        buf.write("\2\2\u00c7\u00c8\5\32\16\2\u00c8\u00ca\7\61\2\2\u00c9")
        buf.write("\u00cb\5\36\20\2\u00ca\u00c9\3\2\2\2\u00ca\u00cb\3\2\2")
        buf.write("\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\5^\60\2\u00cd\27\3")
        buf.write("\2\2\2\u00ce\u00d6\7\6\2\2\u00cf\u00d6\7\r\2\2\u00d0\u00d6")
        buf.write("\7\t\2\2\u00d1\u00d6\7\17\2\2\u00d2\u00d6\7\21\2\2\u00d3")
        buf.write("\u00d6\7\4\2\2\u00d4\u00d6\5 \21\2\u00d5\u00ce\3\2\2\2")
        buf.write("\u00d5\u00cf\3\2\2\2\u00d5\u00d0\3\2\2\2\u00d5\u00d1\3")
        buf.write("\2\2\2\u00d5\u00d2\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d4")
        buf.write("\3\2\2\2\u00d6\31\3\2\2\2\u00d7\u00da\5\34\17\2\u00d8")
        buf.write("\u00da\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00d8\3\2\2\2")
        buf.write("\u00da\33\3\2\2\2\u00db\u00dc\5\20\t\2\u00dc\u00dd\7\65")
        buf.write("\2\2\u00dd\u00de\5\34\17\2\u00de\u00e1\3\2\2\2\u00df\u00e1")
        buf.write("\5\20\t\2\u00e0\u00db\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1")
        buf.write("\35\3\2\2\2\u00e2\u00e3\7\25\2\2\u00e3\u00e4\7B\2\2\u00e4")
        buf.write("\37\3\2\2\2\u00e5\u00e6\7\26\2\2\u00e6\u00e7\7\62\2\2")
        buf.write("\u00e7\u00e8\5\"\22\2\u00e8\u00e9\7\63\2\2\u00e9\u00ea")
        buf.write("\7\24\2\2\u00ea\u00eb\5$\23\2\u00eb!\3\2\2\2\u00ec\u00ed")
        buf.write("\7=\2\2\u00ed\u00ee\7\65\2\2\u00ee\u00f1\5\"\22\2\u00ef")
        buf.write("\u00f1\7=\2\2\u00f0\u00ec\3\2\2\2\u00f0\u00ef\3\2\2\2")
        buf.write("\u00f1#\3\2\2\2\u00f2\u00f3\t\3\2\2\u00f3%\3\2\2\2\u00f4")
        buf.write("\u00f5\78\2\2\u00f5\u00f6\5@!\2\u00f6\u00f7\79\2\2\u00f7")
        buf.write("\'\3\2\2\2\u00f8\u00f9\5*\26\2\u00f9\u00fa\7/\2\2\u00fa")
        buf.write("\u00fb\5*\26\2\u00fb\u00fe\3\2\2\2\u00fc\u00fe\5*\26\2")
        buf.write("\u00fd\u00f8\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe)\3\2\2")
        buf.write("\2\u00ff\u0100\5,\27\2\u0100\u0101\t\4\2\2\u0101\u0102")
        buf.write("\5,\27\2\u0102\u0105\3\2\2\2\u0103\u0105\5,\27\2\u0104")
        buf.write("\u00ff\3\2\2\2\u0104\u0103\3\2\2\2\u0105+\3\2\2\2\u0106")
        buf.write("\u0107\b\27\1\2\u0107\u0108\5.\30\2\u0108\u010e\3\2\2")
        buf.write("\2\u0109\u010a\f\4\2\2\u010a\u010b\t\5\2\2\u010b\u010d")
        buf.write("\5.\30\2\u010c\u0109\3\2\2\2\u010d\u0110\3\2\2\2\u010e")
        buf.write("\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f-\3\2\2\2\u0110")
        buf.write("\u010e\3\2\2\2\u0111\u0112\b\30\1\2\u0112\u0113\5\60\31")
        buf.write("\2\u0113\u0119\3\2\2\2\u0114\u0115\f\4\2\2\u0115\u0116")
        buf.write("\t\6\2\2\u0116\u0118\5\60\31\2\u0117\u0114\3\2\2\2\u0118")
        buf.write("\u011b\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a\3\2\2\2")
        buf.write("\u011a/\3\2\2\2\u011b\u0119\3\2\2\2\u011c\u011d\b\31\1")
        buf.write("\2\u011d\u011e\5\62\32\2\u011e\u0124\3\2\2\2\u011f\u0120")
        buf.write("\f\4\2\2\u0120\u0121\t\7\2\2\u0121\u0123\5\62\32\2\u0122")
        buf.write("\u011f\3\2\2\2\u0123\u0126\3\2\2\2\u0124\u0122\3\2\2\2")
        buf.write("\u0124\u0125\3\2\2\2\u0125\61\3\2\2\2\u0126\u0124\3\2")
        buf.write("\2\2\u0127\u0128\7&\2\2\u0128\u012b\5\62\32\2\u0129\u012b")
        buf.write("\5\64\33\2\u012a\u0127\3\2\2\2\u012a\u0129\3\2\2\2\u012b")
        buf.write("\63\3\2\2\2\u012c\u012d\7\"\2\2\u012d\u0130\5\64\33\2")
        buf.write("\u012e\u0130\5\66\34\2\u012f\u012c\3\2\2\2\u012f\u012e")
        buf.write("\3\2\2\2\u0130\65\3\2\2\2\u0131\u0132\7B\2\2\u0132\u0133")
        buf.write("\7\62\2\2\u0133\u0134\5@!\2\u0134\u0135\7\63\2\2\u0135")
        buf.write("\u0138\3\2\2\2\u0136\u0138\58\35\2\u0137\u0131\3\2\2\2")
        buf.write("\u0137\u0136\3\2\2\2\u0138\67\3\2\2\2\u0139\u013a\7\60")
        buf.write("\2\2\u013a\u013b\5(\25\2\u013b\u013c\7\61\2\2\u013c\u013f")
        buf.write("\3\2\2\2\u013d\u013f\5:\36\2\u013e\u0139\3\2\2\2\u013e")
        buf.write("\u013d\3\2\2\2\u013f9\3\2\2\2\u0140\u0148\7=\2\2\u0141")
        buf.write("\u0148\7>\2\2\u0142\u0148\7?\2\2\u0143\u0148\7@\2\2\u0144")
        buf.write("\u0148\7B\2\2\u0145\u0148\5h\65\2\u0146\u0148\5&\24\2")
        buf.write("\u0147\u0140\3\2\2\2\u0147\u0141\3\2\2\2\u0147\u0142\3")
        buf.write("\2\2\2\u0147\u0143\3\2\2\2\u0147\u0144\3\2\2\2\u0147\u0145")
        buf.write("\3\2\2\2\u0147\u0146\3\2\2\2\u0148;\3\2\2\2\u0149\u014c")
        buf.write("\5> \2\u014a\u014c\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014a")
        buf.write("\3\2\2\2\u014c=\3\2\2\2\u014d\u014e\5(\25\2\u014e\u014f")
        buf.write("\7\65\2\2\u014f\u0150\5> \2\u0150\u0153\3\2\2\2\u0151")
        buf.write("\u0153\5(\25\2\u0152\u014d\3\2\2\2\u0152\u0151\3\2\2\2")
        buf.write("\u0153?\3\2\2\2\u0154\u0155\5(\25\2\u0155\u0156\7\65\2")
        buf.write("\2\u0156\u0157\5@!\2\u0157\u015a\3\2\2\2\u0158\u015a\5")
        buf.write("(\25\2\u0159\u0154\3\2\2\2\u0159\u0158\3\2\2\2\u015aA")
        buf.write("\3\2\2\2\u015b\u0166\5D#\2\u015c\u0166\5H%\2\u015d\u0166")
        buf.write("\5J&\2\u015e\u0166\5R*\2\u015f\u0166\5T+\2\u0160\u0166")
        buf.write("\5V,\2\u0161\u0166\5X-\2\u0162\u0166\5Z.\2\u0163\u0166")
        buf.write("\5\\/\2\u0164\u0166\5^\60\2\u0165\u015b\3\2\2\2\u0165")
        buf.write("\u015c\3\2\2\2\u0165\u015d\3\2\2\2\u0165\u015e\3\2\2\2")
        buf.write("\u0165\u015f\3\2\2\2\u0165\u0160\3\2\2\2\u0165\u0161\3")
        buf.write("\2\2\2\u0165\u0162\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0164")
        buf.write("\3\2\2\2\u0166C\3\2\2\2\u0167\u0168\5F$\2\u0168\u0169")
        buf.write("\7:\2\2\u0169\u016a\5(\25\2\u016a\u016b\7\66\2\2\u016b")
        buf.write("E\3\2\2\2\u016c\u0173\7B\2\2\u016d\u016e\7B\2\2\u016e")
        buf.write("\u016f\7\62\2\2\u016f\u0170\5@!\2\u0170\u0171\7\63\2\2")
        buf.write("\u0171\u0173\3\2\2\2\u0172\u016c\3\2\2\2\u0172\u016d\3")
        buf.write("\2\2\2\u0173G\3\2\2\2\u0174\u0175\7\f\2\2\u0175\u0176")
        buf.write("\5(\25\2\u0176\u0179\5B\"\2\u0177\u0178\7\b\2\2\u0178")
        buf.write("\u017a\5B\"\2\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2")
        buf.write("\u017aI\3\2\2\2\u017b\u017c\7\n\2\2\u017c\u017d\7\60\2")
        buf.write("\2\u017d\u017e\5L\'\2\u017e\u017f\7\65\2\2\u017f\u0180")
        buf.write("\5N(\2\u0180\u0181\7\65\2\2\u0181\u0182\5P)\2\u0182\u0183")
        buf.write("\7\61\2\2\u0183\u0184\5B\"\2\u0184K\3\2\2\2\u0185\u0186")
        buf.write("\7B\2\2\u0186\u0187\7:\2\2\u0187\u0188\5(\25\2\u0188M")
        buf.write("\3\2\2\2\u0189\u018a\5(\25\2\u018a\u018b\t\4\2\2\u018b")
        buf.write("\u018c\5(\25\2\u018cO\3\2\2\2\u018d\u018e\5(\25\2\u018e")
        buf.write("Q\3\2\2\2\u018f\u0190\7\20\2\2\u0190\u0191\5(\25\2\u0191")
        buf.write("\u0192\5B\"\2\u0192S\3\2\2\2\u0193\u0194\7\7\2\2\u0194")
        buf.write("\u0195\5^\60\2\u0195\u0196\7\20\2\2\u0196\u0197\5(\25")
        buf.write("\2\u0197\u0198\7\66\2\2\u0198U\3\2\2\2\u0199\u019a\7\5")
        buf.write("\2\2\u019a\u019b\7\66\2\2\u019bW\3\2\2\2\u019c\u019d\7")
        buf.write("\23\2\2\u019d\u019e\7\66\2\2\u019eY\3\2\2\2\u019f\u01a2")
        buf.write("\7\16\2\2\u01a0\u01a3\5(\25\2\u01a1\u01a3\3\2\2\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a4\u01a5\7\66\2\2\u01a5[\3\2\2\2\u01a6\u01a9\5h\65")
        buf.write("\2\u01a7\u01a9\5l\67\2\u01a8\u01a6\3\2\2\2\u01a8\u01a7")
        buf.write("\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\7\66\2\2\u01ab")
        buf.write("]\3\2\2\2\u01ac\u01ad\78\2\2\u01ad\u01ae\5`\61\2\u01ae")
        buf.write("\u01af\79\2\2\u01af\u01b2\3\2\2\2\u01b0\u01b2\7\3\2\2")
        buf.write("\u01b1\u01ac\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2_\3\2\2")
        buf.write("\2\u01b3\u01b4\5b\62\2\u01b4\u01b5\5`\61\2\u01b5\u01b8")
        buf.write("\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7\u01b3\3\2\2\2\u01b7")
        buf.write("\u01b6\3\2\2\2\u01b8a\3\2\2\2\u01b9\u01bc\5d\63\2\u01ba")
        buf.write("\u01bc\5f\64\2\u01bb\u01b9\3\2\2\2\u01bb\u01ba\3\2\2\2")
        buf.write("\u01bcc\3\2\2\2\u01bd\u01be\5B\"\2\u01be\u01bf\5d\63\2")
        buf.write("\u01bf\u01c2\3\2\2\2\u01c0\u01c2\5B\"\2\u01c1\u01bd\3")
        buf.write("\2\2\2\u01c1\u01c0\3\2\2\2\u01c2e\3\2\2\2\u01c3\u01c4")
        buf.write("\5\6\4\2\u01c4\u01c5\5f\64\2\u01c5\u01c8\3\2\2\2\u01c6")
        buf.write("\u01c8\5\6\4\2\u01c7\u01c3\3\2\2\2\u01c7\u01c6\3\2\2\2")
        buf.write("\u01c8g\3\2\2\2\u01c9\u01ca\7B\2\2\u01ca\u01cb\7\60\2")
        buf.write("\2\u01cb\u01cc\5<\37\2\u01cc\u01cd\7\61\2\2\u01cd\u01d0")
        buf.write("\3\2\2\2\u01ce\u01d0\5l\67\2\u01cf\u01c9\3\2\2\2\u01cf")
        buf.write("\u01ce\3\2\2\2\u01d0i\3\2\2\2\u01d1\u01d2\5h\65\2\u01d2")
        buf.write("\u01d3\7\65\2\2\u01d3\u01d4\5j\66\2\u01d4\u01d7\3\2\2")
        buf.write("\2\u01d5\u01d7\5h\65\2\u01d6\u01d1\3\2\2\2\u01d6\u01d5")
        buf.write("\3\2\2\2\u01d7k\3\2\2\2\u01d8\u01e2\5n8\2\u01d9\u01e2")
        buf.write("\5p9\2\u01da\u01e2\5r:\2\u01db\u01e2\5t;\2\u01dc\u01e2")
        buf.write("\5x=\2\u01dd\u01e2\5z>\2\u01de\u01e2\5|?\2\u01df\u01e2")
        buf.write("\5~@\2\u01e0\u01e2\5\u0080A\2\u01e1\u01d8\3\2\2\2\u01e1")
        buf.write("\u01d9\3\2\2\2\u01e1\u01da\3\2\2\2\u01e1\u01db\3\2\2\2")
        buf.write("\u01e1\u01dc\3\2\2\2\u01e1\u01dd\3\2\2\2\u01e1\u01de\3")
        buf.write("\2\2\2\u01e1\u01df\3\2\2\2\u01e1\u01e0\3\2\2\2\u01e2m")
        buf.write("\3\2\2\2\u01e3\u01e4\7\27\2\2\u01e4\u01e5\7\60\2\2\u01e5")
        buf.write("\u01e6\7\61\2\2\u01e6o\3\2\2\2\u01e7\u01e8\7\30\2\2\u01e8")
        buf.write("\u01e9\7\60\2\2\u01e9\u01ea\5(\25\2\u01ea\u01eb\7\61\2")
        buf.write("\2\u01ebq\3\2\2\2\u01ec\u01ed\7\31\2\2\u01ed\u01ee\7\60")
        buf.write("\2\2\u01ee\u01ef\7\61\2\2\u01efs\3\2\2\2\u01f0\u01f1\7")
        buf.write("\32\2\2\u01f1\u01f2\7\60\2\2\u01f2\u01f3\5(\25\2\u01f3")
        buf.write("\u01f4\7\61\2\2\u01f4u\3\2\2\2\u01f5\u01f6\7\33\2\2\u01f6")
        buf.write("\u01f7\7\60\2\2\u01f7\u01f8\7\61\2\2\u01f8w\3\2\2\2\u01f9")
        buf.write("\u01fa\7\34\2\2\u01fa\u01fb\7\60\2\2\u01fb\u01fc\5(\25")
        buf.write("\2\u01fc\u01fd\7\61\2\2\u01fdy\3\2\2\2\u01fe\u01ff\7\35")
        buf.write("\2\2\u01ff\u0200\7\60\2\2\u0200\u0201\7\61\2\2\u0201{")
        buf.write("\3\2\2\2\u0202\u0203\7\36\2\2\u0203\u0204\7\60\2\2\u0204")
        buf.write("\u0205\5(\25\2\u0205\u0206\7\61\2\2\u0206}\3\2\2\2\u0207")
        buf.write("\u0208\7\37\2\2\u0208\u0209\7\60\2\2\u0209\u020a\5@!\2")
        buf.write("\u020a\u020b\7\61\2\2\u020b\177\3\2\2\2\u020c\u020d\7")
        buf.write(" \2\2\u020d\u020e\7\60\2\2\u020e\u020f\7\61\2\2\u020f")
        buf.write("\u0081\3\2\2\2+\u0085\u008b\u008f\u009b\u00a1\u00aa\u00af")
        buf.write("\u00b2\u00b8\u00be\u00ca\u00d5\u00d9\u00e0\u00f0\u00fd")
        buf.write("\u0104\u010e\u0119\u0124\u012a\u012f\u0137\u013e\u0147")
        buf.write("\u014b\u0152\u0159\u0165\u0172\u0179\u01a2\u01a8\u01b1")
        buf.write("\u01b7\u01bb\u01c1\u01c7\u01cf\u01d6\u01e1")
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
    RULE_stmtsOrVardecls = 47
    RULE_stmtOrVardecl = 48
    RULE_statementList = 49
    RULE_vardeclList = 50
    RULE_functionCall = 51
    RULE_functionCallList = 52
    RULE_specialFunc = 53
    RULE_readInteger = 54
    RULE_printInteger = 55
    RULE_readFloat = 56
    RULE_writeFloat = 57
    RULE_readBoolean = 58
    RULE_printBoolean = 59
    RULE_readString = 60
    RULE_printString = 61
    RULE_superFunction = 62
    RULE_preventDefault = 63

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
                   "blockStmt", "stmtsOrVardecls", "stmtOrVardecl", "statementList", 
                   "vardeclList", "functionCall", "functionCallList", "specialFunc", 
                   "readInteger", "printInteger", "readFloat", "writeFloat", 
                   "readBoolean", "printBoolean", "readString", "printString", 
                   "superFunction", "preventDefault" ]

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
            self.state = 129 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 128
                self.decls()
                self.state = 131 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MT22Parser.IDENTIFIER):
                    break

            self.state = 133
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
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
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
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.vardeclAssign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
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
            self.state = 143
            self.vardeclAssignment()
            self.state = 144
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
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(MT22Parser.IDENTIFIER)
                self.state = 147
                self.match(MT22Parser.COMMA)
                self.state = 148
                self.vardeclAssignment()
                self.state = 149
                self.match(MT22Parser.COMMA)
                self.state = 150
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
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
            self.state = 155
            self.match(MT22Parser.IDENTIFIER)
            self.state = 156
            self.match(MT22Parser.COLON)
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.AUTO, MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.state = 157
                self.typ()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.state = 158
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 161
            self.match(MT22Parser.ASSIGN)
            self.state = 162
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
            self.state = 164
            self.identifierList()
            self.state = 165
            self.match(MT22Parser.COLON)
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.AUTO, MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.state = 166
                self.typ()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.state = 167
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 170
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
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 172
                self.match(MT22Parser.INHERIT)


            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 175
                self.match(MT22Parser.OUT)


            self.state = 178
            self.match(MT22Parser.IDENTIFIER)
            self.state = 179
            self.match(MT22Parser.COLON)
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.AUTO, MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.state = 180
                self.typ()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.state = 181
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
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(MT22Parser.IDENTIFIER)
                self.state = 185
                self.match(MT22Parser.COMMA)
                self.state = 186
                self.identifierList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
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
            self.state = 190
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
            self.state = 192
            self.match(MT22Parser.IDENTIFIER)
            self.state = 193
            self.match(MT22Parser.COLON)
            self.state = 194
            self.match(MT22Parser.FUNCTION)
            self.state = 195
            self.returnType()
            self.state = 196
            self.match(MT22Parser.LP)
            self.state = 197
            self.parameterList()
            self.state = 198
            self.match(MT22Parser.RP)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 199
                self.inheritanceSubpart()


            self.state = 202
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
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(MT22Parser.BOOLEAN)
                pass
            elif token in [MT22Parser.INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.match(MT22Parser.INTEGER)
                pass
            elif token in [MT22Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 206
                self.match(MT22Parser.FLOAT)
                pass
            elif token in [MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 207
                self.match(MT22Parser.STRING)
                pass
            elif token in [MT22Parser.VOID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 208
                self.match(MT22Parser.VOID)
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 6)
                self.state = 209
                self.match(MT22Parser.AUTO)
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 7)
                self.state = 210
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
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT, MT22Parser.INHERIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
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
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.parameter()
                self.state = 218
                self.match(MT22Parser.COMMA)
                self.state = 219
                self.parameterPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
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
            self.state = 224
            self.match(MT22Parser.INHERIT)
            self.state = 225
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
            self.state = 227
            self.match(MT22Parser.ARRAY)
            self.state = 228
            self.match(MT22Parser.LSB)
            self.state = 229
            self.dimensions()
            self.state = 230
            self.match(MT22Parser.RSB)
            self.state = 231
            self.match(MT22Parser.OF)
            self.state = 232
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
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(MT22Parser.INTEGERLIT)
                self.state = 235
                self.match(MT22Parser.COMMA)
                self.state = 236
                self.dimensions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
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
            self.state = 240
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
            self.state = 242
            self.match(MT22Parser.LB)
            self.state = 243
            self.expressionListNonnull()
            self.state = 244
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
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.expr1()
                self.state = 247
                self.match(MT22Parser.DOUBLECOLON)
                self.state = 248
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
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
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.expr2(0)
                self.state = 254
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUAL) | (1 << MT22Parser.NOTEQUAL) | (1 << MT22Parser.LESSTHAN) | (1 << MT22Parser.LESSEQUAL) | (1 << MT22Parser.GREATERTHAN) | (1 << MT22Parser.GREATEREQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 255
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
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
            self.state = 261
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 268
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 263
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 264
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AND or _la==MT22Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 265
                    self.expr3(0) 
                self.state = 270
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
            self.state = 272
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 279
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 274
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 275
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADD or _la==MT22Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 276
                    self.expr4(0) 
                self.state = 281
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
            self.state = 283
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 290
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 285
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 286
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MUL) | (1 << MT22Parser.DIV) | (1 << MT22Parser.MODUL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 287
                    self.expr5() 
                self.state = 292
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
            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(MT22Parser.NOT)
                self.state = 294
                self.expr5()
                pass
            elif token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.MINUS, MT22Parser.LP, MT22Parser.LB, MT22Parser.INTEGERLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLEANLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
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
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(MT22Parser.MINUS)
                self.state = 299
                self.expr6()
                pass
            elif token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.LP, MT22Parser.LB, MT22Parser.INTEGERLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLEANLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
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
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.match(MT22Parser.IDENTIFIER)
                self.state = 304
                self.match(MT22Parser.LSB)
                self.state = 305
                self.expressionListNonnull()
                self.state = 306
                self.match(MT22Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
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
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.match(MT22Parser.LP)
                self.state = 312
                self.expression()
                self.state = 313
                self.match(MT22Parser.RP)
                pass
            elif token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.LB, MT22Parser.INTEGERLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLEANLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
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
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(MT22Parser.INTEGERLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.match(MT22Parser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 320
                self.match(MT22Parser.BOOLEANLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 321
                self.match(MT22Parser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 322
                self.match(MT22Parser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 323
                self.functionCall()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 324
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
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.MINUS, MT22Parser.NOT, MT22Parser.LP, MT22Parser.LB, MT22Parser.INTEGERLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLEANLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
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
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.expression()
                self.state = 332
                self.match(MT22Parser.COMMA)
                self.state = 333
                self.expressionPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
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
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.expression()
                self.state = 339
                self.match(MT22Parser.COMMA)
                self.state = 340
                self.expressionListNonnull()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
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
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.assignStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.ifStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 347
                self.forStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 348
                self.whileStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 349
                self.doWhileStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 350
                self.breakStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 351
                self.continueStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 352
                self.returnStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 353
                self.callStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 354
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
            self.state = 357
            self.lhs()
            self.state = 358
            self.match(MT22Parser.ASSIGN)
            self.state = 359
            self.expression()
            self.state = 360
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
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.match(MT22Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.match(MT22Parser.IDENTIFIER)
                self.state = 364
                self.match(MT22Parser.LSB)
                self.state = 365
                self.expressionListNonnull()
                self.state = 366
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
            self.state = 370
            self.match(MT22Parser.IF)
            self.state = 371
            self.expression()
            self.state = 372
            self.statement()
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 373
                self.match(MT22Parser.ELSE)
                self.state = 374
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
            self.state = 377
            self.match(MT22Parser.FOR)
            self.state = 378
            self.match(MT22Parser.LP)
            self.state = 379
            self.initExpr()
            self.state = 380
            self.match(MT22Parser.COMMA)
            self.state = 381
            self.conditionExpr()
            self.state = 382
            self.match(MT22Parser.COMMA)
            self.state = 383
            self.updateExpr()
            self.state = 384
            self.match(MT22Parser.RP)
            self.state = 385
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
            self.state = 387
            self.match(MT22Parser.IDENTIFIER)
            self.state = 388
            self.match(MT22Parser.ASSIGN)
            self.state = 389
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
            self.state = 391
            self.expression()
            self.state = 392
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUAL) | (1 << MT22Parser.NOTEQUAL) | (1 << MT22Parser.LESSTHAN) | (1 << MT22Parser.LESSEQUAL) | (1 << MT22Parser.GREATERTHAN) | (1 << MT22Parser.GREATEREQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 393
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
            self.state = 395
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
            self.state = 397
            self.match(MT22Parser.WHILE)
            self.state = 398
            self.expression()
            self.state = 399
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
            self.state = 401
            self.match(MT22Parser.DO)
            self.state = 402
            self.blockStmt()
            self.state = 403
            self.match(MT22Parser.WHILE)
            self.state = 404
            self.expression()
            self.state = 405
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
            self.state = 407
            self.match(MT22Parser.BREAK)
            self.state = 408
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
            self.state = 410
            self.match(MT22Parser.CONTINUE)
            self.state = 411
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
            self.state = 413
            self.match(MT22Parser.RETURN)
            self.state = 416
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.MINUS, MT22Parser.NOT, MT22Parser.LP, MT22Parser.LB, MT22Parser.INTEGERLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLEANLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.state = 414
                self.expression()
                pass
            elif token in [MT22Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 418
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
        self.enterRule(localctx, 90, self.RULE_callStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 420
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 421
                self.specialFunc()
                pass


            self.state = 424
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
        self.enterRule(localctx, 92, self.RULE_blockStmt)
        try:
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.match(MT22Parser.LB)
                self.state = 427
                self.stmtsOrVardecls()
                self.state = 428
                self.match(MT22Parser.RB)
                pass
            elif token in [MT22Parser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
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
        self.enterRule(localctx, 94, self.RULE_stmtsOrVardecls)
        try:
            self.state = 437
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.T__0, MT22Parser.BREAK, MT22Parser.DO, MT22Parser.FOR, MT22Parser.IF, MT22Parser.RETURN, MT22Parser.WHILE, MT22Parser.CONTINUE, MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.LB, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.stmtOrVardecl()
                self.state = 434
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
        self.enterRule(localctx, 96, self.RULE_stmtOrVardecl)
        try:
            self.state = 441
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.statementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 440
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
        self.enterRule(localctx, 98, self.RULE_statementList)
        try:
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
                self.statement()
                self.state = 444
                self.statementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
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
        self.enterRule(localctx, 100, self.RULE_vardeclList)
        try:
            self.state = 453
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.vardecl()
                self.state = 450
                self.vardeclList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
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
        self.enterRule(localctx, 102, self.RULE_functionCall)
        try:
            self.state = 461
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.match(MT22Parser.IDENTIFIER)
                self.state = 456
                self.match(MT22Parser.LP)
                self.state = 457
                self.expressionListNullable()
                self.state = 458
                self.match(MT22Parser.RP)
                pass
            elif token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
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
        self.enterRule(localctx, 104, self.RULE_functionCallList)
        try:
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.functionCall()
                self.state = 464
                self.match(MT22Parser.COMMA)
                self.state = 465
                self.functionCallList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 467
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
        self.enterRule(localctx, 106, self.RULE_specialFunc)
        try:
            self.state = 479
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.READINTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
                self.readInteger()
                pass
            elif token in [MT22Parser.PRINTINTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 471
                self.printInteger()
                pass
            elif token in [MT22Parser.READFLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 472
                self.readFloat()
                pass
            elif token in [MT22Parser.WRITEFLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 473
                self.writeFloat()
                pass
            elif token in [MT22Parser.PRINTBOOLEAN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 474
                self.printBoolean()
                pass
            elif token in [MT22Parser.READSTRING]:
                self.enterOuterAlt(localctx, 6)
                self.state = 475
                self.readString()
                pass
            elif token in [MT22Parser.PRINTSTRING]:
                self.enterOuterAlt(localctx, 7)
                self.state = 476
                self.printString()
                pass
            elif token in [MT22Parser.SUPER]:
                self.enterOuterAlt(localctx, 8)
                self.state = 477
                self.superFunction()
                pass
            elif token in [MT22Parser.PREVENTDEFAULT]:
                self.enterOuterAlt(localctx, 9)
                self.state = 478
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
        self.enterRule(localctx, 108, self.RULE_readInteger)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.match(MT22Parser.READINTEGER)
            self.state = 482
            self.match(MT22Parser.LP)
            self.state = 483
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
        self.enterRule(localctx, 110, self.RULE_printInteger)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(MT22Parser.PRINTINTEGER)
            self.state = 486
            self.match(MT22Parser.LP)
            self.state = 487
            self.expression()
            self.state = 488
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
        self.enterRule(localctx, 112, self.RULE_readFloat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.match(MT22Parser.READFLOAT)
            self.state = 491
            self.match(MT22Parser.LP)
            self.state = 492
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
        self.enterRule(localctx, 114, self.RULE_writeFloat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(MT22Parser.WRITEFLOAT)
            self.state = 495
            self.match(MT22Parser.LP)
            self.state = 496
            self.expression()
            self.state = 497
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
        self.enterRule(localctx, 116, self.RULE_readBoolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(MT22Parser.READBOOLEAN)
            self.state = 500
            self.match(MT22Parser.LP)
            self.state = 501
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
        self.enterRule(localctx, 118, self.RULE_printBoolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(MT22Parser.PRINTBOOLEAN)
            self.state = 504
            self.match(MT22Parser.LP)
            self.state = 505
            self.expression()
            self.state = 506
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
        self.enterRule(localctx, 120, self.RULE_readString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(MT22Parser.READSTRING)
            self.state = 509
            self.match(MT22Parser.LP)
            self.state = 510
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
        self.enterRule(localctx, 122, self.RULE_printString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.match(MT22Parser.PRINTSTRING)
            self.state = 513
            self.match(MT22Parser.LP)
            self.state = 514
            self.expression()
            self.state = 515
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
        self.enterRule(localctx, 124, self.RULE_superFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(MT22Parser.SUPER)
            self.state = 518
            self.match(MT22Parser.LP)
            self.state = 519
            self.expressionListNonnull()
            self.state = 520
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
        self.enterRule(localctx, 126, self.RULE_preventDefault)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            self.match(MT22Parser.PREVENTDEFAULT)
            self.state = 523
            self.match(MT22Parser.LP)
            self.state = 524
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
         




