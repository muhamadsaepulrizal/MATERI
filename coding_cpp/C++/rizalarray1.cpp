#include <conio.h>
#include <stdio.h>
main()
{
	int i;
	char nama[5][20];
	float nilai1[5];
	float nilai2[5];
	float hasil[5];
	for(i=1; i<=2; i++)
	{
		printf("Data ke- %d \n",i);
		printf("Nama Siswa :"); scanf(" %[^\n]",&nama[i]);
		printf("Nilai MidTest :"); scanf("%f", &nilai1[i]);
		printf("Nilai final :"); scanf("%f", &nilai2[i]);
		hasil[i] = (nilai1[i] * 0.40)+ (nilai2[i]*0.60);
		printf("\n");
	}
	printf("----------------------------------------------------");
	printf("-------------\n");
	printf("No.     Nama Siswa             Nilai    Nilai  Hasil\n");
	printf("                               Midtest  Final  Ujian\n");
	printf("----------------------------------------------------");
	printf("-------------\n");
	for(i=1; i<=2; i++)
	{
		printf("%-4d\t",i);
		printf("%-20s\t",nama[i]);
		printf("%.2f\t",nilai1[i]);
		printf("%.2f\t",nilai2[i]);
		printf("%.2f\n",hasil[i]);
	}
	printf("-----------------------------------------------------");
	printf("-------------\n");
	getch();
}

