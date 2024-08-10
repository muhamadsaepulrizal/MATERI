#include <iostream>
using namespace std;

int main()
{
	float a,b,hasil;
	char aritmatika;
	
	cout<<"Selamat Datang Di Program Kalkulator"<<endl;
	cout<<"====================================\n\n";
	
	
	//masukan input dari user
	cout<<"Masukan Nilai Pertama: ";cin>>a;
	cout<<"pilih Operator:|| + | - | * | / | %(modulus) || : ";cin>>aritmatika;
	cout<<"Masukan Nilai Kedua: ";cin>>b;
	
	
	cout<<"\n\nHasil Perhitungan\n";
	cout <<a<<" "<<aritmatika<<" "<<b;
	
	if (aritmatika == '+'){
		hasil= a+b;
		cout<<" = "<<hasil<<endl;
	}else if(aritmatika == '-'){
		hasil= a-b;
		cout<<" = "<<hasil<<endl;
	}else if(aritmatika == '*'){
		hasil= a*b;
		cout<<" = "<<hasil<<endl;
	}else if(aritmatika == '/'){
		hasil= a/b;
		cout<<" = "<<hasil<<endl;
	}else{
		cout<<"\tOperator salah"<<endl;
	}
	
	cout<<"\nHatur nuhun"<<endl;
	cout<<"=========================="<<endl;
	
	
	
	
	
	
	
	cin.get();
	return 0;
}
