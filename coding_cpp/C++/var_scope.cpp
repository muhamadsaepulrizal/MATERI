#include <iostream>

using namespace std;

//global scope
int x = 10;//variabel global

int ambilvarglobal(){
	return x;
}

int main(){
	cout <<"variabel global: "<<x<<endl;
	
	//lokal scope
	int x = 5; //variabel lokal main
	cout <<"variabel lokal main: "<<x<<endl;
	
	cout <<"variabel global: "<<ambilvarglobal()<<endl;
	
	{
		//scope bloke
		int x = 2;
		cout<<"variabel blok: "<<x<<endl;
	}
	
	cin.get();
	return 0;
}
