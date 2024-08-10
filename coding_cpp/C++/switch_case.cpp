#include <iostream>
using namespace std;

int main()
{
	int a;
	
	cout<<"masukan nilai a : ";cin>>a;
	
	switch (a){
		case 1:
			cout<<"ini adalah 1"<<endl;
			break;
		case 2:
			cout<<"ini adalah 2"<<endl;
			break;
		case 3:
			cout<<"ini adalah 3"<<endl;
			break;
		case 4:
			cout<<"ini adalah 4"<<endl;
			break;
		case 5:
			cout<<"ini adalah 5"<<endl;
			break;
		default:
			cout<<"angka tidak ditemukan"<<endl;
			break;
	}
	
	cout <<"akhir program"<<endl;
	
	
	
	
	cin.get();
	return 0;
}
