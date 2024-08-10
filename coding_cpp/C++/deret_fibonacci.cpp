#include <iostream>

using namespace std;


//STUDI KASUS
int main(){
	// Rumus : f_n = f_n1 + f_n2
	
	int n;
	int fn,fn1,fn2;
	cout <<"Program Deret Fibonacci\n";
	cout <<"Masukan Nilai ke-n: ";cin>>n;
	
	//inisialisasi jadi nanti fn= fn1+fn2 artinya fn = 1+0 hasilnya fn 1 dan seterusnya 1+1=2, 1+2=3, 2+3=5, dst
	fn1 = 1; 
	fn2 = 0;
	fn = fn1+fn2;
	cout <<fn<<endl;
	for (int i=1; i<n; i++){
		fn = fn1+fn2;
		fn2 = fn1;
		fn1 = fn;
		cout <<fn<<endl;
		
	}
	
	
	
	cin.get();
	return 0;
}
