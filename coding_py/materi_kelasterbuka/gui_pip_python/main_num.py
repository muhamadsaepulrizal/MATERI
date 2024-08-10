'''kagunaan numpy:
1. matriks
'''
import os
os.system('cls')

import numpy as np

list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])

print(f"list a   = {list_a}")
print(f"vektor a = {vector_a}")

#print(list_a**2) #ini bakal error karena list tak bisa di kuadratkan
print(f"hasil kuadrat vektor a = {vector_a**2}") #ini bisa di kuadratkan karena pakai import numpy as np
print(f"hasil x5  vektor a     = {vector_a*5}") 
print(f"jika ingin mencetak 2 kali pakai list = {list_a*2}") #ouput = [1,2,3,4,1,2,3,4]

matriks_b = np.array([(1,2),(3,4)]) #matriks 2x2
print(f"matriks b:\n{matriks_b}")
print(f"matriks b dikuadratkan:\n{matriks_b**2}")

zeros_c = np.zeros((2,2))#ini untuk membuat matriks kosong pakai (zeros)
print(f"zeros c:\n{zeros_c}")

ones_d = np.ones((2,2))#ini untuk membuat matriks isi angkanya 1 semua dgn (ones)
print(f"ones d:\n{ones_d}")

jumlah = (matriks_b * matriks_b**2) + ones_d
print(f"operasi matriks:\n{jumlah}")

