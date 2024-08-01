#Creating node
class Node():
    def __init__(self,data=None):
        self.data=data
        self.next=None
class Singlelinkedlist():
    def __init__(self):
        #creating empty list
        self.head=None
        self.tail=None
        self.count=0
    def iterate_item(self):
        #joining links
        current_item=self.tail
        while current_item:
            val=current_item.data
            current_item=current_item.next
            yield val
    def append_item(self,data):
        #adding elements to linked list
        node = Node(data)
        if self.head:
            self.head.next=node
            self.head=node
        else:
            self.tail=node
            self.head=node
        self.count+=1

items = Singlelinkedlist()
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')

for val in items.iterate_item():
    print(val)