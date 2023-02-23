# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("\u00b8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3<\n\3\3")
        buf.write("\4\3\4\5\4@\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6J\n")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\5\tW\n")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\5\n^\n\n\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\5\rk\n\r\3\16\3\16\3\16\3\16")
        buf.write("\5\16q\n\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\21\3\21\5\21\u0080\n\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u0087\n\22\3\23\3\23\3\23\3\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\5\24\u0092\n\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\5\25\u0099\n\25\3\26\3\26\3\26\3\26\3\26\3\26\7")
        buf.write("\26\u00a1\n\26\f\26\16\26\u00a4\13\26\3\27\3\27\3\27\3")
        buf.write("\27\3\27\5\27\u00ab\n\27\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\2\3*\33\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\2\4\3\2\16\17")
        buf.write("\3\2\3\4\2\u00b0\2\64\3\2\2\2\4;\3\2\2\2\6?\3\2\2\2\b")
        buf.write("A\3\2\2\2\nI\3\2\2\2\fK\3\2\2\2\16P\3\2\2\2\20V\3\2\2")
        buf.write("\2\22]\3\2\2\2\24_\3\2\2\2\26b\3\2\2\2\30j\3\2\2\2\32")
        buf.write("p\3\2\2\2\34r\3\2\2\2\36w\3\2\2\2 \177\3\2\2\2\"\u0086")
        buf.write("\3\2\2\2$\u0088\3\2\2\2&\u0091\3\2\2\2(\u0098\3\2\2\2")
        buf.write("*\u009a\3\2\2\2,\u00aa\3\2\2\2.\u00ac\3\2\2\2\60\u00b0")
        buf.write("\3\2\2\2\62\u00b5\3\2\2\2\64\65\5\4\3\2\65\66\7\2\2\3")
        buf.write("\66\3\3\2\2\2\678\5\6\4\289\5\4\3\29<\3\2\2\2:<\5\6\4")
        buf.write("\2;\67\3\2\2\2;:\3\2\2\2<\5\3\2\2\2=@\5\b\5\2>@\5\f\7")
        buf.write("\2?=\3\2\2\2?>\3\2\2\2@\7\3\2\2\2AB\5\62\32\2BC\5\n\6")
        buf.write("\2CD\7\7\2\2D\t\3\2\2\2EF\7\24\2\2FG\7\6\2\2GJ\5\n\6\2")
        buf.write("HJ\7\24\2\2IE\3\2\2\2IH\3\2\2\2J\13\3\2\2\2KL\5\62\32")
        buf.write("\2LM\7\24\2\2MN\5\16\b\2NO\5\26\f\2O\r\3\2\2\2PQ\7\b\2")
        buf.write("\2QR\5\20\t\2RS\7\t\2\2S\17\3\2\2\2TW\5\22\n\2UW\3\2\2")
        buf.write("\2VT\3\2\2\2VU\3\2\2\2W\21\3\2\2\2XY\5\24\13\2YZ\7\7\2")
        buf.write("\2Z[\5\22\n\2[^\3\2\2\2\\^\5\24\13\2]X\3\2\2\2]\\\3\2")
        buf.write("\2\2^\23\3\2\2\2_`\5\62\32\2`a\5\n\6\2a\25\3\2\2\2bc\7")
        buf.write("\n\2\2cd\5\30\r\2de\7\13\2\2e\27\3\2\2\2fg\5\32\16\2g")
        buf.write("h\5\30\r\2hk\3\2\2\2ik\5\32\16\2jf\3\2\2\2ji\3\2\2\2k")
        buf.write("\31\3\2\2\2lq\5\b\5\2mq\5\34\17\2nq\5\36\20\2oq\5$\23")
        buf.write("\2pl\3\2\2\2pm\3\2\2\2pn\3\2\2\2po\3\2\2\2q\33\3\2\2\2")
        buf.write("rs\7\24\2\2st\7\5\2\2tu\5&\24\2uv\7\7\2\2v\35\3\2\2\2")
        buf.write("wx\7\24\2\2xy\7\b\2\2yz\5 \21\2z{\7\t\2\2{|\7\7\2\2|\37")
        buf.write("\3\2\2\2}\u0080\5\"\22\2~\u0080\3\2\2\2\177}\3\2\2\2\177")
        buf.write("~\3\2\2\2\u0080!\3\2\2\2\u0081\u0082\5&\24\2\u0082\u0083")
        buf.write("\7\6\2\2\u0083\u0084\5\"\22\2\u0084\u0087\3\2\2\2\u0085")
        buf.write("\u0087\5&\24\2\u0086\u0081\3\2\2\2\u0086\u0085\3\2\2\2")
        buf.write("\u0087#\3\2\2\2\u0088\u0089\7\23\2\2\u0089\u008a\5&\24")
        buf.write("\2\u008a\u008b\7\7\2\2\u008b%\3\2\2\2\u008c\u008d\5(\25")
        buf.write("\2\u008d\u008e\7\f\2\2\u008e\u008f\5*\26\2\u008f\u0092")
        buf.write("\3\2\2\2\u0090\u0092\5(\25\2\u0091\u008c\3\2\2\2\u0091")
        buf.write("\u0090\3\2\2\2\u0092\'\3\2\2\2\u0093\u0094\5*\26\2\u0094")
        buf.write("\u0095\7\r\2\2\u0095\u0096\5*\26\2\u0096\u0099\3\2\2\2")
        buf.write("\u0097\u0099\5*\26\2\u0098\u0093\3\2\2\2\u0098\u0097\3")
        buf.write("\2\2\2\u0099)\3\2\2\2\u009a\u009b\b\26\1\2\u009b\u009c")
        buf.write("\5,\27\2\u009c\u00a2\3\2\2\2\u009d\u009e\f\4\2\2\u009e")
        buf.write("\u009f\t\2\2\2\u009f\u00a1\5,\27\2\u00a0\u009d\3\2\2\2")
        buf.write("\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3")
        buf.write("\2\2\2\u00a3+\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00ab")
        buf.write("\5.\30\2\u00a6\u00ab\5\60\31\2\u00a7\u00ab\7\24\2\2\u00a8")
        buf.write("\u00ab\7\20\2\2\u00a9\u00ab\7\22\2\2\u00aa\u00a5\3\2\2")
        buf.write("\2\u00aa\u00a6\3\2\2\2\u00aa\u00a7\3\2\2\2\u00aa\u00a8")
        buf.write("\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab-\3\2\2\2\u00ac\u00ad")
        buf.write("\7\b\2\2\u00ad\u00ae\5&\24\2\u00ae\u00af\7\t\2\2\u00af")
        buf.write("/\3\2\2\2\u00b0\u00b1\7\24\2\2\u00b1\u00b2\7\b\2\2\u00b2")
        buf.write("\u00b3\5 \21\2\u00b3\u00b4\7\t\2\2\u00b4\61\3\2\2\2\u00b5")
        buf.write("\u00b6\t\3\2\2\u00b6\63\3\2\2\2\17;?IV]jp\177\u0086\u0091")
        buf.write("\u0098\u00a2\u00aa")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'='", "','", "';'", 
                     "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'return'" ]

    symbolicNames = [ "<INVALID>", "INTTYPE", "FLOATTYPE", "EQUAL", "COMMA", 
                      "SEMI", "LB", "RB", "LBRACE", "RBRACE", "ADD", "MINUS", 
                      "MUL", "DIV", "INTLIT", "FLOATLIST", "FLOATLIT", "RETURN", 
                      "ID", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_idlist = 4
    RULE_funcdecl = 5
    RULE_paramdecl = 6
    RULE_paramlist = 7
    RULE_paramprime = 8
    RULE_param = 9
    RULE_body = 10
    RULE_stmtlist = 11
    RULE_stmt = 12
    RULE_assignstmt = 13
    RULE_callstmt = 14
    RULE_exprlist = 15
    RULE_exprime = 16
    RULE_returnstmt = 17
    RULE_expr = 18
    RULE_expr1 = 19
    RULE_expr2 = 20
    RULE_expr3 = 21
    RULE_subexpr = 22
    RULE_callexpr = 23
    RULE_typ = 24

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "idlist", "funcdecl", 
                   "paramdecl", "paramlist", "paramprime", "param", "body", 
                   "stmtlist", "stmt", "assignstmt", "callstmt", "exprlist", 
                   "exprime", "returnstmt", "expr", "expr1", "expr2", "expr3", 
                   "subexpr", "callexpr", "typ" ]

    EOF = Token.EOF
    INTTYPE=1
    FLOATTYPE=2
    EQUAL=3
    COMMA=4
    SEMI=5
    LB=6
    RB=7
    LBRACE=8
    RBRACE=9
    ADD=10
    MINUS=11
    MUL=12
    DIV=13
    INTLIT=14
    FLOATLIST=15
    FLOATLIT=16
    RETURN=17
    ID=18
    WS=19
    ERROR_CHAR=20

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

        def decllist(self):
            return self.getTypedRuleContext(BKOOLParser.DecllistContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.decllist()
            self.state = 51
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(BKOOLParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(BKOOLParser.DecllistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = BKOOLParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.decl()
                self.state = 54
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(BKOOLParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = BKOOLParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
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

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.typ()
            self.state = 64
            self.idlist()
            self.state = 65
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_idlist)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(BKOOLParser.ID)
                self.state = 68
                self.match(BKOOLParser.COMMA)
                self.state = 69
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(BKOOLParser.ID)
                pass


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

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def paramdecl(self):
            return self.getTypedRuleContext(BKOOLParser.ParamdeclContext,0)


        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = BKOOLParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.typ()
            self.state = 74
            self.match(BKOOLParser.ID)
            self.state = 75
            self.paramdecl()
            self.state = 76
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_paramdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamdecl" ):
                return visitor.visitParamdecl(self)
            else:
                return visitor.visitChildren(self)




    def paramdecl(self):

        localctx = BKOOLParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paramdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(BKOOLParser.LB)
            self.state = 79
            self.paramlist()
            self.state = 80
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramprime(self):
            return self.getTypedRuleContext(BKOOLParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = BKOOLParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paramlist)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTTYPE, BKOOLParser.FLOATTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.paramprime()
                pass
            elif token in [BKOOLParser.RB]:
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


    class ParamprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def paramprime(self):
            return self.getTypedRuleContext(BKOOLParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamprime" ):
                return visitor.visitParamprime(self)
            else:
                return visitor.visitChildren(self)




    def paramprime(self):

        localctx = BKOOLParser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramprime)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.param()
                self.state = 87
                self.match(BKOOLParser.SEMI)
                self.state = 88
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.typ()
            self.state = 94
            self.idlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(BKOOLParser.LBRACE, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(BKOOLParser.StmtlistContext,0)


        def RBRACE(self):
            return self.getToken(BKOOLParser.RBRACE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(BKOOLParser.LBRACE)
            self.state = 97
            self.stmtlist()
            self.state = 98
            self.match(BKOOLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(BKOOLParser.StmtlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = BKOOLParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_stmtlist)
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.stmt()
                self.state = 101
                self.stmtlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(BKOOLParser.AssignstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(BKOOLParser.CallstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnstmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stmt)
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.assignstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 108
                self.callstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 109
                self.returnstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = BKOOLParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(BKOOLParser.ID)
            self.state = 113
            self.match(BKOOLParser.EQUAL)
            self.state = 114
            self.expr()
            self.state = 115
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = BKOOLParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(BKOOLParser.ID)
            self.state = 118
            self.match(BKOOLParser.LB)
            self.state = 119
            self.exprlist()
            self.state = 120
            self.match(BKOOLParser.RB)
            self.state = 121
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprime(self):
            return self.getTypedRuleContext(BKOOLParser.ExprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = BKOOLParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exprlist)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.exprime()
                pass
            elif token in [BKOOLParser.RB]:
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


    class ExprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def exprime(self):
            return self.getTypedRuleContext(BKOOLParser.ExprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprime" ):
                return visitor.visitExprime(self)
            else:
                return visitor.visitChildren(self)




    def exprime(self):

        localctx = BKOOLParser.ExprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exprime)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.expr()
                self.state = 128
                self.match(BKOOLParser.COMMA)
                self.state = 129
                self.exprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = BKOOLParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(BKOOLParser.RETURN)
            self.state = 135
            self.expr()
            self.state = 136
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(BKOOLParser.Expr1Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.expr1()
                self.state = 139
                self.match(BKOOLParser.ADD)
                self.state = 140
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
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
                return self.getTypedRuleContexts(BKOOLParser.Expr2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr2Context,i)


        def MINUS(self):
            return self.getToken(BKOOLParser.MINUS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = BKOOLParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr1)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.expr2(0)
                self.state = 146
                self.match(BKOOLParser.MINUS)
                self.state = 147
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
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
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKOOLParser.DIV, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.expr3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 155
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 156
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.MUL or _la==BKOOLParser.DIV):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 157
                    self.expr3() 
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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

        def subexpr(self):
            return self.getTypedRuleContext(BKOOLParser.SubexprContext,0)


        def callexpr(self):
            return self.getTypedRuleContext(BKOOLParser.CallexprContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)




    def expr3(self):

        localctx = BKOOLParser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr3)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.subexpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.callexpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 166
                self.match(BKOOLParser.INTLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 167
                self.match(BKOOLParser.FLOATLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_subexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpr" ):
                return visitor.visitSubexpr(self)
            else:
                return visitor.visitChildren(self)




    def subexpr(self):

        localctx = BKOOLParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(BKOOLParser.LB)
            self.state = 171
            self.expr()
            self.state = 172
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_callexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallexpr" ):
                return visitor.visitCallexpr(self)
            else:
                return visitor.visitChildren(self)




    def callexpr(self):

        localctx = BKOOLParser.CallexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_callexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(BKOOLParser.ID)
            self.state = 175
            self.match(BKOOLParser.LB)
            self.state = 176
            self.exprlist()
            self.state = 177
            self.match(BKOOLParser.RB)
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

        def INTTYPE(self):
            return self.getToken(BKOOLParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(BKOOLParser.FLOATTYPE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = BKOOLParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.INTTYPE or _la==BKOOLParser.FLOATTYPE):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[20] = self.expr2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




