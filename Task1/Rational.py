class Rational(object):
    def __init__(self, numerator=1, denominator=1):
        self.__numerator = numerator
        self.__denominator = denominator

    # set header fraction
    def numerator(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Error: value is incorrect')
        self.__numerator = value

    # set footer fraction
    def denominator(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Error: value is incorrect')
        self.denominator = value

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    #  addition '+'
    def __add__(self, other):
        return Rational(self.__numerator + other.__numerator, self.__denominator + other.__denominator)

    # multiply '*'
    def __mul__(self, other):
        return Rational(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    # subtraction '-'
    def __sub__(self, other):
        return Rational(self.__numerator - other.__numerator, self.__denominator - other.__denominator)

    # division math '/'
    def __truediv__(self, other):
        return Rational(self.__numerator / other.__numerator, self.__denominator / other.__denominator)

    def calcFraction(*args):
        try:
            return eval(''.join(map(str, args)))
        except TypeError:
            return None
