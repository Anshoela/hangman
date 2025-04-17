def add ():
    print("Adding your number ")
    n=float(input("Enter your number"))
    b=float(input("Enter your second number"))
    return n+b

def sub():
    print("Subtraction your number")
    n=float(input("Enter your number"))
    b=float(input("Enter your second number "))
    return n-b

def mul():
    print("Multiplying the number ")
    n=float(input("Enter your number "))
    b=float(input("Enter your second number"))
    return n*b

def div():
    print("Dividing the number")
    n=float(input("Enter your number"))
    b=float(input("Enter your second number "))
    if b==0:
        return "Cannot divide with 0"
    return n/b

while True :
    res = []
    print (" the calculator")
    print ("Enter 'a' for Addition")
    print ("Enter 's' for Subtraction")
    print ("Enter 'm' for Multiplication")
    print ("Enter 'd' for Division")
    print ("Enter 'q' for Quit")
    c= input(" ")
    if c!= 'q':
        if c =='a':
            res = add()
            print("Your answer is =",res)
        elif c=='s':
            res= sub()
            print("Your answer is =",res)
        elif c=='m':
            res= mul()
            print("Your answer is =",res)
        elif c=='d':
            res= div()
            print("Your answer is =",res)
    else:
        print(" NEVER GIVE UP NEVER WHATTTTTTTTTTTTTTTTT!?!?!?!?!?!?!?!?! NVMQuitting....")
        break
