#include <iostream>

using namespace std;

int main()
{
	//assignment
	
	int a = 22;
	cout <<"nilai awal dari a adalah: "<<a<<endl;
	
	//assignment operator
	
	//variabel = variabel operator       ekspresi
	//   a     =   a         -       3/ bisa juga (1+3) 
	
	//variabel  operator=    ekspresi 
	//    a      +=             3
	
	a+=3;
	cout<<"nilai a ditambah 3 menjadi: "<<a<<endl;
	
	a-=3;
	cout<<"nilai a dikurang 3 menjadi: "<<a<<endl;
	
	a/=3;
	cout<<"nilai a dibagi 3 menjadi: "<<a<<endl;
	
	a*=3;
	cout<<"nilai a dikali 3 menjadi: "<<a<<endl;
	
	a%=3;
	cout<<"nilai a dibagi 3 menjadi: "<<a<<endl;
	
	
	
	cin.get();
	return 0;
}
