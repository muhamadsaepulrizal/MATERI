#array adalah variabel kumpulan tipe data yang sejenis
coding = ['python', 'c++', 'pascal']#array dibaca dari index 0,contoh penulisannya seperti disamping
print(coding[0])#contoh pemanggilan untuk array
print(len(coding))#bisa juga di kombinasi dengan fungsi len untuk tahu berapa data di array
print()

#untuk menjadikan baris kebawah kita bisa gunakan looping for
for bahasa in coding:
    print(bahasa)
print()

#bisa juga dengan looping while

awal = 1

while awal <= 10: #syarat(apakah 1 kurang dari 10)
    print(awal) #jika kurang dari 10 maka cetak kelayar
    awal= awal+1 #nilai awal(1)= 1+1 jadi 2, nilai awal(2)= 2=1 jadi 3, begitu sterusnya sampe 10
    #awal += 1 #bisa dugunakan untuk mengganti awal=awal+1
