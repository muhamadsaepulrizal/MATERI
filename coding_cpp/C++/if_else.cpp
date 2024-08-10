#include <iostream>

using namespace std;

int main()
{
	int a;
	
	cout<<"masukan nilai a: ";cin>>a;
	
	if (a>5){
		cout<<"nilai lebih dari lima"<<endl;
	}else if (a==5){
		cout<<"nilai adalah lima"<<endl;
	}else{
		cout<<"nilai kurang dari lima"<<endl;
	}
	
	cout<<"selesai"<<endl;
	
	cin.get();
	return 0;
}
