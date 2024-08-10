#modul matematika dengan from (nama modul) lalu import (fungsi,dll)
#jadi u/ penulisannya tidak ribet 

#cara 1 jika ingin ambil salah satu fungsi atau hanya dua pakai(,)
#ini lebih disarankan 
from modul1 import tambah,kali

#cara 2 jika ambil semua tambah (*) setelah import seperti dibawah
#hanya bingungnya kita tidak tau modul1 isinya apa saja jika dengan (*)
from modul1 import *

hasil_tambah = tambah(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")


hasil_kali = kali(1,2,3,4,5)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = pangkat(3)
print(f"2 pangkat 3 = {pangkat_3(2)}")


#akses modul dengan lebih elegan




