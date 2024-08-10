#include <iostream>

using namespace std;

double volumekubus(double p=1, double l=1, double t=1); //double t=1 adalah default argument atau nilai standar jika di main utama tidak diinputkan nilainya

int main(){
	
	cout <<"volume kubus: "<<volumekubus(3,4,5)<<endl;
	cout <<"volume kubus: "<<volumekubus(3,4)<<endl;
	cout <<"volume kubus: "<<volumekubus(3,4,2)<<endl;
	cout <<"volume kubus: "<<volumekubus(3)<<endl;
	cout <<"volume kubus: "<<volumekubus()<<endl;
	
	cin.get();
	return 0;
}

double volumekubus(double p, double l, double t){
	return p*l*t;
}
