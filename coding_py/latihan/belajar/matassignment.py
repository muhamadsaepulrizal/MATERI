print('\nmateri operatos assignment')
print('-'*50)
#operasi yang dapat dlakukan dengan penyingkatan
#operasi ditambah dengan assignment

a = 5 # adalah assignment
print('nilai a = ',a)

#contoh operatos assignment
a += 1 #sama dengan a = a+1
print('nilai a += 1, nilai a menjadi: ',a)# jadi 6

a -= 2 #sama dengan a = a-1
print('nilai a -= 2, nilai a menjadi: ',a)# dari 6-2 jadi 4

a *= 5 #sama dengan a = a*5
print('nilai a *= 5, nilai a menjadi: ',a)#dari 4*5 jadi 20
 
a /= 2 #sama dengan a = a/2
print('nilai a /= 2, nilai a menjadi: ',a)#dari 20/2 jadi 10

#mdulus
b = 10
print('\nnilai b = ',b)
b %=3
print('nilai b %= 3, nilai b menjadi: ',b)#10 modulus 3 = 1

#floor divison
b = 10
print('\nnilai b = ',b)
b //=3
print('nilai b //= 3, nilai b menjadi: ',b)#10 dibagi 3, dibulatkan kebawah = 3

#pangkat
a = 5
print('\nnilai a = ',a)
a **= 3
print('nilai a **= 3, nilai a menjadi: ',a)

#operator bitwise
#or
c = True
print('\nnilai c = ',c)
c |= False #output True kaena c=True di or dengan False = True
print('nilai c |= False, nilai c menjadi: ',c)

c = False
print('nilai c = ',c)
c |= False #output False
print('nilai c |= False, nilai c menjadi: ',c)

#and
c = True
print('\nnilai c = ',c)
c &= False #output False
print('nilai c &= False, nilai c menjadi: ',c)

c = True
print('nilai c = ',c)
c &= True #output False
print('nilai c &= True, nilai c menjadi: ',c)

#xor
c = True
print('\nnilai c = ',c)
c ^= False #output False
print('nilai c ^= False, nilai c menjadi: ',c)

c = True
print('nilai c = ',c)
c ^= True #output False
print('nilai c ^= True, nilai c menjadi: ',c)

#geser geser 
d = 0b0100
print('\nnilai d = ',format(d,'04b'))#kenapa 4 karena diatas me menulis 0100(4 angka)
d >>= 2
print('nilai d >>= 2, nilai d menjadi: ',format(d,'04b'))
d <<= 1
print('nilai d <<= 1, nilai d menjadi: ',format(d,'04b'))