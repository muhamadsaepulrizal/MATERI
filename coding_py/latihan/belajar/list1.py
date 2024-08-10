print("\nMateri List")
print("="*50)
## List
## list (kumpulan data) atau pengganti array jika dibahasa lain tapi bisa untuk beda tipe data

#Kumpulan data numbers
data_angka=[1,2,3]
print(data_angka)

#kumpulan data string
data_string = ["ucup, otong, odah"]
print(data_string)

#kumpulan data boolean
data_bool = [True,False,False,True]
print(data_bool)

#kumpulan campuran
data_mix = [1, "bala-bala", 2, "cireng", "ucup", True, "otong", False]
print(data_mix)

## cara alternatif membuat list
data_range = range(0,10,2)#angka pertama=awal, kedua=sebelum akhir, ketiga=increment/ (start,stop,step)
print(data_range)
data_list = list(data_range)#jadi muncul dari 0 sampai 9
print(data_list)

#membuat list dengan for loop, list comprehension
datalist_pakefor = [i**2 for i in range(0,10)]
print(datalist_pakefor)

#membuat list pake for dan if
list_for_if = [i for i in range(0,10) if i != 5]
print(list_for_if)

#genap
list_for_if = [i for i in range(0,10) if i % 2 == 0]
print(list_for_if)

#ganjil
list_for_if = [i for i in range(0,10) if i % 2 == 1]
print(list_for_if)
print("-"*50)

print("\n\nMateri manipulasi list2")
print("="* 50)
##operasi / manipulasi data list

data = ["ucup", "otong", "dudung"]#berdasarkan index [0,1,2]/ mulai dari belakang gunakan [-1]
print(data)

#mengambil data dari list
dataa = data[0]
print(f"data pertama/ index 0 = {dataa}")
data_akhir = data[2]#[2]/[-1] untuk menagmbil data terakhir jika tidak tau berapa datanya
print(f"data terakhir adalah = {data_akhir}")

#mengambil info jumlah data dalam list
panjang_data = len(data)#dihitung bukan dari index 0
print(f"panjang datanya = {panjang_data}")

##manipulasi data list

#menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = {data}")
data.insert(1,"asep")#data.insert(posisi,item)
print(f"data sesudah ditambah = {data}")

#menambah data diakhir (bisa pakai append)
data.append("jajang")#append otomatis diakhir
print(f"data sesudah ditambah diakhir = {data}")

#menggabungkan list
data_baru = ["ujang", "usep", "dadu"]
data.extend(data_baru)#data_baru otomatis ada diakhir setelah data
print(f"data gabungan  = {data}")

#MERUBAH DATA
# kita ubah data ke 2 (otong) jadi (michael)
data[2] = "michael" #si "otong" diganti jadi "michael" 
print(f"data rubahan  = {data}")

#menghilangka data
data.remove("ujang")#si "ujang" dihapus
print(f"data remove  = {data}")

#menghilangkan data paling belakang
dataakhir=data.pop()#"dadu" dihilangkan
print(f"data akhir diremove  = {data}")

print(f"data yang dihilangkan diakhir yaitu = {dataakhir}")
print("-"*50)

print("\nMateri operasi list")
print("="*50)
data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
print(f"data angka:\n{data_angka}")

#count angka: menghitung berapa kali angka tsb muncul pakai .count
jumlah_data4 = data_angka.count(4)
jumlah_data3 = data_angka.count(3)
print(f"jumlah data 4 = {jumlah_data4}")
print(f"jumlah data 3 = {jumlah_data3}")

#ambil/hitung posisi / (ambil index)
data = ["ucup", "otong", "dudung", "ujang"]
print(f"data = {data}")

index_dudung = data.index("dudung")
print(f"data dudung ada di index ke-{index_dudung}")
index_ujang = data.index("ujang")
print(f"data ujang ada di index ke-{index_ujang}")

#mengurutkan list
#angka
print(f"data angka sebelum di sort/urut: {data_angka}")#sebelum di sort
data_angka.sort()#proses/ cara mengurutkan
print(f"data angka setelah di sort/urut: {data_angka}")#setelah di sort

#string: berdasarkan urutan huruf depannya berdasarkan abjad/ berguna untuk absen
print(f"data angka sebelum di sort/urut: {data}")#sebelum di sort
data.sort()
print(f"data angka setelah di sort/urut: {data}")#sebelum di sort

#balik list/ dari besar kekecil, syarat harus di sort dahulu
data_angka.reverse()
print(f"data angka setelah di sort/urut lalu dari yang terbesar: {data_angka}")#setelah di sort
print("-"*50)

print("\nMateri copy list")
print("="*50)

## teknik menduplikat list
a = ["ucup","otong","dudung"]
print(f"a = {a}")
b = a
print(f"b = {b}")#sama dengan a

#merubah member dari a

#merubah kedua list
a[1]="michael"#merubah a dan b juga
b.sort()#bahkan saat sort b, a pun juga ikut ke sort
print(f"a = {a}")
print(f"b = {b}")#sama dengan a
print(f"a = {a}")
print(f"b = {b}")#sama dengan a

#addres kedua list
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")#kenapa ikut, karena address sama

#menduplikat list supaya jika 1 dirobah, 1 nya lagi gak ikut robah
#dengan copy
print("list c dengan a.copy()/ full duplicat")
c = a.copy()#membuat list baru dng address beda
print(f"a = {a}")#sama dengan b
print(f"b = {b}")#sama dengan a
print(f"c = {c}")#sama tapi address beda
print(f"address a = {hex(id(a))}")#sama
print(f"address b = {hex(id(b))}")#sama
print(f"address c = {hex(id(c))}")#beda addres 
print("kita ubah data 0")
c[1]= "acep"
print(f"a = {a}")#sama dengan b
print(f"b = {b}")#sama dengan a
print(f"c = {c}")#sama tapi address beda dan dirubah pun diatas gak rubah
print("-"*50)



































