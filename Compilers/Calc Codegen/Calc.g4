grammar Calc;

/*LEXER RULES*/

ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';
LBRACE : '(';
RBRACE : ')';
EQ : '=';
SEMI : ';';

fragment ALPHA : [a-zA-Z_];
VAR : ALPHA+;

fragment DIGIT : [0-9];
NUMBER : DIGIT+;

WS : [ \n\t\f\r]+ -> skip;

/*parser rules*/

calculator : LBRACE statement* expr RBRACE;

statement : VAR EQ expr SEMI;

expr :  VAR
	| NUMBER
	| expr (MUL | DIV) expr
	| expr (ADD | SUB) expr
	| LBRACE expr RBRACE;

