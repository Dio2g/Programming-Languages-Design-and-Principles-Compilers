import antlr4 as ant
from DecafLexer import DecafLexer
from DecafParser import DecafParser
from DecafVisitor import DecafVisitor
from SymbolTable import HEAP, STACK, SymbolTable, VarSymbol, MethodSymbol

class DecafSemanticChecker(DecafVisitor):
    
    def __init__(self):
        super().__init__()
        self.st = SymbolTable()
        
    def visitProgram(self, ctx:DecafParser.ProgramContext):
        self.st.enterScope()
        self.visitChildren(ctx)
        self.st.exitScope()
    
    def visitMethod_decl(self, ctx:DecafParser.Method_declContext):
        line_num = ctx.start.line
        method_name = ctx.ID(0).getText()
        return_type = ctx.return_type().getText()
    
        method_params = []
        for i in range(len(ctx.data_type())):
            param_type = ctx.data_type(i).getText()
            param_name = ctx.ID(i+1).getText()
            param_symbol = VarSymbol(id=param_name, type=param_type, line=line_num, size=8, mem=STACK)
            method_params.append(param_symbol)

        method_symbol = self.st.probe(method_name)

        method_symbol = MethodSymbol(id=method_name,
                                      type=return_type,
                                      line=line_num,
                                      params=method_params)
        self.st.addSymbol(method_symbol)
            
        self.visitChildren(ctx)

    def visitMethod_call(self, ctx:DecafParser.Method_callContext):
        line_num = ctx.start.line
        method_name = ctx.method_name().getText()
        method_symbol = self.st.probe(method_name)

        if method_symbol != None:
            
            if len(method_symbol.params) != len(ctx.expr()):
                print("Trying to call method on line " + str(line_num) + " with wrong number of parameters. Method expects " + str(len(method_symbol.params)) + " parameters")
            else:
                for i in range(len(ctx.expr())):
                    if method_symbol.params[i].type == "int" and ctx.expr(i).literal().bool_literal() != None:
                        print("Trying to call method on line " + str(line_num) + " with incorrect parameter type. Method expects type int for parameter " + str(i))    
                    elif method_symbol.params[i].type == "boolean" and ctx.expr(i).literal().int_literal() != None:
                        print("Trying to call method on line " + str(line_num) + " with incorrect parameter type. Method expects type bool for parameter " + str(i))  
                        
        self.visitChildren(ctx)

filein = open('test.dcf', 'r')
lexer = DecafLexer(ant.InputStream(filein.read()))

stream = ant.CommonTokenStream(lexer)

parser = DecafParser(stream)
tree = parser.program()

visitor = DecafSemanticChecker()
visitor.visit(tree)



