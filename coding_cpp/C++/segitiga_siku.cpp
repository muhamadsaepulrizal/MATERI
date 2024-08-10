#include <iostream>

using namespace std;

int main(){
	int n;
	cout<<"segitiga siku-siku\n";
	
	cout <<"Masukan Panjang Pola: ";cin>>n;
	
	cout <<"Pola 1"<<endl;
	
	for(int i=1; i<=n; i++){ //looping untuk kebawah
		for (int j=1; j<=i; j++){ //looping ke kanan
			cout <<"*";	
		}
		cout<<endl;
	}
	
	
	cout <<"Pola 2"<<endl;
	
	for(int i=1; i<=n; i++){
		for (int j=n; j>=i; j--){ //kenapa j=n karena kita ingin dimulai dari angka yang diinputkan,
			cout <<"@";				// j>=1 karena n pasti lebih besar dari 1
		}							//kenapa j-- karena dari n yang dinputkan akan terus dikurang sampe kebawah(1)
		cout<<endl;
	}
	
	cout<<"Pola 3\n";
	
	for(int i=1; i<=n; i++){
		for(int j=1; j<=i; j++){ //looping untuk spasi
			cout <<" ";
		}
		for(int k=n; k>=i; k--){
			cout <<"#";
		}
		cout<<endl;
	}
	
	cout<<"Pola 4\n";
	
	for(int i=1; i<=n; i++){
		for(int j=n; j>i; j--){ //looping untuk spasi
			cout <<" ";
		}
		for(int k=1; k<=i; k++){
			cout <<"$";
		}
		cout<<endl;
	}
	
	
	cout<<"\n\nsegitiga sama kaki\n";
	
	cout<<"Pola 5 \n";
	
	for(int i=1; i<=n; i++){
		for(int j=n; j>i; j--){
			cout <<" ";
		}
		for(int k=1; k<= (2*i-1); k++){ //i nya berubah dari 1,2,3,4,5 menjadi 1,3,5,7,9 dst.....
			/* kenapa rumusnya 2*i-1 (2*i - beda(1 bedanya)) 
				karena untuk membuat segitiga siku siku harus 2*i-1= 2*1-1=1, 2*2-1=3, 2*3-1=5, dst......9
				sehingga tercipta seditiga seperti ini:
				  &
				 &&&
				&&&&&		 
			*/
			cout <<"&";
		}
		cout<<endl;
	}
	
	
	cout<<"Pola 6\n";
	
	for(int i=1; i<=n; i++){
		for(int j=1; j<=i; j++){
			cout <<" ";
		}
		for(int k=n; k>=(2*i-n); k--){ 
			cout <<"#";
		}
		cout<<endl;
	}
	
	cout<<"\n\nKetupat\n";
	
	cout<<"Pola 7 \n";
	
	for(int i=1; i<=n; i++){
		for(int j=n; j>i; j--){
			cout <<" ";
		}
		for(int k=1; k<= (2*i-1); k++){
			cout <<"&";
		}
		cout<<endl;
	}
	for(int i=2; i<=n; i++){
		for(int j=1; j<i; j++){
			cout <<" ";
		}
		for(int k=n; k>=(2*i-n); k--){
			cout <<"&";
		}
		cout<<endl;
	}
	
	// kenapa kadang j>=i atau j<=i karena diatas i=1
	
	

	cin.get();
	return 0;
}


