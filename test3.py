from lexer import Lexer
from custom_parser import Parser
from interpreter import Interpreter

code = """
let a = 5.0;
let b = a * 7;
let c = a + b;
let d = b / c ;

print(b);
print(c);
print(d);
"""

# Initialize the lexer and get the tokens

lexer = Lexer(code)
tokens = lexer.get_tokens()
print("\nTokens:", tokens)

# Pass the list of tokens to the parser
parser = Parser(tokens)
ast = parser.parse()
print("\nAST:", ast)

# Interpret the AST
interpreter = Interpreter()
interpreter.interpret(ast)
