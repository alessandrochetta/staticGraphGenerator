//
//  Node.cpp
//  chetta
//
//  Created by Alessandro on 11/29/14.
//  Copyright (c) 2014 Alessandro. All rights reserved.
//

#include "Node.h"

Node::Node() : next_(NULL), value_(0){
}

Node::Node(int value) : next_(NULL), value_(value){}

void Node::value(int new_value){
    value_ = new_value;
}

int Node::value(){
    return value_;
}

void Node::next(Node &new_next){
    next_ = &new_next;
}

Node* Node::next(){
    return next_;
}
