'''Tutorial membaca file ekxternal (.txt)'''

import os
os.system("cls")

print(3*"=", " Membaca file txt ",3*"=")

#dibuka dengan open
file = open("data.txt",mode="r") #menampung isi file txt kedalam sebuah var dengan("r")= only read

#cek status apakar read,write, dll
print(f"1. status read : {file.readable()}")#bisa dibaca? (True/False)
print(f"2. status write: {file.writable()}")#bisa ditulsi? (True/Flase)



# print(file.read())#untuk membaca isi seluruh file nya u/ only read ("r")

# print(file.readline(),end="") #untuk membaca isi file baris perbaris
# print(file.readline(),end="") #(,end="") u/ saat line selanjutnya tidak pakai enter \n diganti str kosong

# print(file.readlines())#untuk mebaca isi seluruh file tapi dlm bentuk list



print(f"apakah file sudah di close: {file.closed}")
#harus ditutup dengan close
file.close()
print(f"apakah file sudah di close: {file.closed}")

## salah satu teknik membuka file di python
print("\n",3*"=", " Membaca file txt dengan with ",3*"=")

#lebih simple pakai with u/ mengolah file didalamya
with open("data.txt",mode="r") as file:
    content = file.readline()
    print(content,end="") 
    print(f"apakah file sudah di close: {file.closed}") #ini akan false karena masih dibuka

print(f"apakah file sudah di close: {file.closed}") #ini akan True karea sudah ditutup



