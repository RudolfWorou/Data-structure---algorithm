#pragma once
#ifndef DEF_QUEUE
#define DEF_QUEUE
#include "Node.h"

class queue {
	Node* head;
	Node* tail;

	public:
		queue();
		~queue();
		void add(int value);
		Node* getHead() const;
		void remove();
		int peak() const;
		void display(std::ostream& flux) const;
		friend std::ostream& operator<<(std::ostream& flux, queue const& qu);
};




#endif // !DEF_QUEUE

