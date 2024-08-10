#include <iostream>

using namespace std;

void fungsi(int * /* b, (b, bisa dipakai atau tidak)*/);
void kuadrat(int * /* (*valptr*) bisa dipakai atau tidak */);

int main(){
	
	int a = 5;
	cout<<"address a: "<<&a<<endl;
	cout<<"  nilai a: "<<a<<endl;
	//fungsi(&a); //fungsi dengan input pointer
	
	kuadrat(&a);
	cout <<"nilai kuadrat a: "<<a<<endl;
	
	cin.get();
	return 0;
}


//jadi ini sama dengan *aptr 
// jadi ini 1 memory
void fungsi (int *b){ 
	cout<<"address b: "<<b<<endl;
	cout<<"  nilai b: "<<*b<<endl; //dereferencing  
	
}

void kuadrat(int *valptr){
	*valptr = (*valptr) * (*valptr);
}

//jika ingin 2 memory penulisannya sperti ini :
/*
void fungsi (int b){ 
	cout<<"address b: "<<b<<endl;
	cout<<"  nilai b: "<<&b<<endl; //dereferencing  
	
}


int main(){
	
	int a = 5;
	cout<<"address a: "<<&a<<endl;
	cout<<"  nilai a: "<<a<<endl;
	fungsi(a); //fungsi dengan input pointer
	
	cin.get();
	return 0;
}

*/
