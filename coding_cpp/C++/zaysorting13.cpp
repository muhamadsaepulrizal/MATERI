#include <iostream>
using namespace std;

int main(){
	int n = 10;
	int data[n] = {2, 5, 9, 12, 14, 15, 19, 21, 28, 31};
	int cari = 19;
	int mid;
	int left = 0;
	int right = n-1;
	int flag = 0;
	int stepCounter = 0;
	
	while( (left <= right) && (flag == 0) ){
		stepCounter++;
		mid = (left+right)/2;
		cout << "\n#Tahap" << stepCounter << endl;
		cout << " Left: " << left << ", Mid:" << mid << ",Right:" << right << endl;
		cout << " Data tengah: " << data[mid] << ", Cari: " << cari << endl;
		
		if (data[mid] == cari){
			flag = 1;
		} else if (cari < data[mid]){
			cout << cari << " < " << data[mid] << ", maka cari di kiri" << endl;
			right = mid-1;
		} else {
			cout << cari << " > " << data[mid] << ", maka cari di kanan" << endl;
			left = mid+1;
		}
	}
	
	cout << endl;
	if(flag == 1){
		cout << " angka " << cari << " dapat ditemukan " << endl;
	} else {
		cout << " angka " << cari << " tidak dapat ditemukan " << endl;
	}
	
	cout << "Jumlah langkah: " << stepCounter << endl;
	
	return 0;
}
