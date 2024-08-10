# __main__ seperti dalam C++ ada int main(){}
# __main__ adl top lvl code envorment

print(__name__) #akan keluar __main__ 

# __name__ = __main__ , ini akan terjadi jika ada di file diprogram utama

# __name__ pada file program utama:
print(f"nilai __name__ pada main_main.py = '{__name__}'")

#si __name__ output nya akan __main__ saat dipanggil sebagai program utama
#jika  __name__ hasi import dari pakage atau modul lain maka output nya nama pakage atau module tsb

#berikut contoh __name__ pada module lain:
import fungsi #outputnya akan 'fungsi'

#contoh penggunaan __main__ :
#deklarasi
def f_tambah(a:int,b:int)->int:
    return a+b

#fungsi utama
if __name__ == "__main__":
    angka1= 10
    angka2= 40
    hasil = angka1+angka2
    print(f"hasil tambah {angka1} + {angka2} = {hasil}")

##import package
import package

