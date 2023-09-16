class Emp(object):
    
    def __init__(self,name,last):
        self.name=name
        self.last=last
    
    
    
class Dev(Emp):
    
    def __init__(self,name,last,ext):
        super().__init__(name,last)
        self.ext=ext
    
obj=Emp("ram","kumar")
obj2=Dev("shyam","ku","fjf")
print(obj2.name)
