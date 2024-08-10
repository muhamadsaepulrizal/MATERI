import os
os.system("cls")
#bentuk umum dalam struct/class dalam python:
'''
class nama_objek:
    variabel1 = nilai
    variabel2 = nilai
nama_pengguna = nama_objek
'''
#contoh
'''
class belanja:
    barang = None
    id = None
    harga = None
    banyak = None
data = belanja
'''

#definisikan struct "belanja"
class belanja:
    barang = None
    harga = None
    banyak = None
    Id = None

print("Program Penjualan Barang".center(60))
print("".center(60,"="))

#input data untuk barang  1:
print("input data barang".center(60,"-"))
data = belanja()
data.barang = input("Masukkan Nama barang\t\t: ")
data.Id = input("Masukkan Id barang\t\t: ")
data.banyak = int(input("Masukkan Banyak barang\t\t: "))
data.harga = int(input("Masukkan Harga barang (Rp.)\t: "))
print()
print()

#menampilkan data untuk barang 1:
print("output data betang".center(60,"-"))
print(f"Nama barang   : {data.barang}")
print(f"Id barang     : {data.Id}")
print(f"Banyak barang : {data.banyak}")
print(f"Harga barang  : {data.harga}")

#menghitung total belanja:
total = data.banyak*data.harga
print("".center(60,"="))
print(f"Total belanjaan adalah = {total}")









