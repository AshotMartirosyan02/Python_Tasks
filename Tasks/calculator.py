from decimal import Decimal


def add(x, y):
    return int(x + y) if int(x + y) == float(x + y) else Decimal(str(x)) + Decimal(str(y))


def sub(x, y):
    return int(x - y) if int(x - y) == float(x - y) else Decimal(str(x)) - Decimal(str(y))

def mul(x, y):
    return int(x * y) if int(x * y) == float(x * y) else Decimal(str(x)) * Decimal(str(y))

def div(x, y):
    try:
        return int(x / y) if int(x / y) == float(x  / y) else Decimal(str(x)) / Decimal(str(y))
    except ZeroDivisionError as e:
        return  e

def div_floor(x, y):
    try:
        return int(x// y)
    except ZeroDivisionError as e:
        return  e


def enter_num(st):
    while True:
        try:
            num = float(input(st))
            return  num
        except:
            print("You dont enter a number:  ")

def calculator():
    while True:
        print("\nMenu\n")
        print("1. Add")
        print("2. Sub")
        print("3. Multi")
        print("4. Div math")
        print("5. div flore")
        print("0. Exit")

        choice = input('take what you want (0 - 5):   ')
        if choice == "0":
            print("Bye")
            break
        if choice in ('1', '2', '3', '4', '5'):
            num1 = enter_num("Enter the first number: ")
            num2 = enter_num("Enter the second number: ")
            di = {"1": add, "2": sub, "3": mul, "4": div, "5": div_floor}
            res = di[choice](num1, num2)
            print(f"Result:   {res}")
        else:
            print('Please enter a number between 0 and 5.\n')
calculator()