// 1913418
grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
/* -------------------------------------------------- PARSER -------------------------------------------------- */
program: decls+ | array_type | expression | statement EOF;

decls: var_decl | func_decl;

// Variable Declaration
var_decl: identifier_list COLON (typ | array_type) (assign_value_list | assign_func_call | assign_array)? SEMI;
identifier_list: IDENTIFIER COMMA identifier_list | IDENTIFIER;
typ: BOOLEAN | INTEGER | FLOAT | STRING | AUTO;
assign_value_list: ASSIGN value_list;
assign_func_call: ASSIGN function_call_list;
value_list: value_list_type_int | value_list_type_float | value_list_type_string | value_list_type_boolean;
value_list_type_int: INTEGER_LIT COMMA value_list_type_int | INTEGER_LIT;
value_list_type_float: FLOAT_LIT COMMA value_list_type_float | FLOAT_LIT;
value_list_type_string: STRING_LIT COMMA value_list_type_string | STRING_LIT;
value_list_type_boolean: BOOLEAN_LIT COMMA value_list_type_boolean | BOOLEAN_LIT;
assign_array: ASSIGN ARRAY_LIT;

// Parameters
parameter: INHERIT? OUT? IDENTIFIER COLON typ;

// Function Declaration
func_decl: IDENTIFIER COLON FUNCTION return_type LP parameter_list RP inheritance_subpart? statement;
return_type: BOOLEAN | INTEGER | FLOAT | STRING | VOID | AUTO;
parameter_list: parameter_prime | ;
parameter_prime: parameter COMMA parameter_prime | parameter;
inheritance_subpart: INHERIT IDENTIFIER;

// Array Type
array_type: ARRAY LSB dimensions RSB OF typ;
dimensions: INTEGER_LIT COMMA dimensions | INTEGER_LIT;

// Expression
expression: expr1 DOUBLE_COLON expr1 | expr1;
expr1: expr2 (EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | LESS_EQUAL | GREATER_EQUAL) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | MINUS) expr4 | expr4;
expr4: expr4 (MUL | DIV | MODUL) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: MINUS expr6 | expr7;
expr7: expr7 factor | expr8;
expr8: LP expression RP | factor;
factor: INTEGER_LIT | FLOAT_LIT | BOOLEAN_LIT | STRING_LIT | IDENTIFIER | function_call | IDENTIFIER LSB value_list_type_int RSB;

// Expression List (nullable, comma-separated)
expression_list: expression_prime | ;
expression_prime: expression COMMA expression_prime | expression;

// Statement
statement: assign_stmt | if_stmt | for_stmt | while_stmt | do_while_stmt | break_stmt | continue_stmt | return_stmt | call_stmt | block_stmt;

assign_stmt: lhs ASSIGN expression SEMI;
lhs: IDENTIFIER | IDENTIFIER LSB value_list_type_int RSB;

if_stmt: IF expression statement (ELSE statement)?;

for_stmt: FOR LP scalar_variable ASSIGN init_expr COMMA condition_expr COMMA update_expr RP statement;
scalar_variable: IDENTIFIER;
init_expr: expression;
condition_expr: IDENTIFIER (EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | LESS_EQUAL | GREATER_EQUAL) expression;
update_expr: IDENTIFIER (ADD | MINUS | MUL | DIV | MODUL) expression;

while_stmt: WHILE expression statement;

do_while_stmt: DO block_stmt WHILE expression SEMI;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

return_stmt: RETURN expression SEMI;

call_stmt: (function_call | special_func) SEMI;

block_stmt: LB stmts_or_var_decls RB | '{}';
stmts_or_var_decls: stmt_or_var_decl stmts_or_var_decls | ;
stmt_or_var_decl: statement_list | var_decl_list;
statement_list: statement statement_list | statement;
var_decl_list: var_decl var_decl_list | var_decl;

// Function Call
function_call: IDENTIFIER LP exp_list RP;
exp_list: exp_prime | ;
exp_prime: expression COMMA exp_prime | expression;

// Function Call List
function_call_list: function_call COMMA function_call_list | function_call;

// Special Functions
special_func: read_integer | print_integer | read_float | write_float | print_boolean | read_string | print_string | super_ | prevent_default;

read_integer: READINTEGER LP RP;
print_integer: PRINTINTEGER LP (INTEGER_LIT | IDENTIFIER) RP;
read_float: READFLOAT LP RP;
write_float: WRITEFLOAT LP (FLOAT_LIT | IDENTIFIER) RP;
read_boolean: READBOOLEAN LP RP;
print_boolean: PRINTBOOLEAN LP (BOOLEAN_LIT | IDENTIFIER) RP;
read_string: READSTRING LP RP;
print_string: PRINTSTRING LP (STRING_LIT | IDENTIFIER) RP;
super_: SUPER LP expression_list RP;
prevent_default: PREVENTDEFAULT LP RP;

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
READINTEGER: 'readInteger';
PRINTINTEGER: 'printInteger';
READFLOAT: 'readFloat';
WRITEFLOAT: 'writeFloat';
READBOOLEAN: 'readBoolean';
PRINTBOOLEAN: 'printBoolean';
READSTRING: 'readString';
PRINTSTRING: 'printString';
SUPER: 'super';
PREVENTDEFAULT: 'preventDefault';

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
DOUBLE_QUOTE: '"';

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
fragment NOTESC: '\\' ~('b' | 'f' | 'n' | 'r' | 't' | '"' | '\'' | '\\');
fragment ESC : '\\' ('b'|'f'|'r'|'n'|'t'|'\''|'\\'|'"');
fragment CHAR: '\\"' (~[\n\\"] | CHAR | ESC)*? '\\"';
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
STRING_LIT: DOUBLE_QUOTE (ESC | ~[\n\\"] | CHAR)* DOUBLE_QUOTE { self.text = str(self.text[1:-1]) };

// Array
ARRAY_LIT: LB EXPS? RB;

// IDENTIFIERS
IDENTIFIER: (LETTER | UNDERSCORE) (LETTER | UNDERSCORE | DIGIT)*;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

UNCLOSE_STRING: DOUBLE_QUOTE (~[\\"] | CHAR | ESC)*? ([\r\n] | EOF) {
		raise UncloseString(self.text[1:]) if self.text[len(self.text)-1] != '\n' and self.text[len(self.text)-1] != '\r' else UncloseString(self.text[1:-1])
};
ILLEGAL_ESCAPE: DOUBLE_QUOTE (~[\\"] | CHAR | ESC)* NOTESC {raise IllegalEscape(self.text[1:])};
ERROR_CHAR: .{raise ErrorToken(self.text)};
