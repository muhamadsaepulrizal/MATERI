#include <iostream>
using namespace std;

void log(int result){
	cout <<"usia anda adalah " <<result <<endl;
	
}

int main(){
	int tl = 0; //tl = tahun lahir
	
	cout <<"masukan tahun  lahir anda : ";
	cin >>tl;
	
	log(tl);
	
	if (tl>50){
		cout <<"anda sudah tua";
	}else if (tl>20){
		cout <<"anda dewasa";
	}else if (tl>15){
		cout <<"anda remaja";
	}else {
		cout <<"anda masih anak anak";
	}
	
}
