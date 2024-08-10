#include <iostream>

using namespace std;

int main(){
	
	int n;
	int fn, fn1,fn2;
	int i;
	
	cout<<"Program Deret Fibonacci dengan Do Whiile\n";
	cout<<"Masukan NIlai ke-n: ";cin>>n;
	
	fn1=1;
	fn2=0;
	do{
		fn=fn1+fn2;
		fn2=fn1;
		fn1=fn;
		cout<<fn<<endl;
		i++;
	}while(i<n);
	
	
	
	
	cin.get();
	return 0;
}
