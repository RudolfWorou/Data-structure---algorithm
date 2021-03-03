#include <iostream>
#include "Node.h"

using namespace std;

Node::Node(int data) : data(data), next(NULL) {}

Node::~Node() {}

void Node::display(ostream& flux) const {
	if (this == nullptr) {
		flux << "<empty Node>" << endl;
	}
	else {
		flux << data;
		Node* current = next;
		while (current != NULL) {
			flux << " -> " << current->data;
			current = current->next;
		}
		flux << endl;
	}
}

Node* Node::getNext() const {
	return next;
}

int Node::getValue() const {
	return data;
}

void Node::setNext(Node* new_node) {
	next = new_node;
}

ostream& operator<<(ostream& flux, Node const& node) {
	node.display(flux);
	return flux;
}