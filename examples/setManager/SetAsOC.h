//
//  SetAsOC.h
//  chetta
//
//  Created by Alessandro on 11/30/14.
//  Copyright (c) 2014 Alessandro. All rights reserved.
//

#ifndef chetta_SetAsOC_h
#define chetta_SetAsOC_h
#include "Set.h"
#include "OrderedCollection.h"
class SetAsOC : public Set{
public:
    SetAsOC();
    SetAsOC(const SetAsOC& set);
    virtual ~SetAsOC();
    virtual SetAsOC& add(int element);
    virtual int operator[](const int index) const;
    virtual int size() const;
    virtual void clear();
    //virtual copy method
    virtual SetAsOC* copy();
};

#endif
