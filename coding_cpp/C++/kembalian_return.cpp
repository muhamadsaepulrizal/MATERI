#include <iostream>

using namespace std;

//fungsi kembalian
int kuadrat(int x){ //contoh fungsi kuadrat
	int y;
	y= x*x;
	return y;
}

int kali(int a, int b){
	int c;
	c= a*b;
	return c;
}

int main(){
	int input, hasil, a, b, hasil2;
	cout <<"Nilai Kuadrat dari: ";cin>>input;
	hasil= kuadrat(input);
	cout <<"Hasil Kuadratnya adalah "<<hasil<<endl;
	
	cout <<"masukan NIlai ke-1: ";cin>>a;
	cout <<"masukan NIlai ke-2: ";cin>>b;
	hasil2= kali(a,b);
	cout <<"Hasil Kalinya adalah "<<hasil2<<endl;
	
	
	
	cin.get();
	return 0;
}
