#include <iostream>
using namespace std;


//contoh penggunaan function dan void log (sebagai tamplate)
double pertambahan(double x, double y) {return x+y;}
double pengurangan(double x, double y) {return x-y;}
double perkalian(double x, double y) {return x*y;}
double pembagian(double x, double y) {return x/y;}

void log (double result){
	cout <<"hasil operasi aritmatika dari 5 dan 10 adalah "<<result <<endl;
}

int main(){
	//cara pemanggilannya
	double tambah = pertambahan (10,5);
	log(tambah);
	
	double kurang = pengurangan (10,5);
	log(kurang);
	
	double kali = perkalian (10,5);
	log(kali);
	
	double bagi = pembagian (10,5);
	log(bagi);
	
}
