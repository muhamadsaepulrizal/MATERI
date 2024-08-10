import os
os.system("cls")

#definisi fungsi
def tambah(a,b):
    return a + b
#angka1 = int(input("masukkan angka ke-1: "))
#angka2 = int(input("masukkan angka ke-2: "))

#print(f"{angka1} + {angka2} = {tambah(angka1,angka2)}")


#contoh yang lebih komplesk

def tambah2(a,b):
    return a+b
def kurang(a,b):
    return a-b
def kali(a,b):
    return a*b
def bagi(a,b): 
    #menghindari pembagian dengan nol(0) 
    if b != 0: #jika user menginputkan nilai bukan 0 maka pembagian jalan
        return a/b
    else: #jika user input nilai dengan 0 maka tidak jalan
        print("error tidak bisa dibagi dengan nol")
        return 0
while True:
    os.system("cls")
    angka1 = float(input("masukkan angka ke-1: "))
    operasi = input("masukkan operasi ( +|-|x|bagi(/) ): ")
    angka2 = float(input("masukkan angka ke-2: "))

    #match case bisa dipakai di python versi 3.1.0 keatas
    match operasi:
        case '+':
            print(f"{angka1} + {angka2} = {tambah(angka1,angka2)}")
        case '-':
            print(f"{angka1} - {angka2} = {kurang(angka1,angka2)}")
        case 'x':
            print(f"{angka1} x {angka2} = {kali(angka1,angka2)}")
        case '/':
            print(f"{angka1} / {angka2} = {bagi(angka1,angka2)}")
        case _: #case untuk default
            print("Tidak valid periksa operasi yang dimasukkan")
    lanjut = input("lanjut atau berhenti (y/n): ")
    if lanjut == "n":
        break
    


        
