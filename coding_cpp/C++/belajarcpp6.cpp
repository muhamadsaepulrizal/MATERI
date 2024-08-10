#include <iostream>
using namespace std;

// aritmatika
int main(){
	// aritmatika ada +(tambah), -(kurang, *(kali), /(bagi), %(modulus).
	
	int a=11;
	int b=4;
	
	int hasil;
	
	//penjumlahan
	//cout <<a + b;
	
	hasil= a+b;
	cout <<a <<" + " <<b <<" = " <<hasil <<endl;
	
	//pengurangan
	hasil= a-b;
	cout <<a <<" - " <<b <<" = " <<hasil <<endl;
	
	//perkalian
	hasil= a*b;
	cout <<a <<" * " <<b <<" = " <<hasil <<endl;
	
	//pembagian kenapa hasil bagi dari 11/2 adalah 5 tidak 5,5 karena tipe datanya int jika ingin ada koma bisa gunakan float atau double
	hasil= a/b;
	cout <<a <<" / " <<b <<" = " <<hasil <<endl;
	
	//modulus
	hasil= a%b;
	cout <<a <<" modulus " <<b <<" = " <<hasil <<endl;
	
	
	
	
	
	
	
	
	
	
	
	cin.get();
	return 0;
}
