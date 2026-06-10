from math_functions import add, subtract, multiply, divide, show_menu, show_history, show_action_menu
continue_work = "1"
history = []
print(history)
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
while True:
    show_action_menu()
    continue_work = input("Продолжить работу? (1-4): ")
    if continue_work == "2":
        show_history(history)
    if continue_work == "3":
        history.clear ()
        print("История очищена!")
    if continue_work == "4":
        print("Cпасибо за использование калькулятора!")
        show_history(history)
        break
    if continue_work != "1" and continue_work != "2" and continue_work != "3" and continue_work != "4":
        print("Ошибка! Нужно вводить '1', '2', '3' или '4'.")
    
        #continue_work = input("Продолжить работу? (1-4): ")
        
    