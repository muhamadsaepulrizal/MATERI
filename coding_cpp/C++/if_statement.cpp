#include <iostream>
using namespace std;

int main()
{
	int a;
	
	cout<<"Masukan angka: ";cin>>a;
	
	//if statement
	//(kondisi) dalam bentuk boolean/bool
	
	/*
	if (kondisi)
	{
		statement
		kalau kondisi True maka stetement dijalankan dan jika false tidak dijalankan
	}
	*/
	
	//contoh:
	
	if (a < 3)
	{
		cout<<"hallo tiga"<<endl;
	}
	
	cout<<"selesai"<<endl;
	cin.get();
	return 0;
}
