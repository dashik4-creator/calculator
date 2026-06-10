from math_functions import add, subtract, multiply, divide, show_menu, show_history, show_action_menu, calculator
continue_work = "1"
history = []
print(history)
calculator(history)
while True:
    show_action_menu()
    continue_work = input("Продолжить работу? (1-4): ")
    if continue_work == 1:
        calculator(history)
    elif continue_work == "2":
        show_history(history)
    elif continue_work == "3":
        history.clear ()
        print("История очищена!")
    elif continue_work == "4":
        print("Cпасибо за использование калькулятора!")
        show_history(history)
        break
    if continue_work != "1" and continue_work != "2" and continue_work != "3" and continue_work != "4":
        print("Ошибка! Нужно вводить '1', '2', '3' или '4'.")
    
        
    