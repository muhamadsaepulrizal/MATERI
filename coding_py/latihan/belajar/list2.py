print("\nMateri nested list/list bersarang")
print("="*50)

data_0 = [1,2]
data_1 = [3,4,5]


data_list_biasa = [1,2,3,4]
print(f"list biasa = {data_list_biasa}")

#list didalam list
list_2d = [data_0,data_1]
print(f"list 2d = {list_2d}")

#contoh penggunaan
peserta_0 = ["ucup", 25, "laki-laki"]
peserta_1 = ["otong", 14, "laki-laki"]
peserta_2 = ["dedeh", 50, "wanita"]

list_peserta = [peserta_0,peserta_1,peserta_2]
print(f"peserta = {list_peserta}")


for i in list_peserta:
    print(f"Nama         : {i[0]}")
    print(f"Umur         : {i[1]}")
    print(f"Jenis kelamin: {i[2]}\n")

#masalah dengan reference
list_copy = list_peserta.copy()
print(f"peserta copy  = {list_copy}")
print("-"*50)

print("\nMateri deep copy nested list")
print("="*50)

data_0 = [1,2]
data_1 = [3,4]

data_2d = [data_0,data_1,10]
print(f"data      = {data_2d}")
data_2dcopy = data_2d.copy()
print(f"data copy = {data_2dcopy}")


#mengambil data dari nested list
data = data_2d[0][0]#mengambil depannya aja [1] [index list1][index didalam list 1]
print(f"data = {data}")


#adress semuanya
print(f"address data      = {hex(id(data_2d))}")
print(f"address data copy = {hex(id(data_2dcopy))}")

print("address dari member ke-1")
print(f"address data      = {hex(id(data_2d[0]))}")
print(f"address data copy = {hex(id(data_2dcopy[0]))}")

data_2d[1][0] = 5
data_2d[2] = 9
print(f"data      = {data_2d}")
print(f"data copy = {data_2dcopy}")

#menggunakan deep copy untuk meng copy nested list dengan import librarynya 
#seperti dibawah
from copy import deepcopy

data_2d = [data_0,data_1,10]
data_2d_deepcopy = deepcopy(data_2d)
print(f"address data          = {hex(id(data_2d))}")
print(f"address data deepcopy = {hex(id(data_2d_deepcopy))}")

print("address dari member ke-1")
print(f"address data          = {hex(id(data_2d[0]))}")
print(f"address data deepcopy = {hex(id(data_2d_deepcopy[0]))}")

print("merubah member")
data_2d[1][0]= 300
print(f"data          = {data_2d}")
print(f"data copy     = {data_2dcopy}")
print(f"data deepcopy = {data_2d_deepcopy}")
print("-"*50)


print("\nMateri looping list dan enumerate")
print("="*50)
#looping dari list

#for loop
print("for loop")
kumpulan_angka = [4,6,7,3,5,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")


peserta = ["ucup","otong","dadang","diding"]

for nama in peserta:
    print(f"nama = {nama}")

#for loop dan range/ lebih ribetnya
print("\nfor loop dan range")
kumpulan_angka = [10,5,6,4,2,9]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

#while loop
print("\nwhile loop")

kumpulan_angka = [9,5,6,3,4]
panjang = len(kumpulan_angka)

i = 0
while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

#list komprehension
print("\nlist comprehension")
data = ["ucup",8,9,3,"otong"]
[print (f"data = {i}") for i in data]

angka = [9,5,6,3,4]
print(f"angkanya   = {angka}")
angka_kuadrat = [i**2 for i in angka]
print(f"kuadratnya = {angka_kuadrat}")


#enumerate : diambil data dan indexnya
print("\nEnumerate")
data_list = ["ucup",8,9,3,"otong"]

for index,data in enumerate(data_list):
    print(f"index={index}, nama={data} ")
















































