class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def sisip_depan(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def hapus_belakang(self):
        if self.head is None:
            print("Linked List Kosong.......")
            return
        
        last = self.head
        while last.next is not None:
            last = last.next

        if last.prev is not None:
            last.prev.next = None
        
        if last == self.head:
            self.head = None

        del last

    def hapus_tengah(self, data):
        if self.head is None:
            print("Linked List Kosong........")
            return
        
        current = self.head
        while current is not None and current.data != data:
            current = current.next

        if current is None:
            print(f"Elemen {data} tidak ditemukan di dalam linked list.")
            return
        
        if current.prev is not None:
            current.prev.next = current.next

        if current.next is not None:
            current.next.prev = current.prev

        if current == self.head:
            self.head = current.next

        del current

    def cetak(self):
        if self.head is None:
            print("Linked List Kosong.........")
        else:
            current = self.head
            while current is not None:
                print(current.data, end="")
                if current.next is not None:
                    print("<==>", end="")
                current = current.next
            print()


#Contoh pengunaan
dll = DoublyLinkedList()
print("="*30)
print("Nama  : Muhamad Saepul Rizal")
print("Nim   : 2306142")
print("Kelas : E")
print("="*30)
print("\t\t==OPERASI PADA DOUBLE LINKED LIST==\n")

#penyisipan simpul di depan
print("Penyisipan simpul di depan\n")
for huruf in ['A','B','C','D','E','F']:
    dll.sisip_depan(huruf)
dll.cetak()

#hapus simpul belakang
print("\nSetelah hapus simpul belakang")
dll.hapus_belakang()
dll.cetak()

print("\nSetelah hapus simpul belakang")
dll.hapus_belakang()
dll.cetak()

#hapus simpul tengah
huruf_tengah = input("\nMasukkan huruf tengah yang akan dihapus: ")
dll.hapus_tengah(huruf_tengah)
dll.cetak()

