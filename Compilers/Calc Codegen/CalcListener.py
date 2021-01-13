# Generated from Calc.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete listener for a parse tree produced by CalcParser.
class CalcListener(ParseTreeListener):

    # Enter a parse tree produced by CalcParser#calculator.
    def enterCalculator(self, ctx:CalcParser.CalculatorContext):
        pass

    # Exit a parse tree produced by CalcParser#calculator.
    def exitCalculator(self, ctx:CalcParser.CalculatorContext):
        pass


    # Enter a parse tree produced by CalcParser#statement.
    def enterStatement(self, ctx:CalcParser.StatementContext):
        pass

    # Exit a parse tree produced by CalcParser#statement.
    def exitStatement(self, ctx:CalcParser.StatementContext):
        pass


    # Enter a parse tree produced by CalcParser#expr.
    def enterExpr(self, ctx:CalcParser.ExprContext):
        pass

    # Exit a parse tree produced by CalcParser#expr.
    def exitExpr(self, ctx:CalcParser.ExprContext):
        pass



del CalcParser