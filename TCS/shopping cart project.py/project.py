class Shoppingcart():
    def __init__(self):
        self.cart={}
    def add(self,name,price,units):
        if name in self.cart:
            self.cart[name]['quantity'] += units
        else:
            self.cart[name] = {'price': price, 'quantity': units}
    def delete_item(self,name):
        if name in self.cart:
            del self.cart[name]
            print(f"{name} has been removed from the cart.")
        else:
            print(f"{name} is not in the cart.")
    def update(self,name,units):
        if name in self.cart:
            self.cart[name]['quantity'] = units
            if units == 0:
                self.delete_item(name)
            print(f"Updated {name} to quantity {units}.")
        else:
            print(f"{name} is not in the cart.")
    def calculate(self):
        total = sum(details['price'] * details['quantity'] for details in self.cart.values())
        print(f"Total cost of items in the cart: ${total:.2f}")
    def display(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            for item, details in self.cart.items():
                print(f"Item: {item}, Price: {details['price']}, Quantity: {details['quantity']}")
    
obj=Shoppingcart()
choice=1
while choice!=0:
    print("1.Add Item to Cart\n2.View Cart\n3. Calculate Cart Total\n4. Modify the Item\n5. Delete the Item\n6. Quit")
    choice=int(input('Enter your choice: '))
    if choice==1:
        name=input('enter the item:')
        price=int(input('enter price:'))
        units=int(input('enter number of units:'))
        obj.add(name,price,units)
        obj.display()
    elif choice==2:
        obj.display()
    elif choice==3:
        obj.display()
        obj.calculate()
    elif choice==4:
        name = input("Enter the item name to modify: ")
        quantity = int(input("Enter the new quantity: "))
        obj.update(name, quantity)
        obj.display()
    elif choice==5:
        name = input("Enter the item name to delete: ")
        obj.delete_item(name)
        obj.display()
    elif choice==6:
        obj.display()
        print("Thank you for shopping with us!")
        exit(0)
    else:
        print("Invalid Choice!!!")
print()