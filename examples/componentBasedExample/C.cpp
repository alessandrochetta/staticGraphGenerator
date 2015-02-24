#include <iostream>

class C {
	public:
		C(){ std::cout<<"I'm C"<<std::endl; }
		K k;
		I i;
		T t;
		V v;
};

class K {
	public:
		I i;
		T t;
		V v;
};

class I {
	public:
		K i;
		T t;
		V v;
};

class T {
	public:
		I i;
		K t;
		V v;
};

class V {
	public:
		I i;
		T t;
		K v;
};