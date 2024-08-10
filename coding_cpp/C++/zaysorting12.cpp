#include <iostream>
using namespace std;

int main(){
	
	int n = 10;
	int data[n] = {9, 4, 1, 7, 5, 12, 4, 13, 4, 10};
	int cari = 4;
	bool ketemu = false;
	int penghitung = 0;
	
	for (int i = 0; i < n; i++){
		if(data[i] == cari){
			ketemu = true;
			penghitung++;
		}
		
	}
	
	if (ketemu){
		cout << "ditemukan sebanyak " << penghitung << endl;
	} else {
		cout << "tidak ditemukan pada data." << endl;
	}
	return 0;
}
