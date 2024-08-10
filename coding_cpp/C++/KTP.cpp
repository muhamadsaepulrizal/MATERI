#include <stdio.h>

int main(){
	
	char
	nik[20],nama[50],ttl[50],jk[20],alamat[50],rtrw[20],keldes[40],kec[40],agama[20],sp[20],pekerjaan[40],kewarga[10],bh[20];
	
	//input
	
	printf("\tPROVINSI JAWA BARAT\n\tKABUPATEN GARUT\n");
	printf("NIk :");scanf("%19s",nik);
	while (getchar()!='\n');
	printf("Masukan Nama:");scanf("%49s",nama);
	while (getchar()!='\n');
	printf("Masukan Tempat/Tanggal lahir:");scanf("%49s",ttl);
	while (getchar()!='\n');
	printf("Masukan Jenis Kelamin:");scanf("%19s",jk);
	while (getchar()!='\n');
	printf("Masukan Alamat:");scanf("%49s",alamat);
	while (getchar()!='\n');
	printf("Masukan RT/RW:");scanf("%19s",rtrw);
	while (getchar()!='\n');
	printf("Masukan Kel/Desa:");scanf("%39s",keldes);
	while (getchar()!='\n');
	printf("Masukan Kecamatan:");scanf("%39s",kec);
	while (getchar()!='\n');
	printf("Masukan Agama:");scanf("%19s",agama);
	while (getchar()!='\n');
	printf("Masukan Status Perkawinan:");scanf("%19s",sp);
	while (getchar()!='\n');
	printf("Masukan Pekerjaan:");scanf("%39s",pekerjaan);
	while (getchar()!='\n');
	printf("Masukan Kewarganegaraan:");scanf("%9s",kewarga);
	while (getchar()!='\n');
	printf("Masukan Berlaku Hingga:");scanf("%19s",bh),
	
	
	//output

	printf("\n\tPROVINSI JAWA BARAT\n\t KABUPATEN GARUT\n");
	printf("\nNIK\t\t\t:%s",nik);
	printf("\nNama\t\t\t:%s",nama);
	printf("\nTempat/Tanggal lahir\t:%s",ttl);
	printf("\nJenis Kelamin\t\t:%s",jk);
	printf("\nAlamat\t\t\t:%s",alamat);
	printf("\nRT/Rw\t\t\t:%s",rtrw);
	printf("\nKel/Desa\t\t:%s",keldes);
	printf("\nkec\t\t\t:%s",kec);
	printf("\nagama\t\t\t:%s",agama);
	printf("\nStatus Perkawinan\t:%s",sp);
	printf("\nPekerjaan\t\t:%s",pekerjaan);
	printf("\nKewarganegaraan\t\t:%s",kewarga);
	printf("\nBerlaku Hingga\t\t:%s",bh);
	
	//fungsi (/t) untuk mewakili TAB, sedangkan untuk (/n) mewakili garis baru kali ini saya gunakan untuk memindahkan teks  ke garis berikutnya di bagian output
}
