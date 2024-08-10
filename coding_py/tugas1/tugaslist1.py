class Node:
    def __init__(self, nama, umur, tinggi):
        self.nama = nama
        self.umur = umur
        self.tinggi = tinggi
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.posisi = None
    
    def tambah_awal_list(self):
        nama = input("Masukkan Nama: ")
        umur = int(input("Masukkan Umur: "))
        tinggi = float(input("Masukkan Tinggi: "))
        baru = Node(nama,umur,tinggi)
        baru.next = self.head
        self.head = baru
    
    def menambah_node_di_akhir(self):
        nama = input("Masukkan Nama: ")
        umur = int(input("Masukkan Umur: "))
        tinggi = float(input("Masukkan Tinggi: "))
        temp = self.head
        if temp is None:
            self.head = Node(nama,umur,tinggi)
            self.posisi = self.head
        else:
            while temp.next:
                temp=temp.next
            temp.next = Node(nama,umur,tinggi)
    
    def display_list(self):
        temp = self.head
        print()
        if temp is None:
            print("List kosong!")
        else:
            while temp:
                print(f"Nama: {temp.nama}, Umur: {temp.umur}, Tinggi: {temp.tinggi}", end="")
                if temp == self.posisi:
                    print("<<<< posisi node",end="")
                print()
                temp = temp.next
            print("Akhir list!")

    def hapus_awal_node(self):
        if self.head is None:
            print("List kosong!")
        else:
            self.head = self.head.next
    
    def hapus_akhir_node(self):
        if self.head is None:
            print("List kosong!")
        elif self.head.next is None:
            self.head = None
        else:
            temp1 = self.head
            temp2 = self.head.next
            while temp2.next:
                temp1 = temp1.next
                temp2 = temp2.next
            temp1.next = None
    
    def tambah_tengah_list(self):
        if self.head is None:
            print("Belum ada data!! silahkan isi data terlebih dahulu.")
            return
        posisi_sisip = int(input("Akan disisipkan setelah data ke?: "))
        bantu = self.head
        baru = Node(None,None,None)
        for _ in range(posisi_sisip - 1):
            if bantu.next is not None:
                bantu = bantu.next
            else:
                print("posisi sisip tidak valid")
                return
        nama = input("Masukkan Nama: ")
        umur = int(input("Masukkan Umur: "))
        tinggi = float(input("Masukkan Tinggi: "))
        baru.nama = nama
        baru.umur = umur
        baru.tinggi = tinggi
        baru.next = bantu.next
        bantu.next = baru
    
    def hapus_tengah_list(self):
        if self.head is None:
            print("List kosong!")
        else:
            banyakdata = 0
            bantu = self.head
            while bantu is not None:
                banyakdata = 1
                bantu = bantu.next
            posisi_hapus = int(input("Akan dihapus pada data ke?: "))
            if posisi_hapus < 1 or posisi_hapus > banyakdata:
                print("Posisi hapus tidak valid!")
                return
            bantu = self.head
            poshapus = 1
            while poshapus < (posisi_hapus - 1):
                bantu = bantu.next
                posisi += 1
            hapus = bantu.next
            bantu.next = hapus.next
            del hapus

def main():
    print("Nama : Muhamad saepul rizal")
    print("Nim  : 2306142")
    print("kelas: E")
    linked_list = LinkedList()
    while True:
        print("\nMENU PILIHAN: ")
        print("0. Keluar program")
        print("1. Tambah awal list")
        print("2. Tambah akhir list")
        print("3. Tambah tengah list")
        print("4. Hapus awal list")
        print("5. Hapus akhir list")
        print("6. Hapus tengah list")
        print()
        linked_list.display_list()
        print()
        option = int(input("Pilihan >> "))
        if option == 0:
            break
        elif option == 1:
            linked_list.tambah_awal_list()
        elif option == 2:
            linked_list.menambah_node_di_akhir()
        elif option == 3:
            linked_list.tambah_tengah_list()
        elif option == 4:
            linked_list.hapus_awal_node()
        elif option == 5:
            linked_list.hapus_akhir_node()
        elif option == 6:
            linked_list.hapus_tengah_list()
        else:
            print("pilihan tidak valid")
if __name__ == "__main__":
    main()

        
        
