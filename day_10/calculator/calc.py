# calculator

def calculator():
    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        return n1 / n2

    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }


    num1 = float(input("What's the first number? : "))
    for symbol in operations:
        print(symbol)
    keep_running = True
    while keep_running == True:
        operation = input("What operation do you want to perform? : ")
        if operation in operations:
            num2 = float(input("What's the next number? : "))
            result = operations[operation](num1, num2)
            continue_calc = input(f"type 'y' to continue calculating with {result} or any other key to exit : ")
            print(continue_calc.lower())
            while continue_calc.lower() != 'y' and continue_calc.lower() != 'n':
                continue_calc = input('I did not understand, please enter y or n : ')
            if continue_calc == 'y':
                num1 = result
                operation = input('What operation do you want to perform? : ')
                num2 = float(input("What's the next number? : "))
                result = operations[operation](num1, num2)
                print(f'{num1} {operation} {num2} = {result}')
                continue_calc = input(f"type 'y' to continue calculating with {result} or any other key to exit : ")
                if continue_calc == 'y':
                    keep_running = True
                else:
                    keep_running = False
            elif input("Press 'y' to start a fresh calculation or 'n' to exit: ").lower == 'n':
                keep_running = False
                print(f'{num1} {operation} {num2} = {result}')
        else:
            print('Bye!')
calculator()

