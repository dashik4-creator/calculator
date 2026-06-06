num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

operation = input("Введите операцию (+ - * /): ")

if operation == "+":
    print("Результат:", num1 + num2)

elif operation == "-":
    print("Результат:", num1 - num2)

elif operation == "*":
    print("Результат:", num1 * num2)

elif operation == "/":
    print("Результат:", num1 / num2)

else:
    print("Неизвестная операция")