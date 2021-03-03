 class Node{
        
        
        public:
        int data;
        static Node next;
        Node(int d=-10){data=d;next=Node();};
        bool isEmpty(){
           return(data==-10);
        }
      };