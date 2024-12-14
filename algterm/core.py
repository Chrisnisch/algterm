import re


class Term:

    def __init__(self, symbol, arity, expression=None):
        """
        Initialize a Term object.

        :param arity: Arity of the term (0 for constants/variables, >= 1 for functions).
        :param symbol: Symbol representing the term.
        :param expression: Optional; expression for the term if it represents a function.
        """
        self.set_arity(arity)
        self.set_symbol(symbol)
        self.expression = expression if expression else None

    def set_arity(self, n):
        if n < 0:
            raise ValueError("Arity must be non-negative.")
        self.arity = n

    def set_symbol(self, s: str):
        """
        Set or validate the symbol for the term.

        :param s: Symbol for the term.
        """

        var_pattern = r'^[a-z](_\d*)?$'
        const_pattern = r'^[\u03b1-\u03c9](_\d*)?$'
        func_pattern = r'^[A-z](_\d*)?$'

        if self.arity == 0:
            if bool(re.match(const_pattern, s)) or bool(re.match(var_pattern, s)):
                self.symbol = s
            else:
                raise ValueError("Invalid name for a constant or variable.")
        elif self.arity >= 1:
            if bool(re.match(func_pattern, s)):
                self.symbol = s
            else:
                raise ValueError("Function symbols must be lowercase Latin letters.")

    def set_expression(self, expr):
        """
        Set or update the expression for the term.

        :param expr: The new expression.
        """
        if self.arity == 0:
            raise ValueError("Constants or variables cannot have expressions.")
        self.expression = expr

    def copy(self):
        """
        Create a copy of the current Term object.

        :return: A new Term object with the same attributes.
        """
        return Term(self.arity, str(self.symbol))

    def __repr__(self):
        """
        String representation of the Term object.

        :return: A string describing the term.
        """
        if self.expression:
            return f'{self.symbol}^({self.arity}) = {self.expression}'
        return f'{self.symbol}'


if __name__ == '__main__':

    x_1 = Term('x_1', 0)
    f = Term('f', 3, 'x + y - z')
    print(x_1)
    print(f)

