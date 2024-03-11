a=int(input("Enter a number"))
b=int(input("Enter a number"))
op=input("add/sub/mul/div")
if(op=="add"):
    print(a+b)
elif(op=="sub"):
    print(a-b)
elif(op=="mul"):
    print(a*b)
elif(op=="div"):
    print(a/b)
else:
    print("Invalid operator")
