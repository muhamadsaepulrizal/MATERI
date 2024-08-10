import os

os.system("cls")
print("Materi pointer\n")
print("-"*50)
a = 10
p =hex(id(a)) #pointer p mengambil alamat dari variabel a

print(f"Alamat memory dari variabel a yaitu: {hex(id(a))} dengan nilai = {a}")
print(f"pointer p menyimpan alamat pada memory {p} dengan nilai {a}\n")

a = 20
print(f"Alamat memory dari variabel a yaitu: {hex(id(a))} dengan nilai = {a}")
print(f"pointer p menyimpan alamat pada memory {p} dengan nilai {a}\n")

b = 35
p = hex(id(b))
print(f"Alamat memory dari variabel a yaitu: {hex(id(a))} dengan nilai = {a}")
print(f"pointer p menyimpan alamat pada memory {p} dengan nilai {b}\n")
print("-"*50,"\n")

print("Materi Array")
print("-"*50)


#pengaplikasian pointer pada array
x = [0]*5 #satu variabel array semua datanya disimpan disatu memory
print(hex(id(x[0])))
print(hex(id(x[1])))
print(hex(id(x[2])))
print(hex(id(x[3])))
print(hex(id(x[4])))

#didalam python tidak ada array, penggantinya adalah list
#semua data dalam array harus memiliki tipe data yang sama
#semua elemen/data dalam array dapat di akses lewat index (index mulai dari 0)
x = [0,1,2,3,4]
x[0] = 10
print(x,"\n")

#array 1 dimensi
def array1_dimesi():
    x = [0]*5 #menginisialisasi list/array dengan isi 5 dan bernilai 0 semua
    print("array 1 dimensi")
    #mencetak list sebelum diubah
    print("list sebelum diubah")
    for i in range(len(x)):
        print(f"index ke {i} = {x[i]}")

    #mengubah elemen dalam list(array) contoh index ke 3
    x[3]= 300
    #mencetak list setelah afa yang dirubah
    print("\nlist setelah dirubah (pada index ke 3)")
    for i in range(len(x)):
        print(f"index ke {i} = {x[i]}")
    print()

#array 2 dimensi
def array2_dimensi():
    print("array 2 dimensi")
    #membuat matriks 5x5 dengan menginisialisasi semua elemen degan nilai 0
    x = [[0]*5 for _ in range(5)]
    print("list sebelum diubah")
    for i in range(len(x)):
        print(f"index ke {i} = {x[i]}")
    x[4][2]= 10 #beri nilai 10 pada baris ke 4 kolom ke 2
    print("\nlist setelah diubah")
    for i in range(len(x)):
        print(f"index ke {i} = {x[i]}")
    print()

#array string
def array_string():
    print("array string")
    #membuat list dengan panjang 10 dan menginisialisasi semua elemen dengan string kosong
    teks = [""]*10

    #menetapkan string "hallo" ke index ke-2
    teks[2]= "hallo"
    print(teks[2])



array1_dimesi()
array2_dimensi()
array_string()

























