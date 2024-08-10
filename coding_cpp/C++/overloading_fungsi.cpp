#include <iostream>

using namespace std;

//overloading = menimpa

//basic function
int luaskotak(int panjang, int lebar){
	int luas = panjang*lebar;
	return luas;
}

//overloadingnya
int luaskotak(int sisi){
	int luas = sisi*sisi;
	return luas;
}

double luaskotak(double sisi){
	return sisi*sisi;
}


int main(){
	
	cout <<"Luas Kotak 2x3: "<<luaskotak(2,3)<<endl;
	cout <<"Luas Kotak 2: "<<luaskotak(2)<<endl; //ini akan mengambil overloading fungsi karena nilai nya ada satu
	cout <<"Luas Kotak 2,5: "<<luaskotak(2.5)<<endl;
		
	cin.get();
	return 0;
}


