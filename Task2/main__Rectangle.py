import Rectangle

engineProgramLoop = True
while engineProgramLoop:
    while True:
        print("\nЭта программа поможет найти вам периметр и квадрат,прямоугольника")

        height = float(input("Введите высоту вашего прямоугольника, пожалуйста: "))
        width = float(input("Введите ширину вашего прямоугольника, пожалуйста: "))
        userChoose = int(input("\nВведите 1, если вам нужен квадрат\nВведите 2, если вам нужен периметр "
                                  "\nВведите 3, если вам нужны квадрат и периметр: "))
        rectangleUser = Rectangle.Rectangle(height, width)

        rectangleUser.outputRectangle(rectangleUser.findPerimeter(), rectangleUser.findSquare(), userChoose)

        exitUser = (input("\nЕсли вы хотите выйти из программы, введите q: "))
        if (exitUser == 'q'):
            engineProgramLoop = False;
            break;



