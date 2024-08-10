#include <stdio.h>

int main(){
	
	int x[5];
	
	printf("%p\n",(void*)&x[0]);
	printf("%p\n",(void*)&x[1]);
	printf("%p\n",(void*)&x[2]);
	printf("%p\n",(void*)&x[3]);
	printf("%p\n",(void*)&x[4]);
	
	
	return 0;
}
