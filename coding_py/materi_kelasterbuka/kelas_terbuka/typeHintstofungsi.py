import os
import string
'''type Hints untuk fungsi digunakan untuk mengenali 
    suatu fungsi inputnya harus dalam bentuk tipe data apa??!!
'''

#bentuk standard fungsi 
'''
studi kasus:
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(1)
fungsi("ucup")
fungsi(True)
'''
# penggunaan Type Hints
def fungsi_dengan_hints(argument:int) -> int: #-> = (outputnya)
    '''ini fungsi dengan hints'''
    output = 10**argument
    return output

hasil = fungsi_dengan_hints(2)
print(hasil)

def display(argument:string): 
    print(argument)

display("hallo") 





















