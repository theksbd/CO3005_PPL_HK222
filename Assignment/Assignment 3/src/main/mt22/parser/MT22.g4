// 1913418
grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
/* -------------------------------------------------- PARSER -------------------------------------------------- */
program: decls+ EOF;

decls: vardecl | funcdecl;

// Variable Declaration
vardecl: vardeclAssign | vardeclNoAssign;

vardeclAssign: vardeclAssignment SEMI;
vardeclAssignment: IDENTIFIER COMMA vardeclAssignment COMMA expression | vardeclAssignBaseCase;
vardeclAssignBaseCase: IDENTIFIER COLON (typ | arrayType) ASSIGN expression;

vardeclNoAssign: identifierList COLON (typ | arrayType) SEMI;

// Parameters
parameter: INHERIT? OUT? IDENTIFIER COLON (typ | arrayType);

// Identifier List (nonnull, comma-separated)
identifierList: IDENTIFIER COMMA identifierList | IDENTIFIER;
typ: BOOLEAN | INTEGER | FLOAT | STRING | AUTO;

// Function Declaration
funcdecl: IDENTIFIER COLON FUNCTION returnType LP parameterList RP inheritanceSubpart? blockStmt;
returnType: BOOLEAN | INTEGER | FLOAT | STRING | VOID | AUTO | arrayType;
parameterList: parameterPrime | ;
parameterPrime: parameter COMMA parameterPrime | parameter;
inheritanceSubpart: INHERIT IDENTIFIER;

// Array Type
arrayType: ARRAY LSB dimensions RSB OF elementTyp;
dimensions: INTEGERLIT COMMA dimensions | INTEGERLIT;
elementTyp: BOOLEAN | INTEGER | FLOAT | STRING;

arrayLit: LB expressionListNonnull RB;

// Expression
expression: expr1 DOUBLECOLON expr1 | expr1;
expr1: expr2 (EQUAL | NOTEQUAL | LESSTHAN | GREATERTHAN | LESSEQUAL | GREATEREQUAL) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | MINUS) expr4 | expr4;
expr4: expr4 (MUL | DIV | MODUL) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: MINUS expr6 | expr7;
expr7: IDENTIFIER LSB expressionListNonnull RSB | expr8;
expr8: LP expression RP | factor;
factor: INTEGERLIT | FLOATLIT | BOOLEANLIT | STRINGLIT | IDENTIFIER | functionCall | arrayLit;

// Expression List (nullable, comma-separated)
expressionListNullable: expressionPrime | ;
expressionPrime: expression COMMA expressionPrime | expression;

// Expression List (nonnull, comma-separated)
expressionListNonnull: expression COMMA expressionListNonnull | expression;

// Statement
statement: assignStmt | ifStmt | forStmt | whileStmt | doWhileStmt | breakStmt | continueStmt | returnStmt | callStmt | blockStmt;

assignStmt: lhs ASSIGN expression SEMI;
lhs: IDENTIFIER | IDENTIFIER LSB expressionListNonnull RSB;

ifStmt: IF expression statement (ELSE statement)?;

forStmt: FOR LP initExpr COMMA conditionExpr COMMA updateExpr RP statement;
initExpr: IDENTIFIER ASSIGN expression;
conditionExpr: expression (EQUAL | NOTEQUAL | LESSTHAN | GREATERTHAN | LESSEQUAL | GREATEREQUAL) expression;
updateExpr: expression;

whileStmt: WHILE expression statement;

doWhileStmt: DO blockStmt WHILE expression SEMI;

breakStmt: BREAK SEMI;

continueStmt: CONTINUE SEMI;

returnStmt: RETURN (expression | ) SEMI;

callStmt: (specialFunc SEMI) | (IDENTIFIER LP expressionListNullable RP SEMI);

blockStmt: LB blockBody RB | EMPTYBLOCK;
blockBody: stmtsOrVardecls | ;
stmtsOrVardecls: stmtOrVardecl stmtsOrVardecls | stmtOrVardecl;
stmtOrVardecl: statement | vardecl;

// Statement List (nonnull, comma-separated)
statementList: statement statementList | statement;

// Variable Declaration List (nonnull, comma-separated)
vardeclList: vardecl vardeclList | vardecl;

// Function Call
functionCall: specialFunc | IDENTIFIER LP expressionListNullable RP;

// Function Call List (nonnull, comma-separated)
functionCallList: functionCall COMMA functionCallList | functionCall;

// Special Functions
specialFunc: readInteger | printInteger | readFloat | writeFloat | printBoolean | readString | printString | superFunction | preventDefault;

readInteger: READINTEGER LP RP;
printInteger: PRINTINTEGER LP expression RP;
readFloat: READFLOAT LP RP;
writeFloat: WRITEFLOAT LP expression RP;
readBoolean: READBOOLEAN LP RP;
printBoolean: PRINTBOOLEAN LP expression RP;
readString: READSTRING LP RP;
printString: PRINTSTRING LP expression RP;
superFunction: SUPER LP expressionListNonnull RP;
preventDefault: PREVENTDEFAULT LP RP;

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
NOTEQUAL: '!=';
LESSTHAN: '<';
LESSEQUAL: '<=';
GREATERTHAN: '>';
GREATEREQUAL: '>=';
DOUBLECOLON: '::';

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
DOUBLEQUOTE: '"';
EMPTYBLOCK: '{}';

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
fragment INTS: (INTEGERLIT COMMA INTS) | INTEGERLIT;
fragment FLOATS: (FLOATLIT COMMA FLOATS) | FLOATLIT;
fragment STRINGS: (STRINGLIT COMMA STRINGS) | STRINGLIT;

// COMMENTS
COMMENT: (CPPCOMMENT | CCOMMENT) -> skip;

// LITERALS
// Integer
INTEGERLIT: INTPART { self.text = self.text.replace("_","") };

// Float
FLOATLIT: (INTPART FRACPART EXPPART? | INTPART EXPPART | INTPART FRACPART | FRACPART EXPPART) { self.text = self.text.replace("_","") };

// Boolean
BOOLEANLIT: TRUE | FALSE;

// String
STRINGLIT: DOUBLEQUOTE (ESC | ~[\n\\"] | CHAR)* DOUBLEQUOTE { self.text = str(self.text[1:-1]) };

// Array
ARRAYLIT: LB EXPS? RB;

// IDENTIFIERS
IDENTIFIER: (LETTER | UNDERSCORE) (LETTER | UNDERSCORE | DIGIT)*;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

UNCLOSE_STRING: DOUBLEQUOTE (~[\\"] | CHAR | ESC)*? ([\r\n] | EOF) {
		raise UncloseString(self.text[1:]) if self.text[len(self.text)-1] != '\n' and self.text[len(self.text)-1] != '\r' else UncloseString(self.text[1:-1])
};
ILLEGAL_ESCAPE: DOUBLEQUOTE (~[\\"] | CHAR | ESC)* NOTESC {raise IllegalEscape(self.text[1:])};
ERROR_CHAR: .{raise ErrorToken(self.text)};
