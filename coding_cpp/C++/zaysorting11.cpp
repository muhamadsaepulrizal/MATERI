#include <iostream>
using namespace std;

int main(){
	
	int n = 10, cari = 10, i;
	int data[n] = {9, 4, 1, 7, 5, 12, 4, 13, 4, 10};
	bool ketemu = false;
	
	for (i = 0; i < n; i++){
		if(data[i] == cari){
			ketemu = true;
			break;
		}
	}
	
	if (ketemu){
		cout << cari << " ditemukan pada index ke-" << i << endl;
	} else {
		cout << cari << " tidak dapat ditemukan pada data." << endl;
	}
	return 0;
}
