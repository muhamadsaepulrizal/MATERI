import os
os.system('cls')
print("\nmateri default argument")
print("="*70)

#default fungsi argumen adalah fungsi tanpa argument

#contoh default argument 1 dengan 1 variabel
def say_hello(nama = "ganteng"):
    print(f"Hallo {nama}")

say_hello("rizal")
say_hello()

#contoh 2, fungsi dengan 1 input biasa dan 1 default argument
def sapa_dia( nama, pesan="apa kabar?"):
    print(f"hai {nama}, {pesan}")

sapa_dia( "dudung","kamu ganteng")
sapa_dia("otong")

#contoh 3
def hitung_pangkat(angka, pangkat=2):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,3))
hasil = hitung_pangkat(angka=5,pangkat=3)#argument yang paling bawah yg dipakai
print(hasil)

#contoh 4 merubah salah satu,
def fungsi(input1=1, input2=2, input3=3, input4=4):
    hasil = input1+input2+input3+input4
    return hasil

print(fungsi())
print(fungsi(input4=5))#merubah salah satu argument diatas
    
