import Rational

def main():
    while (True):
        print(
            "\nЭта программа поможет вам вычислить (*, /, -, +) "
            "и вывести стандартную и десятичную дробь из ваших двух чисел \ n")

        num1__numerator = float(input("Числитель num1: "))
        num1__denumerator = float(input("Знаменатель num1: "))
        num2__numerator = float(input("Числитель num2: "))
        num2__denumerator = float(input("Знаменатель num2: "))
        operation = input("Операция (/,*,+,-): ")

        fraction1 = Rational.Rational(num1__numerator, num1__denumerator)
        fraction2 = Rational.Rational(num2__numerator, num2__denumerator)
        res = Rational.Rational.calcFraction(fraction1, operation, fraction2)

        print(f"Вы выбрали операцию < {operation} >.\nРезультат: {res}")
        exitPoint = input("Нажмите Enter чтобы выйти.")
        if len(exitPoint) < 1:
            break


if __name__ == '__main__':
    main()
