
class Node:
    def __init__(self,data=None,next=None):
            self.data=data
            self.next=next

class stack:

    

    def __init__(self,top=None):
        self.top=top
    def peak(self):
        return self.top.data
    def isEmpty(self):
        return self.top==None
    def push(self,data):
        node=Node(data=data)
        if self.top!=None:
            node.next=self.top
        self.top=node
        
    def pop(self):
        if(self.top!=None):
            data=self.top.data
            if(self.top.next!=None):
                self.top=self.top.next
            else:
                self.top=None
            return data
        return None
            
        

def main():
    new_stack=stack()
    new_stack.push(5)
    new_stack.push(2)
    print(new_stack.pop())
    print("The new head is {}".format( new_stack.peak()))

if __name__ == "__main__":
    main()