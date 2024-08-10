print("\nMateri Latihan List")
print("="*50)

#list untuk apa

#program list buku

#untuk mengumpulkan list buku
list_buku =[]
#supaya berulang kita gunakan while true
while True:
    print("\nMasukkan data buku dibawah")
    judul = input("Judul Buku\t:")
    penulis = input("Penulis Buku\t:")


    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)#setiap input buku baru, ditambahkan ke list buku
    
    #print(list_buku)
    print("\n\n","="*10,"DATA BUKU (NO|JUDUL|PENULIS)","="*10)
    #print("No.\t|Judul\t\t\t|Penulis")
    for index,buku in enumerate(list_buku):
        print(f" {index+1} | {buku[0]} | {buku[1]}")
    print("","="*50)

    islanjut = input("Apakah ingin dilanjukan? (y/n): ")
    if islanjut == "n":
        break
print("PROGRAM SELESAI")

    


