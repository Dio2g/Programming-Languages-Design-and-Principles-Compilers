# Generated from Calc.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("B\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\13\6\13\61\n\13\r\13\16\13")
        buf.write("\62\3\f\3\f\3\r\6\r8\n\r\r\r\16\r9\3\16\6\16=\n\16\r\16")
        buf.write("\16\16>\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\2\25\13\27\2\31\f\33\r\3\2\5\5\2C\\aac|\3\2\62")
        buf.write(";\5\2\13\f\16\17\"\"\2B\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\25\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\3\35\3\2\2\2\5\37\3\2\2\2\7!\3\2\2\2\t#\3\2\2\2\13%\3")
        buf.write("\2\2\2\r\'\3\2\2\2\17)\3\2\2\2\21+\3\2\2\2\23-\3\2\2\2")
        buf.write("\25\60\3\2\2\2\27\64\3\2\2\2\31\67\3\2\2\2\33<\3\2\2\2")
        buf.write("\35\36\7-\2\2\36\4\3\2\2\2\37 \7/\2\2 \6\3\2\2\2!\"\7")
        buf.write(",\2\2\"\b\3\2\2\2#$\7\61\2\2$\n\3\2\2\2%&\7*\2\2&\f\3")
        buf.write("\2\2\2\'(\7+\2\2(\16\3\2\2\2)*\7?\2\2*\20\3\2\2\2+,\7")
        buf.write("=\2\2,\22\3\2\2\2-.\t\2\2\2.\24\3\2\2\2/\61\5\23\n\2\60")
        buf.write("/\3\2\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63")
        buf.write("\26\3\2\2\2\64\65\t\3\2\2\65\30\3\2\2\2\668\5\27\f\2\67")
        buf.write("\66\3\2\2\289\3\2\2\29\67\3\2\2\29:\3\2\2\2:\32\3\2\2")
        buf.write("\2;=\t\4\2\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?")
        buf.write("@\3\2\2\2@A\b\16\2\2A\34\3\2\2\2\6\2\629>\3\b\2\2")
        return buf.getvalue()


class CalcLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    LBRACE = 5
    RBRACE = 6
    EQ = 7
    SEMI = 8
    VAR = 9
    NUMBER = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'='", "';'" ]

    symbolicNames = [ "<INVALID>",
            "ADD", "SUB", "MUL", "DIV", "LBRACE", "RBRACE", "EQ", "SEMI", 
            "VAR", "NUMBER", "WS" ]

    ruleNames = [ "ADD", "SUB", "MUL", "DIV", "LBRACE", "RBRACE", "EQ", 
                  "SEMI", "ALPHA", "VAR", "DIGIT", "NUMBER", "WS" ]

    grammarFileName = "Calc.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


