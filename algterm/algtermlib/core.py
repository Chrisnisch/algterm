import copy
import re
import sympy


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
        self.set_expression(expr) if expr else None

    def __set_arity(self, n):
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
        func_pattern = (r'^[a-zA-Z](_[a-zA-Z0-9]+)?\([a-z\u03b1-\u03c9](_[a-zA-Z0-9]+)?(\s*,\s*[a-z\u03b1-\u03c9](_['
                        r'a-zA-Z0-9]+)?)*\)$')

        if bool(re.match(const_pattern, s)) or bool(re.match(var_pattern, s)):
            self.symbol = s
            self.__set_arity(0)
        elif bool(re.match(func_pattern, s)):
            self.symbol = s
            self.__set_arity(len(s[1:-1].split(',')))
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

    def copy(self):
        """
        Create a copy of the current Term object.

        :return: A new Term object with the same attributes.
        """
        return copy.deepcopy(self)

    def __repr__(self):
        """
        String representation of the Term object.

        :return: A string describing the term.
        """
        return f'{self.symbol}'

    def __add__(self, other):
        return Expression(self, other, operator='+')

    def __mul__(self, other):
        return Expression(self, other, operator='*')

    def __truediv__(self, other):
        return Expression(self, other, operator='/')

    def __pow__(self, power):
        return Expression(self, power, operator='^')


class Expression:
    def __init__(self, left, right=None, operator=None):
        """
        Initialize an expression.

        :param left: Left operand (Term or Expression).
        :param right: Right operand (Term, Expression, or None for unary operators).
        :param operator: Operator as a string ('+', '*', '**', etc.).
        """
        self.left = left
        self.right = right
        self.operator = operator

    def __add__(self, other):
        return Expression(self, other, operator='+')

    def __mul__(self, other):
        return Expression(self, other, operator='*')

    def __truediv__(self, other):
        return Expression(self, other, operator='/')

    def __pow__(self, power):
        return Expression(self, power, operator='^')

    def __repr__(self):
        """
        Generate a string representation of the expression with minimal parentheses.

        :return: String representation of the expression.
        """
        if not self.operator:
            return str(self.left)

        # Define operator precedence
        precedence = {'+': 1, '*': 2, '/': 2, '^': 3}

        # Get the precedence of the current operator
        current_precedence = precedence[self.operator]

        # Determine whether to wrap left and right operands in parentheses
        left_repr = (
            f"({self.left})" if isinstance(self.left, Expression) and precedence.get(self.left.operator, 0) < current_precedence else f"{self.left}"
        )
        right_repr = (
            f"({self.right})" if isinstance(self.right, Expression) and precedence.get(self.right.operator, 0) <= current_precedence else f"{self.right}"
        )

        return f"{left_repr} {self.operator} {right_repr}"


def simp(expr):
    """
    Simplify the expression using sympy.ratsimp().

    :param expr: expression to simplify
    :return: simplified expression
    """
    return str(sympy.ratsimp(str(expr))).replace("**", "^")
