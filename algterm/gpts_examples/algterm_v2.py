def is_nullary(token: str):
    """
    Determine if a token is a nullary term (constant or variable).

    :param token: The token to check.
    :return: True if the token is a nullary term, False otherwise.
    """
    import re
    return re.match(r"^[a-zA-Z_][a-zA-Z_0-9]*$", token) is not None


def tokenize_expression(expr: str):
    """
    Tokenize the expression into a list of terms and operators.

    :param expr: The expression to tokenize (as a string).
    :return: List of tokens (terms and operators).
    """
    import re
    # Match variables, constants, and operators (+, -, *, /, ^, etc.)
    token_pattern = r"[a-zA-Z_][a-zA-Z_0-9]*|[+\-*/^()]|\d+(?:\.\d+)?"
    return re.findall(token_pattern, expr)


class Term:
    def __init__(self, arity: int, symbol: str, expression=None, value=None):
        """
        Initialize a Term object.

        :param arity: Arity of the term (0 for constants/variables, >= 1 for functions).
        :param symbol: Symbol representing the term (as a string).
        :param expression: Optional; expression for the term if it represents a function (as a string).
        :param value: Optional; numerical value for the term if it is a constant.
        """
        self.set_arity(arity)
        self.symbol = symbol
        self.expression = expression
        self.value = value if arity == 0 else None
        self.nullary_terms = []  # List to store nullary terms (constants/variables) extracted from expression

        if self.expression:
            self.parse_expression()

    def set_arity(self, n: int):
        if n < 0:
            raise ValueError("Arity must be non-negative.")
        self.arity = n

    def set_expression(self, expr: str):
        """
        Set or update the expression for the term.

        :param expr: The new expression (as a string).
        """
        if self.arity == 0:
            raise ValueError("Constants or variables cannot have expressions.")
        self.expression = expr
        self.parse_expression()

    def parse_expression(self):
        """
        Parse the expression to extract nullary terms and identify its structure.
        """
        if not self.expression:
            raise ValueError("Expression is empty.")

        tokens = tokenize_expression(self.expression)
        self.nullary_terms = [token for token in tokens if is_nullary(token)]

    def __repr__(self):
        """
        String representation of the Term object.

        :return: A string describing the term.
        """
        if self.expression:
            return f"{self.symbol}^({self.arity}) = {self.expression}"
        else:
            return f"{self.symbol}"


# Examples to demonstrate functionality
def examples():
    # Example 1: Creating a constant
    alpha = Term(0, "alpha", value=3.14)
    print(alpha)  # Output: alpha

    # Example 2: Creating a variable
    x = Term(0, "x")
    print(x)  # Output: x

    # Example 3: Creating a function with an expression
    f = Term(2, "f", expression="x + y - 2*y")
    print(f)  # Output: f^(2) = x + y - 2*y


# Run examples
if __name__ == "__main__":
    examples()
