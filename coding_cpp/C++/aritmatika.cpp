#include <iostream>
using namespace std;

int main(){
	/*
	aritmatika ada  +(tambah), -(kurang), /(bagi), *(kali), %(modulus)
	*/
	
	
	int a = 6;
	int b = 4;
	int hasil;
	
	//penjumlahan
	hasil = a+b;
	cout<<"hasil penjumlahan adalah "<<hasil<<endl;
	
	//pengurangan
	hasil = a-b;
	cout<<"hasil pengurangan adalah "<<hasil<<endl;
	
	//perkalian
	hasil = a*b;
	cout<<"hasil perkalian adalah "<<hasil<<endl;
	
	//pembagian
	hasil = a/b;
	cout<<"hasil pembagian adalah "<<hasil<<endl;
	
	//sisa hasil bagi (modulud)
	hasil = a%b;
	cout<<"hasil pembagian adalah "<<hasil<<endl;
	
	
	cin.get();
	return 0;
}
