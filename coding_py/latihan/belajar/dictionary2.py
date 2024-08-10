import datetime


print("\nMateri Multi Keys & Nesting Dictionary")
print("="*50)



mhs1 = {
    'nama':'ucup surucup',
    'nim': '2306142',
    'sks_lulus':130,
    'beasiswa':False,
    'lahir':datetime.datetime(2004,12,10)
}

mhs2 = {
    'nama':'otong surotong',
    'nim': '2306160',
    'sks_lulus':140,
    'beasiswa':True,
    'lahir':datetime.datetime(2004,5,11)
}

mhs3 = {
    'nama':'asep sikasyep',
    'nim': '2306155',
    'sks_lulus':135,
    'beasiswa':False,
    'lahir':datetime.datetime(2004,10,29)
}


data_mhs ={
    'MAH001': mhs1,
    'MAH002': mhs2,
    'MAH003': mhs3
}

print(F"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*50)

for mhs in data_mhs.keys():
    KEY = mhs
    NAMA = data_mhs[KEY]['nama']
    NIM = data_mhs[KEY]['nim']
    SKS = data_mhs[KEY]['sks_lulus']
    BEASISWA = data_mhs[KEY]['beasiswa']
    LAHIR = data_mhs[KEY]['lahir'].strftime("%x")

    
    print(F"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")


#Note : >6(rata kanan), <6(rata kiri), ^6(center)




