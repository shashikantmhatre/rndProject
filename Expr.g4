grammar Expr;
prog:   stat+ EOF;

stat
    : defStat
    | returnStat
    | assignStat
    | ifStat
    | foreachStat
    | forStat
    | addFunction
    ;

defStat
    : 'let' variable (',' variable)*
    ;

variable
    :   ID ('=' booleanExp )?
    ;

assignStat
    : assignNode '=' booleanExp
    ;

assignNode
    : ID ('.' ID )?
    ;

ifStat
    : 'if' booleanExp 'then' stat+ (elseStat)? 'end'
    ;

elseStat
    : 'else' stat+
    ;

foreachStat
    : 'foreach' ID 'in' nodeReference 'do' stat+ 'end'
    ;

forStat
    : 'for' ID 'in' INT 'do' stat+ 'end'
    ;

addFunction
    :   'add' '(' ID ',' node ')'
    ;

returnStat
    : 'return' booleanExp
    ;

booleanExp
    : NOT? '(' booleanExp ')'   #ParenBoolean
    | booleanExp op=('=' | '<>' | '<' | '<=' | '>' | '>=') booleanExp   #RelationalExp
    | booleanExp op=(AND | OR ) booleanExp #LogicalExp
    | arithmeticExp #BooleanArithmetic
    ;

arithmeticExp
    : '(' arithmeticExp ')' #ParenArithmetic
    | op=(ADD | SUB) arithmeticExp   #UnaryArithmetic
    | arithmeticExp op=('*'|'/') arithmeticExp      #MulDiv
    | arithmeticExp op=('+'|'-') arithmeticExp      #AddSub
    | node  #ArithmeticNode
    ;

node
    : STRING
    | INT
    | booleanValue
    | nodeReference
    | getFunction
    | objectNode
    | listNode
    ;

objectNode
    : '{' '}'
    ;

listNode
    : '[' ']'
    ;

getFunction
    : 'get' '(' booleanExp ( ',' INT )? ')'
    ;

nodeReference
    :   withPredicate ('.' nodeReference )?
    ;

withPredicate
    : ID ('['  booleanExp     ']')?
    ;

booleanValue
    : boolConst=( TRUE | FALSE )
    ;

MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
AND :   'and' ;
OR  :   'or' ;
TRUE :  'true' ;
FALSE : 'false' ;
NOT : 'not' ;

ID  :   [a-zA-Z][a-zA-Z_0-9-]* ;      // match identifiers
INT :   ('0'..'9')+('.' ('0'..'9')*)? ;         // match integers
STRING : '"' (ESC|.)*? '"'; // match " anything with \n \" ; "


NEWLINE : '\r'? '\n' -> skip;     // return newlines to parser (is end-statement signal)
LINE_COMMENT : '#' ~[\r\n]* -> skip; // match "#" stuff '\n'
COMMENT : '/*' .*? '*/' -> skip; // match /*' stuff '/*'
WS  :   [ \n\f\r\t]+ -> skip;  // toss out whitespace

fragment
ESC: '\\\''| '\\"' |  '\\\\' ; // 2-char sequence \" and \\