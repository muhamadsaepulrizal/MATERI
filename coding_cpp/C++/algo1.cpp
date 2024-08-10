#include <stdio.h>

int main(){
	
	int a = 10;
	int *p = &a;
	
	printf("Alamat memori dari variabel a yaitu = %p dengan nilai = %d\n", &a, a);
	printf("Pointer p menyimpan alamat pada memori = %p dengan nilai = %d\n\n",p,*p);
	
	a = 20;
	
	printf("Alamat memori dari variabel a yaitu = %p dengan nilai = %d\n", &a, a);
	printf("Pointer p menyimpan alamat pada memori = %p dengan nilai = %d\n\n",p,*p);
	
	int b = 25;
	p = &b;
	
	printf("Alamat memori dari variabel a yaitu = %p dengan nilai = %d\n", &a, a);
	printf("Pointer p menyimpan alamat pada memori = %p dengan nilai = %d\n",p,*p);
	
	
	return 0;
}
