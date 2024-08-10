#perkondisian atau if, elif, else
# susunannya: 1.if 2.elif 3.else

# == (sama dengan)
# > (lebih dari)
# < (kurang dari)
# != (tidak sama dengan)
# >= (lebih besar sama dengan)
# <= (kurang dari sama dengan)
# ada juga AND(dan) dan or(atau)

#usia = 22
#if usia == 20:
#    print('anda masih muda dan remaja')
#else:
#    print('gak cocok')

print('='*55)
print('                      program cek usia')
print('='*55)
usia = int(input('Silahkan masukan usia anda(dalam bentuk angka): '))

if usia >= 5 and usia <= 10:
    print('hallo anda masih anak anak!')
elif usia >10 and usia <=20:
    print('hallo anda sudah remaja!')
elif usia >20 and usia <=50:
    print('hallo anda sudah dewasa!')
elif usia >50 and usia <=80:
    print('hallo anda sudah lansia!')
else:
    print('--anda sudah hampir mati WASPADA!--')
print('')
print('terima kasih')
print('='*55)



