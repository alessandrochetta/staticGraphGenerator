//
//  main.cpp
//  chetta
//
//  Created by Alessandro on 11/29/14.
//  Copyright (c) 2014 Alessandro. All rights reserved.
//

#include <iostream>

#include "SetAsList.h"
#include "SetAsOC.h"

void userInterface();
void printSetContent(Set& set);

int main(int argc, const char * argv[]) {

    userInterface();
    
    return 0;
}

void userInterface(){
    //variable in wich the user choice is stored
    char userChoice = ' ';
    Set* a = nullptr;
    Set* b = nullptr;
    //tmp needed to implement the switch functionality
    Set* tmp;
    //elementToAdd needed to implement the add functionality
    int elementToAdd;
    
    std::cout<<"---Set calculator app---"<<std::endl;
    
    do {
        std::cin>>userChoice;
        switch (userChoice) {
            case 'l':
                if (a != nullptr)
                    delete a;
                if (b != nullptr)
                    delete b;
                
                a = new SetAsList;
                b = new SetAsList;
                break;
                
            case 'o':
                if (a != nullptr)
                    delete a;
                if (b != nullptr)
                    delete b;
                
                a = new SetAsOC;
                b = new SetAsOC;
                break;
                
            case 'e':
                //creates a NEW instance from the other set
                //in this way it can always instantiate the right run time type
                delete a;
                a = b->copy();
                //it makes the new set empty
                a->clear();
                break;
                
            case 's':
                tmp = a;
                a = b;
                b = tmp;
                break;
                
            case 'c':
                delete b;
                //virtual copy method
                b = a->copy();
                break;
                
            case 'd':
                std::cout<<"A: ";
                printSetContent(*a);
                std::cout<<"B: ";
                printSetContent(*b);
                break;
                
            case 'a':
                std::cout<<"type the number: ";
                std::cin>>elementToAdd;
                a->add(elementToAdd);
                break;
                
            case 'u':
                a->setUnion(*b);
                break;
                
            case 'i':
                a->setIntersection(*b);
                break;
                
            default:
                break;
                
        }
    }while (userChoice!='q');

    delete a;
    delete b;
    std::cout<<"--------bye--------"<<std::endl;
    
}

void printSetContent(Set& set){
    for(int i=0; i<set.size(); i++)
        std::cout<<set[i]<<" ";
    std::cout<<std::endl;
}