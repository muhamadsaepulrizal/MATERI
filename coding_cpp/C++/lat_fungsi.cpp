#include <iostream>

using namespace std;

//fungsi menghitung luas persegi panjang
double hitungluas(double p, double l){
	double luas = p*l;
	return luas;
}


//fungsi menghitung keliling persegi panjang
double hitungkeliling(double p, double l){
	double keliling = 2*(p+l);
	return keliling;
}

int main(){
	double panjang,lebar,hasil1,hasil2;
	int pilih;
	cout <<"===========Hitung luas atau keliling segitiga==========="<<endl;
	cout <<"======================================================="<<endl;
	cout <<"1. Menhitung luas"<<endl;
	cout <<"2. Menghitung keliling"<<endl;
	cout <<"Silahkan Pilih 1/2 : ";cin>>pilih;
	if (pilih == 1){
		cout<<"=========Hitung Luas==========="<<endl;
		cout<<"Masukan Panjang: ";cin>>panjang;
		cout<<"Masukan Lebar: ";cin>>lebar;
		hasil1 = hitungluas(panjang,lebar);	
		cout <<"Luasnya adalah: "<<hasil1;
	}else if(pilih == 2){
		cout<<"=========Hitung Keliling==========="<<endl;
		cout<<"Masukan Panjang: ";cin>>panjang;
		cout<<"Masukan Lebar: ";cin>>lebar;
		hasil2 = hitungkeliling(panjang,lebar);
		cout <<"Kelilingnya adalah: "<<hasil2;
	}else{
		cout<<"\n\n Mohon Pilih 1/2"<<endl;
	}
	
	cin.get();
	return 0;
}
