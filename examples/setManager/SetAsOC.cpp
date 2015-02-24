//
//  SetAsOC.cpp
//  chetta
//
//  Created by Alessandro on 11/30/14.
//  Copyright (c) 2014 Alessandro. All rights reserved.
//

#include "SetAsOC.h"

SetAsOC::SetAsOC(){
    set_ = new OrderedCollection;
}

SetAsOC::SetAsOC(const SetAsOC& set){
    set_ = new OrderedCollection;
    for(int i=0; i<set.size(); i++)
        set_->add(set[i]);
}

SetAsOC* SetAsOC::copy(){
    SetAsOC* tmp = new SetAsOC(*this);
    return tmp;
}

SetAsOC& SetAsOC::add(int element){
    if(!set_->contains(element))
        set_->add(element);
    return *this;
}

int SetAsOC::operator[](const int index) const{
    return (*set_)[index];
}

int SetAsOC::size() const{
    return set_->size();
}

void SetAsOC::clear(){
    set_->clear();
}


SetAsOC::~SetAsOC(){
    delete set_;
}