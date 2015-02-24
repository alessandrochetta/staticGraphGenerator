#include <iostream>
#include "C.cpp"

class B {
	public:
		B(){ 
			std::cout<<"I'm B"<<std::endl; 
			C c;
			G g;
			H h;
			J j;
		}
};

class G{
public:
	H h;
	J j;
};

class H{
public:
	G h;
	J j;
};

class J{
public:
	H h;
	G j;
};