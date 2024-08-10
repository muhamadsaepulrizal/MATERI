print()
print('materi 7: operasi logika atau boolean')
print('-'*50)
""""
not
or
and
xor(^)
"""

#not
print('===NOT===')
a = False
c = not a
print('data a = ',a)
print('----------not')
print('data c = ',c)

#or: salah satu True maka output True
print('===OR===')
a = True
b = True
c = a or b #or itu seperti tambah 
print(a,' or ',b,' = ',c)
a = False
b = False
c = a or b #or itu seperti tambah 
print(a,' or ',b,' = ',c)
a = True
b = False
c = a or b #or itu seperti tambah 
print(a,' or ',b,' = ',c)
a = False
b = True
c = a or b #or itu seperti tambah 
print(a,' or ',b,' = ',c)

#and: harus keduanya True maka output True
print('===AND===')
a = True
b = True
c = a and b #and itu seperti kali 
print(a,' and ',b,' = ',c)
a = False
b = False
c = a and b #and itu seperti kali 
print(a,' and ',b,' = ',c)
a = True
b = False
c = a and b #and itu seperti kali 
print(a,' and ',b,' = ',c)
a = False
b = True
c = a and b #and itu seperti kali 
print(a,' and ',b,' = ',c)

#xor: jika input sama contoh True True maka output false
# atau akan True jika salah satu input True
print('===XOR===')
a = True
b = True
c = a ^ b  
print(a,' xor ',b,' = ',c)#False
a = False
b = False
c = a ^ b 
print(a,' xor ',b,' = ',c)#False
a = True
b = False
c = a ^ b 
print(a,' xor ',b,' = ',c)#True
a = False
b = True
c = a ^ b  
print(a,' xor ',b,' = ',c)#True
print()

