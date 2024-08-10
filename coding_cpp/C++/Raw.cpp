#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
	std::string nama_file="contoh_file.txt";
	
	//membuka file untuk dibaca
	std::ifstream file(nama_file);
	std::string isifile;
	
	//mengecek apakah file berhasil dibuka
	if (file.is_open()){
		//membaca isi file
		std::getline(file,isifile);
		//menampilah isi file
		std::cout <<"nama saya rizal" <<isifile <<endl;
		
		//manutup file setelah dibaca
		file.close();
	}else{
		std::cerr <<"gagal membuka file untuk dibaca" <<endl;
	}
	
	return 0;
}
