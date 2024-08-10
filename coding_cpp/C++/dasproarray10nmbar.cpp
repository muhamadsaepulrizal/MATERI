#include <stdio.h>

int main(){
	char namabarang[10][50];
	float hargabarang[10];
	
	for (int i=0; i<10; i++){
		printf("masukan nama barang ke-%d:",i+1);
		scanf("%s",&namabarang[i]);
		
		printf("maskukan harga barang ke-%d:", i+1);
		scanf("%f",&hargabarang[i]);
	}
	
	printf("\nDaftar barang\n");
	for (int i=0; i<10; i++){
		printf("%d. Nama barang: %s, Harga barang: %.2f\n", i+1, namabarang[i], hargabarang[i]);
	}
	
	return 0;
}
