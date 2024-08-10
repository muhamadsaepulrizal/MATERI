#include <iostream>
using namespace std;

//komparsi

int main(){
	int a = 3;
	int b = 2;
	
	bool hasil1, hasil2, hasil3, hasil4;
	
	//komparasi sebanding ==
	hasil1 =  (a == b);
	cout << hasil1 <<endl;
	
	//tidak sebanding !=
	hasil2 =  (a != b);
	cout << hasil2 <<endl;
	
	//kurang dari
	hasil3 = (a < b);
	cout <<hasil3 <<endl;
	
	//lebih dari
	hasil4 = (a > b);
	cout <<hasil4 <<endl;
	
	
	
	
	
	
	
	
	cin.get();
	return 0;
}
