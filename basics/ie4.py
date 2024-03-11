score=int(input("Enter a score"))
if(score<=35):
    print("poor")
elif(score>35 and score<=75):
    print("average")
elif(score>75 and score<100):
    print("good")
else:
    print("out of range")