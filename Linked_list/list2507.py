class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def append(self,val):
        if self.head == None:
            self.head=Node(val)
        else:
            cur =self.head
            while(cur.next):
                cur=cur.next
            cur.next=Node(val)
    def display(self):
        if self.head ==None:
            return 
        else:
            cur=self.head
            while(cur):
                print(cur.data,end ="->")
                cur=cur.next
    def insertatindex(self,pos,val):
        newnode=Node(val)
        cur = self.head
        pos=pos-1
        while(pos>0):
            cur = cur.next
            pos-=1
        newnode.next=cur.next
        cur.next=newnode
    def removeatindex(self,pos,val):
        newnode=Node(val)
        cur = self.head
        pos=pos-1
        while(pos>0):
            cur = cur.next
            pos-=1
        cur.next=cur.next.next
    
l=Linkedlist()
l.append(7)
l.append(8)
l.append(2)
l.append(9)
l.display()
print()
l.insertatindex(2,16)
l.display()