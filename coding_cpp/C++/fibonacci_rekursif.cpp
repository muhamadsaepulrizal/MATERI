#include <iostream>

using namespace std;

int fibonacci(int n){
	if ((n==0) or (n == 1)){
		return n;
	}else{
		return fibonacci(n-1)+fibonacci(n-2);
	}
}

int main(){
	int angka, hasil;
	cout<<"Menghitung fibonacci ke-n: ";cin>>angka;
	hasil = fibonacci(angka);
	cout<<"Nilainya adalah = "<<hasil<<endl;
	
	cin.get();
	return 0;
}


