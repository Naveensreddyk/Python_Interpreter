
import re

# Token types: Defines the regular expressions (regex) for various token categories.
TOKEN_SPECIFICATION = [
    ('NUMBER',   r'\d+(\.\d+)?'),   # Matches integer or decimal numbers
    ('ASSIGN',   r'='),             # Matches assignment operator (=)
    ('PLUS',     r'\+'),            # Matches addition operator (+)
    ('MINUS',    r'-'),             # Matches subtraction operator (-)
    ('MUL',      r'\*'),            # Matches multiplication operator (*)
    ('DIV',      r'/'),             # Matches division operator (/)
    ('LPAREN',   r'\('),            # Matches left parenthesis '('
    ('RPAREN',   r'\)'),            # Matches right parenthesis ')'
    ('LBRACE',   r'\{'),            # Matches left brace '{'
    ('RBRACE',   r'\}'),            # Matches right brace '}'
    ('SEMI',     r';'),             # Matches statement terminator (;)
    ('ID',       r'[A-Za-z_]\w*'),  # Matches identifiers (variable names)
    ('WHITESPACE', r'\s+'),         # Matches whitespace characters (spaces, tabs, etc.) – ignored
    ('COMMENT',   r'#.*'),          # Matches comments starting with '#' – ignored
]

# Keywords dictionary: Maps keywords to their token types
KEYWORDS = {
    'let': 'LET',     # Keyword for variable declaration
    'print': 'PRINT', # Keyword for print statement
    'if': 'IF',       # Keyword for if condition
    'else': 'ELSE',   # Keyword for else block
    'int': 'INT',     # Keyword for integer data type
}

class Lexer:
    def __init__(self, text):
        self.text = text    # Input source code text
        self.tokens = []    # List to store tokens

    def tokenize(self):
        """Tokenizes the input text using regular expressions."""
        # Create a regex pattern by joining all token types
        token_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in TOKEN_SPECIFICATION)
        
        # Iterate over all matches in the text
        for match in re.finditer(token_regex, self.text):
            kind = match.lastgroup   # The name of the matched group (token type)
            value = match.group()    # The actual value of the match

            # Skip whitespace and comments
            if kind in ('WHITESPACE', 'COMMENT'):
                continue

            # Check if the token is a keyword
            if kind == 'ID' and value in KEYWORDS:
                kind = KEYWORDS[value]  # Replace ID with the keyword's token type

            # Handle numeric values (convert to int or float as appropriate)
            if kind == 'NUMBER':
                value = float(value) if '.' in value else int(value)

            # Append the token (kind and value) to the list of tokens
            self.tokens.append((kind, value))

    def get_tokens(self):
        """Returns the list of tokens after tokenizing the input."""
        self.tokenize()
        return self.tokens
