judul = "Materi if dan else statement".center(50)
print("\n\n"+judul)
print("="*50)
# URUTANNYA: 
#1. if, elif, else nya
#2. kondisinya
#3. aksinya
#cara penulisan = if kondisi: aksi

nama = input("siapa nama anda: ")
print("nama nya adalah: "+nama)
print("-"*20)
if nama == "ucup":# if dan kondisinya
    print("kamu ucup yang dicari, ganten abiez")#aksinya: dilakukan jika kondisi True maka dijalankan
elif nama == "otong":
    print("kamu otong yang dicari, keren abiess")#aksi lain, jika kondisi True maka dijalankan
else:
    print("kamu bukan yang dicari")#aksi terakhir jika if dan elif diatas kondisinya tidak ada yg terpenuhi
print(f"terima kasih {nama}")
print("\n\n")

