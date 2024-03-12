class teacher:
    def __init__(self,nm,reg):
        self.name=nm
        self.regno=reg
    def display(self):
        print("Name:",self.name)
        print("RegNo:",self.regno)
t1=teacher("shabana",87)
t2=teacher("joyce",23)
t1.display()