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