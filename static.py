class Emp:
    pay=10
    def __init__(self,name,last):
        self.name=name
        self.last=last
        self.email=name+"-"+last+"@ygmail.com"
        
    @staticmethod
    def add(a,b):
        return a+b

    

print(Emp.add(20,30))
