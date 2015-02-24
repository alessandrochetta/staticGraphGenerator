//
//  Set.h
//  chetta
//
//  Created by Alessandro on 11/30/14.
//  Copyright (c) 2014 Alessandro. All rights reserved.
//

#ifndef chetta_Set_h
#define chetta_Set_h
#include "dynamicDataStructure.h"
class Set{
public:
    virtual ~Set(){};
    virtual Set& add(int element) = 0;
    virtual int operator[](const int index) const = 0;
    virtual int size() const = 0;
    virtual void clear() = 0;
    Set& setUnion(const Set& set);
    Set& setIntersection(const Set& set);
    bool contains(int element) const;
    //method for the virtual copy constructor
    virtual Set* copy() = 0;
    
protected:
    dynamicDataStructure* set_;
};

#endif
