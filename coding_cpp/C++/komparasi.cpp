#include <iostream>
using namespace std;

int main()
{
	int a = 2;
	int b = 5;
	
	bool hasil1, hasil2;
	
	//komparasi (membandingkan)
	
	//sebanding (==)
	hasil1 = (a == b); 
	cout <<hasil1 <<endl;//hasilnya aakan 0 atau 1, 0 adalah false dan 1 adalah true
	
	//tak sebnading (!=)
	hasil2 = (a != b); 
	cout <<hasil2 <<endl;//hasilnya aakan 0 atau 1, 0 adalah false dan 1 adalah true
	
	//tak kurang dari (<) jika ingin kurang dari sama dengan maka pakai (<=)
	hasil2 = (a < b); 
	cout <<hasil2 <<endl;//hasilnya aakan 0 atau 1, 0 adalah false dan 1 adalah true
	
	//tak lebih dari(>) jika ingin lebih dari sama dengan maka pakai (>=)
	hasil2 = (a > b); 
	cout <<hasil2 <<endl;//hasilnya aakan 0 atau 1, 0 adalah false dan 1 adalah true
	
	
	
	
	cin.get();
	return 0;
}
