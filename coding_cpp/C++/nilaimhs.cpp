#include <iostream>
#include <vector>

using namespace std;

struct nilaimhs{
	string nama;
	double nilai;
};

void inputnilaimhs(vector<nilaimhs>& data, string nama, double nilai){
	nilaimhs nilaimahasiswa;
	nilaimahasiswa.nama=nama;
	nilaimahasiswa.nilai =nilai;
	data.push_back(nilaimahasiswa);
}
void tampilkannilaimhs(const vector<nilaimhs>&data){
	cout<<"Nilai mahasiswa"<<endl;
	for (const nilaimhs& nilaimahasiswa : data){
		cout<<nilaimahasiswa.nama<<": "<<nilaimahasiswa.nilai<<endl;
	}
}

int main(){
	vector<nilaimhs>dataNilai;
	
	int pilih;
	string nama;
	double nilai;
	
	do{
		cout<<"1. Input nilai mahasiswa "<<endl;
		cout<<"2. Tampilkan nilai amahasiswa"<<endl;
		cout<<"3. keluar"<<endl
		cout<<"pilih menu (1-3): "; cin>>pilih;
		
		switch(pilih){
			case 1:
				cout<<"masukan nama mahasiswa: ";cin.ignore();
				getline(cin.nama);
				cout <<"masukan nilai mahasiswa: ";cin>>nilai;
				inputnilaimhs(dataNilai, nama, nilai);
				break;
			case 2:
				tampilkannilaimhs(datanilai);
				break;						
		}	
	}while(pilih !=3 );
	
	return 0;
}
