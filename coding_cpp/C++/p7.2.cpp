#include <stdio.h>
#include <conio.h>

int main(){
	int x,anak_ayam,sisa;
	
	printf("jumlah anak ayam =");scanf("%d",&anak_ayam);
	printf("============================\n\n");
	
	for ( x=anak_ayam; x>1; x-- ){
		sisa=x-1;
		printf("anak ayam turun %d, mati satu tinggal %d \n\n",x,sisa);
	}
	
	printf("ANAK AYAM TURUN 1, MATI SATU TINGGAL INDUKNYA\n");
	getch();
}
