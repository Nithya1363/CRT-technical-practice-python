class stack:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def traverse(self):
        print("Index\tValues")
        for i,v in enumerate(self.items):
            print(f"{i}\t{v}")
    def push(self,a):
        self.items.append(a)
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[-1]
s=stack()
while True:
    print("Stack Operations\n1. Push (Insert Element)\n2. Pop (Delete Element)\n3. Traverse (View Elements)\n4. Peek (Viewing the First Element)\n5. Size (Number of Elements)\n6. Quit")
    choice=int(input('enter your choice: '))
