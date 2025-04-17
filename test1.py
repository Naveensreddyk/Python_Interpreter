from lexer import *
from custom_parser import *
from interpreter import *
from astnodes import *

if __name__ == "__main__":
    code = """
let x = 10;
let y = 20;
let z = x + y;
print(z);
"""
lexer = Lexer(code)
tokens = lexer.get_tokens()

print("\nTokens:", tokens)

parser = Parser(tokens)
ast = parser.parse()

print("\nAST:", ast)

interpreter = Interpreter()
interpreter.interpret(ast)

print()



