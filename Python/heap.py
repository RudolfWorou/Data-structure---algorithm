class Minheap:
    def __init__(self,items,capacity=10,size=0):
        self.capacity=capacity
        self.size=size
        self.items=items

    # Obtaining the indexes of the childs and the parents
    def getLeftChildIndex(self,parentIndex): return 2*parentIndex+1
    def getRightChildIndex(self,parentIndex): return 2*parentIndex+2
    def getParentIndex(self,childIndex): return (childIndex-1)/2

    # Check if a node has a left child, a right child and a parent
    def hasLeftChild(self,index): return self.getLeftChildIndex(index)<self.size
    def hasRightChild(self,index): return self.getRightChildIndex(index)<self.size
    def hasParent(self,index): return self.getParentIndex(index)>=0

    # getting the value of the left child, the right child and the parent
    def leftChild(self,index): return self.items[self.getLeftChildIndex(index)]
    def rightChild(self,index): return self.items[self.getRightChildIndex(index)]
    def parent(self,index): return self.items[self.getParentIndex(index)]

    # swapping between two indices 
    def swap(self,firstIndex,secondIndex):
        self.items[firstIndex],self.items[secondIndex]=self.items[secondIndex],self.items[firstIndex]
    
    # adding more capacity if needed
    def ensureExtraCapacity(self):
        if(self.size==self.capacity):
            self.items+=[None for i in range(self.capacity)]
            self.capacity*=2
    
    # the root of the tree
    def peek(self):
        if(self.size==0): raise ValueError("The heap is empty")
        return self.items[0]
    
    #
    def poll(self):
        if(self.size==0): raise ValueError("The heap is empty")
        item=self.items[0]
        self.items[0]=self.items[size-1]
        self.size-=1
        self.heapifyDown()
        return item
    def add(self, item):
        self.ensureExtraCapacity()
        self.items[self.size]=item
        self.size+=1
        self.heapifyUp()
    def heapifyUp(self):
        index=self.size-1
        while self.hasParent(index) and self.parent(index)>self.items(index):
            self.swap(self.getParentIndex(index),index)
            index=self.getParentIndex(index)
    def heapifyDown(self):
        index=0
        while self.hasLeftChild:
            smallerChildIndex=self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.rightChild(index)<self.leftChild(index):
                smallerChildIndex=self.getRightChildIndex(index)
            if self.items[index]<self.items[smallerChildIndex]:
                break
            else:
                self.swap(index,smallerChildIndex)
            index=smallerChildIndex


def main():

    L=Minheap(items=[7,5,4,3,9])
    L.add(10)
    L.add(15)
    L.add(20)
    L.add(17)
    L.add(25)

if __name__=="__main__":
    main()