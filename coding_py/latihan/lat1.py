#print('hello bro')

# variabel untuk tipe data string nama = 'rizal'
nama = 'bambang' #tipe data string
usia = 20 #tipe data integer
tinggi_badan = 170.5 #tipe data float/decimal
punya_duit = True #tipe data boolean/bool bernilai True/False
punya_duit = False #menimpa yang atas

#menyapa = 'hallo semua nama saya '
#print(menyapa + nama)

#konfersi tipe data saat pemangilan 
#int(10) ==> 10
#str(5) ==> '5'
#float(5) ==> 5.0

print('hallo nama saya ' + nama)
print('usia saya ' + str(usia)) #output harus str karena awalnya sudah str
print('tinggi badan saya ' + str(tinggi_badan))
print(punya_duit)

print('hallo nama saya adalah ' + nama + ' usia saya adalah ' + str(usia) + ' tinggi badan saya adalah ' + str(tinggi_badan) + ' cm dan saya sedang tidak punya duit? ' + str(punya_duit))