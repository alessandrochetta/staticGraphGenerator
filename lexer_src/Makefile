# Makefile for cminus

CC=gcc
LEX=flex
YACC=bison
MV=/bin/mv
RM=/bin/rm
CP=/bin/cp

LIBRARIES=-ll 

CFLAGS=-g

PROGRAM=lexer

OBJECTS=cmlexer.o 

SOURCES=cmlexer.l 


$(PROGRAM): $(OBJECTS)
	$(CC) $(CFLAGS) -o $(PROGRAM) $(OBJECTS) $(LIBRARIES)
	$(CP) $(PROGRAM) ../

cmlexer.o: cmlexer.c cmparser.tab.h globals.h
	$(CC) $(CFLAGS) -c cmlexer.c

cmlexer.c: cmlexer.l 
	$(LEX)  -o cmlexer.c cmlexer.l 

clean:
	$(RM) $(PROGRAM) $(OBJECTS) 
