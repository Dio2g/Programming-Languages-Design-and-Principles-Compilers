# Generated from Calc.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete generic visitor for a parse tree produced by CalcParser.

class CalcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalcParser#calculator.
    def visitCalculator(self, ctx:CalcParser.CalculatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#statement.
    def visitStatement(self, ctx:CalcParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#expr.
    def visitExpr(self, ctx:CalcParser.ExprContext):
        return self.visitChildren(ctx)



del CalcParser