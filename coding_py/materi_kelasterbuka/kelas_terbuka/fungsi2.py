print("materi fungsi dengan return")
print("="*50) 

''' fungsi dengan kembalian(return value)
input masuk ke fungsi lalu fungsi mengeluarkan/mengembalikan output
tamplate fungsi dengan return(kembalian):
def nama_fungsi(argumen/input/parameter):
    badan fungsi
    return output
'''


def kuadrat(input_angka): #fungsi kuadrat
    output_kuadrat = input_angka**2 #output_kuadrat = input_angka(10) dikuadratkan
    return output_kuadrat #outputnya (output_kuadrat) di return ke y/z(atau apapun variabel) dibawah

y = kuadrat(10)#10 masuk ke fungsi jadi input_kuadrat
print(y)

#contoh lain
z = 10 + kuadrat(7)
print(z)

#bisa juga return nya langsung ke print
print(kuadrat(5))


#fungsi tambah (fungsi return dengan multi input)
def fungsi_tambah(angka_1,angka_2):
    return angka_1 + angka_2

a = fungsi_tambah(10,40)
print(a)

#fungsi dengan return banyak
def operasi_matematika(angka1,angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali   = angka1 * angka2
    bagi   = angka1 / angka2
    return tambah,kurang,kali,bagi

#berurutan returnnya
#tambah ke t, kurang ke k, kali ke k2, bagi ke b
t,k,k2,b = operasi_matematika(10,5)


print(f"hasil tambah = {t}")
print(f"hasil kurang = {k}")
print(f"hasil kali   = {k2}")
print(f"hasil bagi   = {b}")
