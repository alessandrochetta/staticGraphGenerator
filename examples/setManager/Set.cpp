//
//  Set.cpp
//  chetta
//
//  Created by Alessandro on 11/30/14.
//  Copyright (c) 2014 Alessandro. All rights reserved.
//

#include "Set.h"
#include "SetAsOC.h"

Set& Set::setUnion(const Set &set){
    for(int i=0; i<set.size(); i++)
        if (!set_->contains(set[i]))
            set_->add(set[i]);
    return *this;
}

Set& Set::setIntersection(const Set &set){
    //set in wich it stores the common elements between sets
    SetAsOC tmp;
    //finds common elements
    for(int i=0; i<set.size(); i++)
        if(set_->contains(set[i]))
            tmp.add(set[i]);
    //makes the set empty
    set_->clear();
    //adds to the set all the common elements found
    for(int i=0; i<tmp.size(); i++)
        set_->add(tmp[i]);
    return *this;
}

bool Set::contains(int element) const{
    return set_->contains(element);
}