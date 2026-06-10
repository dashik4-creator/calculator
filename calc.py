from math_functions import add, subtract, multiply, divide, show_menu
continue_work = "Да"
history = []
print(history)
while continue_work == "Да":
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка! Нужно вводить числа.")
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    show_menu ()
    operation = input("Введите операцию: ")
    if operation == "1":
        result = add(num1, num2)
        history.append(f"{num1} + {num2} = {result}")
        print("Результат:", result)
    elif operation == "2":
        result = subtract(num1, num2)
        history.append(f"{num1} - {num2} = {result}")
        print("Результат:", result)
    elif operation == "3":
        result = multiply(num1, num2)
        history.append(f"{num1} * {num2} = {result}")
        print("Результат:", result)
    elif operation == "4":
        if num2 == 0:
            print("Ошибка! На ноль делить нельзя.")
        else:
            result = divide(num1, num2)
            history.append(f"{num1} / {num2} = {result}")
            print("Результат:", result)
    else:
        print("Неизвестная операция")
    continue_work = input("Продолжить работу? Да/Нет:")
    if continue_work == "Нет":
        print("Cпасибо за использование калькулятора!")
        print("История операций:")
        for entry in history:
            print(entry)
    if continue_work != "Да" and continue_work != "Нет":
        print("Ошибка! Нужно вводить 'Да' или 'Нет'.")
        continue_work = input("Продолжить работу? Да/Нет:")
        if continue_work == "Нет":
            print("Cпасибо за использование калькулятора!")