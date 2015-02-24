//
//  OrderedCollection.cpp
//  chetta
//
//  Created by Alessandro on 11/30/14.
//  Copyright (c) 2014 Alessandro. All rights reserved.
//

#include "OrderedCollection.h"

OrderedCollection::OrderedCollection(){
    collection_= new int[INITIAL_SIZE];
    size_=0;
    space_=INITIAL_SIZE;
}

OrderedCollection& OrderedCollection::add(int element){
    collection_[size_] = element;
    size_++;
    //check wether the array is full
    if(size_==space_)
        this->grow();
    return *this;
}

int OrderedCollection::operator[](const int index) const{
    return collection_[index];
}

int OrderedCollection::size() const{
    return size_;
}

void OrderedCollection::clear(){
    delete [] collection_;
    collection_ = new int[INITIAL_SIZE];
    size_ = 0;
    space_ = INITIAL_SIZE;
}

OrderedCollection::~OrderedCollection(){
    delete [] collection_;
}

bool OrderedCollection::contains(int element) const{
    for (int i=0; i<size_; i++)
        if(collection_[i]==element)
            return true;
    
    return false;
}

void OrderedCollection::grow(){
    //add 5 more positions in the array
    space_=space_+5;
    int* tmp = new int[space_];
    //copy the elements stored in the array into the new array
    for(int i=0; i<size_; i++)
        tmp[i]=collection_[i];
    //delete the old array
    delete [] collection_;
    //bind the new array to the class member identifier
    collection_=tmp;
}
