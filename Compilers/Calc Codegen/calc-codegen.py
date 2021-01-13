import antlr4 as ant
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from CalcVisitor import CalcVisitor
from SymbolTable import HEAP, STACK, SymbolTable, VarSymbol, MethodSymbol

class CalcSemanticChecker(CalcVisitor):
    def __init__(self):
        super().__init__()
        self.head = '.data\n'
        self.body = '.global main\n'
        self.st = SymbolTable()

    def visitCalculator(self, ctx:CalcParser.CalculatorContext):
        self.st.enterScope()
        self.body += 'main:\n'
        self.visitChildren(ctx)
        self.body += 'ret\n'
        self.st.exitScope()


    def visitStatement(self, ctx:CalcParser.StatementContext):
        var_name = ctx.VAR().getText()
        var_symbol = VarSymbol(id=var_name,type='int',line=ctx.start.line,size=8,mem=STACK)
        self.st.addSymbol(var_symbol)
        mem_location = var_symbol.getAddr()
        self.visit(ctx.expr())
        self.body += 'movq %rax, ' + str(mem_location) + '(%rsp)\n'
        self.visitChildren(ctx)

    def visitExpr(self, ctx:CalcParser.ExprContext):
        if ctx.NUMBER() != None:
            number = ctx.NUMBER().getText()
            self.body += 'movq $' + number + ', %rax\n'
        elif ctx.VAR() != None:
            var_name = ctx.VAR().getText()
            var_symbol = self.st.lookup(var_name)
            
            mem_location = var_symbol.getAddr()
            self.body += 'movq ' + str(mem_location) + '(%rsp), %rax\n'
            
        elif len(ctx.expr()) == 2:
            self.visit(ctx.expr(0))
            self.body += 'movq %rax, %r10\n'
            
            self.st.stack_pointer[-1] += 8
            self.body += 'movq %r10, ' + str(-self.st.stack_pointer[-1]) + '(%rsp)\n'
            
            self.visit(ctx.expr(1))
            
            self.body += 'movq %rax, %r11\n'
            
            self.body += 'movq ' + str(-self.st.stack_pointer[-1]) + '(%rsp), %r10\n'
            self.st.stack_pointer[-1] += 8
            
            if ctx.ADD():
                self.body += 'addq %r10, %r11\n'
            elif ctx.SUB():
                self.body += 'subq %r11, %r10\n'
                self.body += 'movq %r10, %r11\n'
            elif ctx.MUL():
                self.body += 'imul %r10, %r11\n'
            elif ctx.DIV():
                self.body += 'movq $0, %rdx\n'
                self.body += 'movq %r11, %rbx\n'
                self.body += 'movq %r10, %rax\n'
                self.body += 'idiv %rbx\n'
                self.body += 'movq %rax, %r11\n'
                
                
            self.body += 'movq %r11, %rax\n'
        else:    
            self.visitChildren(ctx)

filein = open('test.calc', 'r')
lexer = CalcLexer(ant.InputStream(filein.read()))

stream = ant.CommonTokenStream(lexer)

parser = CalcParser(stream)
tree = parser.calculator()

visitor = CalcSemanticChecker()
visitor.visit(tree)

code = visitor.head + visitor.body
print(code)
