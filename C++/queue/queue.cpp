#include <iostream>
#include "Node.h"
#include "queue.h"

using namespace std;

queue::queue() : head(NULL), tail(NULL) {}

queue::~queue() {}

void queue::add(int value) {
	Node* ptr = new Node(value);

	if (tail != NULL) {
		tail->setNext(ptr);
		tail = ptr;
	}
	if (head == NULL) {
		head = ptr;
		tail = ptr;
	}
}

void queue::remove() {
	if (head != NULL) {
		if (head->getNext() == NULL)
			tail = NULL;
		head = head->getNext();
	}
}

Node* queue::getHead() const {
	return head;
}

int queue::peak() const {
	if (head != NULL)
		return head->getValue();
	return NULL;
}


void queue::display(std::ostream& flux) const {
	if (head != NULL)
		head->display(flux);
	else
		flux << "<empty queue>" << endl;
}

ostream& operator<<(std::ostream& flux, queue const& qu) {
	qu.display(flux);
	return flux;
}