#include<stdio.h>
#include<stdlib.h>

void makanan(){
int makan;
	printf("Daftar menu makanan\n");
	printf("====================\n");
	printf("1.Roti\n");
	printf("2.Mie\n");
	printf("3.Soto\n");
	printf("4.Baso\n");
	printf("5.Sate\n");
	printf("pilih menu makanan anda =");scanf("%d",&makan);
	
	if(makan==1){
	printf("anda telah memesan Roti");
	}
	else if(makan==2){
	printf("anda telah memesan Mie");
	}
	else if(makan==3){
	printf("anda telah memesan soto");
	}
	else if(makan==4){
	printf("anda telah memesan Baso");
	}
	else if(makan==5){
	printf("anda telah memesan Sate");
	}
	else{
	printf("tidak tersedia");
	}
}
void minuman(){
int minum;
	printf("Daftar menu minuman\n");
	printf("====================\n");
	printf("1.Teh\n");
	printf("2.Aqua\n");
	printf("3.Susu\n");
	printf("4.Jus\n");
	printf("5.Kopi\n");
	printf("pilih menu minuman anda =");scanf("%d",&minum);
	
	if(minum==1){
		printf("anda telah memesan Teh");
	}
	else if(minum==2){
		printf("anda telah memesan Aqua");
	}
	else if(minum==3){
		printf("anda telah memesan Susu");
	}
	else if(minum==4){
		printf("anda telah memesan Jus");
	}
	else if(minum==5){
		printf("anda telah memesan Kopi");
	}
	else{
		printf("tidak tersedia");
	}
}
int main(){
	int pilih;
	printf("Daftar menu Warung\n");
	printf("==============\n");
	printf("1.Menu makanan\n");
	printf("2.Menu minuman\n");
	printf("=================\n");
	printf("masukan pilihan menu anda :");scanf("%d",&pilih);
	
	switch(pilih){
		case 1:
		system("cls");
		makanan();
		break;
		case 2:
		system("cls");
		minuman();
		break;
		default:
		printf("Pilihan yang anda masukan tidak ada di daftar menu");
	}
}
