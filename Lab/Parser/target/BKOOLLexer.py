# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("\u008e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\r\3\r\3\16\3\16\3\17\6\17S\n\17\r\17\16\17T\3")
        buf.write("\20\3\20\3\20\3\20\7\20[\n\20\f\20\16\20^\13\20\3\21\6")
        buf.write("\21a\n\21\r\21\16\21b\3\22\3\22\6\22g\n\22\r\22\16\22")
        buf.write("h\3\23\3\23\5\23m\n\23\3\23\6\23p\n\23\r\23\16\23q\3\24")
        buf.write("\3\24\3\24\5\24w\n\24\3\24\5\24z\n\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\26\6\26\u0084\n\26\r\26\16\26\u0085")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\2\2\31\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\2#\2%\2\'\22)\23+\24-\25/\26\3\2\5\3\2\62;")
        buf.write("\4\2C\\c|\5\2\13\f\17\17\"\"\2\u0093\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2")
        buf.write("\2\2/\3\2\2\2\3\61\3\2\2\2\5\65\3\2\2\2\7;\3\2\2\2\t=")
        buf.write("\3\2\2\2\13?\3\2\2\2\rA\3\2\2\2\17C\3\2\2\2\21E\3\2\2")
        buf.write("\2\23G\3\2\2\2\25I\3\2\2\2\27K\3\2\2\2\31M\3\2\2\2\33")
        buf.write("O\3\2\2\2\35R\3\2\2\2\37V\3\2\2\2!`\3\2\2\2#d\3\2\2\2")
        buf.write("%j\3\2\2\2\'s\3\2\2\2){\3\2\2\2+\u0083\3\2\2\2-\u0087")
        buf.write("\3\2\2\2/\u008b\3\2\2\2\61\62\7k\2\2\62\63\7p\2\2\63\64")
        buf.write("\7v\2\2\64\4\3\2\2\2\65\66\7h\2\2\66\67\7n\2\2\678\7q")
        buf.write("\2\289\7c\2\29:\7v\2\2:\6\3\2\2\2;<\7?\2\2<\b\3\2\2\2")
        buf.write("=>\7.\2\2>\n\3\2\2\2?@\7=\2\2@\f\3\2\2\2AB\7*\2\2B\16")
        buf.write("\3\2\2\2CD\7+\2\2D\20\3\2\2\2EF\7}\2\2F\22\3\2\2\2GH\7")
        buf.write("\177\2\2H\24\3\2\2\2IJ\7-\2\2J\26\3\2\2\2KL\7/\2\2L\30")
        buf.write("\3\2\2\2MN\7,\2\2N\32\3\2\2\2OP\7\61\2\2P\34\3\2\2\2Q")
        buf.write("S\t\2\2\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2\2\2U\36")
        buf.write("\3\2\2\2V\\\5\'\24\2WX\5\t\5\2XY\5\'\24\2Y[\3\2\2\2ZW")
        buf.write("\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2] \3\2\2\2^\\")
        buf.write("\3\2\2\2_a\t\2\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2")
        buf.write("\2\2c\"\3\2\2\2df\7\60\2\2eg\t\2\2\2fe\3\2\2\2gh\3\2\2")
        buf.write("\2hf\3\2\2\2hi\3\2\2\2i$\3\2\2\2jl\7g\2\2km\7/\2\2lk\3")
        buf.write("\2\2\2lm\3\2\2\2mo\3\2\2\2np\t\2\2\2on\3\2\2\2pq\3\2\2")
        buf.write("\2qo\3\2\2\2qr\3\2\2\2r&\3\2\2\2sy\5!\21\2tv\5#\22\2u")
        buf.write("w\5%\23\2vu\3\2\2\2vw\3\2\2\2wz\3\2\2\2xz\5%\23\2yt\3")
        buf.write("\2\2\2yx\3\2\2\2z(\3\2\2\2{|\7t\2\2|}\7g\2\2}~\7v\2\2")
        buf.write("~\177\7w\2\2\177\u0080\7t\2\2\u0080\u0081\7p\2\2\u0081")
        buf.write("*\3\2\2\2\u0082\u0084\t\3\2\2\u0083\u0082\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2")
        buf.write("\u0086,\3\2\2\2\u0087\u0088\t\4\2\2\u0088\u0089\3\2\2")
        buf.write("\2\u0089\u008a\b\27\2\2\u008a.\3\2\2\2\u008b\u008c\13")
        buf.write("\2\2\2\u008c\u008d\b\30\3\2\u008d\60\3\2\2\2\f\2T\\bh")
        buf.write("lqvy\u0085\4\b\2\2\3\30\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTTYPE = 1
    FLOATTYPE = 2
    EQUAL = 3
    COMMA = 4
    SEMI = 5
    LB = 6
    RB = 7
    LBRACE = 8
    RBRACE = 9
    ADD = 10
    MINUS = 11
    MUL = 12
    DIV = 13
    INTLIT = 14
    FLOATLIST = 15
    FLOATLIT = 16
    RETURN = 17
    ID = 18
    WS = 19
    ERROR_CHAR = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'='", "','", "';'", "'('", "')'", "'{'", 
            "'}'", "'+'", "'-'", "'*'", "'/'", "'return'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "FLOATTYPE", "EQUAL", "COMMA", "SEMI", "LB", "RB", 
            "LBRACE", "RBRACE", "ADD", "MINUS", "MUL", "DIV", "INTLIT", 
            "FLOATLIST", "FLOATLIT", "RETURN", "ID", "WS", "ERROR_CHAR" ]

    ruleNames = [ "INTTYPE", "FLOATTYPE", "EQUAL", "COMMA", "SEMI", "LB", 
                  "RB", "LBRACE", "RBRACE", "ADD", "MINUS", "MUL", "DIV", 
                  "INTLIT", "FLOATLIST", "INTPART", "FRACPART", "EXPPART", 
                  "FLOATLIT", "RETURN", "ID", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[22] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


