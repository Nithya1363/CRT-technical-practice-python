class Order():
    def __init__(self):
        self.n=[]
    def add(self,a):
        return self.n.append(a)
    def remove(self,b):
        return self.n.remove(b)
    def display(self):
        return (self.n)
    
obj=Order()
choice=1
while choice != 0:
    print("0.No Money\n1.idli\n2.bondas\n3.dosa\n4.puri\n5.Washroom\n6.In the potta")
    choice = int(input())
    if choice==1:
        n=int(input('Enter number of Idlis: '))
        obj.add(n)
        print(f"list: {obj.display()}")
    elif choice == 2:
        n=int(input('Enter number of Bondas : '))
        obj.add(n)
        print(f"list: {obj.display()}")
    elif choice == 3:
        n=int(input('Enter number of Dosas : '))
        obj.add(n)
        print(f"list: {obj.display()}")
    elif choice == 4:
        n=int(input('Enter number of Puris : '))
        obj.add(n)
        print(f"list: {obj.display()}")
    elif choice==5:
        n=int(input("Enter what you want to send out:"))
        obj.remove(n)
        print(f"list: {obj.display()}")
    elif choice==6:
        print(f"in the potta: {obj.display()}")
    elif choice==0:
        print("I will accept pindi medhipify")
    else:
        print("Bayatiki poraa yedhava......!!!")
print()