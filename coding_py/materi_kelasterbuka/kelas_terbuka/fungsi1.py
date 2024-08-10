#fungsi yaitu untuk suapaya kita tidak mengulang syntax/ kode program yg sama
#dalam python tidak ada namanya prototype function
#jadi mendefinisikan fungsi harus diatas program utama 
#pemanggilan fungsi harus setelah fungsinya dibuat


print("\nMateri Function")

'''membuat fungsi'''

def hello_world():#def for definiton: untuk mendefinisikan fungsi
    '''ini adl fungsi menampilkan hello world'''
    print("hello world")
    print("kedapa ucup surucup")
    print("dan kepada otong suroton")

def identitas():
    print("="*50)
    print("Nama  : Muhamad Saepul Rizal")
    print("Nim   : 2306142")
    print("Kelas : Informatika E")
    print("="*50,"\n")
#cara pemanggilan fungsi   
identitas()
hello_world()
print("-"*50,"\n")


print("Materi fungsi dengan argumen")
print("="*50)

#fungsi dengan argumen (bisa diisi dengan input)
# struktur fungsi/tamplate:
#def nama_fungsi(argument/parameter/input):(argumen:bisa int,bool,list, dll)
#    badan fungsi
#    badan fungsi

#contoh 1 fungsi inpur nama
def hello_wolrd1(nama):
    '''fungsi hello wordl menerima input 
    dengan variabel nama'''
    print(f"selamat datang dunia wahai {nama}")

#cara pemanggilan
hello_wolrd1("rizal")#namanya yg diinput langsung dimasukkan ke dlm fungsi
hello_wolrd1("asep")#namanya yg diinput langsung dimasukkan ke dlm fungsi

#fungsi tambah
def tambah(angka1,angka2):
    hasil = angka1+angka2
    print(f"{angka1} + {angka2} = {hasil}")
#pemanggilannya
tambah(1,5)#dibaca 1 + 5 masuk ke fungsi, 1 ke angka1, 5 ke angka2
tambah(355,200)#dibaca 1 + 5 masuk ke fungsi, 1 ke angka1, 5 ke angka2

#contoh fungsi dengan input list
def grup(list_peserta):

    #data peserta mengcopy dari list_peserta(anggota):
    data_peserta = list_peserta.copy()#copy, karena kita tidak ingin jika 1 dirubah yang lain ikut

    #membuat loop untuk peserta dalam data_peserta
    #dimana data_peserta hasil copy/ sama dengan list_peserta/anggota:
    for peserta in data_peserta:

        #loop nya mencetak yang terhormat peserta {peserta}/ (list_peserta/anggota)
        print(f"yang terhormat peserta {peserta}")

#membuat list:
anggota = ["ucup", "dudung", "asep"]

#list anggota dimasukkan ke fungsi grup:
grup(anggota)#di fungsi grup(list_peserta) var anggota diganti saat masuk ke fungsi menjadi list_peserta
#selain anggota kita juga bisa masukkan list lain/ yg mana saat masuk ke fungsi nama list nya berubah jadi list_peserta




    

