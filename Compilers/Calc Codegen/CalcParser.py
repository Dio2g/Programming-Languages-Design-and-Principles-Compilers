# Generated from Calc.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write(",\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\7\2\13\n\2\f\2\16\2")
        buf.write("\16\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4\37\n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4")
        buf.write("\'\n\4\f\4\16\4*\13\4\3\4\2\3\6\5\2\4\6\2\4\3\2\5\6\3")
        buf.write("\2\3\4\2-\2\b\3\2\2\2\4\22\3\2\2\2\6\36\3\2\2\2\b\f\7")
        buf.write("\7\2\2\t\13\5\4\3\2\n\t\3\2\2\2\13\16\3\2\2\2\f\n\3\2")
        buf.write("\2\2\f\r\3\2\2\2\r\17\3\2\2\2\16\f\3\2\2\2\17\20\5\6\4")
        buf.write("\2\20\21\7\b\2\2\21\3\3\2\2\2\22\23\7\13\2\2\23\24\7\t")
        buf.write("\2\2\24\25\5\6\4\2\25\26\7\n\2\2\26\5\3\2\2\2\27\30\b")
        buf.write("\4\1\2\30\37\7\13\2\2\31\37\7\f\2\2\32\33\7\7\2\2\33\34")
        buf.write("\5\6\4\2\34\35\7\b\2\2\35\37\3\2\2\2\36\27\3\2\2\2\36")
        buf.write("\31\3\2\2\2\36\32\3\2\2\2\37(\3\2\2\2 !\f\5\2\2!\"\t\2")
        buf.write("\2\2\"\'\5\6\4\6#$\f\4\2\2$%\t\3\2\2%\'\5\6\4\5& \3\2")
        buf.write("\2\2&#\3\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)\7\3\2\2")
        buf.write("\2*(\3\2\2\2\6\f\36&(")
        return buf.getvalue()


class CalcParser ( Parser ):

    grammarFileName = "Calc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'", 
                     "'='", "';'" ]

    symbolicNames = [ "<INVALID>", "ADD", "SUB", "MUL", "DIV", "LBRACE", 
                      "RBRACE", "EQ", "SEMI", "VAR", "NUMBER", "WS" ]

    RULE_calculator = 0
    RULE_statement = 1
    RULE_expr = 2

    ruleNames =  [ "calculator", "statement", "expr" ]

    EOF = Token.EOF
    ADD=1
    SUB=2
    MUL=3
    DIV=4
    LBRACE=5
    RBRACE=6
    EQ=7
    SEMI=8
    VAR=9
    NUMBER=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CalculatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(CalcParser.LBRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def RBRACE(self):
            return self.getToken(CalcParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.StatementContext)
            else:
                return self.getTypedRuleContext(CalcParser.StatementContext,i)


        def getRuleIndex(self):
            return CalcParser.RULE_calculator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCalculator" ):
                listener.enterCalculator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCalculator" ):
                listener.exitCalculator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalculator" ):
                return visitor.visitCalculator(self)
            else:
                return visitor.visitChildren(self)




    def calculator(self):

        localctx = CalcParser.CalculatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_calculator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(CalcParser.LBRACE)
            self.state = 10
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 7
                    self.statement() 
                self.state = 12
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 13
            self.expr(0)
            self.state = 14
            self.match(CalcParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CalcParser.VAR, 0)

        def EQ(self):
            return self.getToken(CalcParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(CalcParser.SEMI, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CalcParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(CalcParser.VAR)
            self.state = 17
            self.match(CalcParser.EQ)
            self.state = 18
            self.expr(0)
            self.state = 19
            self.match(CalcParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CalcParser.VAR, 0)

        def NUMBER(self):
            return self.getToken(CalcParser.NUMBER, 0)

        def LBRACE(self):
            return self.getToken(CalcParser.LBRACE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def RBRACE(self):
            return self.getToken(CalcParser.RBRACE, 0)

        def MUL(self):
            return self.getToken(CalcParser.MUL, 0)

        def DIV(self):
            return self.getToken(CalcParser.DIV, 0)

        def ADD(self):
            return self.getToken(CalcParser.ADD, 0)

        def SUB(self):
            return self.getToken(CalcParser.SUB, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalcParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalcParser.VAR]:
                self.state = 22
                self.match(CalcParser.VAR)
                pass
            elif token in [CalcParser.NUMBER]:
                self.state = 23
                self.match(CalcParser.NUMBER)
                pass
            elif token in [CalcParser.LBRACE]:
                self.state = 24
                self.match(CalcParser.LBRACE)
                self.state = 25
                self.expr(0)
                self.state = 26
                self.match(CalcParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 36
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = CalcParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 31
                        _la = self._input.LA(1)
                        if not(_la==CalcParser.MUL or _la==CalcParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 32
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = CalcParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 34
                        _la = self._input.LA(1)
                        if not(_la==CalcParser.ADD or _la==CalcParser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 35
                        self.expr(3)
                        pass

             
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




