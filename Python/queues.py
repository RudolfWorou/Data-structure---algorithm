
class Node:
    def __init__(self,data=None,next=None):
            self.data=data
            self.next=next

class queue:
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail
    def isEmpty(self):
        return self.head==None
    def peak(self):
        return self.head.data

    def add(self,data):
        node=Node(data=data)
        if self.tail!=None:
            self.tail.next=node
        self.tail=node
        if self.head==None:
            self.head=node
    def remove(self):
        data=self.head.data
        self.head=self.head.next
        if(self.head==None):
            self.tail=None
        return data

def main():
    new_queue=queue()
    new_queue.add(5)
    new_queue.add(2)
    print(new_queue.remove())
    print("The new head is {}".format( new_queue.peak()))

if __name__ == "__main__":
    main()