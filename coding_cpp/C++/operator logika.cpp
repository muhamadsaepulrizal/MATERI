#include <iostream>
using namespace std;

int main()
{
	int a = 3;
	int b = 2;
	
	bool hasil;
	
	//operator logika ada not(!), ada and (==), ada or(or).
	
	//not (!) : megubah yang true menjadi false atau yang false menjadi true
	cout<<"untuk not"<<endl;
	hasil = !(a==3);
	cout<<hasil<<endl;
	
	//and (and/&&) : kadua nilai harus benar untuk menghasilkan nilai True
	cout<<"untuk and"<<endl;
	hasil = (a==3) && (b==2); //true and true = True
	cout<<hasil<<endl;
	hasil = (a==4) && (b==2); //false and true = False
	cout<<hasil<<endl;
	hasil = (a==3) and (b==4); //true and false = False
	cout<<hasil<<endl;
	hasil = (a==5) and (b==4); //fals and false = False
	cout<<hasil<<endl;
	
	/*or (or/||) : jika kedua nilai benar hasilnya True dan
					jika salah satu nilai yang benar antara dua nilai atau lebih maka hasilnya tetap True 
					dan akan False jika kedua atau semua nilai salah
	*/
	cout<<"untuk or"<<endl;
	hasil = (a==3) || (b==2); //true and true = True
	cout<<hasil<<endl;
	hasil = (a==4) || (b==2); //false and true = True
	cout<<hasil<<endl;
	hasil = (a==3) or (b==4); //true and false = True
	cout<<hasil<<endl;
	hasil = (a==5) or (b==4); //fals and false = False
	cout<<hasil<<endl;
	
	
	
	
	cin.get();
	return 0;
}
