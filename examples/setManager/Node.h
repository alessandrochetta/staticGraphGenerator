//
//  Node.h
//  chetta
//
//  Created by Alessandro on 11/29/14.
//  Copyright (c) 2014 Alessandro. All rights reserved.
//

#ifndef chetta_Node_h
#define chetta_Node_h
#include <stdio.h>
class Node{
public:
    Node();
    Node(int value);
    int value();
    void value(int new_value);
    Node* next();
    void next(Node& new_next);
    
private:
    int value_;
    Node* next_;
};

#endif
