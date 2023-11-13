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
