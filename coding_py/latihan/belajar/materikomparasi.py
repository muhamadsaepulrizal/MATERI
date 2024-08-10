print()
print('materi 6 oprasi komparasi/membandingkan nilai output berupa boolean')
print('-'*50)
""""
operator:
> (lebih besar), < (lebih kecil)
>= (lebih besar sama dengan), <= (lebih kecil sama dengan)
== (sama dengan), !=(tidak sama dengan/kalau beda maka output True)
is dan is not
"""

a = 4
b = 2
hasil = a > 3
print(a,' > ',3,' = ',hasil)#output True

#is dan is not
#is: memandingkan memory/object contoh a is b output False
# is not a is not b output True

x = 5
y = 5
print('nilai x = ',x,', id = ',hex(id(x)))
print('nilai y = ',y,', id = ',hex(id(y)))
#untuk python jika ada nilai yg sama maka akan otomatis dimasukan ke memori yang sama

hasil2 = x is y
print('x is y = ',hasil2)
hasil3 = x is not y
print('x is not y = ',hasil3)

""""
jadi is dan == sama hanya
== bisa x==y, bisa x==5
is bisa x is y, tidak bisa x is 5.

untuk is not dan != sama hanya
!= bisa x!=y, bisa x!=5
is not bisa x is not y, tidak bisa x is not 5.
"""

