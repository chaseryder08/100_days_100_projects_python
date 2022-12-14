from 
#calculator

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

def calculator():

    num1 = float(input("Enter number: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        
        operator_sym = (input("Enter operator: "))
        num2 = float(input("Enter number: "))
        calc_function = operations[operator_sym]
        answer = calc_function(num1, num2)

        print(f"{num1} {operator_sym} {num2} = {answer}")

        next_step = input(f"Type 'y' to continue calculating with {answer}, type 's' to start fresh, or type 'n' to exit: ")
        
        if next_step == 'y':            
            num1 = answer
        elif next_step == 's':
            calculator()
        else:
            should_continue = False

calculator()