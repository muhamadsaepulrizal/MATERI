import datetime
import os
import string
import random

print("\nMateri Latihan Dictionary")
print("="*50)

#tamplate dict mahasiswa
mhs_tamplate = {
    'nama':'nama',
    'nim':'0000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mhs ={}

# for windows os.system('cls')
# for linux os.system('clear')
while True:
    os.system("cls")

    print(f"{'Selamat datang':^20}")
    print(f"{'Data Mahasiswa':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mhs_tamplate.keys())#cara mengubah tampalte mhs_tamplate diatas jadi kosong
    #print(mahasiswa)


    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("Nim Mahasiswa: ")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
    TAHUN = int(input("Tahun lahir (YYYY): "))
    BULAN = int(input("Bulan lahir (1-12): "))
    TANGGAL = int(input("Tanggal lahir (1-31): "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN,BULAN,TANGGAL)

    #print(mahasiswa)
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mhs.update({KEY:mahasiswa})#untuk memasukkan ke dict kosong diatas
    
    #header
    print(f"\n{'KEY':<6} {'NAMA':<17} {'NIM':<8} {'SKS Lulus':<10} {'Tanggal Lahir':<10}")
    print("-"*50)
    for mhs in data_mhs.keys():

        KEY = mhs
        NAMA = data_mhs[KEY]['nama']
        NIM = data_mhs[KEY]['nim']
        SKS = data_mhs[KEY]['sks_lulus']
        #BEASISWA = data_mhs[KEY]['beasiswa']
        LAHIR = data_mhs[KEY]['lahir'].strftime("%x")
        print(F"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")
    print("\n")
    bereskah = input("Sudah beres? (y/n): ")
    if bereskah == 'n':
        break

print("\nAkhir program")















