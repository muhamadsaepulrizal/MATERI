'''Exception, Error, Try and Except'''
# salah satu untuk saat input 0 di operasi pembagian/ runtime error
# exception akan terjadi saat program mengalami error saat runtime

#contoh sederhana u/ menangkap exception

from math import nan

## Contoh Sederhana
# input_user = int(input("masukkan angka: "))
# hasil = nan
# 
# try:
#     hasil = 10/input_user
# except:
#     print("input tidak boleh 0")
# print(f"hasil = {hasil}")

## Contoh 1
# jadi ketika input salah program akan meminta input yg benar dengan try and except 
while(True):
    angka = int(input("msukkan angka pembagi: "))
    try:
        hasil = 10/angka
        print(f"hasil = {hasil}")
        is_done =  input("lanjutkan (y/n)? : ")
        if is_done == "n":
            break
    except:
        print("\npembagi nol silahkan input angka lain!!! ")

print("akhir dari program 1\n")


## Contoh 2

try:
    with open("data.txt","r") as file: #coba cek apakah ada file data.txt
        print(file.read()) #baca apakah ada
    #break
except: #jika tidak ada maka except akan dijalankan lalu membuat file data.txt
    #dengan codingan berikut 
    print("file data.txt tidak ditemukan, membuat file baru")
    with open("data.txt","w",encoding="utf-8") as file:
        file.write("file baru")
    #break

print("akhir dari program 2")







