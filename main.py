import math

while True:
    txt = input(
        "Выберите действие:  \n 1 - сложение \n 2 - вычитание \n 3 - умножение \n 4 - деление \n 5 - возведение в степень \n 6 - квадратный   корень \n 7 - факториал \n 8 - sin \n 9 - cos \n 10 - tan \n 0 - Turn off \n");
    if not txt in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '0']:
        print("Ошибка");
        continue
    if txt == '1':
        try:
            znachenie1 = float(input("Введите первое число:"))
            znachenie2 = float(input("Введите второе число:"))
        except ValueError:
            print("Ошибка")
            continue
        print("Ответ:", znachenie1 + znachenie2);
    if txt == '2':
        try:
            znachenie1 = float(input("Введите первое число:"))
            znachenie2 = float(input("Введите второе число:"))
        except ValueError:
            print("Ошибка")
            continue
        print("Ответ:", znachenie1 - znachenie2);
    if txt == '3':
        try:
            znachenie1 = float(input("Введите первое число:"))
            znachenie2 = float(input("Введите второе число:"))
        except ValueError:
            print("Ошибка")
            continue
        print("Ответ:", znachenie1 * znachenie2);
    if txt == '4':
        try:
            znachenie1 = float(input("Введите первое число:"))
            znachenie2 = float(input("Введите второе число:"))
        except ValueError:
            print("Ошибка")
            continue
        if znachenie2 == 0:
            print("Делить на ноль нельзя!!!")
        else:
            print("Ответ:", znachenie1 / znachenie2);
    if txt == "5":
        try:
            znachenie1 = float(input("Введите первое число:"))
            znachenie2 = float(input("Введите второе число:"))
        except ValueError:
            print("Ошибка")
            continue
        print("Ответ:", znachenie1 ** znachenie2);
    if txt == "6":
        try:
            znachenie1 = float(input("Введите число:"))
        except ValueError:
            print("Ошибка")
            continue
        if znachenie1 < 0:
           print("Корень меньше нуля быть не может :)")
        else:
           print("Ответ:", (znachenie1 ** 0.5));
    if txt == "7":
        try:
            znachenie1 = int(input("Введите число:"))
        except ValueError:
            print("Ошибка")
            continue
        if znachenie1 < 0:
            print("Факториал тоже должен быть больше нуля :_)")
        else:
            print("Ответ:", math.factorial(znachenie1));
    if txt == "8":
        try:
            znachenie1 = float(input("Введите число:"))
        except ValueError:
            print("Ошибка")
            continue
        print("Ответ:", math.sin(znachenie1));
    if txt == "9":
        try:
            znachenie1 = float(input("Введите число:"))
        except ValueError:
            print("Ошибка")
            continue
        print("Ответ:", math.cos(znachenie1));
    if txt == "10":
        try:
            znachenie1 = float(input("Введите число:"))
        except ValueError:
            print("Ошибка")
            continue
        print("Ответ:", math.tan(znachenie1));
    if txt == "0":
        break
