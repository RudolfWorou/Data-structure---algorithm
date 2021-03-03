#pragma once
#ifndef DEF_NODE
#define DEF_NODE

class Node {
	int data;
	Node* next;

	public:
		Node(int data);
		~Node();
		void display(std::ostream& flux) const;
		Node* getNext() const;
		int getValue() const;
		void setNext(Node* new_node);
		friend std::ostream& operator<<(std::ostream& stream, Node const& node);
};

#endif // !DEF_NODE



