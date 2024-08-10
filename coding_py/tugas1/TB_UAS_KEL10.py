import os
import random

#fungsi membersihkan layar
def clear():
        os.system('cls') #clear screen untuk windows

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None 

class Dll:
    def  __init__(self):
        self.head = None


    #fungsi tambahkan node baru kedalam list 
    def tambah(self,data):
        node_baru = Node(data)
        if not self.head: 
            self.head = node_baru 
            return 
        terakhir = self.head 
        while terakhir.next: 
            terakhir = terakhir.next 
        terakhir.next = node_baru 
        node_baru.prev = terakhir 

    #fungsi Tambah di posisi tertentu
    def tambahdi_posisi(self, data, posisi):
        node_baru = Node(data)
        if posisi == 0:
            node_baru.next = self.head
            if self.head:
                self.head.prev = node_baru
            self.head = node_baru
            return
    
        sekarang = self.head
        current_position = 0
        while sekarang and current_position < posisi - 1:
            sekarang = sekarang.next
            current_position += 1
    
        if sekarang is None:
            # Jika posisi lebih besar dari panjang daftar, tambahkan di akhir
            self.tambah(data)
        else:
            node_baru.next = sekarang.next
            node_baru.prev = sekarang
            if sekarang.next:
                sekarang.next.prev = node_baru
            sekarang.next = node_baru

    #fungsi hapus yang menghapus node dari list
    def hapus(self,data):
        sekarang = self.head 
        while sekarang: 
            if sekarang.data == data: 
                if sekarang.prev: 
                    sekarang.prev.next = sekarang.next 
                if sekarang.next: 
                    sekarang.next.prev = sekarang.prev 
                if sekarang == self.head: 
                    self.head = sekarang.next 
                return 
            sekarang = sekarang.next 
    
    #fungsi untuk mencari data dalam list
    def cari(self, data):
        sekarang = self.head
        while sekarang:
            if sekarang.data == data:
                return True
            sekarang = sekarang.next
        return False 

    #fungsi untuk menampilkan semua data dalam list
    def tampilkan(self):
        sekarang = self.head
        item = []
        while sekarang: 
            item.append(sekarang.data) 
            sekarang = sekarang.next 
        return item 
    
    #fungsi untuk mengurutkan daftar playstation
    def urutkan(self, urutan_asli):
        playstations = self.tampilkan()
        playstations.sort(key=lambda ps: urutan_asli[ps])
        self.head = None
        for ps in playstations:
            self.tambah(ps)

class sistem_sewa_playstations:
    def __init__(self):
        self.ps_tersedia = Dll() 
        self.ps_disewa = {} 
        self.posisi_semula = {f"ps {i}": i-1 for i in range(1, 6)}  # menyimpan posisi asli ps

        for i in range(1, 6):
            self.tambah_playstations(f"ps {i}")

        if not self.ps_tersedia.tampilkan():
            #jika daftar kosong. tambahkan satu persatu secara acak
            self.tambah_ps_acak()

    def tambah_ps_acak(self):
        ps_random = f" ps {random.randint(1,5)}"
        self.tambah_playstations(ps_random)


    def tambah_playstations(self, ps):
        posisi = self.posisi_semula[ps]
        self.ps_tersedia.tambahdi_posisi(ps, posisi)
        self.ps_tersedia.urutkan(self.posisi_semula)

    def hapus_playstations(self, ps):
        self.ps_tersedia.hapus(ps)

    def sewa_playstations(self, ps, info_penyewa):
        if self.ps_tersedia.cari(ps):
            self.ps_disewa[ps] = info_penyewa 
            self.hapus_playstations(ps)
            print("-"*70)
            print(f"{ps} berhasil disewa oleh {info_penyewa['nama']} untuk {info_penyewa['durasi']} jam")
            harga_perjam = {
                "ps 1": 2000,
                "ps 2": 4000,
                "ps 3": 6000,
                "ps 4": 8000,
                "ps 5": 10000,

            } 
            durasi = int(info_penyewa['durasi'])
            total_biaya = harga_perjam[ps]*durasi 
            print(f"silahkan bayar Rp. {total_biaya:,} di meja kasir.")

            syarat = int(info_penyewa['durasi'])
            if syarat >= 10:
                print("serahkan KTP anda di meja kasir jika ingin membawa ps kerumah")
            print("-"*70)
        else:
            print(f"{ps} tidak tersedia atau sudah disewa.")

    def tampilkan_daftar_penyewa(self):
        if self.ps_disewa:
            print("Daftar Penyewa".center(70, "="))
            for ps, info in self.ps_disewa.items():
                print(f"PlayStation\t: {ps}")
                print(f"Nama\t\t: {info['nama']}")
                print(f"No Wa\t\t: {info['nowa']}")
                print(f"Durasi\t\t: {info['durasi']} jam")
                print("-"*70)
        else:
            print("Belum ada penyewa.")

    def kembalikan_playstations(self, ps):
        if ps in self.ps_disewa:
            del self.ps_disewa[ps]
            self.tambah_playstations(ps)
            print(f"{ps} berhasil dikembalikan.")
        else:
            print("-"*70)
            print("tidak valid!!")
            print("1. periksa kembali daftar playstation")
            print("2. input misal (ps 5) untuk mengembalikan playstation 5 ke daftar.")
            print("-"*70)
    
    def tampilkan_ps_tersedia(self):
        return self.ps_tersedia.tampilkan()
    
    #fungsi menu login admin
def login_admin(sistem_sewa):
    pass_admin = "kel10"  # password admin
    clear()
    print("Login Admin".center(70,"="))
    password = input("Masukkan Password Admin: ")
    if pass_admin == password:  # memeriksa password admin
        while True:
            clear()
            print("Menu Admin".center(70, "="))
            print("1. Lihat Daftar Playstation Yang Tersedia")
            print("2. Lihat Daftar Penyewa")
            print("3. Tambahkan Playstation Yang Sudah Dikembalikan Kedalam Daftar")
            print("4. Kembali")
            pilih2 = input("Pilih (1/4)\t:")
            match pilih2:
                case '1':
                    ps_tersedia = sistem_sewa.tampilkan_ps_tersedia()
                    if ps_tersedia:
                        print("Playstation Yang Tersedia".center(70, "="))
                        for ps in ps_tersedia:
                            print(ps)
                    else:
                        print("Mohon Maaf Semua Playstation Sibuk")
                    input("Tekan Enter Untuk Kembali Memilih Menu.....")
                case '2':
                    sistem_sewa.tampilkan_daftar_penyewa()
                    input("Tekan Enter Untuk Kembali Memilih Menu.....")
                case '3':
                    nama_ps = input("Masukkan nama PlayStation yang dikembalikan: ")
                    sistem_sewa.kembalikan_playstations(nama_ps)
                    input("Tekan Enter Untuk Kembali Memilih Menu.....")
                case '4':  # kembali ke menu login
                    break
    else:
        print("Password salah!!")
        input("Tekan Enter Untuk Kembali Memilih Menu.....")

#fungsi untuk login
def login():
    clear()
    print("Sewa Playstation".center(70,"="))
    print("1. Admin Playstations")
    print("2. Lihat daftar Playstation")
    print("3. Sewa Playstation")
    print("4. Keluar")
    pilih = input("Pilih (1/4)\t: ")
    return pilih
    
#fungsi utama Program Sewa Playstation
def main():
    sistem_sewa = sistem_sewa_playstations()
    while True:
        pilih4 = login()
        match pilih4:
            case '1':
                login_admin(sistem_sewa)
            case '2':
                ps_tersedia = sistem_sewa.tampilkan_ps_tersedia()
                if ps_tersedia:
                    print("Playstation Yang tersedia".center(70, "="))
                    for ps in ps_tersedia:
                        print(ps)
                else:
                    print("Mohon Maaf Semua Playstation Sibuk")
                input("Tekan Enter Untuk Kembali Memilih Menu.....")
            case '3':
                ps_tersedia = sistem_sewa.tampilkan_ps_tersedia()
                if ps_tersedia:
                    print("-"*70)
                    print("Petunjuk : 1. Saat memilih Playstation")
                    print("              Ketik Misal (ps 5) untuk menyewa playstation 5")
                    print("           2. Pastikan Playstation yang ingin disewa tersedia di daftar")
                    print("           2. -----------------Aturan durasi penyewaan----------------")
                    print("              -Kurang dari 10 jam main ditempat")
                    print("              -Lebih dari 10 jam boleh dibawa kerumah dengan syarat") 
                    print("               mohon menyerahkan KTP anda sebagai jaminan") 
                    print("           3. ---------------Harga Sewa Tiap Playstation--------------")
                    print("              -Playstation 1 = 1 jam Rp. 2.000")
                    print("              -Playstation 2 = 1 jam Rp. 4.000")
                    print("              -Playstation 3 = 1 jam Rp. 6.000")
                    print("              -Playstation 4 = 1 jam Rp. 8.000")
                    print("              -Playstation 5 = 1 jam Rp. 10.000")
                    print("           4. Tekan Enter 2 kali ")
                    print("              untuk batalkan penyewaan sebelum memilih ps.")
                    print("-"*70)
                    print("Playstation Yang tersedia".center(70, "="))
                    for ps in ps_tersedia:
                        print(ps)
                    print("-"*70)
                    ps = input("Pilih Dan Masukkan Playstation Yang Ingin Disewa: ")
                    if ps in ps_tersedia:
                        nama = input("Masukkan Nama lengkap Anda\t: ")
                        no_wa= input("Masukkan No Wa anda\t\t: ")
                        durasi = input("Berapa Jam Ingin Menyewa\t: ")
                        info_penyewa = {
                            'nama':nama, 
                            'nowa':no_wa,
                            'durasi':durasi
                        }
                        sistem_sewa.sewa_playstations(ps, info_penyewa)
                    else:
                        print(f"Tidak valid perhatikan petunjuk diatas untuk melakukan penyewaan.")
                else:
                    print("Tidak ada Playstation Yang Tersedia.")
                input("Tekan Enter Untuk Kembali Memilih Menu.....")

                
            case '4':
                break
if __name__ == "__main__":
    main()



                    





                




 

    







