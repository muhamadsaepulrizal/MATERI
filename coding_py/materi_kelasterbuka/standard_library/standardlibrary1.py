'''EKSPLORE DI CHROME PYTHON STANDARD LIBRARY 
    UNTUK MEPERMUDAH CODING PROGRAM KITA '''

import datetime

data_waktu = datetime.datetime.now()
print(f"waktu sekarang (lengkap): {data_waktu}") #akan keluar tahun,bulan,tangal,jam lengkap
print(f"waktu sekarang (tahun)  : {data_waktu.year}") #hanya tahun
print(f"waktu sekarang (hari)   : {data_waktu.strftime('%A')}") #hari saja

from collections import Counter

## contoh ribet:
#data = ["a","b","c","d","a","d","e"]
#
#count = 0
#for i in data:
#    if i == "a":
#        count += 1
#print(count)

## contoh dengan counter
data = ["a","b","c","d","a","d","e"]
data_count = Counter(data)
print(f"data count = {data_count}")
print(f"jumlah a   = {data_count['a']}") #ini versi simple dari kode diatas dng import Counter


import io #baca teks io (input/output)

file = io.open("file_text.txt","r") #untuk membaca file (file_text.txt)=nama filenya, (r)perintah only read/baca 
print(file.read())#u/ menampilkan isi filenya gunakan syntax berikut <-
