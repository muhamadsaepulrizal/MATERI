#include <iostream>

using namespace std;

// fungsi rekursif terbatas
int pangkat_iterasi(int a, int b){
	int hasil = a;
	for (int i=1; i< b; i++){
		hasil = hasil*a;
	}
	return hasil;
}

int pangkat_rekursif(int a, int b){
	if (b <= 1){ // ini finite rekursif
		cout<<"\nini adalah akhir dari rekursif ";
		return a;
	}else{
		cout<<"\nrekursif\n";
		return a * pangkat_rekursif(a,(b-1));
	}
}

int main(){
	int a;
	int b;
	cout<<"angka : ";cin>>a;
	cout<<"Pangkat : ";cin>>b;
	cout<<"Hasil iterasi = "<<pangkat_iterasi(a,b)<<endl;
	cout<<"Hasil rekursif = "<<pangkat_rekursif(a,b);
	
	
	  
	cin.get();
	return 0;
}
