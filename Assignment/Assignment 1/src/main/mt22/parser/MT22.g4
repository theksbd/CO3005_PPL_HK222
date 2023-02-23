grammar MT22;
// 1913418

@lexer::header {
from lexererr import *
}

// @parser::header {
// from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener

// class NewErrorListener(ConsoleErrorListener):
//     INSTANCE = None

//     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
// 	    return SyntaxException("Error on line " + str(line) +
//                               " col " + str(column) + ": " + offendingSymbol.text)

// NewErrorListener.INSTANCE = NewErrorListener()

// class SyntaxException(Exception):
//     def __init__(self, msg):
//         self.message = msg
// }

options {
	language = Python3;
}
/* -------------------------------------------------- PARSER -------------------------------------------------- */
program: decls+ EOF;

decls: var_decl | func_decl | array_type | statement | expression;

// Array type -------------------------------------------------------------
array_type: ARRAY LSB dimesion RSB OF typ;
dimesion: dimesion_type_int | dimesion_type_float;
dimesion_type_int:
	INTEGER_LIT COMMA dimesion_type_int
	| INTEGER_LIT;
dimesion_type_float:
	FLOAT_LIT COMMA dimesion_type_float FLOAT_LIT;

// Variable declaration
var_decl: identifier_list COLON typ (equal_exp | equal_func_call);
identifier_list: IDENTIFIER COMMA identifier_list | IDENTIFIER;
typ: BOOLEAN | INTEGER | FLOAT | STRING;
equal_exp: (ASSIGN expression_list SEMI) | SEMI;
equal_func_call: (ASSIGN function_call SEMI) | SEMI;
expression_list: exp_list_type_int | exp_list_type_float;
exp_list_type_int:
	INTEGER_LIT COMMA exp_list_type_int
	| INTEGER_LIT;
exp_list_type_float:
	FLOAT_LIT COMMA exp_list_type_float
	| FLOAT_LIT;
exp_list_type_string:
	STRING_LIT COMMA exp_list_type_string
	| STRING_LIT;

// Parameters
parameter: INHERIT? OUT? IDENTIFIER COLON typ;

// expression declarations --------------------------------------------------
expression: expression_1 DOUBLE_COLON expression_1 | expression_1;

expression_1:
	expression_2 (
		EQUAL
		| NOT_EQUAL
		| LESS_THAN
		| GREATER_THAN
		| LESS_EQUAL
		| GREATER_EQUAL
	) expression_2
	| expression_2;

expression_2:
	expression_2 (AND | OR) expression_3
	| expression_3;

expression_3:
	expression_3 (ADD | MINUS) expression_4
	| expression_4;

expression_4:
	expression_4 (MUL | DIV | MODUL) expression_5
	| expression_5;

expression_5: NOT expression_5 | expression_6;

expression_6: MINUS expression_6 | expression_7;

expression_7: expression_7 factor | expression_8;

expression_8: (LP expression RP) | factor;

factor: (
		INTEGER_LIT
		| FLOAT_LIT
		| STRING_LIT
		| IDENTIFIER
		| function_call
	)
	| IDENTIFIER LSB exp_list_type_int RSB;

// function call ------------------------------------------------------------
function_call: IDENTIFIER LP exp_list RP;
exps_list: exp_list |;
exp_list: expression COMMA exp_list | expression;

// statement ----------------------------------------------------------------
statement:
	assign_stmt
	| if_stmt
	| for_stmt
	| while_stmt
	| do_while_stmt
	| block_stmt
	| return_stmt
	| continue_stmt
	| break_stmt
	| call_stmt
	| var_decl;

// assignment statement ------------------------------------------------------
assign_stmt: lhs ASSIGN expression SEMI;
lhs: IDENTIFIER LSB exp_list_type_int RSB | IDENTIFIER;

// if statement --------------------------------------------------------------
if_stmt: (IF expression statement ELSE statement)
	| IF expression statement;

// for statement -------------------------------------------------------------
for_stmt:
	LP scala_val ASSIGN init_expr COMMA condition_expr COMMA update_expr RP statement;
scala_val: IDENTIFIER;
init_expr: INTEGER_LIT | IDENTIFIER;
condition_expr:
	IDENTIFIER (
		LESS_THAN
		| GREATER_THAN
		| LESS_EQUAL
		| GREATER_EQUAL
		| NOT_EQUAL
		| EQUAL
	) (IDENTIFIER | expression);
update_expr: IDENTIFIER (ADD | MINUS | MUL | MODUL) expression;

// while statement ------------------------------------------------------------
while_stmt: WHILE LP expression RP statement;

// Do while statement ---------------------------------------------------------
do_while_stmt: DO block_stmt WHILE expression;

// call statement -------------------------------------------------------------
call_stmt: function_call SEMI;

// block statement ------------------------------------------------------------
block_stmt: (LB statement* RB) | '{}';
// statement_list: statement statement_list | statement;

//break statement -------------------------------------------------------------
break_stmt: BREAK SEMI;

// continue statement ---------------------------------------------------------
continue_stmt: CONTINUE SEMI;

// return statement -----------------------------------------------------------
return_stmt: RETURN expression SEMI;

// Function declaration
func_decl: IDENTIFIER COLON FUNCTION return_type LP parameter_list RP inheritance_subpart? statement;
return_type: BOOLEAN | INTEGER | FLOAT | STRING | VOID | AUTO;
parameter_list: parameter_prime | ;
parameter_prime: parameter COMMA parameter_prime | parameter;
inheritance_subpart: INHERIT IDENTIFIER;

/* -------------------------------------------------- LEXER -------------------------------------------------- */

// KEYWORDS
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';

// OPERATORS
ADD: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MODUL: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS_THAN: '<';
LESS_EQUAL: '<=';
GREATER_THAN: '>';
GREATER_EQUAL: '>=';
DOUBLE_COLON: '::';

// SEPARATORS
LP: '(';
RP: ')';
LSB: '[';
RSB: ']';
DOT: '.';
COMMA: ',';
SEMI: ';';
COLON: ':';
LB: '{';
RB: '}';
ASSIGN: '=';

// FRAGMENTS
fragment CPPCOMMENT: '//' ~[\r\n]*;
fragment CCOMMENT: '/*' .*? '*/';
fragment UPPERCASE: [A-Z];
fragment LOWERCASE: [a-z];
fragment LETTER: UPPERCASE | LOWERCASE;
fragment UNDERSCORE: '_';
fragment DIGIT: [0-9];
fragment INTPART: '0' | [1-9] DIGIT* (UNDERSCORE DIGIT+)*;
fragment FRACPART: '.' DIGIT*;
fragment SIGN: '+' | '-';
fragment EXPPART: [eE] SIGN? DIGIT+;
fragment TRUE: 'true';
fragment FALSE: 'false';
fragment ESC : '\\' ('b'|'f'|'r'|'n'|'t'|'\''|'\\') ;
fragment CHAR: '\\"' .*? '\\"';
fragment EXPS: INTS | FLOATS | STRINGS;
fragment INTS: (INTEGER_LIT COMMA INTS) | INTEGER_LIT;
fragment FLOATS: (FLOAT_LIT COMMA FLOATS) | FLOAT_LIT;
fragment STRINGS: (STRING_LIT COMMA STRINGS) | STRING_LIT;

// COMMENTS
COMMENT: (CPPCOMMENT | CCOMMENT) -> skip;

// LITERALS
// Integer
INTEGER_LIT: INTPART { self.text = self.text.replace("_","") };

// Float
FLOAT_LIT: (INTPART FRACPART EXPPART? | INTPART EXPPART | INTPART FRACPART | FRACPART EXPPART) { self.text = self.text.replace("_","") };


// Boolean
BOOLEAN_LIT: TRUE | FALSE;

// String
STRING_LIT: '"' (ESC | ~[\r\n\\"] | CHAR)* '"' { self.text = self.text[1:-1] };

// Array
ARRAY_LIT: LB EXPS? RB;

// IDENTIFIERS
IDENTIFIER: (LETTER | UNDERSCORE) (LETTER | UNDERSCORE | DIGIT)*;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

UNCLOSE_STRING: '"' (~[\\"] | CHAR)*? {raise UncloseString(self.text)};
ILLEGAL_ESCAPE: (~[\\"] | CHAR)*? '"' {raise IllegalEscape(self.text)};
ERROR_CHAR: .{raise ErrorToken(self.text)};
// UNCLOSE_STRING: .;
// ILLEGAL_ESCAPE: .;