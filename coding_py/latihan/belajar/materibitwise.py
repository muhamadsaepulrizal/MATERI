print()
print('materi operator bitwise or(|), and(&), xor(^), shiftright(>>), shiftleft(<<)')
print('-'*50)
""""
oeprator bitwise(masing masing bit)
atau operasi biner
atau binary
contoh:
int 2 >   00000010
index :   76543210
karena 2:       2(2 pangkat 1= 2)
jika 1  :        2(2pangkat 0 = 1)

contoh soal : 00001001
jawab       :     2pangkat3
            :        2pangkat0
            :     ditambah = 2pangkat3=8, 2pangkat0=1, jadi 8+1=9

contoh soal :
2 | 1(| sama dengan or)
jawab       : 00000010
            : 00000001
            : 00000011
            :       2pangkat1=2
            :        2pangkat0=1, jadi 2+1=3
"""

#bitiwise or (|)
a = 9
b = 5

c = a|b
print('====OR====')
print('nilai: ',a,',  binary: ',format(a,'08b'))
print('nilai: ',b,',  binary: ',format(b,'08b'))
print('----------------------------- (|)/or atau bisa dilogikakan tambah(+)')
print('nilai: ',c,', binary: ',format(c,'08b')) 

#bitiwise and (&)
c = a&b
print('====AND====')
print('nilai: ',a,',  binary: ',format(a,'08b'))
print('nilai: ',b,',  binary: ',format(b,'08b'))
print('----------------------------- (&)/and atau bisa dilogikakan kali(*)')
print('nilai: ',c,',  binary: ',format(c,'08b')) 

#bitiwise xor (^)
c = a^b
print('====XOR====')
print('nilai: ',a,',   binary: ',format(a,'08b'))
print('nilai: ',b,',   binary: ',format(b,'08b'))
print('----------------------------- (^)/ output 1 jika 2input berbeda, output 0 jika 2input sama')
print('nilai: ',c,',  binary: ',format(c,'08b')) 

#bitiwise not (~)
c = ~a
print('====NOT====')
print('nilai: ',a,',    binary: ',format(a,'08b'))
print('----------------------------- (~)/not')
print('nilai: ',c,',  binary: ',format(c,'08b')) 
print('----------------------------- (^)/xor')
d = 0b00001001
e = 0b11111111
print('nilai: ',e^d,',  binary: ',format(e^d,'08b')) 


#shifting
#shift right (>>)
c = a >> 2
print('====shiftright(>>)====')
print('nilai: ',a,',  binary: ',format(a,'08b'))
print('----------------------------- (>>)/shiftright output 1 geser kekanan')
print('nilai: ',c,',  binary: ',format(c,'08b')) 

#shift left (<<)
c = a << 2
print('====shiftleft(<<)====')
print('nilai: ',a,',   binary: ',format(a,'08b'))
print('----------------------------- (<<)/shiftleft output 1 geser kekiri')
print('nilai: ',c,',  binary: ',format(c,'08b')) 





