#include <iostream>

using namespace std;

int main()
{
	// increment dan decrement
	// pre(sebelum) increment dan post(sesudah) increment
	
	int a = 5;
	int b = 5;
	
	//postincrement (sesudah) a++ (a = a+1)
	cout <<a<<endl;
	cout <<a++<<endl;
	cout <<a<<endl<<endl;
	
	//preincrement (sebelum)
	cout <<b<<endl;
	cout <<++b<<endl;0;
	cout <<b<<endl;
	
	/*
		note: dan untuk decremenet sama juga ada 2 yaitu post decremenet dan pre decrement 
		postdecrement ( a-- ) predecrement ( --b )
		hasil run
		5		5
		5		4
		4		4


	*/	
	cin.get();
	return 0;
}
