print("\nMateri Perulangan for")
print("="*50)

#perulangan (looping)

#perulangan for
#for kondisi:
#    aksi

#ini dengan list
angka2 =[0,5,2,10,4]#ini adalah list, list cocok untuk acak
print(angka2)

for i in angka2:# i atau yg lain, hanya pengantu variabel yg akan dimasukan ke looping
    print(f"i sekarang --> {i}")
print("akhir program 1\n")

#ini dengan range
angka3 = range(5)#range cocok untuk berurutan
for i in angka3:
    #print(f"i sekarang --> {i}")
    print("saya keren")
print("akhir program 2\n")
    
angka4 = range(1,5)#range cocok untuk berurutan, angka 1 untuk kita mau mulai dari 1
for i in angka4:
    print(f"i sekarang --> {i}")
print("akhir program 2\n")

#menggunakan string
datastr = "saya ganteng"#huruf dari kata "saya ganteng" akan berjejer kebawah
for huruf in datastr:
    print(huruf)
print("-"*50)

print("\n\nMateri While looping")
print("="*50)
#while = ketika
#while kondisi:
#        aksi

angka = 0 #si 0 ini akan masuk ke looping lalu ditambah 1, sampau 5 dan looping berhenti
print(f"angka awal -> {angka}")

while angka < 5:#kondisi jika True maka dijalankan, jika False maka akan berhenti
    angka += 1 #inisiasi supaya while loop berhenti jadi saat diulang 0 ditambah 1 sampai 5, dan 5 tidak lebih besar dari 5
    print(f"angka saat looping -> {angka}")
    print("kece abiez")
print("cukup")
print("-"*50)


print("\n\nMateri Continue And Pass And Break")
print("="*50)
# continue, pass, break

#pass ->> berfungsi sebagai dami, tidak akan di eksekusi
angka = 0
while angka < 5:
    angka += 1
    if angka == 3:#angka 3 akan diganti wadaw
        pass #tidak akan dieksekusi
        #print("wadaw")
    print(angka)

#continue akan membuat meloncat ke aksi selanjutnya
angka = 0
print(f"angka sekarang --> {angka}")
while angka < 5:
    angka += 1
    print(f"angka sekarang --> {angka}") #aksi 1
    if angka == 3:
        print("nice balik lagi")
        continue#fungsinya akan balik lagi langsung ke looping, printa("wassup")/yg lain dilewat/skip ke step selanjutnya
    print("wassup!") #aksi 2 yag dicontohkan dilewat/ continue

print("finish")
print("-"*10)

#break

#contoh break 1
angka = 0
while angka < 5:
    angka += 1
    print(f"angka sekarang {angka}")
    if angka == 3:
        print("stop")
        break
    print("masih jalan")
print("akhir")
print("-"*10)

#contoh break 2
data = int(input("mau hitung sampai berapa: "))
angka = 0

while True:
    angka +=1
    print(f"count = {angka}")

    if  angka == data: #jika angka = data yang dimasuka(data)
        print("stop/break")# maka print nice lalu dibawah di breakk supaya berhenti sesuai data yang dimasukkan (data)
        break#akasn nge cut dari 3 (nice), 4 dan 5 tidak di looping (di break)
    print("lanjut")
print("cukup finish")
print("-"*50)














