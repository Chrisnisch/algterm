import sympy


class Term:
    def __init__(self, arity: int, symbol: str, expression=None, value=None):
        """
        Initialize a Term object.

        :param arity: Arity of the term (0 for constants/variables, >= 1 for functions).
        :param symbol: Symbol representing the term.
        :param expression: Optional; expression for the term if it represents a function.
        :param value: Optional; numerical value for the term if it is a constant.
        """
        self.set_arity(arity)
        self.set_symbol(symbol)
        self.expression = expression if expression else None
        self.value = value

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

    def set_value(self, v):
        """
        Set or update the value for the term.

        :param v: Numerical value for the constant.
        """
        if self.arity != 0:
            raise ValueError("Only constants can have values.")
        self.value = v

    def copy(self):
        """
        Create a copy of the current Term object.

        :return: A new Term object with the same attributes.
        """
        return Term(self.arity, str(self.symbol), self.expression, self.value)

    def simplify(self):
        """
        Simplify the expression of the term if it is a function.

        :return: Simplified expression.
        """
        if self.expression is None:
            raise ValueError("No expression to simplify.")
        return sympy.simplify(self.expression)

    def __repr__(self):
        """
        String representation of the Term object.

        :return: A string describing the term.
        """
        if self.arity == 0:
            if self.value is not None:
                return f"Constant({self.symbol}, value={self.value})"
            return f"Variable({self.symbol})"
        return f"Function({self.symbol}, arity={self.arity}, expression={self.expression})"


# Examples to demonstrate functionality
def examples():
    # Example 1: Creating a constant
    alpha = Term(0, "π", value=3.14)
    print(alpha)  # Output: Constant(alpha, value=3.14)

    # Example 2: Creating a variable
    x = Term(0, "x")
    print(x)  # Output: Variable(x)

    # Example 3: Creating a function with an expression
    f = Term(2, "f", expression="x - y")
    print(f)  # Output: Function(f, arity=2, expression=x + y)

    # Example 4: Simplifying a function's expression
    f.set_expression("(2*x + x) * y - 1/2*x + 7/2*x")
    print(f.simplify())  # Output: 2*x*y

    # Example 5: Copying a term
    g = f.copy()
    print(g)  # Output: Function(f, arity=2, expression=(x + x) * y)


# Run examples
if __name__ == "__main__":
    examples()
