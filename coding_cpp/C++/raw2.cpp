#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main(){
	//nama file yang ditulis
	std::string namafile= "contoh_file.txt";
	
	//data yang ingin ditulis ke dalam file
	std:: string data="ini adalah tambah";
	
	//membuka file untuk ditulis
	std::ofstream file(namafile);
	
	//mengecek apakah file berhasil buka
	if (file.is_open()){
		//menulis data ke dlm file
		file<<data<<endl;
		
		std:: cout<<"data telah ditlis ke dlm file"<<endl;
		
		//menutup file setelah selesai ditulis
		file.close();
	}else{
		std:: cer<<"gagal membuka file"<<endl;
	}
	return 0;
}
