#include <iostream>

using namespace std;

int main(){
	
	// int a mempunyai nilai dan address	
	int a = 5;

	//pointer
	int *aptr = &a;	
	
	cout<<"ini adalah nilai dari a: "<<a<<endl;
	cout<<"alamat dari nilai a: "<<aptr<<endl;
	
	//mengambil nilai dari sebuah pointer (dereferencing)
	a=10;
	cout <<"Mengambil nilai dari pointer aptr: "<<*aptr<<endl;
	
	cin.get();
	return 0;
}
