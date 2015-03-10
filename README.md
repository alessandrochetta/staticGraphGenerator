# staticGraphGenerator
The project aim is to analyze C++ code to represent graphically its dependencies graph -- Visit the wiki to to figure out how the system works

Main languages:
- Python - parser.py - the parser
- C - lexer - to tokenize the C++ files
- Javascript - graphex.html - to render the dependencies graph

The main system is written in python, it uses a flex based lexer to parse and tokenize the C++ source code. The tokens are then analyzed by the parser, written in python, to find each declaration of instance. A Javascript application renders the relations using D3.js graphic library.