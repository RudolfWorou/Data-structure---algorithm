

#include <iostream>
#include "Node.h"
#include "queue.h"

using namespace std;

int main() {
    Node node = Node(5);
    Node node2= Node(2);
    Node* ptr = new Node(10);
    node.setNext(ptr);
    cout << node;

    queue qu = queue();
    cout << qu;
    qu.add(5);
    qu.add(7);
    cout << qu;
    qu.remove();
    cout << qu;

    delete ptr;
    return 0;
}
