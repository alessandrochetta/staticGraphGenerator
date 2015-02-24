#include <iostream>
#include "C.cpp"

class B {
	public:
		B(){ 
			std::cout<<"I'm B"<<std::endl; 
			C c;
		}
};