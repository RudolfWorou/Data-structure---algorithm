class binaryTree:
    def __init__(self,data=None,left=None,right=None):
            self.data=data
            self.left=left
            self.right=right
    def insert(self,value):
        if self.data==None:
            self.data=value
        else:
            if value<=self.data:
                if self.left==None:
                    self.left=binaryTree(value)
                else:
                    self.left.insert(value)
            else:
                if self.right==None:
                    self.right=binaryTree(value)
                else:
                    self.right.insert(value)
    def contains(self,value):
        if value==self.data:
            return True
        elif value <self.data:
            if self.left==None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right==None:
                return False
            else:
                return self.right.contains(value)

    def printInorder(self):
        if(self.left!=None):
            self.left.printInorder()
        print(self.data,end=" ")
        if(self.right!=None):
            self.right.printInorder()
        
    

def main():
    L=binaryTree()
    L.printInorder()
    print("")
    for j in range(10):
        L.insert(j)
        L.printInorder()
        print("")
    print("Does the tree contains -1 ",L.contains(-1))
    print("Does the tree contains 5 ",L.contains(5))
    L.printInorder()

if __name__=="__main__":
    main()


        