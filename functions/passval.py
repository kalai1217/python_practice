user="mj"
passw="12"
uname=input()
upass=input()
def validate():
    if(uname==user and passw==upass):
        return("valid")
    else:
        return("invalid")
b=validate()
print(b)