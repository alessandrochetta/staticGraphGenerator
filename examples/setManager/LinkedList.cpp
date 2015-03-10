//
//  LinkedList.cpp
//  chetta
//
//  Created by Alessandro on 11/29/14.
//  Copyright (c) 2014 Alessandro. All rights reserved.
//

#include "LinkedList.h"


LinkedList::LinkedList() : head_(NULL), size_(0){}

int LinkedList::size() const{
    return size_;
}

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

/*not necessary anymore - used for testing
dynamicDataStructure& LinkedList::remove(int element){
    if(head_==nullptr)
        return *this;
        
    if(head_->value()==element)
    {
        delete head_;
        head_=head_->next();
        size_--;
        return *this;
    }
    
    Node* currentNode = head_;
    Node* previousNode = currentNode;
    
    for(;currentNode!=nullptr;previousNode=currentNode, currentNode=currentNode->next())
        if(currentNode->value()==element)
        {
            previousNode->next(*currentNode->next());
            delete currentNode;
            size_--;
        }
    return *this;
}*/

void LinkedList::clear(){
    if(head_==NULL)
        return;
    deleteNode(head_);
    size_ = 0;
    head_ = NULL;
}

void LinkedList::deleteNode(Node* n){
    if(n->next()!=NULL)
        this->deleteNode((n->next()));

    delete n;
}

int LinkedList::operator[](const int index) const{
    Node* currentNode = head_;
    for(int count=0;currentNode!=NULL; currentNode=currentNode->next(), count++)
        if(count == index)
            return currentNode->value();
    return 0;
}

bool LinkedList::contains(int element) const{
    Node* currentNode = head_;
    for(;currentNode!=NULL; currentNode=currentNode->next())
        if(currentNode->value() == element)
            return true;
    return false;

}

LinkedList::~LinkedList(){
    clear();
}

