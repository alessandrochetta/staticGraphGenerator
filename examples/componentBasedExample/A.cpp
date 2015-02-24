#include <iostream>
#include "B.cpp"

class A {
  public:
    A() { 
    		std::cout<<"I'm A"<<std::endl;
    		B b;
    		U a = b;
    		W *d;
    		Z &d;
    		Y a(b);
    	}
};

//declaration outside of a class scope
Class c;

class U: A{
public:
	W w;
	Z z;
	Y y;
};

class W: A{
public:
	Z z;
	Y y;
};

class Z: U{
public:
	W w;
	U z;
	Y y;
};

class Y: U{
public:
	W w;
	U z;
}