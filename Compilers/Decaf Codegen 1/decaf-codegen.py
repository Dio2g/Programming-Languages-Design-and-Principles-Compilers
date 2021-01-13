import antlr4 as ant
from DecafLexer import DecafLexer
from DecafParser import DecafParser
from DecafVisitor import DecafVisitor
from SymbolTable import HEAP, STACK, SymbolTable, VarSymbol, MethodSymbol, param_registers

class DecafSemanticChecker(DecafVisitor):
    def __init__(self):
        super().__init__()
        self.head = '.data\n'
        self.body = '.global main\n'
        self.st = SymbolTable()
        
    def visitProgram(self, ctx:DecafParser.ProgramContext):
        self.st.enterScope()
        self.visitChildren(ctx)
        self.st.exitScope()
        
    def visitStatement(self, ctx:DecafParser.StatementContext):
        if ctx.location():
            location_name = ctx.location().getText()
            location_symbol = self.st.lookup(location_name)
            mem_location = location_symbol.getAddr()
            self.visitChildren(ctx)
            
            self.body += 'movq %rax, ' + str(mem_location) + '(%rsp)\n'
        else:
            self.visitChildren(ctx)
        
    def visitVar_decl(self, ctx:DecafParser.Var_declContext):
        line_num = ctx.start.line
        data_type = ctx.data_type().getText()
        
        var_count = len(ctx.ID())
        for i in range(var_count):
            var_name = ctx.ID(i).getText()
            var_symbol = self.st.probe(var_name)
            
            if var_symbol != None:
                print('Error on line',line_num,'var',var_name,'is already declared on line',var_symbol.line)
            else:
                var_symbol = VarSymbol(id=var_name,
                                         type=data_type,
                                         line=line_num,
                                         size=8,
                                         mem=STACK)
                self.st.addSymbol(var_symbol)
        
        self.visitChildren(ctx)
    
    
    def visitField_decl(self, ctx:DecafParser.Field_declContext):
        line_num = ctx.start.line
        data_type = ctx.data_type().getText()
        
        field_count = len(ctx.field_name())
        for i in range(field_count):
            field_name = ctx.field_name(i).ID().getText()
            
            if ctx.field_name(i).int_literal() != None:
                array_size = int(ctx.field_name(i).int_literal().getText())
                if array_size <= 0:
                    print('Error on line',line_num,'array declared with length 0')
            else:
                array_size = 1
            
            field_symbol = self.st.probe(field_name)
            
            if field_symbol != None:
                print('Error on line',line_num,'field',field_name,'is already declared on line',field_symbol.line)
            else:
                field_symbol = VarSymbol(id=field_name,
                                         type=data_type,
                                         line=line_num,
                                         size=8 * array_size,
                                         mem=HEAP)
                self.st.addSymbol(field_symbol)
        
        self.visitChildren(ctx)
        
    def visitMethod_decl(self, ctx:DecafParser.Method_declContext):
        line_num = ctx.start.line
        method_name = ctx.ID(0).getText()
        method_type = ctx.return_type().getText()
        method_params = []
        
        for i in range(len(ctx.data_type())):
            param_type = ctx.data_type(i).getText()
            param_name = ctx.ID(i+1).getText()
            param_symbol = VarSymbol(id=param_name,type=param_type,line=line_num,size=8,mem=STACK)
            method_params.append(param_symbol)
            
        method_symbol = MethodSymbol(method_name,
                                     method_type,
                                     line_num,
                                     method_params)
        self.st.addSymbol(method_symbol)
        
        self.body += method_name + ':\n'
        if method_name == 'main':
            self.body += 'movq %rsp, %rbp\n'
            
        self.st.enterScope()
        for i in range(len(method_params)):
            self.st.addSymbol(method_params[i])
            self.body += 'movq ' + param_registers[i] + ',' + str(method_params[i].getAddr()) + '(%rsp)\n'
            
        self.visitChildren(ctx)
        self.body += 'ret\n'
        self.st.exitScope()
        
    def visitMethod_call(self, ctx:DecafParser.Method_callContext):
        if ctx.method_name():
            for i in range(len(ctx.expr())):
                self.visit(ctx.expr(i))
                self.st.stack_pointer[-1] += 8
                self.body += 'movq %rax, ' + str(-self.st.stack_pointer[-1]) + '(%rsp)\n'
            
            for i in range(len(ctx.expr())):
                self.body += 'movq ' + str(-self.st.stack_pointer[-1]) + '(%rsp), ' + param_registers[len(ctx.expr())-i-1] + '\n'
                self.st.stack_pointer[-1] -= 8
        
            stack_len = self.st.stack_pointer[-1]
            stack_len = stack_len + ((stack_len//8+1) % 2)*8
            self.body += 'subq $' + str(stack_len) + ', %rsp\n'
            
            method_name = ctx.method_name().getText()
            self.body += 'call ' + method_name + '\n'
            self.body += 'addq $' + str(stack_len) + ', %rsp\n'
            
        elif ctx.CALLOUT():
            print(self.st.stack_pointer[-1])
            function_name = ctx.STRING_LITERAL().getText()
            function_name = function_name.replace('"','')
            for i in range(len(ctx.callout_arg())):
                if ctx.callout_arg(i).STRING_LITERAL():
                    string_name = "mystring"+str(ctx.start.start)
                    self.head += string_name+": .asciz "+ctx.callout_arg(i).STRING_LITERAL().getText()+"\n"
                    self.st.stack_pointer[-1] += 8
                    self.body += 'movq $'+string_name+"," + str(-self.st.stack_pointer[-1]) + '(%rsp)\n'
                    
                elif ctx.callout_arg(i).expr():
                    self.visit(ctx.callout_arg(i).expr())
                    self.st.stack_pointer[-1] += 8
                    self.body += 'movq %rax, ' + str(-self.st.stack_pointer[-1]) + '(%rsp)\n'
            
            for i in range(len(ctx.callout_arg())):     
                    self.body += 'movq ' + str(-self.st.stack_pointer[-1]) + '(%rsp), ' + param_registers[len(ctx.callout_arg())-i-1] + '\n'
                    self.st.stack_pointer[-1] -= 8
            
            print(self.st.stack_pointer[-1])            
            stack_len = self.st.stack_pointer[-1]
            stack_len = stack_len + ((stack_len//8+1) % 2)*8
            self.body += 'subq $' + str(stack_len) + ', %rsp\n'
            
            self.body += 'call ' + function_name + '\n'
            self.body += 'addq $' + str(stack_len) + ', %rsp\n'
                    
        
    def visitExpr(self, ctx:DecafParser.ExprContext):
        if ctx.literal():
            int_literal = ctx.literal().getText()
            self.body += 'movq $' + int_literal + ', %rax\n'
        elif ctx.location():
            location_name = ctx.location().getText()
            location_symbol = self.st.lookup(location_name)
            location_addr = str(location_symbol.getAddr())
            
            if location_symbol.mem == HEAP:
                self.body += 'movq ' + location_addr + '(%rbp), %rax\n'
            elif location_symbol.mem == STACK: 
                self.body += 'movq ' + location_addr + '(%rsp), %rax\n'
        elif len(ctx.expr()) == 2:
            self.visit(ctx.expr(0))
            self.body += 'movq %rax, %r10\n'

            self.st.stack_pointer[-1] += 8
            self.body += 'movq %r10, ' + str(-self.st.stack_pointer[-1]) + '(%rsp)\n'

            self.visit(ctx.expr(1))
            self.body += 'movq %rax, %r11\n'

            self.body += 'movq ' + str(-self.st.stack_pointer[-1]) + '(%rsp), %r10\n'
            self.st.stack_pointer[-1] -= 8

            if ctx.PLUS():
                self.body += 'addq %r10, %r11\n'
            elif ctx.MINUS():
                self.body += 'subq %r11, %r10\n'
                self.body += 'movq %r10, %r11\n'
            elif ctx.MULTIPLY():
                self.body += 'imul %r10, %r11\n'
            elif ctx.DIVIDE():
                self.body += 'movq $0, %rdx\n'
                self.body += 'movq %r11, %rbx\n'
                self.body += 'movq %r10, %rax\n'
                self.body += 'idiv %rbx\n'
                self.body += 'movq %rax, %r11\n'

            self.body += 'movq %r11, %rax\n'
        else:
            self.visitChildren(ctx)

filein = open('test.dcf', 'r')
lexer = DecafLexer(ant.InputStream(filein.read()))

stream = ant.CommonTokenStream(lexer)

parser = DecafParser(stream)
tree = parser.program()

visitor = DecafSemanticChecker()
visitor.visit(tree)

code = visitor.head + visitor.body
print(code)
