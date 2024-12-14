import sympy


class Term:

    def __init__(self, arity: int, symbol: str, expression=None):
        """
        Initialize a Term object.

        :param arity: Arity of the term (0 for constants/variables, >= 1 for functions).
        :param symbol: Symbol representing the term.
        :param expression: Optional; expression for the term if it represents a function.
        """
        self.set_arity(arity)
        self.set_symbol(symbol)
        self.expression = expression if expression else None

    def set_arity(self, n: int):
        if n < 0:
            raise ValueError("Arity must be non-negative.")
        self.arity = n

    def set_symbol(self, s: str):
        """
        Set or validate the symbol for the term.

        :param s: Symbol for the term.
        """
        if self.arity == 0:
            if len(s) == 1 and s.islower() and s.isalpha():
                # Greek constants (e.g., alpha, beta)
                self.symbol = sympy.Symbol(s)
            elif s[0].isalpha() and s[0].islower():
                # Latin variables (e.g., x, y_1)
                self.symbol = sympy.Symbol(s)
            else:
                raise ValueError("Invalid symbol for a constant or variable.")
        elif self.arity >= 1:
            if s.isalpha() and s.islower():
                self.symbol = sympy.Symbol(s)
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
        return Term(self.arity, str(self.symbol), self.expression)

    def __repr__(self):
        """
        String representation of the Term object.

        :return: A string describing the term.
        """
        if self.expression:
            return f"{self.symbol}^({self.arity}) = {self.expression}"  # f^(n) - означает функцию n переменных
        else:
            return f'{self.symbol}'


def simplify(func):
    """
    Simplify the expression.

    :return: Simplified expression.
    """
    if func.expression is None:
        raise ValueError("No expression to simplify.")
    return sympy.simplify(func.expression)


# Examples to demonstrate functionality
def examples():
    # Example 1: Creating a constant
    pi = Term(0, "π")
    print(f'const example: {pi}')  # Output: π

    # Example 2: Creating a variable
    x = Term(0, "x")
    print(f'var example: {x}')  # Output: x

    # Example 3: Creating a function with an expression
    f = Term(2, "f", expression="x - y")
    print(f'func example: {f}')  # Output: f^(2) = x - y

    # Example 4: Simplifying a function's expression
    f.set_expression("x + y - 2*x")
    print(f'new expression for func {f.symbol}: {f.expression}')
    print(f'simplified func: {simplify(f)}')  # Output: -x + y

    # Example 5: Copying a term
    g = f.copy()
    g.set_symbol('g')
    print(f'new func {g.symbol} copied from {f.symbol}: {g}')  # Output: g^(2) = x + y - 2*x


# Run examples
if __name__ == "__main__":
    examples()
