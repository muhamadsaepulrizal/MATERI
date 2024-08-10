'''contoh membuat exception'''

from numbers import Number

def tambah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):
        raise "input harus angka" #ini exception nya, sifatnya seperti break,return
    return a+b

print(tambah(10,5))

#contoh lain
angka = 0
try:
    hasil = 10/angka
except Exception as error_message:
    print(error_message)

    




