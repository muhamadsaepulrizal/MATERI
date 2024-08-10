#include <iostream>

using namespace std;

int kuadrat(int x){ //contoh fungsi kuadrat
	int y;
	y= x*x;
	return y;
}

void tampilkan(int input){
	cout <<input;
	
}

int main(){
	int input, hasil;
	cout <<"Nilai Kuadrat dari: ";cin>>input;
	hasil= kuadrat(input);
	//cout <<"Hasil Kuadratnya adalah "<<hasil<<endl; yang asalnya begini menjadi
	tampilkan(hasil);
	cin.get();
	return 0;
}
