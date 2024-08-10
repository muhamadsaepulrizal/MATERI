import os
#fungsi untuk membersihkan layar
def clear():
    os.system('cls')

class Node:
    def __init__(self, nama_penyewa, ps_berapa, no_wa):
        self.nama_penyewa = nama_penyewa
        self.ps_berapa = ps_berapa
        self.no_wa = no_wa
        self.next = None
        self.prev = None

class dll:
    def __init__(self):
        self.head = None
        self.tail = None

    #fungsi menambahkan penyewa kedalam list
    def menambah_penyewa(self, nama_penyewa, ps_berapa, no_wa):
        node_baru = Node(nama_penyewa, ps_berapa, no_wa)
        if self.head is None:
            self.head = self.tail = node_baru
        else:
            self.tail.next = node_baru
            node_baru.prev = self.tail
            self.tail = node_baru

    #fungsi menghapus penyewa dalam list
    def menghapus_penyewa(self, nama_penyewa):
        current = self.head
        while current:
            if current.nama_penyewa == nama_penyewa:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return 
            current = current.next

    #fungsi menampilkan daftar penyewa
    def menampilkan_penyewa(self):
        current = self.head
        while current:
            print(f"Nama Penyewa : {current.nama_penyewa}, Playstation Berapa: {current.ps_berapa}, No. WhatsApp: {current.no_wa}")
            current = current.next

class bisnis_rental_ps:
    def __init__(self):
        self.penyewa = dll()
        self.password_admin = "kelompok4"

    #fungsi menu login untuk pemilik usaha
    def login_admin(self):
        password = input("Masukkan Password Admin!: ")
        if password == self.password_admin:
            return True
        else:
            print("Password Admin Salah... Periksa Lagi!!")
            return False
        
    #fungsi tampilan menu pemilik usaha
    def menu_admin(self):
        while True:
            clear()
            print("MENU ADMIN".center(50,"="))
            print("1. Lihat Daftar Penyewa Playstation")
            print("2. Hapus Penyewa Playstation")
            print("3. Logout")
            pilih = input("Pilih Menu Diatas(1/2/3): ")
            if pilih == '1':
                clear()
                self.penyewa.menampilkan_penyewa()
                input("\nTekan Enter Untuk kembali....")
            elif pilih == '2':
                clear()
                nama_penyewa = input("Masukkan Nama Penyewa Yang Akan Dihapus: ")
                self.penyewa.menghapus_penyewa(nama_penyewa)
                print("Data Penyewa Telah Dihapus.")
                input("\nTekan Enter Untuk kembali....")
            elif pilih == '3':
                break
            else:
                print("Pilihan Tidak Valid, Silahkan Pilih Yang Ada Di Menu")
                input("\nTekan Enter Untuk Kembali....")

    #fungsi tampilan menu penyewa
    def menu_penyewa(self):
        clear()
        print("MENU PENYEWA".center(50,"="))
        print("silahkan isi data dibawah ini".center(50,"-"))
        nama_penyewa = input("Masukkan Nama Penyewa\t\t: ")
        ps_berapa = input("Masukkan Playstation Berapa\t: ")
        no_wa = input("Masukkan No WhatsApp Anda\t: ")
        self.penyewa.menambah_penyewa(nama_penyewa, ps_berapa, no_wa)
        print("Data Penyewa Telah Disimpan")
        input("\nLangkah Terakhir Tekan Enter, Lalu Silahkan Ke Meja Pembayaran....")

    #fungsi Menu Utama
    def menu_utama(self):
        while True:
            clear()
            print("SEWA PLAYSTATION".center(50,"="))
            print("Hiburan Paling Bagus Saat Stress".center(50,"-"))
            print("1. Login Sebagai Admin ")
            print("2. Login Sebagai Penyewa")
            print("3. Keluar") 
            pilih = input("Pilih Menu (1/2/3): ")
            if pilih == '1':
                if self.login_admin():
                    self.menu_admin()
            elif pilih == '2':
                self.menu_penyewa()
            elif pilih == '3':
                break
            else:
                print("Pilihan Tidak Valid, Silahkan Pilih Yang Ada Di Menu")
                input("\nTekan Enter Untuk Kembali....")

if __name__ == "__main__":
    sistem = bisnis_rental_ps()
    sistem.menu_utama()           



