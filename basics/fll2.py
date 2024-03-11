a=[]
sum=0
for i in range(10):
    b=int(input("Enter value"+str(i)))
    a.append(b)
print(a)
for i in a:
    sum=sum+i
print(sum)