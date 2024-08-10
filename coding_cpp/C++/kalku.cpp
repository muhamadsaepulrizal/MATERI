#include <iostream>
using namespace std;

double tambah(double a, double b){
	return a+b;
}
double kurang(double a, double b){
	return a-b;
}
double kali(double a, double b){
	return a*b;
}
double bagi(double a, double b){
	if (b != 0){
		return a/b;
	}else{
		cout <<"error";
		return 0;
	}
}

int main(){
	double angka1, angka2;
	cout <<"masukan angka pertama"; cin>>angka1;
	cout <<"masukan angka kedua"; cin>>angka2;
	
	
	char pilih;
	cout <<"pilih operasi (+,-,*,/): "; cin>>pilih;
	
	switch(pilih) {
		case '+':
			cout<<"hasil penambahan: "<<tambah(angka1,angka2)<<endl;
			break;
		case '-':
			cout<<"hasil pengurangan: "<<kurang(angka1,angka2)<<endl;
			break;
		case '*':
			cout<<"hasil perkalian: "<<kali(angka1,angka2)<<endl;
			break;
		case '/':
			cout<<"hasil pembagian: "<<bagi(angka1,angka2)<<endl;
			break;  
		default:
			cout <<"operasi tidak valid" <<endl;	
	}
	return 0;
	
}
