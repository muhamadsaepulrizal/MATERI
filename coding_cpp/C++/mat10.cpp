 #include <stdio.h>
 
 int main(){
 	char nama [10][50];
 	float harga [10];
 	for (int i=0; i<10; i++){
 		printf("masukan nama barang ke-%d:", i+1);
 		scanf("%s",&nama[i]);
 		printf("masukan harga barang ke-%d:", i+1);
 		scanf("%f",&harga[i]);
	}
	FILE *tulisdata = fopen("Belajar.txt","w");
	printf("\n daftar nama barang:\n");
	for(int i=0; i<10; i++){
		printf("%d nama : %s, harga : %.2f\n",i+1,nama[i],harga[i]);
		fprintf(tulisdata,"Nama : %s\n",nama[i]);
		fprintf(tulisdata,"harga : %.2f\n",harga[i]);
	}
	fclose(tulisdata);
	return 0;	
 }
