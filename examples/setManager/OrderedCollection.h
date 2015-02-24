//
//  OrderedCollection.h
//  chetta
//
//  Created by Alessandro on 11/30/14.
//  Copyright (c) 2014 Alessandro. All rights reserved.
//

#ifndef chetta_OrderedCollection_h
#define chetta_OrderedCollection_h
#include "dynamicDataStructure.h"
#define INITIAL_SIZE 10

class OrderedCollection : public dynamicDataStructure{
public:
    OrderedCollection();
    virtual ~OrderedCollection();
    virtual int size() const;
    virtual OrderedCollection& add(int element);
    virtual int operator[](const int index) const;
    virtual void clear();
    
    virtual bool contains(int element) const;
    
private:
    int* collection_;
    int size_;
    int space_;
    void grow();
};

#endif
