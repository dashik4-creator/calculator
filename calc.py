continue_work = "Да"
while continue_work == "Да":
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка! Нужно вводить числа.")
        exit()
    operation = input("Введите операцию (+ - * /): ")
    if operation == "+":
     print("Результат:", num1 + num2)
    elif operation == "-":
        print("Результат:", num1 - num2)
    elif operation == "*":
        print("Результат:", num1 * num2)
    elif operation == "/":
        if num2 == 0:
            print("Ошибка! На ноль делить нельзя.")
        else:
            print("Результат:", num1 / num2)
    else:
        print("Неизвестная операция")
    continue_work = input("Продолжить работу? Да/Нет:")