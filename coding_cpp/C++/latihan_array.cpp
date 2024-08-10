#include <iostream>

using namespace std;

int main(){
	
	int nilai[11];
	
	cout<<" PROGRAM MENAMPILKAN GRAFIK NILAI"<<endl;
	cout<<"=================================="<<endl<<endl;
	
	for (int i=1; i<11; i++){
		cout<<"jumlah mahasiswa dengan nilai ";
		if(i==1){
			cout<<"  0-9: ";
		}else if(i==10){
			cout<<"  100: ";
		}
		else{
			cout<<i*10<<"-"<<(i*10)+9<<": ";
		}
		cin>>nilai[i];
		
	}
	
	cout<<endl;
	cout<<"       GRAFIK NILAI"<<endl;
	cout<<"=================================="<<endl<<endl;
	for(int i=1; i<11; i++){
		if(i==1){
			cout<<"  0-9: ";
		}else if(i==10){
			cout<<"  100: ";
		}
		else{
			cout<<i*10<<"-"<<(i*10)+9<<": ";
		}
		for(int bintang=0; bintang<nilai[i]; bintang++){
			cout<<"*";
		}
		cout<<endl;
		
	}
	
	
	cin.get();
	return 0;
}
