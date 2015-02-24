#include <iostream>
#include "B.cpp"

class A {
  public:
    A() { 
    		std::cout<<"I'm A"<<std::endl;
    		B b;
    	}
};
