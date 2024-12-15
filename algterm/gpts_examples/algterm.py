import re
from collections import defaultdict


class Term:
    def __init__(self, symbol, expr=None):
        """
        Initialize a Term object.

        :param symbol: Symbol representing the term.
        """
        self.symbol = None
        self.arity = None
        self.expression = None

        self.set_symbol(symbol)
        if expr:
            self.set_expression(expr)

    def set_arity(self, n):
        if n < 0:
            raise ValueError('Arity must be non-negative')
        self.arity = n

    def set_symbol(self, s: str):
        """
        Set or validate the symbol for the term.

        :param s: Symbol for the term.
        """
        var_pattern = r'^[a-z](_[a-zA-Z0-9]+)?$'
        const_pattern = r'^[\u03b1-\u03c9](_[a-zA-Z0-9]+)?$'
        func_pattern = r'^[a-zA-Z](_[a-zA-Z0-9]+)?\([a-z\u03b1-\u03c9](_[a-zA-Z0-9]+)?(\s*,\s*[a-z\u03b1-\u03c9](_[a-zA-Z0-9]+)?)*\)$'

        if re.match(const_pattern, s) or re.match(var_pattern, s):
            self.symbol = s
            self.set_arity(0)
        elif re.match(func_pattern, s):
            self.symbol = s
            self.set_arity(len(s[s.index('(') + 1:s.index(')')].split(',')))
        else:
            raise ValueError('Invalid term name')

    def set_expression(self, expr):
        """
        Set or update the expression for the term.

        :param expr: The expression.
        """
        if self.arity == 0:
            raise ValueError('Constants or variables cannot have expressions')
        self.expression = Expression(expr)

    def __repr__(self):
        return self.symbol

    def __add__(self, other):
        return Expression(('+', self, other))

    def __mul__(self, other):
        return Expression(('*', self, other))

    def __pow__(self, power):
        return Expression(('^', self, power))


class Expression:
    def __init__(self, value):
        """
        Initialize expression.

        :param value: Tuple representing an operation, Term, or a constant.
        """
        self.value = value

    def __add__(self, other):
        return Expression(('+', self, other))

    def __mul__(self, other):
        return Expression(('*', self, other))

    def __pow__(self, power):
        return Expression(('^', self, power))

    def simplify(self):
        """
        Simplify the expression recursively.

        :return: A simplified Expression.
        """
        return self._simplify_recursive(self.value)

    def _simplify_recursive(self, node):
        """
        Simplify the expression tree recursively.

        :param node: Current node in the expression tree.
        :return: Simplified node.
        """
        if isinstance(node, Term) or isinstance(node, (int, float)):
            return node
        if isinstance(node, Expression):  # Раскрываем вложенные выражения
            return self._simplify_recursive(node.value)

        op, left, right = node

        left = self._simplify_recursive(left)
        right = self._simplify_recursive(right)

        if op == '+':
            if isinstance(left, Term) and isinstance(right, Term) and left.symbol == right.symbol:
                return Term(left.symbol)  # Объединение однотипных термов
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left + right
        elif op == '*':
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left * right
        elif op == '^':
            if isinstance(right, (int, float)):
                return left ** right

        return (op, left, right)

    def __repr__(self):
        return self._to_string(self.value)

    def _to_string(self, node):
        """
        Convert the expression tree to a string representation.

        :param node: Current node in the tree.
        :return: String representation.
        """
        if isinstance(node, Term):
            return node.symbol
        if isinstance(node, (int, float)):
            return str(node)
        if isinstance(node, Expression):  # Раскрытие Expression
            return self._to_string(node.value)

        op, left, right = node
        left_str = self._to_string(left)
        right_str = self._to_string(right)

        if op == '+':
            return f"({left_str} + {right_str})"
        elif op == '*':
            return f"({left_str} * {right_str})"
        elif op == '^':
            return f"({left_str}^{right_str})"
        return ""


if __name__ == '__main__':
    # Example usage
    x = Term('x')  # Variable x
    y = Term('y')  # Variable y
    alpha = Term('α')  # Constant α

    # Define an expression
    expr = x + y + x * y + alpha
    print("Expression:", expr)

    # Simplify
    simplified = expr.simplify()
    print("Simplified Expression:", simplified)
