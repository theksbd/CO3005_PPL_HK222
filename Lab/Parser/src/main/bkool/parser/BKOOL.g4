grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

/* ------------------------ Ex 1 ------------------------ */
// A program in BKOOL consists of many declarations, which are variable and function declarations. 

// program: decllist EOF;

// decllist: decl decllist | decl;

// decl: vardecl | funcdecl;

// vardecl: 'vardecl';

// funcdecl: 'funcdecl';

// WS: [ \t\r\n] -> skip;

// ERROR_CHAR: . {raise ErrorToken(self.text)};

/* ------------------------ Ex 2 ------------------------ */
// A program in BKOOL consists of many declarations, which are variable and function declarations. 
// A variable declaration starts with a type, which is int or float, then a comma-separated list of identifiers and ends with a semicolon. 
// A function declaration also start with a type and then an identifier, which is the function name, and then parameter declaration and ends with a body. The parameter declaration starts with a left round bracket ’(’ and a null-able semicolon-separated list of parameters and ends with a right round bracket ’)’. Each parameter always starts with a type and then a comma-separated list of identifier. 

// program: decllist EOF;

// //And some other rules for variable declaration, function declaration and other rules
// decllist: decl decllist | decl;

// decl: vardecl | funcdecl;

// vardecl: typ idlist SEMI;
// idlist: ID COMMA idlist | ID;

// funcdecl: typ ID paramdecl body;
// paramdecl: LB paramlist RB;
// paramlist: paramprime | ;
// paramprime: param SEMI paramprime | param;
// param: typ idlist;
// body: 'body';

// typ: INTTYPE | FLOATTYPE;

// INTTYPE: 'int';

// FLOATTYPE: 'float';

// ID: [a-zA-Z]+;// includes a sequence of alphabetic characters.

// COMMA: ',';

// SEMI: ';';

// LB: '(';

// RB: ')';

// WS: [ \t\r\n] -> skip;

// ERROR_CHAR: . {raise ErrorToken(self.text)};

/* ------------------------ Ex 3 ------------------------ */
/* A program in BKOOL consists of many declarations, which are variable and function declarations. 

A variable declaration starts with a type, which is int or float, then a comma-separated list of identifiers and ends with a semicolon. 

A function declaration also start with a type and then an identifier, which is the function name, and then parameter declaration and ends with a body. The parameter declaration starts with a left round bracket ’(’ and a null-able semicolon-separated list of parameters and ends with a right round bracket ’)’. Each parameter always starts with a type and then a comma-separated list of identifier. A body starts with a left curly bracket ’{’, follows by a null-able list of variable declarations or statements and ends with a right curly bracket ’}’. 

There are 3 kinds of statements: assignment, call and return. All statements must end with a semicolon. An assignment statement starts with an identifier, then an equal ’=’, then an expression. A call starts with an identifier and then follows by a null-able comma-separated list of expressions enclosed by round brackets. A return statement starts with a symbol ’return’ and then an expression.  */

// program: decllist EOF;

// //And some other rules for variable declaration, function declaration and other rules
// decllist: decl decllist | decl;
// decl: vardecl | funcdecl;

// vardecl: typ idlist SEMI;
// idlist: ID COMMA idlist | ID;

// funcdecl: typ ID paramdecl body;
// paramdecl: LB paramlist RB;
// paramlist: paramprime | ;
// paramprime: param SEMI paramprime | param;
// param: typ idlist;
// body: LBRACE stmtlist RBRACE;
// stmtlist: stmt stmtlist | stmt;
// stmt: vardecl | assignstmt | callstmt | returnstmt;
// assignstmt: ID EQUAL expr SEMI;
// callstmt: ID LB exprlist RB SEMI;
// exprlist: exprime | ;
// exprime: expr COMMA exprime | expr;
// returnstmt: RETURN expr SEMI;


// typ: INTTYPE | FLOATTYPE;

// INTTYPE: 'int';

// FLOATTYPE: 'float';

// EQUAL: '=';

// COMMA: ',';

// SEMI: ';';

// LB: '(';

// RB: ')';

// LBRACE: '{';

// RBRACE: '}';

// expr: 'expr';

// RETURN: 'return';

// ID: [a-zA-Z]+;// includes a sequence of alphabetic characters.

// WS: [ \t\r\n] -> skip;

// ERROR_CHAR: . {raise ErrorToken(self.text)};

/* ------------------------ Ex 4 ------------------------ */
/* A program in BKOOL consists of many declarations, which are variable and function declarations. 

A variable declaration starts with a type, which is int or float, then a comma-separated list of identifiers and ends with a semicolon. 

A function declaration also start with a type and then an identifier, which is the function name, and then parameter declaration and ends with a body. The parameter declaration starts with a left round bracket ’(’ and a null-able semicolon-separated list of parameters and ends with a right round bracket ’)’. Each parameter always starts with a type and then a comma-separated list of identifier. A body starts with a left curly bracket ’{’, follows by a null-able list of variable declarations or statements and ends with a right curly bracket ’}’. 

There are 3 kinds of statements: assignment, call and return. All statements must end with a semicolon. An assignment statement starts with an identifier, then an equal ’=’, then an expression. A call starts with an identifier and then follows by a null-able comma-separated list of expressions enclosed by round brackets. A return statement starts with a symbol ’return’ and then an expression. 

An expression is a construct which is made up of operators and operands. They calculate on their operands and return new value. There are four kinds of infix operators: ’+’, ’-’, ’*’ and ’/’ where ’+’ have lower precedence than ’-’ while ’*’ and ’/’ have the highest precedence among these operators. The ’+’ operator is right associative, ’-’ is non-associative while ’*’ and ’/’ is left-associative. To change the precedence, a sub-expression is enclosed in round brackets. The operands can be an integer literal, float literal, an identifier, a call or a sub-expression. */
program: decllist EOF;

//And some other rules for variable declaration, function declaration and other rules
decllist: decl decllist | decl;
decl: vardecl | funcdecl;

vardecl: typ idlist SEMI;
idlist: ID COMMA idlist | ID;

funcdecl: typ ID paramdecl body;
paramdecl: LB paramlist RB;
paramlist: paramprime | ;
paramprime: param SEMI paramprime | param;
param: typ idlist;
body: LBRACE stmtlist RBRACE;
stmtlist: stmt stmtlist | stmt;
stmt: vardecl | assignstmt | callstmt | returnstmt;
assignstmt: ID EQUAL expr SEMI;
callstmt: ID LB exprlist RB SEMI;
exprlist: exprime | ;
exprime: expr COMMA exprime | expr;
returnstmt: RETURN expr SEMI;

expr: expr1 ADD expr2 | expr1;
expr1: expr2 MINUS expr2 | expr2;
expr2: expr2 (MUL | DIV) expr3 | expr3;
expr3: subexpr | callexpr | ID | INTLIT | FLOATLIT;
subexpr: LB expr RB;
callexpr: ID LB exprlist RB;

typ: INTTYPE | FLOATTYPE;

INTTYPE: 'int';

FLOATTYPE: 'float';

EQUAL: '=';

COMMA: ',';

SEMI: ';';

LB: '(';

RB: ')';

LBRACE: '{';

RBRACE: '}';

ADD: '+';

MINUS: '-';

MUL: '*';

DIV: '/';

INTLIT: [0-9]+;

FLOATLIST: FLOATLIT (COMMA FLOATLIT)*;

fragment INTPART: [0-9]+;
fragment FRACPART: '.' [0-9]+;
fragment EXPPART: 'e' '-'? [0-9]+;
FLOATLIT: INTPART (FRACPART EXPPART? | EXPPART);

RETURN: 'return';

ID: [a-zA-Z]+;// includes a sequence of alphabetic characters.

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};