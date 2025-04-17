from astnodes import *
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        """Returns the current token."""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, token_type):
        """Consumes the current token if it matches the expected type."""
        token = self.current_token()
        if token and token[0] == token_type:
            self.pos += 1
            return token
        raise SyntaxError(f"Expected {token_type}, got {token}. Error at position {self.pos}")

    def factor(self):
        """Parses numbers or parentheses."""
        token = self.current_token()
        if token[0] == 'NUMBER':
            self.eat('NUMBER')
            return NumNode(token[1])
        elif token[0] == 'LPAREN':
            self.eat('LPAREN')
            node = self.expr()
            self.eat('RPAREN')
            return node
        elif token[0] == 'ID':
            self.eat('ID')
            return VarNode(token[1])
        raise SyntaxError("Invalid factor")

    def term(self):
        """Parses multiplication and division."""
        node = self.factor()
        while self.current_token() and self.current_token()[0] in ('MUL', 'DIV'):
            token = self.current_token()
            self.eat(token[0])
            node = BinOpNode(left=node, op=token[0], right=self.factor())
        return node

    def expr(self):
        """Parses addition and subtraction."""
        node = self.term()
        while self.current_token() and self.current_token()[0] in ('PLUS', 'MINUS'):
            token = self.current_token()
            self.eat(token[0])
            node = BinOpNode(left=node, op=token[0], right=self.term())
        return node

    def assignment(self):
        """Parses assignment statements."""
        self.eat('LET')
        var_name = self.eat('ID')[1]
        self.eat('ASSIGN')
        expr = self.expr()
        self.eat('SEMI')
        return AssignNode(var_name, expr)

    def print_statement(self):
        """Parses print statements."""
        self.eat('PRINT')
        self.eat('LPAREN')
        expr = self.expr()
        self.eat('RPAREN')
        self.eat('SEMI')
        return PrintNode(expr)

    def statement(self):
        if self.current_token()[0] == 'LET':
            return self.assignment()
        elif self.current_token()[0] == 'PRINT':
            return self.print_statement()
        elif self.current_token()[0] == 'IF':
            return self.conditional()
        raise SyntaxError("Invalid statement")

    
    def parse(self):
        """Parses the entire token stream into a list of statements."""
        statements = []
        while self.current_token() is not None:  
            # Explicitly check for `None`
            try:
                statements.append(self.statement())
            except SyntaxError as e:
                print(f"SyntaxError: {e}. Remaining tokens: {self.tokens[self.pos:]}")
                break  
            # Exit parsing loop on error
        return statements


    def conditional(self):
        self.eat('IF')
        self.eat('LPAREN')
        condition = self.expr()
        self.eat('RPAREN')
        true_block = self.statement()
        false_block = None
        if self.current_token() and self.current_token()[0] == 'ELSE':
            self.eat('ELSE')
            false_block = self.statement()
        return IfNode(condition, true_block, false_block)
    


