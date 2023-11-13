import math

class Calculator:
    def f_add(self, alpha, beta):
        return alpha + beta

    def f_subtract(self, alpha, beta):
        return alpha - beta

    def f_multiply(self, alpha, beta):
        return alpha * beta

    def f_divide(self, alpha, beta):
        if beta != 0:
            return alpha / beta
        else:
            raise ValueError('Cannot divide by zero.')

    def f_square_root(self, alpha):
        if alpha >= 0:
            return math.sqrt(alpha)
        else:
            raise ValueError('Cannot calculate the square root of a negative number.')

# Example usage:
# calc = Calculator()
# result_addition = calc.f_add(10, 5)
# result_subtraction = calc.f_subtract(10, 5)
# result_multiplication = calc.f_multiply(10, 5)
# result_division = calc.f_divide(10, 5)
# result_square_root = calc.f_square_root(25)
