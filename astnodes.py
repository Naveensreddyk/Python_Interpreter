class NumNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"NumNode({self.value})"

class VarNode:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"VarNode({self.name})"

class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"BinOpNode({self.left}, {self.op}, {self.right})"

class AssignNode:
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr

    def __repr__(self):
        return f"AssignNode({self.var}, {self.expr})"

class PrintNode:
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"PrintNode({self.expr})"


class IfNode:
    def __init__(self, condition, true_body, false_body=None):
        self.condition = condition
        self.true_body = true_body
        self.false_body = false_body

    def __repr__(self):
        return f"IfNode(condition={self.condition}, true_body={self.true_body}, false_body={self.false_body})"
