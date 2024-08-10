import os
#print("\nLatihan Fungsi")
#print("="*50)

##program menghitung luas dan keliling persegi panjang
def header():
    '''ini adalah fungsi untuk header''' #bagusnya komen seperti ini saat dibawah fungsi bisa dipakai keterangan saat fungsi di panggil di main program
    os.system('cls')
    print(f"{'PROGRAM MENGHITUNG LUAS':^50}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^50}")
    print("1. Hitung Luas")
    print("2. Hitung Keliling")
    print(f"{'-'*50:^50}")

def input_user():
    '''ini adalah fungsi untuk input user'''
    lebar = int(input("Masukkan Nilai Lebar: "))
    panjang = int(input("Masukkan Nilai Panjang: "))
    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''ini adalah fungsi menghitung luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''ini adalah fungsi menghitung keliling'''
    return 2*(lebar+panjang)

def display(massage,value):
    '''ini adalah fungsi display dengan tamplate (Hasil Perhitungan)
    ada 2 nilai (massage for pesan spesifik, value for nilai yang ingin ditampilkan)'''
    print(f"Hasil Perhitungan {massage} = {value}")



#main program
while True:
    header()
    opsi = input("Pilih Perhitungan (1/2): ")
    if opsi == "1":
        #buat konstanta dengan penulisan pakai capslock untuk menampung fungsi fungsi diatas:
        LEBAR,PANJANG = input_user()
        LUAS = hitung_luas(LEBAR,PANJANG)
        display("Luasnya adalah", LUAS)
    elif opsi == "2":
        #buat konstanta dengan penulisan pakai capslock untuk menampung fungsi fungsi diatas:
        LEBAR,PANJANG = input_user()
        KEL = hitung_keliling(LEBAR,PANJANG)
        display("Kelilingnya adalah", KEL)
    else:
        print("invalid pilih 1 atau 2")
    
    isContinue = input("apakah lanjut (y/n)?: ")
    if isContinue == "n":
        break


print(f"{'-'*50:^50}")
print(f"{"Program selesai Thanks":^50}")



