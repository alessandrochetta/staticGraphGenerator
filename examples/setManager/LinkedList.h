//
//  LinkedList.h
//  chetta
//
//  Created by Alessandro on 11/29/14.
//  Copyright (c) 2014 Alessandro. All rights reserved.
//

#ifndef chetta_LinkedList_h
#define chetta_LinkedList_h
#include "Node.h"
#include "dynamicDataStructure.h"

class LinkedList : public dynamicDataStructure{
public:
    LinkedList();
    virtual ~LinkedList();
    virtual int size() const;
    virtual dynamicDataStructure& add(int element);
    virtual int operator[](const int index) const;
    virtual void clear();
    
    virtual bool contains(int element) const;
private:
    Node* head_;
    int size_;
    void deleteNode(Node* n);
};

#endif
