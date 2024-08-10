print("\n\nLatihan Perulangan")
print("="*50)
#latihan perulangan membuat segitiga

sisi = 6
#1. dummy variabel
print("Awal for")
count = 1 
for i in range (sisi):
    print("*"*count)
    count +=1
print("Akhir for")

#2. menggunakan while
print("Awal while")
count = 1
while True:
    print("*"*count)
    count+=1
    if count > sisi:
        break
print("Akhir while")

#3. menggunakan hanya ganjil saja
print("Awal while")
count = 1
while True:
    if count % 2:
        #print jika ganjil
        print("*"*count)
        count+=1
    else:
        #kembali ke atas jika genap
        count+=1
        continue
        
    #akan break jika count melebihi sisi/ berhenti looping
    if count > sisi:
        break
print("Akhir while")

#4. menggunakan hanya ganjil saja segitiga sama kaki
print("Awal while")
count = 1
spasi = int(sisi/2)
while True:
    if count % 2:
        #print jika ganjil
        print(" "*spasi,"*"*count)
        spasi -=1
        count+=1
    else:
        #kembali ke atas jika genap
        count+=1
        continue    
    #akan break jika count melebihi sisi/ berhenti looping
    if count > sisi:
        break
print("Akhir while")



#4. menggunakan hanya ganjil saja segitiga sama kaki
print("Awal while")
count = 1
spasi = int(sisi/2)
while True:
    if count % 2:
        #print jika ganjil
        print(" "*spasi,"*"*count)
        spasi -=1
        count+=1
    else:
        #kembali ke atas jika genap
        count+=1
        continue    
    #akan break jika count melebihi sisi/ berhenti looping
    if count > sisi:
        break
#mulai kerucut
count = count-2
spasi = 1
while True:
    if count%2:
        print(" "*spasi,"*"*count)
        spasi +=1
        count -=1
    else:
        count-=1
        continue
    if count == 0:
        break
print("Akhir while")

print("\n\nmembuat segitiga dengan center")
print("="*50)

segitiga = int(input("masukan jumlah sisi: "))
if segitiga:
    segitiga = segitiga
else:
    segitiga-=1
angka = 2
while angka < segitiga:
    print((angka*"@").center(segitiga))
    angka +=2
while angka > 0:
    print((angka*"@").center(segitiga))
    angka -=2
print("cukup")




































