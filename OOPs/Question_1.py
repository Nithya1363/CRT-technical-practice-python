class Rectangle():
    #attr
    def __init__(self,l,b):
        self.b=b
        self.l=l
    #method
    def area(self):
        return self.b*self.l
a=int(input("Length:"))
b=int(input("Breadth:"))
obj=Rectangle(a,b)
print(obj.area())