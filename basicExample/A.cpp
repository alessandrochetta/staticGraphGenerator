#include <iostream>
#include "B.cpp"

// questo e un commento
/*
dichiarazione
comm comm;
*/

class A {
  public:
    A() { 
    		std::cout<<"I'm A"<<std::endl;
    		B b;
    		const C c;
    		A x, y, z;	//todo
    		A * b;
    		A & c;
    		A a = P();
    		P * p = new Classe();
    		Point * const p;
    		const Point * const pconst;
    		 Point & const p;
           const Point & const p;
           Point P();
    	}
};

LinkedList::LinkedList() : head_(NULL), size_(0){}

dynamicDataStructure& LinkedList::add(int element)
{
    Node* new_node = new Node(element);
    if(head_ == NULL)
    {
        head_ = new_node;
        size_++;
        return *this;
    }

    Node* currentNode = head_;
    for(;currentNode->next()!=NULL; currentNode=currentNode->next())
        ;
    currentNode->next(*new_node);

    size_++;

    return *this;
}

int LinkedList::operator[](const int index) const{
    Node* currentNode = head_;
    for(int count=0;currentNode!=NULL; currentNode=currentNode->next(), count++)
        if(count == index)
            return currentNode->value();
    return 0;
}

class subclass : public A
{
    dentro d;
    int x;
};