//
//  SetAsList.cpp
//  chetta
//
//  Created by Alessandro on 11/30/14.
//  Copyright (c) 2014 Alessandro. All rights reserved.
//

#include "SetAsList.h"
#include "LinkedList.h"

SetAsList::SetAsList(){
    set_ = new LinkedList;
}

SetAsList::SetAsList(const SetAsList& set){
    set_ = new LinkedList;
    for(int i=0; i<set.size(); i++)
        set_->add(set[i]);
}

SetAsList& SetAsList::add(int element){
    if(!set_->contains(element))
        set_->add(element);
    return *this;
}

int SetAsList::operator[](const int index) const{
    return (*set_)[index];
}

int SetAsList::size() const{
    return set_->size();
}

void SetAsList::clear(){
    set_->clear();
}

SetAsList::~SetAsList(){
    delete set_;

}

SetAsList* SetAsList::copy(){
    SetAsList* tmp = new SetAsList(*this);
    return tmp;
}
