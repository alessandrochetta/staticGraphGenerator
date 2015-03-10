
/**********************/
/* C header files */
/**********************/

%{
#include "globals.h"
#include "cmparser.tab.h"
char tokenString[TOKENMAX];
int printoutScan = 1;
FILE *token_file;
%}
%option yylineno

/**********************/
/* start your regular definitions  here */
/**********************/


KEYWORD 			"auto"|"break"|"case"|"continue"|"default"|"do"|"for"|"goto"|"register"|"switch"|"byte"|"while"|"throw"|"alignas"|"alignof"|"asm"|"catch"|"concept"|"constexpr"|"decltype"|"enum"|"explicit"|"export"|"extern"|"false"|"true"|"inline"|"mutable"|"namespace"|"noexcept"|"nullptr"|"reinterpret_cast"|"requires"|"static"|"static_assert"|"static_cast"|"struct"|"template"|"this"|"thread_local"|"try"|"typedef"|"typeid"|"typename"|"usign"|"virtual"|"volatile"
OTHER_OPS	        "~"|"?"|"++"|"--"|"!"|"|"|"^"|"<<"|">>"|">>>"|"+="|"-="|"*="|"/="|"^="|"%="|"<<="|">>="|"&="|"|="|">>>="|"and"|"and_eq"|"bitand"|"bitor"|"compl"|"const_cast"|"delete"|"dynamic_cast"|"not"|"not_eq"|"or"|"or_eq"|"sizeof"|"union"|"xor"|"xor_eq"|"\""
ACCESS              "public"|"private"|"protected"
DIGIT				[0-9]
NON_ZERO_DIGIT 		[1-9]
LITERAL				[a-zA-Z]
ID_A				"_"|"$"|{LITERAL}
ID_B				{ID_A}|{DIGIT}
NUMBER 				{NON_ZERO_DIGIT}{DIGIT}*|"0"
NON_NUMBER			"0"{DIGIT}+
SPACES				[ \t\n\r\f\v]
COMMENT				"//"[^\n\r]*
MULTILINE_COMMENT	"/*"([^\*]|[\*]+[^\*\/])*[*]+[/]
STRING              "\""[.|\n]*"\""











/* start your token specifications here */
/* Token names must come from cmparser.tab.h */

%%

"new"   { return TOK_NEW_OPERAND; }
"operator" {return TOK_OPERATOR; }
"class" { return TOK_CLASS; }
"const" { return TOK_CONST; }
"else"	{ return TOK_ELSE; }
"if"		{ return TOK_IF; }
"int"		{ return TOK_FUNDAMENTAL_TYPE; }
"void"      { return TOK_FUNDAMENTAL_TYPE; }
"bool"      { return TOK_FUNDAMENTAL_TYPE; }
"char"      { return TOK_FUNDAMENTAL_TYPE; }
"short"      { return TOK_FUNDAMENTAL_TYPE; }
"long"      { return TOK_FUNDAMENTAL_TYPE; }
"float"      { return TOK_FUNDAMENTAL_TYPE; }
"double"      { return TOK_FUNDAMENTAL_TYPE; }
"wchar_t"      { return TOK_FUNDAMENTAL_TYPE; }
"char16_t"      { return TOK_FUNDAMENTAL_TYPE; }
"char32_t"      { return TOK_FUNDAMENTAL_TYPE; }
"String"      { return TOK_FUNDAMENTAL_TYPE; }
"string"      { return TOK_FUNDAMENTAL_TYPE; }
"signed"      { return TOK_SIGN_UNSIGN; }
"unsigned"      { return TOK_SIGN_UNSIGN; }
"return"	{ return TOK_RETURN; }
{STRING}    {  return TOK_STRING;}
{ACCESS}        {return TOK_ACCESS;}
{OTHER_OPS} 	{ return TOK_OTHER_OPS; }
{KEYWORD}  			{ return TOK_KEYWORD; }
{NON_NUMBER}		{ return TOK_DONT_CARE; }
{ID_A}{ID_B}* 		{ return TOK_ID; }
{NUMBER}			{ return TOK_NUM; }
"("		{ return TOK_LPAREN; }
")"		{ return TOK_RPAREN; }
"["		{ return TOK_LSQ; }
"]"		{ return TOK_RSQ; }
"{"		{ return TOK_LBRACE; }
"}"		{ return TOK_RBRACE; }
"="		{ return TOK_ASSIGN; }
">"		{ return TOK_GT; }
"<"		{ return TOK_LT; }
"=="		{ return TOK_EQ; }
">="		{ return TOK_GE; }
"<="		{ return TOK_LE; }
"!="		{ return TOK_NE; }
"+"		{ return TOK_PLUS; }
"-"		{ return TOK_MINUS; }
"*"		{ return TOK_MULT; }
"/"		{ return TOK_DIV; }
":"     { return TOK_COLON; }
"::"    { return TOK_COLON_COLON; }
";"		{ return TOK_SEMI; }
","		{ return TOK_COMMA; }
"&"     { return TOK_AMP; }
{MULTILINE_COMMENT} ;
{COMMENT}	;
{SPACES} 	;
.			{ return TOK_DONT_CARE; }




%%
/**********************/
/* C support functions */
/**********************/


void printToken(int token, char *str)
{
/* Print the line number, token name and matched lexeme
   -- one per line without any additional characters exactly as below */ 
/* Example  13:TOK_INT: 37*/
    fprintf(token_file,"<line number=\"%d\" ",yylineno);
    switch(token)
        {
            case TOK_FUNDAMENTAL_TYPE:
                fprintf(token_file,"token=\"TOK_FUNDAMENTAL_TYPE\" text=\"%s\"/>\n",str);
                break;
            case TOK_OPERATOR:
                fprintf(token_file,"token=\"TOK_OPERATOR\" text=\"\"/>\n");
                break;
            case TOK_STRING:
                fprintf(token_file,"token=\"TOK_STRING\" text=\"\"/>\n");
                break;
            case TOK_ACCESS:
                fprintf(token_file,"token=\"TOK_ACCESS\" text=\"\"/>\n");
                break;
            case TOK_SIGN_UNSIGN:
                fprintf(token_file,"token=\"TOK_SIGN_UNSIGN\" text=\"%s\"/>\n",str);
                break;
            case TOK_AMP:
                fprintf(token_file,"token=\"TOK_AMP\" text=\"\"/>\n");
                break;
            case TOK_KEYWORD:
                    fprintf(token_file,"token=\"TOK_KEYWORD\" text=\"%s\"/>\n",str);
                break;
            case TOK_DONT_CARE:
                fprintf(token_file,"token=\"TOK_DONT_CARE\" text=\"\"/>\n");
                break;
            case TOK_OTHER_OPS:
                fprintf(token_file,"token=\"TOK_OTHER_OPS\" text=\"\"/>\n");
                break;
            case TOK_ELSE:
                fprintf(token_file,"token=\"TOK_ELSE\" text=\"\"/>\n");
                break;
            case TOK_IF:
                fprintf(token_file,"token=\"TOK_IF\" text=\"\"/>\n");
                break;
            case TOK_RETURN:
                fprintf(token_file,"token=\"TOK_RETURN\" text=\"\"/>\n");
                break;
            case TOK_ID:
                fprintf(token_file,"token=\"TOK_ID\" text=\"%s\"/>\n",str);
                break;
            case TOK_NUM:
                fprintf(token_file,"token=\"TOK_NUM\" text=\"\"/>\n");
                break;
            case TOK_PLUS:
                fprintf(token_file,"token=\"TOK_PLUS\" text=\"\"/>\n");
                break;
            case TOK_MINUS:
                fprintf(token_file,"token=\"TOK_MINUS\" text=\"\"/>\n");
                break;
            case TOK_MULT:
                fprintf(token_file,"token=\"TOK_MULT\" text=\"\"/>\n");
                break;
            case TOK_DIV:
                fprintf(token_file,"token=\"TOK_DIV\" text=\"\"/>\n");
                break;
            case TOK_LT:
                fprintf(token_file,"token=\"TOK_LT\" text=\"\"/>\n");
                break;
            case TOK_LE:
                fprintf(token_file,"token=\"TOK_LE\" text=\"\"/>\n");
                break;
            case TOK_GT:
                fprintf(token_file,"token=\"TOK_GT\" text=\"\"/>\n");
                break;
            case TOK_GE:
                fprintf(token_file,"token=\"TOK_GE\" text=\"\"/>\n");
                break;
            case TOK_EQ:
                fprintf(token_file,"token=\"TOK_EQ\" text=\"\"/>\n");
                break;
            case TOK_NE:
                fprintf(token_file,"token=\"TOK_NE\" text=\"\"/>\n");
                break;
            case TOK_ASSIGN:
                fprintf(token_file,"token=\"TOK_ASSIGN\" text=\"\"/>\n");
                break;
            case TOK_SEMI:
                fprintf(token_file,"token=\"TOK_SEMI\" text=\"\"/>\n");
                break;
            case TOK_COMMA:
                fprintf(token_file,"token=\"TOK_COMMA\" text=\"\"/>\n");
                break;
            case TOK_LPAREN:
                fprintf(token_file,"token=\"TOK_LPAREN\" text=\"\"/>\n");
                break;
            case TOK_RPAREN:
                fprintf(token_file,"token=\"TOK_RPAREN\" text=\"\"/>\n");
                break;
            case TOK_LSQ:
                fprintf(token_file,"token=\"TOK_LSQ\" text=\"\"/>\n");
                break;
            case TOK_RSQ:
                fprintf(token_file,"token=\"TOK_RSQ\" text=\"\"/>\n");
                break;
            case TOK_LBRACE:
                fprintf(token_file,"token=\"TOK_LBRACE\" text=\"\"/>\n");
                break;
            case TOK_RBRACE:
                fprintf(token_file,"token=\"TOK_RBRACE\" text=\"\"/>\n");
                break;
            case TOK_NEW_OPERAND:
                fprintf(token_file,"token=\"TOK_NEW_OPERAND\" text=\"\"/>\n");
                break;
            case TOK_COLON:
                fprintf(token_file,"token=\"TOK_COLON\" text=\"\"/>\n");
                break;
            case TOK_CLASS:
                fprintf(token_file,"token=\"TOK_CLASS\" text=\"\"/>\n");
                break;
            case TOK_CONST:
                fprintf(token_file,"token=\"TOK_CONST\" text=\"\"/>\n");
                break;
            case TOK_COLON_COLON:
                fprintf(token_file,"token=\"TOK_COLON_COLON\" text=\"\"/>\n");
                break;
        }
}

int gettok(void){
    int currentToken;
    
    currentToken=yylex();
    if (currentToken == 0) { // means EOF}
            return 0;
    }
    strncpy(tokenString, yytext, TOKENMAX);
    if (printoutScan) {
        printToken(currentToken,tokenString);
    }
    return currentToken;
}

int main(int argc, char **argv){
    char filename[400];
    strcpy(filename, argv[1]);
    strcat(filename, ".xml");
    printf("%s", filename);
    token_file = fopen(filename, "w");
    fprintf(token_file,"<?xml version=\"1.0\"?>\n");
    fprintf(token_file,"<file name=\"%s\">\n", argv[1]);
   if ( argc > 1 )
       yyin = fopen( argv[1], "r" );
   else
    yyin = stdin;

   while (gettok() !=0) 
    ; //gettok returns 0 on EOF
   fprintf(token_file,"</file>");
    return 0;
} 
