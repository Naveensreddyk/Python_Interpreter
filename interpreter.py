from astnodes import *;

class Interpreter:
    def __init__(self):
        self.variables = {}

    def visit(self, node):
        """Dispatch method to visit nodes based on their type."""
        if isinstance(node, NumNode):
            return node.value
        elif isinstance(node, VarNode):
            if node.name in self.variables:
                return self.variables[node.name]
            raise NameError(f"Variable '{node.name}' not defined.")
        elif isinstance(node, BinOpNode):
            left = self.visit(node.left)
            right = self.visit(node.right)
            if node.op == 'PLUS':
                return left + right
            elif node.op == 'MINUS':
                return left - right
            elif node.op == 'MUL':
                return left * right
            elif node.op == 'DIV':
                return left / right
        elif isinstance(node, AssignNode):
            value = self.visit(node.expr)
            self.variables[node.var] = value
        elif isinstance(node, PrintNode):
            value = self.visit(node.expr)
            print(value)
        elif isinstance(node, IfNode):  # Handle `if` nodes
            condition = self.visit(node.condition)
            if condition:
                for stmt in node.true_body:
                    self.visit(stmt)
            elif node.false_body is not None:
                for stmt in node.false_body:
                    self.visit(stmt)

    def interpret(self, statements):
        for statement in statements:
            self.visit(statement)
