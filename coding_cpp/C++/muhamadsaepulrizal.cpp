#include <stdio.h>
int main(){
	//peogram konversi suhu dari celcius ke fahrenheit
	
	float suhu_celcius, suhu_fahrenheit;
	printf("masukan suhu celciusnya :");
	scanf("%f",&suhu_celcius);
	
	suhu_fahrenheit = (suhu_celcius * 9/5) + 32;
	
	printf("suhu fahrenheitnya adalah : %.2f\n", suhu_fahrenheit);
	
}

