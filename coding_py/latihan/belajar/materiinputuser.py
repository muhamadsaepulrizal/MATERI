print()
print('materi 4 input user')
print('='*50)

data = input('masukan data string: ')#if seperti ini data yang diinput hanya string
print('data: ',data,', tipenya: ',type(data))
print('-'*50)

data2 = int(input('masukan data integer: '))#if input data ingin integer(angka)
print('data2: ',data2,', tipenya: ',type(data2))
print('-'*50)

data3 = float(input('masukan data float: '))#if input ingin float(decimal)
print('data3: ',data3,', tipenya: ',type(data3))
print('-'*50)

#untuk data boolean output 1(True)/0(False): hasil false jika inputan kosong/spasi
data4 = bool(input('masukan data boolean: '))
print('data4: ',data4,', tipenya: ',type(data4))
#bisa juga lewat int dulu sebelum bool if ingin input 0, output False
data5 = bool(int(input('masukan data boolean: ')))
print('data5: ',data5,', tipenya: ',type(data5))
