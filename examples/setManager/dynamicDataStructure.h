//
//  dynamicDataStructure.h
//  chetta
//
//  Created by Alessandro on 11/30/14.
//  Copyright (c) 2014 Alessandro. All rights reserved.
//
//  Class created to exploit polymorphism in the class Set

#ifndef chetta_dynamicDataStructure_h
#define chetta_dynamicDataStructure_h

class dynamicDataStructure{
public:
    virtual ~dynamicDataStructure(){};
    virtual int size() const = 0;
    virtual dynamicDataStructure& add(int element) = 0;
    virtual int operator[](const int index) const = 0;
    virtual void clear() = 0;
    
    virtual bool contains(int element) const = 0;
};

#endif
