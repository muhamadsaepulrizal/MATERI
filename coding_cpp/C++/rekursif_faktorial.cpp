#include <iostream>

using namespace std;

//prototipe
int faktorial(int n);

int main(){
	int angka, hasil;
	
	cout<<"hitung faktorial dari : ";cin>>angka;
	
	hasil = faktorial(angka);
	cout<<"\nFaktorial nya adalah = "<<hasil<<endl;
	
	
	
	cin.get();
	return 0;
}

int faktorial(int n){
	if(n <= 1){ // ini adalah infinite rekursifnya
		cout <<n;
		return n;
	}else{ // ini adalah rekursifnya
		cout <<n<<" x ";
		return  n* faktorial(n-1);
	}
	
}
