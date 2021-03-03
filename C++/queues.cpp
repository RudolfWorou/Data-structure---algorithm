#include <iostream>
#include <vector>
#include "Node.h"
using namespace std;




class Queue{ 
    public:
   
    Node head=Node();
    Node tail=Node();
    Queue(void);
        int peak(){
            return head.data;
        }
        void add (int data){
            Node node=Node(data);
            if (!tail.isEmpty()){
                tail.next=node;
            }
            tail=node;

            if (head.isEmpty()){
                head=node;
            }

        }
        int remove(){
            int data=head.data;
            head=head.next;
            if(head.isEmpty()){
                tail=Node();
            }
            return data;
        }

    };



int main(){
   
    Queue queue=Queue();
    queue.add(5);
    queue.add(2);
    queue.remove();
    cout << queue.peak();

}