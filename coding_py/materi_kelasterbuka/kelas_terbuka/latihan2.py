print()
print('Latihan')
print('='*50)

# soal: ---0+++5---8+++11----
user = float(input('masukan angka: '))
#---0+++
lebih1 = (user > 0)
print('lebih dari 0: ',lebih1)
#+++5---
kurang1 = (user < 5)
print('kurang dari 5: ',kurang1)
#---8+++
lebih2 = (user > 8)
print('lebih dari 8: ',lebih2)
#+++11---
kurang2 = (user < 11)
print('kurang dari 11: ',kurang2)

#---0+++5---8+++11----
hasil1 = lebih1 and kurang1
hasil2 = lebih2 and kurang2
hasilakhir = hasil1 or hasil2
print('angka yang anda masukkan: ',hasilakhir)
