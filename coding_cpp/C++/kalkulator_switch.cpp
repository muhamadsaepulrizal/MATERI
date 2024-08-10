#include <iostream>

using namespace std;
int main()
{
	float a,b,hasil;
	char aritmatika;
	
	cout <<"SELAMAT DATANG DI PROGRAM KALKULATOR SEDERHANA"<<endl;
	cout <<"===============================================\n\n";
	
	cout <<"Masukan nilai pertama : ";cin>>a;
	cout <<"Pilih Operator || (+)Tambah, (-)Kurang, (*)Kali, (/)Bagi : ";cin>>aritmatika;
	cout <<"Masukan nilai kedua : ";cin>>b;
	cout <<"===============================================\n\n";

	cout <<"Hasil Perhitungan\t\t";
	cout <<a<<" "<<aritmatika<<" "<<b;
	
	switch (aritmatika){
		case '+':
			hasil= a+b;
			cout <<" = "<<hasil;
			break;
		case '-':
			hasil= a-b;
			cout <<" = "<<hasil;
			break;
		case '*':
			hasil= a*b;
			cout <<" = "<<hasil;
			break;
		case '/':
			hasil= a/b;
			cout <<" = "<<hasil;
			break;
		default:
			cout <<"\nOperator yang anda masukan salah";
			break;
			
	}	
	cout <<"\n===============================================";
	cout <<"\nTerima Kasih Sudah Menggunakan Program Kami"<<endl;
		
	cin.get();
	return 0;
	
}
