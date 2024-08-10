import sains #hanya perlu import si package untuk modulnya di import di __init_-

'''jadi si __init__ berperan sebagai penghubung
'''

hasil_tambah = sains.math.tambah(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_gaya = sains.fisika.gaya(10,9.8)
print(f"hasil gaya   = {hasil_gaya}")

hasil_kali = sains.math.kali(1,2,3,4,5)
print(f"hasil kali   = {hasil_kali}")

pangkat2 = sains.math.pangkat(2)
print(f"hasil pangkat 2 dari 5 = {pangkat2(5)} ")


#from sains import * #jia begini maka hasrus __all_ di init nya
#
#
#hasil_tambah = math.basic.tambah(1,2,3,4,5)
#print(f"hasil tambah = {hasil_tambah}")
#
#hasil_gaya = fisika.gaya(10,9.8)
#print(f"hasil gaya   = {hasil_gaya}")
#
#hasil_kali = math.basic.kali(1,2,3,4,5)
#print(f"hasil kali   = {hasil_kali}")
