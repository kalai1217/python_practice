sal=int(input("Enter your salary"))
age=int(input("Enter you age"))
if(sal>20000 or age<25):
    loan=int(input("Enter required loan amount"))
    if(loan<=50000):
        print("eligible for loan")
    else:
        print("maximum amt is 50000 only")
else:
    print("not eligibe")