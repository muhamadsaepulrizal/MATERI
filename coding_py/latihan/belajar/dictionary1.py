print("\nMateri Dictionary")
print("="*50)

#list -> contoh dari Array = mengakses data lewat index
data_list = ["ucup","otong","abah"]
print(f"data ke 2 = {data_list[1]}") 

#dictionary (dict) -> adl associative array= akses data lewat identifier (key)
#gunanya untuk data yang berstruktur, bisa pakai ini
data_dic = {
    'cp':'ucup', #key1:value1. dst
    'tg':'otong',
    'dg':'dudung',
    'no':100000,
    'ls':data_list[2] #bahkan bisa memasukkan list juga seperti berikut, bahkan bisa masukkan dictionary lagi
}

print(data_dic['cp'])
print(data_dic['no'])
print(data_dic['ls'])
print("-"*50)

print("\nOperator dictionary")
print("="*50)

data_dic = {
    'cup':'ucup surucup',
    'tg':'otong surotong',
    'dg':'dudung surudung'
}

#panjang dict
LENDIC = len(data_dic)
print(f"panjang dictionari = {LENDIC}")

#mengecek key exist atau tidak
KEY = "cup"
CEKKEY = KEY in data_dic
print(f"apakah {KEY} ada di data_dic = {CEKKEY}")

#mengakses value (red) dengan get
#get berguna jika key gak ada maka output None bukan error
print(data_dic.get("kis","key tidak dapat ditemukan"))
print(data_dic.get("dg"))


#update data
#1
data_dic["cup"]="ucup siganteng"
print(data_dic)
#menambah
data_dic["sep"]="asep surasep" #ditambah diakhir
print(data_dic)

#menambah dengan update
#(kalau ada di robah, kalau gak ada di tambah saja langsung)
data_dic.update({"cup":"ucup surucupp"})
print(data_dic)
data_dic.update({"sz":"saepul rizal"})
print(data_dic)

#mendelet data pada dictionary (del)
del data_dic["sz"]
print(data_dic)
print("-"*50)



print("\nLooping dictionary")
print("="*50)

teman_teman = {
    "cp":"ucup surucup",
    "tg":"otong surotong",
    "dg":"dudung surudung",
    "sep":"asep surasep",
    "cup":"ucuy siencuy"
}

#looping first try (yg keluar adl key nya)
for teman in teman_teman:
    print(teman)

#operator untuk mengambil item/ iterables
keys = teman_teman.keys()
print(keys)
for key in teman_teman.keys():
    print(teman_teman.get(key))#maka yang diambel adalah valuenya

#untuk langsung valuenya
values = teman_teman.values()
print(values)
for value in teman_teman.values():
    print(value)

#ada juga items
item = teman_teman.items()
print(item)
for item in teman_teman.items():
    print(item)#keluarnya sesuai tuple

#untuk menampilkan key dan value sekaligus

for key,value in teman_teman.items():
    print(f"key = {key}, value = {value}")

#mengunakan 1 variabel untuk memanggil salah satu 
for coba in teman_teman.items():
    print(coba[0])
print("-"*50)

print("\nMateri copy dan pop dictionary")
print("="*50)

teman_teman={
    "cup":"ucup surucup",
    "tg":"otong surotong",
    "dg":"dadang suradang",
    "sep":"asep surasep",
    "cuy":"ucuy surucy"
}
#cara mengcopy
friends = teman_teman.copy()#jika pakai .copy friends tidak akan ikut berubah
#kalau teman_teman dirubah, karena friends sudah variabel yang berbeda dengan isinya dari teman_teman

print(f"teman_teman: {teman_teman}")
print(f"friends    : {friends}\n")

teman_teman["cup"]="ucup ganti1"
print(f"teman_teman: {teman_teman}")
print(f"friends    : {friends}\n")

#pop dictionary (mengambil 1 data)/ diambil berdasarkan key
dataasep = friends.pop("sep")
print(f"data asep = {dataasep}")
print(f"friends = {friends}\n")#data asep hilang, karena di pop(transfer) ke dataasep

#pop item dictionary/ otomatis mengambil data terakhir
data_akhir = friends.popitem()
print(f"data aakhir = {data_akhir}")
print(f"friends = {friends}\n")#data ucuy hilang, karena di popitem(di ambil yang paling akhir)

















