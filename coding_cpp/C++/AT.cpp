#include <iostream>
using namespace std;

const int maxt= 100;
float saldo =0;
float transaksi[maxt];
int jmltran=0;
char nama[50];

void ceksaldo(){
	cout <<"Saldo Anda, "<<nama <<": "<<saldo;
	
}
void setortunai(){
	float st;
	cout <<"Masukan Jumlah Setor Tunai: "; cin>>st;
	saldo += st;
	transaksi[jmltran]= st;
	jmltran++;
	cout <<"Setor Tunai Berhasil. Saldo Sekarang: "<<saldo <<endl;
}
void tariktunai(){
	float tt;
	cout <<"Masukan Jumlah Tarik Tunai: "; cin>>tt;
	if (tt > saldo){
		cout<<"Saldo Tidak Mencukupi."<<endl;
	}else{
		saldo -= tt;
		transaksi[jmltran] = -tt;
		jmltran++;
		cout<<"Traik Tunai Berhasil. Saldo Sekarang: "<<saldo<<endl;
	}

	
}
void riwayattransaksi(){
	cout <<"\nRiwayat Transaksi Anda: "<<endl;
	for (int i = 0; i<jmltran; i++){
		if(transaksi[i]>0){
			cout <<"Setor Tunai: "<<transaksi[i]<<endl;
		}else{
			cout <<"Tarik Tunai: "<<-transaksi[i]<<endl;
		}
	}
}

int main(){
	int pilih;
		cout <<"Masukan nama nasabah: ";cin>>nama;
		cout <<"Selamat datang " <<nama <<" di ATM Bank INI"<<endl;
	do {	
		cout <<"\n=====----- Menu Atm -----=====\n"<<endl;
		cout <<"1. Cek Saldo"<<endl;
		cout <<"2. Setor Tunai"<<endl;
		cout <<"3. Tarik Tunai"<<endl;
		cout <<"4. Riwayat Transaksi"<<endl;
		cout <<"5. Keluar"<<endl;
		cout <<"Pilih Menu (1-5): "; cin>>pilih;
		
		switch(pilih){
			case 1:
				ceksaldo();
				break;
			case 2:
				setortunai();
				break;
			case 3:
				tariktunai();
				break;
			case 4:
				riwayattransaksi();
				break;
			case 5:
				cout <<"terima kasih "<<nama<<endl;
				break;
			default:
				cout <<"Pilihan Tidak Valid. Silahkan Pilih Menu Yang Tersedia"<<endl;
				break;
		}	
	}while (pilih != 5);
	
		
	return 0;
}
