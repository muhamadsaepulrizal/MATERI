'''materi import untuk mengambil library dari luar
    fungsinya adl mengambil dari file eksternal (.py)

'''
#1. untuk menyambung program dari eksternal dan menjalankannya
import c_import1 #ada di file c_import1

#2. import dengan data
import c_import2
#data ada di namespace c_import2
print(c_import2.data) #begini cara penulisan jika untuk dara (variabel

#3. import dengan fungsi
import c_import3
hasil = c_import3.tambah(4,5)#sama untuk fungsi harus ada namespacenya (c_import3)
print(hasil)

