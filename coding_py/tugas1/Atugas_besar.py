import os #impor modul os, digunakan untuk berinteraksi dengan sistem operasi(disini digunakan untuk clear screen)
import random #impor modul random digunakan untuk menghasilkan angka acak

#fungsi membersihkan layar
def clear():
    if os.name == 'nt':
        os.system('cls') # cls perintah clerscreen di windows
    else:
        os.system('clear') # clear untuk linux

class Node: #kelas Node, yang akan digunakan untuk mempresentasikan simpul dalam linked list
    def __init__(self,data): #fungsi Khusus __init__ yang dipanggil otomatis saat sebuah node dibuat, (self):parameter yg merujuk pada objek yang sedang dibuat, (data)adalah nilai yang akan disimpan dalam simpul  
        self.data = data #memberkan nilai data ke atribut data dalam objek node yang sedang dibuat
        self.next = None #inisialisasi atribut next sebagi None, menandakan bahwa saat ini simpul tidak ditautkan ke simpul lain dalam list
        self.prev = None #inisialisasi atribut prev sebagai None, menandakan bahwa sekarng simpul tidak memiliki simpul sebelumnya dalam linked list

class Dll: #mendefinisikan kelas Dll untuk (double linked list)
    def  __init__(self): #inisialisasi kelas Dll dengan konstruktor (__init__)
        self.head = None #inisialisasi atribut head sebagai None(kosong), menandakan bahwa saat ini tidak memiliki simpul apapun


    #fungsi tambah: untuk menambahkan node baru kedalam linked list 
    def tambah(self,data):
        node_baru = Node(data) #membuat objek node_baru dengan data yang diberikan
        if not self.head:  #memeriksa apakah linked list kosong dengan memeriksa apakah self.head adalah None
            self.head = node_baru #jika llinked list kosong, simpul baru menjadi head/ kepala linked list
            return #mengakhiri eksekusi fungsi
        terakhir = self.head #inisialisasi juga variabel terakhir sebagi kepala linked list
        while terakhir.next: #looping melalui linked list sampai simpul terakhir ditemukan (simpul terakhir memiliki next yang bernilai None)
            terakhir = terakhir.next #memindahkan variabel terakhir ke simpul berikutnya di linked list
        terakhir.next = node_baru #tetapkan juga simpul baru sebagai simpul berikutnya dari simpul terakhir, sehingga menambahkan simpul baru ke akhir linked list
        node_baru.prev = terakhir #menetakan simpul akhir sebagai simpul sebelumnya dari simpul baru, sehinga memperbarui tautan mundur

    #fungsi tambahdi_posisi tertentu untuk menambahkan simpul baru pada posisi yang diinginkan
    def tambahdi_posisi(self, data, posisi):
        node_baru = Node(data) #membuat objek baru dari kelas node dengan data yang diberikan
        if posisi == 0: #memeriksa apakah posisi yang diminta adl 0, yg berarti simpul baru harus ditambahkan diawal linked list
            node_baru.next = self.head #menyambungkan simpul baru dengan kepala linked list
            if self.head: #memeriksa apakah linked list tidak kosong untuk menghindari kesalahan saat mengakses prev 
                self.head.prev = node_baru #jika linked lost tidak kosong, atus simpul baru sebagai simpul sebelumnya dari kepela linked list
            self.head = node_baru #menetapkan simpul baru sebagai kepala linked list
            return #mengakhisi eksekusi fungsi
    
        sekarang = self.head #inisialisasi variabel sekarang sebagai kelapa linked list
        current_position = 0 #inisialisasi variabel current_position untuk melacak posisi saat ini dalam linked list
        while sekarang and current_position < posisi - 1: #melakukan traversal linked list hingga mencapai posisi sebelum posisi yg diminta atau akhir linked list
            sekarang = sekarang.next #pindah ke simpul berikutnya di linked list
            current_position += 1 #meningkatkan posisi saat ini/ lanjut memeriksa
    
        if sekarang is None: #memeriksa apakah sekarang adl None, yang berarti mencapai akhir linked list
            # Jika posisi lebih besar dari panjang daftar, tambahkan di akhir
            self.tambah(data) #jika sekarang adl None, tambahkan simpul baru ke akhir linked list, lanjutkan menambah simpul baru pada posisi tersebut
        else: #jika posisi diminta valid dan bukan akhir linked list, lanjutkan dngan menambahkan simpul baru pada posisi tersebut
            node_baru.next = sekarang.next #menautkan simpul baru ke simpul berikutnya
            node_baru.prev = sekarang #menautkan simpul sebelumnya ke simpul baru
            if sekarang.next: #mamariksa apakah simoul saat ini bukan simpul terakhir dalam linked list
                sekarang.next.prev = node_baru #jika tidak, tetapkan simpul baru sebagai simpul sebelumnya dari simpul berikutnya
            sekarang.next = node_baru #tetapkan simpul baru sebagai simpul sebelumnya dari simpul berikutnya dari simpul saat ini

    #fungsi hapus yang menghapus node dari list
    def hapus(self,data): 
        sekarang = self.head #inisialisasi var sekarang sebagai kepala linked list
        while sekarang: #loop melalui linked list hingga akhir
            if sekarang.data == data: #periksa apakah data simpul saat ini cocok dengan yg ingin dihapus
                if sekarang.prev: #periksa apakah simpul saat ini bukan merupakan kepala list
                    sekarang.prev.next = sekarang.next #hubungkan simpul sebelumnya dengan simpul setelahnya untuk hapus simpul saat ini
                if sekarang.next: #periksa apakah simpul saat ini bukan merupakan simpul terakhir dlm linked list
                    sekarang.next.prev = sekarang.prev #hubungkan simpul setelahnya dengan simpul sebelumnya untuk menghapus simpul saat ini
                if sekarang == self.head: #periksa apakah simpul saat ini adalah kepala linked list
                    self.head = sekarang.next #jika ya, update kepala linked list ke simpul berikutnya
                return #akhiri eksekusi fungsi
            sekarang = sekarang.next #memindahkan sekarang ke simpul berikutnya dlm linked list
    
    #fungsi untuk mencari data tertentu dalam list
    def cari(self, data):
        sekarang = self.head #inisialisasi variabel skerang sebagai kepala linked list
        while sekarang: #looping melalui linked list hinga akhir
            if sekarang.data == data: #periksa apakah data simpul saat ini cocok dengan data yg ingin dicari
                return True #jika cocok, mengembalikan True untuk menunjukan bahwa dta ditemukkan dlm linked list 
            sekarang = sekarang.next #pindak ke simpul berikutnya
        return False #jika tidak ada kecocokan setelah looping selesai, mengembalikan False untuk menunjukkan bahwa data tidak ditemukkan dalam linked list

    #fungsi untuk menampilkan semua data dalam list
    def tampilkan(self):
        sekarang = self.head #inisialisasi var sekarang sebagi kepala linked list
        item = [] #membuat daftar kosong untuk menyimpan data dari linked list
        while sekarang: #looping melalui linked list hingga mencapai akhir
            item.append(sekarang.data)  #menambahkan data dari simpul saat ini ke daftar item
            sekarang = sekarang.next #pindah ke simpul berikutnya dalam linked list
        return item #mengembalikan daftar item yg berisi semua data dalam linked list
    
    #fungsi untuk mengurutkan daftar playstation sesuai urutan semula/ urutan asli
    def urutkan(self, urutan_asli):
        playstations = self.tampilkan() #mendapatkan daftar ps dari linked list dengan fungsi tampilkan
        playstations.sort(key=lambda ps: urutan_asli[ps]) #mengurutkan daftar ps berdasarkan urutan asli yg diberikan
        self.head = None #mengosongkan linked list dengan mengatur kepla linked list sebagai None
        for ps in playstations:#looping melalui setiap ps dlm daftar yg sudah diurutkan
            self.tambah(ps)  #menambahkan ps ke linked list yang sudah diurutkan satu persatu menggunkan fungsi tambah

class sistem_sewa_playstations: #mendefinisikan class untuk mengelola penyewaan playstation
    def __init__(self):
        self.ps_tersedia = Dll() #inisialisasi atribut ps_tersedia sbagai objek dari kelas Dll, yg digunakan untuk menyimpan daftar ps yang sedang tersedia
        self.ps_disewa = {} #inisialisasi atribut ps_disewa sebagai kamus/dict kosong, yg digunakan untuk menyimpan informasi tentang ps yg disewa
        self.posisi_semula = {f"playstation {i}": i-1 for i in range(1, 6)}  #inis atribut posisi_semula sebagai kamus/dict yg berisi posisi asli dari setiap ps. digunakan saat menambahkan ps secara acak

        for i in range(1, 6): #looping dari 1 sampai 5 untuk menambahkan setia ps ke daftar ps yg tersedia
            self.tambah_playstations(f"playstation {i}") #memanggil fungsi tambah_playstations untuk menambahkan ps ke dfatar ps yg tersedia

        if not self.ps_tersedia.tampilkan(): #periksa apakah daftar ps yg tersedia kosong
            #jika daftar kosong. tambahkan satu persatu secara acak, menggunakan fungsi tambah_ps_acak
            self.tambah_ps_acak()

    #fungsi untuk menambahkan ps secara acak ke daftar ps yg tersedia
    def tambah_ps_acak(self):
        ps_random = f"playstation {random.randint(1,5)}" ##membuat nama ps secara acak dengan menggunakan angka acak antara 1 sampai 5
        self.tambah_playstations(ps_random) #menambahkan ps yg baru dibuat ke daftar ps yg tersedia

    #fungsi untuk menambahkan ps ke daftar ps yg tersedia
    def tambah_playstations(self, ps):
        posisi = self.posisi_semula[ps] #mandapatkan posisi asli ps dari atribut posisi_semula
        self.ps_tersedia.tambahdi_posisi(ps, posisi) #memanggil fungsi tambahdi_posisi dari objek ps_tersedia untuk menambahkan ps pada posisi yg ditentukan
        self.ps_tersedia.urutkan(self.posisi_semula) #memanggil fungsi urutkan dari objek ps_tersedia untuk mengurutkan daftar ps berdasarkan posisi asli

    #fungsi untuk menghapus ps dari daftar ps yg tersedia
    def hapus_playstations(self, ps):
        self.ps_tersedia.hapus(ps) #memanggil fungsi hapus dari objek ps_tersedia untuk menghapus ps ug ditentukan dari daftar ps yg tersedia

    #fungsi untuk melakukan sewa playstation
    def sewa_playstations(self, ps, info_penyewa):
        if self.ps_tersedia.cari(ps): #memeriksa apakah ps yg ingin disewa tersedia dlm daftar ps yg tersedia
            self.ps_disewa[ps] = info_penyewa #jika tersedia, tambah ps ke daftar ps yg disewa bersama dengan informasi si penyewa
            self.hapus_playstations(ps) #kemudian, hpus ps dari daftar ps yg tersedia
        else:
            print(f"{ps} tidak tersedia atau sudah disewa.") #jika tidak ada ps yg tersedia atau sudah disewa, cetak pesannya

    #fungsi untuk menampilkan daftar penyewa
    def tampilkan_daftar_penyewa(self):
        if self.ps_disewa: #memeriksa apakah daftar penyewa tidak kosong, jika tidak kosong tampikan daftar penywa
            print("Daftar Penyewa".center(70, "="))
            for ps, info in self.ps_disewa.items():
                print(f"PlayStation\t: {ps}")
                print(f"Nama\t\t: {info['Nama']}")
                print(f"No Wa\t\t: {info['No wa']}")
                print(f"Durasi\t\t: {info['durasi']} jam")
                print("="*70)
        else:
            print("Belum ada penyewa.")#jika kosong / belum ada penyewa

    #fungsi untuk mengembalikan pd g disewa
    def kembalikan_playstations(self, ps):
        if ps in self.ps_disewa: #memeriksa apakah ps yg ingin dikembalikan ada dlm daftar
            del self.ps_disewa[ps] #jika ada, hapus ps dari daftar penyewaan
            self.tambah_playstations(ps) #kemudian, tambahkan kembali ps ke daftar ps yg tersedia
            print(f"{ps} berhasil dikembalikan.") #cetak pesan berikut
        else:
            print(f"{ps} sudah dikembalikan dan sudah ada dalam daftar.") #jika sudah ada di daftar cetak pesannya
    
    #fungsi menampilkan daftar ps yg tersedia
    def tampilkan_ps_tersedia(self):
        return self.ps_tersedia.tampilkan()#mengembalikan hasi dari fungsi tampilkan dari objek ps_tersedia, yg berisi daftar ps yg tersedia

    
#fungsi untuk login/ tampilan awal
def login():
    clear()
    print("Login Sebagai".center(60,"="))
    print("1. Admin Playstations")
    print("2. Penyewa Playstations")
    print("3. Keluar")
    pilih = input("Pilih (1/3)\t: ")
    return pilih
    
    #fungsi menu login admin
def login_admin(sistem_sewa):
    pass_admin = "kel4"  # membuat password untuk admin  saat login
    clear() #memanggil fungsi clear untuk bersihkan layar
    print("Login Admin".center(70,"="))
    while True:
        password = input("Masukkan Password Admin: ")
        if pass_admin == password:  # memeriksa password admin benar, jika benar jalankan program
            while True:
                clear()
                print("Menu Admin".center(70, "="))
                print("1. Lihat Daftar Playstation Yang Tersedia")
                print("2. Lihat Daftar Penyewa")
                print("3. Tambahkan Playstation Yang Sudah Dikembalikan Kedalam Daftar")
                print("4. Kembali Ke Menu Login")
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
            break
        else:
            print("Password salah")

    #fungsi menu login penyewa
def login_penyewa(sistem_sewa):
    while True:
        clear()
        print("Menu Penyewa".center(70, "="))
        print("1. Lihat Daftar Playstation Yang Tersedia")
        print("2. Sewa Playstation")
        print("3. Kembali Ke Menu Login")
        pilih3 = input("Pilih (1/3)\t:")
        match pilih3:
            case '1':
                ps_tersedia = sistem_sewa.tampilkan_ps_tersedia()
                if ps_tersedia:
                    print("Playstation Yang tersedia".center(70, "="))
                    for ps in ps_tersedia:
                        print(ps)
                else:
                    print("Mohon Maaf Semua Playstation Sibuk")
                input("Tekan Enter Untuk Kembali Memilih Menu.....")
            case '2':
                ps_tersedia = sistem_sewa.tampilkan_ps_tersedia()
                if ps_tersedia:
                    print("-"*70)
                    print("Petunjuk : 1. Saat memilih Playstation")
                    print("              Ketik Misal (playstation 5) untuk menyewa")
                    print("           2. Durasi minimal penyewaan 3 jam") 
                    print("              ketik Misal (3) untuk 3 jam") 
                    print("           3. --------Harga Sewa Tiap Playstation-------")
                    print("              -Playstation 1 = 1 jam Rp. 2.000,00")
                    print("              -Playstation 2 = 1 jam Rp. 4.000,00")
                    print("              -Playstation 3 = 1 jam Rp. 6.000,00")
                    print("              -Playstation 4 = 1 jam Rp. 8.000,00")
                    print("              -Playstation 5 = 1 jam Rp. 10.000,00")
                    print("           4. -------------Durasi Penyewaan-------------")
                    print("              -Kurang dari 10 jam main ditempat")
                    print("              -Lebih dari 10 jam boleh dibawa kerumah")
                    print("-"*70)
                    print("Playstation Yang tersedia".center(70, "="))
                    for ps in ps_tersedia:
                        print(ps)
                    ps = input("Pilih Dan Masukkan Playstation Yang Ingin Disewa: ")
                    if ps in ps_tersedia:
                        nama = input("Masukkan Nama Anda\t: ")
                        no_wa= input("Masukkan No Wa anda\t: ")
                        durasi = input("Berapa Jam Ingin Menyewa: ")
                        info_penyewa = {
                            'Nama':nama, 
                            'No wa':no_wa,
                            'durasi':durasi
                        }
                        sistem_sewa.sewa_playstations(ps, info_penyewa)
                        print(f"{ps} Berhasil Disewa Oleh {nama} Untuk {durasi} Jam.")
                    else:
                        print(f"Maaf {ps} Sedang Disewa atau tidak valid.")
                else: 
                    print("Tidak ada Playstation Yang Tersedia.")
                input("Tekan Enter Untuk Kembali Memilih Menu.....")
            case '3':
                break
    
#fungsi utama Program Sewa Playstation
def main():
    sistem_sewa = sistem_sewa_playstations()
    while True:
        pilih4 = login()
        match pilih4:
            case '1':
                login_admin(sistem_sewa)
            case '2':
                login_penyewa(sistem_sewa)
            case '3':
                break
if __name__ == "__main__":
    main()



                    





                




 

    







