class mob:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("brand",self.brand)
        print("price",self.price)
p1=mob("sam","12k")
p1.display()
