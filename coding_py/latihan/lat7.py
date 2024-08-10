saldo_awal = 5000
hutang=50000
print()
print('            program latihan sederhana dengan saldo')
print('='*70)
print('saldo awal anda sejumlah                    : '+str(saldo_awal))
print('hutang anda sejumlah                        : '+str(hutang))
deposit= int(input('masukan jumlah deposit anda                 : '))
saldo_akhir= saldo_awal+deposit
print('Terima kasih sudah depo, Saldo anda sekarang: '+str(saldo_akhir))

if saldo_akhir >= 50000:
    print('saldo anda cukup untuk bisa bayar hutang')
else:
    print('saldo anda kurang untuk bayar hutang')
print('='*70)
