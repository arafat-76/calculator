import math
history=[]
while True:
    op=input("choose(add/sub/mul/div/sqrt/power/history/quit):")
    if op=="quit":
        print("Bye!")
        break
    elif op=="sqrt":
        a=int(input("enter number"))
        print("Result:",math.sqrt(a))
    elif op=="power":
        a=int(input("enter number"))
        print("Result:",a**2)
    elif op=="history":
        for h in history:
            print(h)
    else:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        if op=="add":
            print("Result:",a+b)
            history.append(str(a)+"+"+str(b)+"="+str(a+b))
        elif op=="sub":
            print("Result:",a-b)
        elif op=="mul":
            print("Result:",a*b)
        elif op=="div":
            print("Result:",a/b)
        else:
            print("invalid operation")

