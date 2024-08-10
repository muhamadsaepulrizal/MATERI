import os
os.system("cls")

'''global and lokal scope(lokal scope variabel)
    global = bisa dikases diambil langsung,
    dengan note: jika ingin dirubah harus tambahkan syntax (global) sebelum nulis variabel
    dan syntax global hanya berlaku di fungsi,
    sedangkan di loop dan if-else tidak perlu pakai syntax global dan var lokal pun bisa diakses 
    lokal = hanya didalam saja (didalam fungsi,dll)
'''

#variabel global
nama_global = "ujang" #ini <- disebut variabel global

#akses variabel global didalam fungsi
def fungsi1():
    print(f"fungsi menampilakan {nama_global}")
fungsi1()

#akses variabel global dalam loop
for i in range(0,5):
    print(f"Loop {i} - {nama_global}")

#akses varabel global dalam percabangan
if True:
    print(f"if menampilkan {nama_global}")

#variabel lokal scope
def fungsi2():
    nama_lokal = "ucup" #ini <- adalah variabel lokal scope yg hanya hidup didlm fungsi2

fungsi2()
#print(nama_lokal) #jadi yg ini tidak bisa dilakukan

#contoh 1: penggunaan (akses variabel)
nama = "otong"
def say_otong():
    print(f"Hello {nama}")

say_otong()
#bisa juga seperti ini karena namanya disebut sebelum perintah menampilakan
#def say_otong():
#    print(f"Hello {nama}")
#nama = "otong"
#
#say_otong()
##seperti ini baru tidak bisa karena perintah say_otong() dilakukan sebelum penyebutan var (namanya)
#def say_otong():
#    print(f"Hello {nama}")
#
#say_otong()
#nama = "otong"

#contoh 2: merubah variabel global
angka = 0 #var global
name = "ucup"

def ubah(angka_baru, name_baru):
    #syntax global hanya berlaku di fungsi
    global angka #fungsi ini mendapat akses merubah angka / (variabel global)
    global name #fungsi ini mendapat akses merubah name / (variabel global)
    angka = angka_baru
    name = name_baru

print(f"sebelum dirubah {angka,name}")
ubah(11,"asep")
print(f"sesudah dirubah {name} {angka}")

#contoh 3:
angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0
    
print(angka)
print(angka_dummy)

if True:
    angka = 5
    angka_dummy = 5

print(angka)
print(angka_dummy)









