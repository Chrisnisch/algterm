from algtermlib.core import Term, simp

if __name__ == '__main__':
    """ For dev """
    x = Term('x')  # терм-переменная x
    y = Term('y')  # терм-переменная y
    alpha = Term('α')  # терм-константа α
    func_f = Term('f(x, y, α)')  # терм-функция f
    expr = alpha * (x + y) + (x + alpha * y) ** 2
    func_f.set_expression(expr)

    print(expr)

    expr1 = alpha * (x + y) + (x + alpha * y) ** 2
    expr2 = (x ** 2 + x * 2 * y + y ** 2) / (x + y)

    print(f'изначальное: {expr1}\nупрощенное: {simp(expr1)}\n')
    print(f'изначальное: {expr2}\nупрощенное: {simp(expr2)}\n')
