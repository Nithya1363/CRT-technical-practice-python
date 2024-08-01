class Check():
    def __init__(self):
        self.n=[]
    def add(self,a):
        return self.n.append(a)
    def remove(self,b):
        return self.n.remove(b)
    def display(self):
        return (self.n)
    
obj=Check()
choice=1
while choice != 0:
    print("0.exit\n1.add\n2.remove\n3.display")
    choice = int(input())
    if choice==1:
        n=int(input('Enter numbers: '))
        obj.add(n)
        print(f"list: {obj.display()}")
    elif choice == 2:
        n=int(input('Enter number you want to remove : '))
        obj.remove(n)
        print(f"list: {obj.display()}")
    elif choice == 3:
        print(f"list: {obj.display()}")
    elif choice == 0:
        print("Exit")
    else:
        print("INVALID INPUT")
print()