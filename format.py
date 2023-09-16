a="ram"
b="kumar"
c="this is {} {}"
d=c.fomrat(b,a)
print(d)




class Emp:
    def __init__(self,name,last):
        self.name=name
        self.last=last
        self.email=name+"-"+last+"@ygmail.com"
        
    def show(self):
        return f"this is {self.name}"
    
obj=Emp("ram","kumar")
print(obj.show())
