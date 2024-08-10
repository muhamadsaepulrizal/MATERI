import os
class belanja:
    barang = None
    Id = None
    banyak = None
    harga = None

#fungsi input data:
def input_data(data):
    data.barang = input("Masukkan Nama barang\t\t: ")
    data.Id = input("Masukkan Id barang\t\t: ")
    data.banyak = int(input("Masukkan Banyak barang\t\t: "))
    data.harga = int(input("Masukkan Harga barang (Rp.)\t: "))

#fungsi output data:
def output_data(data):
    print(f"Nama barang\t\t: {data.barang}")
    print(f"Id barang\t\t: {data.Id}")
    print(f"Banyak barang\t\t: {data.banyak}")
    print(f"Harga barang\t\t: {data.harga}")

os.system("cls")
#menampilkan judul Program
print("Program Penjualan Barang".center(60))
print("".center(60,"="))
print()

#input jumlah barang
jumlah_barang = int(input("Masukkan Jumlah Barang: "))
print("\n")

#deklarasi array di class "belanja
data_barang = [belanja() for _ in range(jumlah_barang)]

print("input data barang".center(60,"-"))
#looping input data barang:
for i in range(jumlah_barang):
    print("Input Data Barang ke-", i+1)
    input_data(data_barang[i])
    print()

print("output data barang".center(60,"-"))
#looping output data barang:
for i in range(jumlah_barang):
    print("\nOutput Data Barang ke-",i+1)
    output_data(data_barang[i])
#menghitung total belanja
total_belanja = sum(data.banyak*data.harga for data in data_barang)
print(f"\nTotal Belanja: Rp.{total_belanja}")

    
