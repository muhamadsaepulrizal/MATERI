#include <iostream>
#include <vector>
using namespace std;

class Buku{
public:
	string judul;
	string penulis;
	bool tersedia;
	
	Buku(const string& judul, const string& penulis) : judul(judul), penulis(penulis), tersedia(true) {}
};
	
int main(){
	vector <Buku> bukulist;
	for (int i = 0; i<= 2; ++i){
		string judul,penulis;
		cout<<"masukan judul buku: "; cin>>judul;
		cout<<"masukun penulis buku: ";cin>>penulis;
		Buku buku(judul, penulis);
		bukulist.push_back(buku);
	}
	
	cout<<"\ndaftar buku:\n";
	for (size_t i=0; i<bukulist.size(); ++i){
		cout<<i+1<<". "<<bukulist[i].judul<<"-"<<bukulist[i].penulis<<endl;
	}
	
	int pilihan;
	cout<<"\nPilih nomor buku yang ingin dipinjam: "; cin>>pilihan;
	
	if (pilihan >=1 && pilihan<= bukulist.size()&& bukulist[pilihan-1].tersedia){
		bukulist[pilihan-1].tersedia=false;
		cout<<"\nBuku "<<bukulist[pilihan-1].judul<<"berhasil dipinjam"<<endl;
	}else{
		cout<<"\pilihan tidak tersedia"<<endl;
	}
	return 0;
}
