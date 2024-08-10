#include <iostream>

using namespace std;

int main()
{
	//incremenet
	cout<<"loop 1\n";
	for (int i = 1; i <= 10; i++){
		cout<<i<<endl; 
		
	}
	
	//asignment operator
	cout<<"loop 2\n";
	for (int i = 1; i <= 10; i += 2){
	cout<<i<<endl; 
		
	}
	
	//decremenet
	cout<<"loop 3\n";
	for (int i = 1; i >= -10; i--){
		cout<<i<<endl; 
		
	}
	
	//campur
	cout<<"loop 4\n";	
	int total = 0;
	for (int i = 1; i <= 10; i++, total += i){
		cout<<i<<"|| "<<total<<endl; 
		
	}	
	cin.get();
	return 0;
}
