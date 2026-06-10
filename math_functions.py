def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def show_menu():
    print("1 - Сложение")
    print("2 - Вычитание")
    print("3 - Умножение")
    print("4 - Деление")
def show_history(history):
    print("История операций:")
    for entry in history:
        print(entry)
def show_action_menu():
    print("1 - Продолжить работу")
    print("2 - Показать историю")
    print("3 - Очистить историю")
    print("4 - Выйти")
def calculator(history):
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