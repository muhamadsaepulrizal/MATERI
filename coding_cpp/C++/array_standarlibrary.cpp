#include <iostream>

using namespace std;

int main(){
	
	//membuat array dengan standard library
	//array<int, jumlah array> nama array
	
	int nilai[5];
	for(int i=0; i<=4; i++){
		nilai[i]=i;
		cout<<"nilai: "<<"{ "<<i<<" } = "<<nilai[i]<<"\t";
		cout<<"addressnya: "<<&nilai[i]<<endl;
	}
	cout <<endl;
	cout <<"ukuran :"<<sizeof(nilai)/sizeof(int)<<endl;
	
	
	cin.get();
	return 0;
}
