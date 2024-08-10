
'''pakage sangat penting untuk kerapihan kode program utama kita
    karena dalam pakage terdapat beberapa module seperti module matematika, module fisika, dll
    dimana didalam module tersebut terdapat fungsi fungsi perhitungan atau logika
    yang akan membantu atau dibutuhkan dalam program utama kita
'''
#import time
#t_start = time.time() #waktu mulai
##main program yang dihutung waktu eksekusinya
#t_end = time.time()#waktu akhir
#print(f"waktu eksekusi programnya = {t_end - t_start}")

#sains = pakage
#matematika, fisika = module
#tambah,gaya = fungsi
import sains.matematika
from sains import fisika #bisa juga seperti ini (untuk memanggil module tertentu dlm suatu pakage)
from sains.fisika import gaya #bisa kaya gini u/hanya import salah satu fungsi dlm modul di suatu pakage
#var untuk menampung = pakagenya(sains).modulnya(matematika).fungsi dalam modul(tambah)(valuenya)
hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"hasil tambah dari pakage adalah = {hasil_tambah}")

hasil_gaya = fisika.gaya(90,10) # hitung gaya fisika dengan massa 90kg, percepatannya 10ms
print(f"hasil perhitungan gaya dengan m=90kg & a=10ms adl: {hasil_gaya}")

hasil_gaya = gaya(80,10) # hitung gaya fisika dengan massa 90kg, percepatannya 10ms
print(f"hasil perhitungan gaya dengan m=80kg & a=10ms adl: {hasil_gaya}")




