#include <iostream>

using namespace std;

int main(){
	int tps[11];
	
	cout<<" PROGRAM GRAFIK NILAI UAS MAHASISWA KELAS E MATA KUIAH DASPRO"<<endl;
	cout<<"==============================================================="<<endl<<endl;
	
	for(int i=1; i<11; i++){
		cout<<"Jumlah nilai mahasiswa dengan nilai ";
		if (i==1){
			cout<<"0-9  : ";
		}else if(i==10){
			cout<<"100  : ";
		}else{
			cout<<i*10<<"-"<<(i*10)+9<<": ";
		}
		cin>>tps[i];
	}
	cout<<endl;
	cout<<"         GRAFIK NILAI UAS KELAS E MATA KULIAH DASPRO"<<endl;
	cout<<"==============================================================="<<endl<<endl;
	for(int i=1; i<11; i++){
		if (i==1){
			cout<<"0-9  : ";
		}else if(i==10){
			cout<<"100  : ";
		}else{
			cout<<i*10<<"-"<<(i*10)+9<<": ";
		}
		for(int grafik=0; grafik<tps[1]; grafik++){
			cout<<"*";
		}
		cout<<endl;
	}
	
	cin.get();
	return 0;
}
