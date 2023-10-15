import math

def add(a,b):
    answer = a + b
    return answer

def sub(a,b):
    answer = a - b
    return  answer

def mul(a,b):
    answer = a * b
    return  answer

def div(a,b):
    answer = a / b
    return  answer
while True:
    print()
    print()

    a = int(input("Insert the first number : "))
    b = int(input("Insert the second number : "))
    
    print("""_________________ OPTIONS____________________

    Addition      = '+'   |  Quit   ="q"
    substraction  = '-'   |
    multiplicatin = '*'   |
    division      = '/'   |
    _____________________________________________""")
    print()
    options = input("select an option from above :")
    print()

    if options == "+":
        print(f"the sum of : {a} + {b} =",add(a,b))

    elif options == "-":
        print(f"the sum of : {a} + {b} =",sub(a,b))

    elif options == "*":
        print(f"the sum of : {a} + {b} =",mul(a,b))

    elif options == "/":
        print(f"the sum of : {a} + {b} =",div(a,b))
    elif options == "q" or options == "Q":
        print("The session has Ended")
        quit()     

    print()
