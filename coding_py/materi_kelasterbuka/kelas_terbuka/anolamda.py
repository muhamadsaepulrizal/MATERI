import os
os.system('cls')
#lambda function
print("MATERI LAMBDA FUNCTION")
print("-"*50)
'''fungsi yang lebih simple'''


#dengan fungsi biasa
def f_kuadrat(angka):
    return angka**2

print(f"hasil dari function kuadrat = {f_kuadrat(3)}")

#dengan lambda function, berikut penulisannya:
# output = lambda argument/input : expression/operasi/dll
kuadrat = lambda angka: angka**2
print(f"hasil dari lambda kuadrat   = {kuadrat(9)}")

#contoh lain lambda dengan 2 input
pangkat = lambda num,pow: num**pow
print(f"hasil dari lambda pangkat   = {pangkat(4,2)}")

##kegunaan?

#sorting untuk list biasa
data_list = ["otong","ucup","dudung"]
data_list.sort()#berurutan berdasarkan urutan alfabet
print(f"sorted list by urutan alpabet = {data_list}")

#sorting berdasarkan panjang huruf
#data_list.sort(key=len)#berurutan berdasarkan data list dengan huruf paling sedikit
#print(f"sorted list by panjang tanpa lambda = {data_list}")

#jika dengan fungsi seperti dibawah ini:
def panjang_nama(nama):
   return len(nama)

data_list.sort(key=panjang_nama)
print(f"sorted list by panjang pakai function = {data_list}")

#sor berdasarkan panjang huruf pakai lambda
data_list = ["otong","ucup","dudung"]
data_list.sort(key= lambda nama:len(nama)) #bentuk ini menggantikan penulisan dengan fungsi seperti diatas
print(f"sorted list by panjang pakai lambda = {data_list}")


##filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

#versi ribet
def kurang_dari_lima(angka):
    return angka<5
data_angka_baru = list(filter(kurang_dari_lima,data_angka))
print(data_angka_baru)

#versi simple
data_angka_baru2 = list(filter(lambda x: x<=5,data_angka))
print(data_angka_baru2)

#kasus genap
data_genap = list(filter(lambda x:(x%2==0),data_angka))
print(data_genap)

#kasus ganjil
data_ganjil = list(filter(lambda x:(x%2!=0),data_angka))
print(data_ganjil)

#kelipatan 3
data_3 = list(filter(lambda x:(x%3==0),data_angka))
print(data_3)
print("\n")

#anonymous function
# currying <= Hasekell Curry(salah satu pembuat teknik lambda)
def pangkat(angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(5,2)
print(f"ini adalah hasil pangkat dari fungsi biasa: {data_hasil}")

#dengan currying menjadi:
def pangkatt(n):
    return lambda angka: angka**n

pangkat2 = pangkatt(2)#jadi disini 2 sebagai pangkatnya
print(f"5 pangkat 2 adalah {pangkat2(5)}")

pangkat3 = pangkatt(3)
print(f"5 pangkat 3 adalah {pangkat3(5)}")

#bisa juga seperti ini
print(f"pangkat bebas adalah {pangkatt(2)(5)}") #penulisan (2)untuk pangkat, (5)u/ yg dipangkatkan


