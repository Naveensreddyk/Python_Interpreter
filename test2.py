from lexer import Lexer
from custom_parser import Parser
from interpreter import Interpreter

code = """
let a = 5;
let b = 3;
let c = a + b * 2 - 4 / 2;
print(a);
print(b);
print(c);
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
