print()
print('materi 1')
"""ini adalah komen multiline
jadi kita bisa menulis komen 
beberapa baris"""
print('hello world')

#mengenal variabel, variable adalah tempat menyimpan data
"""x = 10
x adalah variabel
10 adalah valuenya
= adalah assignment
jadi dalam python untuk deklarasi tipe data tidak memerlukan tipe data
didepan variabelnya sperti di c++ ada (int a), dalam python langsung tulis (a) saja"""
#contoh
panjang = 10000
a=50
print(panjang)
print('nilai a = ',a)

# alt + shift + panah bawah untuk copas sintax
# alt + panah bawah/atas untuk memindah-mindahkan syntax

#assignment indirect
b=a
print('nilai b sama dengan a: ',b)



print()
print('materi 2: tentang tipe data')
#tipe data
# a = 10, a adalah variabeldengan 10 value/nilainya

# tipe data angka satuan = integer
data_integer=4
print(type(data_integer))
print('data: ',data_integer, ', bertipe: ',type(data_integer))
print('-'*50)

#tipe data desimal/float (angka dengan koma koma di python gunakan titik(.)):
data_float=4.5
print(type(data_float))
print('data: ',data_float, ', bertipe: ',type(data_float))
print('-'*50)

#tipe data string(kumpulan karakter):
data_string='hallo world'
print(type(data_string))
print('data: ',data_string, ', bertipe: ', type(data_string))
print('-'*50)

#tipe data boolean(true/false) bernilai biner true=1, false=0:
data_bool= True
print(type(data_bool))
print('data: ',data_bool,', bertipe: ',type(data_bool))
print('-'*50)

#tipe data khusus:
#1. bilangan kompleks
data_complex = complex(5,6)
print(type(data_complex))
print('data: ',data_complex,', bertipe: ',type(data_complex))
print('-'*50)

#tipe data dari bahasa C: caranya seperti dibawah!

from ctypes import c_double

data_cdouble= c_double(100.5)
print(type(data_cdouble))
print('data: ',data_cdouble,', bertipe: ',type(data_cdouble))
print('-'*50)

print()
print('materi 3: casting(merubah tipe data)')
data_int=9
print('data = ',data_int, ', tipe=', type(data_int))

data_float = float(data_int)#disini merubah data int ke float dengan cara float(nama variabel tipe data lain yang ingin jadi float)
print('data = ',data_float,', tipe= ',type(data_float))

data_str = str(data_int)#int ke string
print('data = ',data_str,', tipe= ',type(data_str))

data_bol = bool(data_int)#int ke boolean, untuk boolean akan false jika dan hanya jika nilai 0
print('data = ',data_bol,', tipe= ',type(data_bol))
