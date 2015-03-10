#ifndef BISON_CMPARSER_TAB_H
# define BISON_CMPARSER_TAB_H

# ifndef YYSTYPE
#  define YYSTYPE int
#  define YYSTYPE_IS_TRIVIAL 1
# endif
# define	TOK_ELSE	257
# define	TOK_IF	258
# define	TOK_RETURN	259
# define	TOK_SIGN_UNSIGN	260
# define	TOK_FUNDAMENTAL_TYPE	261
# define	TOK_OTHER_OPS	262
# define	TOK_ID	263
# define	TOK_NUM	264
# define	TOK_PLUS	265
# define	TOK_MINUS	266
# define	TOK_MULT	267
# define	TOK_DIV	268
# define	TOK_LT	269
# define	TOK_LE	270
# define	TOK_GT	271
# define	TOK_GE	272
# define	TOK_EQ	273
# define	TOK_NE	274
# define	TOK_ASSIGN	275
# define	TOK_SEMI	276
# define	TOK_COMMA	277
# define	TOK_LPAREN	278
# define	TOK_RPAREN	279
# define	TOK_LSQ	280
# define	TOK_RSQ	281
# define	TOK_LBRACE	282
# define	TOK_RBRACE	283

# define	TOK_DONT_CARE	284
# define	TOK_NEW_OPERAND	285
# define	TOK_COLON		286
# define 	TOK_CLASS		287
# define	TOK_CONST		288
# define	TOK_COLON_COLON	289
# define	TOK_KEYWORD	290
# define	TOK_AMP	291
# define	TOK_ACCESS 292
# define	TOK_STRING 293
# define	TOK_OPERATOR 294


extern YYSTYPE yylval;

#endif /* not BISON_CMPARSER_TAB_H */
