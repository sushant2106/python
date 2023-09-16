class Emp:
    pay=10
    def __init__(self,name,last):
        self.name=name
        self.last=last
        self.email=name+"-"+last+"@ygmail.com"
        
    def show(self):
        return f"this is {self.name}"
    
    def rais(self):
        return self.pay  #Emp.pay
    
obj1=Emp("ram","kumar")
obj2=Emp("shayam","raj")

# obj1.pay=12
Emp.pay=15
print(obj1.rais())
print(obj2.rais())
