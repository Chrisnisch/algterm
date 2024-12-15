import copy
import re


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
        if self.arity > 0:
            raise Warning('Setting arity 0 to a function')
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
        return Expression(f"{self} + {other}")

    def __mul__(self, other):
        return Expression(f"{self} * {other}")

    def __pow__(self, power):
        return Expression(f"{self}^{power}")


class Expression:
    """ +-full GPTs code """
    def __init__(self, value):
        """
        Initialize expression.

        :param value: Term or other expression.
        """
        if isinstance(value, (Term, Expression, int, float, str)):
            self.value = value
        else:
            raise TypeError('Expression must be initialized with Term, Expression, int, float, or str')

    def __add__(self, other):
        return Expression(f"({self.value} + {other})")

    def __mul__(self, other):
        return Expression(f"{self.value} * {other}")

    def __pow__(self, power):
        return Expression(f"({self.value})^{power}")

    def __repr__(self):
        return str(self.value)


if __name__ == '__main__':
    pass
    # func_f = Term('f(x, y, α)', expr=(x ** 2 + y ** 2 + alpha))  # терм-функция f
    # print(func_f)  # вывод терма-функции: f(x, y, α)
    # print(func_f.expression)  # вывод выражения терма-функции: x^2 + y^2 + α
    #
    # expr = x + func_f.expression ** 2 + alpha  # выражение с термами
    # print(expr)  # выводится полученное выражение: x + (x^2 + y^2 + α)^2 + α
