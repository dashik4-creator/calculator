from math_functions import add, subtract, multiply, divide
continue_work = "Да"
while continue_work == "Да":
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка! Нужно вводить числа.")
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    operation = input("Введите операцию (+ - * /): ")
    if operation == "+":
        result = add(num1, num2)
        print("Результат:", result)
    elif operation == "-":
        result = subtract(num1, num2)
        print("Результат:", result)
    elif operation == "*":
        result = multiply(num1, num2)
        print("Результат:", result)
    elif operation == "/":
        if num2 == 0:
            print("Ошибка! На ноль делить нельзя.")
        else:
            result = divide(num1, num2)
            print("Результат:", result)
    else:
        print("Неизвестная операция")
    continue_work = input("Продолжить работу? Да/Нет:")
    if continue_work == "Нет":
        print("Cпасибо за использование калькулятора!")
    if continue_work != "Да" and continue_work != "Нет":
        print("Ошибка! Нужно вводить 'Да' или 'Нет'.")
        continue_work = input("Продолжить работу? Да/Нет:")
        if continue_work == "Нет":
            print("Cпасибо за использование калькулятора!")