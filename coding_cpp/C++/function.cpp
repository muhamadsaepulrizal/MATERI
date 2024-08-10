#include <iostream>
#include <cmath>
/*

library cmath : referensi www.cppreference.com
ceil(x) : pembulatan ke atas
cos(x)  : cosinus
exp(x)  : eksponen
fabs(x) : nilai absolut dalam float
floor(x) : pembulatan ke bawah
fmod(x) : modulus dalam float
log(x) : logaritma dengan basis natural
log10(x) : logaritma dengan basis 10
pow(x,y) : x pangkat y
sin(x) : sinus
sqrt(x) : akar kuadrat
tan(x) : tangen

*/

using namespace std;

int main(){
	int a;
	
	cout <<"menghitung akar kuadrat dari X: ";cin>>a;	
	cout <<"Akar Kuadrat Nya Adalah: "<<sqrt(a)<<endl;

	cin.get();
	return 0;
}
