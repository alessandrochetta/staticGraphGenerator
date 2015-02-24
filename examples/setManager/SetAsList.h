//
//  SetAsList.h
//  chetta
//
//  Created by Alessandro on 11/30/14.
//  Copyright (c) 2014 Alessandro. All rights reserved.
//

#ifndef chetta_SetAsList_h
#define chetta_SetAsList_h
#include "Set.h"
class SetAsList : public Set{
public:
    SetAsList();
    SetAsList(const SetAsList& set);
    virtual ~SetAsList();
    virtual SetAsList& add(int element);
    virtual int operator[](const int index) const;
    virtual int size() const;
    virtual void clear();
    //virtual copy method
    virtual SetAsList* copy();
    };

#endif
