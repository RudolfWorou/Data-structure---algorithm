class Node:
    def __init__(self,data=None,next=None):
            self.data=data
            self.next=next

class linkedList:
    def __init__(self,head=None):
        self.head=head
    def append(self,data):
        if self.head==None:  # check if there is a head or not
            self.head=Node(data)
        else:
            current=self.head
            while(current.next!=None):
                current=current.next
            current.next=Node(data)
    def prepend(self,data):
        node=Node(data)
        if(self.head!=None):
            node.next=self.head
        self.head=node
    def deleteWithValue(self,data):
        if self.head==None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        current=self.head
        while current.next!=None:
            if(current.next.data==data):
                current.next=current.next.next
                return
            current=current.next
    def __repr__(self):  # printing as a list
        if self.head==None:
            return []
        else:
            current=self.head
            M=[current.data]
            while current.next!=None:
                M.append(current.next.data)
                current=current.next
            return M



def main():
    L=linkedList()
    print(L.__repr__())
    for i in range(10):
        L.append(i)
    print(L.__repr__())
    L.deleteWithValue(5)
    print(L.__repr__())
    L.prepend(11)
    print(L.__repr__())
    
if __name__ =="__main__":
    main()