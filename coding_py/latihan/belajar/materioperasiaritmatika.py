print('materi 5: operasi aritmatika')
print('='*50)

""""
+ adalah tambah
- adalah kurang
* adalah kali
/ adalah bagi
** adalah pangkat
% adalah modulus (sisa bagi contoh 10/3 modulusnya adalah 1)
% (jika tidak ada sisa dlm pembagian contoh 9/3 modulusnya 0)
// floor division (pembagian dibulatkan kebawah contoh 10//3=3, harusnya 3.sekian)
"""

""""
prioritas operasi
1. dalam kurung
2. eksponen (**)
3. kali(*) atau bagi(/) atau modulus(%) atau floor division(//)
4. tambah(+) atau (kurang)
"""

a = 10
b = 3
hasil = a%b
print(hasil)

print()
print('Latihan')
print('='*50)
print('program konversi temperatur celcius ke satuan lain')
print('-'*50)
c = float(input('masukan suhu dalam celcius: '))
print('suhu adalah: ',c,' celcius')

#reamur 4/5*c
r= (4/5)*c
print('suhu dalam reamur adalah: ',r,' reamur')
#fahrenheit 9/5*c+32
f= ((9/5)*c)+32
print('suhu dalam fahrenheit adalah: ',f,' fahrenheit')
#kelvin c+273
k=c+273
print('suhu dalam kelvin adalah: ',k,' kelvin')
print('-'*50)

print('latihan fahrenheit ke kelvin')
print('-'*50)
fah = float(input('masukan suhu dalam fahenheit: '))
print('suhu dalam fahrenheit adalah: ',fah)
#fahrenheit ke kelvin: dengan konversi dulu fahrenheit ke celcius, lalu ke kelvin
cel = 5/9*(fah-32)
kel = cel+273
print('suhu dalam kelvin adalah: ',kel,' kelvin')
print()

print('latihan kelvin ke fahrenheit')
print('-'*50)
kelvin = float(input('masukan suhu dalam kelvin: '))
print('suhu dalam kelvin adalah: ',kelvin)
#kelvin ke fahrenheit: konversi dulu kelvin ke celcius laly ke fahrenheit
celcius = k-273
fahrenheit = ((9/5)*celcius)+32
print('suhu dalam fahrenheit adalah: ',fahrenheit,' fahrenheit')