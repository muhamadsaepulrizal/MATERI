#include <iostream>
#include <cstdlib> //mengandung fungsi random salah satu syntax fungsinya ( rand() )

using namespace std;

int main(){
	 char lanjut;
	 
	 while (true){
	 	cout <<"Lempar Dadu |y/n|"; cin>>lanjut;
	 	if (lanjut == 'y'){
	 		cout <<"Angka "<< 1 + (rand() %6  ) <<endl;
		 }else if (lanjut == 'n'){ 
		 	break;
		 }else{
		 	cout <<"Warning: Ketik y atau n, bro bro dan mba sis!!"<<endl;
		 }
	 }
	
	cin.get();
	return 0;
}
