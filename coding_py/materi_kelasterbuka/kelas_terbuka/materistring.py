print('\nmateri string')
print('='*50)

data = 'ini adalah string'
print(data)
print(type(data))
print('==================================================\n')

#cara embuat string:
""""
string:
1. dengan menggunakan single quote '...'
2. dengan menggunakan double quote "..."
3. string literal atau raw r''
4. multiline literal string """"""""
"""

data = 'pakai single quote'
print(data) 
data = "pakai double quote"
print(data)
#kombinasi
print('"hallo kombinasi"')
print("'hallo kombinasi'")
print("'hallo jum'at")

#mengunakan tanda \
#membuat tanda ' menjadi string dengan \
print('hallo ini jum\'at')

#backlash: untuk memunculkan \ caranya double saja\\
#karne backlash adalah karakter khusus dalam python
print('C:\\user\\anjing')

#tab \t
print('semakin\t\t\t jauh')

#backspace \b
print('semakin     \b\b\b\b\b\b\bdekat')#hati hati kata semakin bisa menghilang

#newline \n \r, mendeteksi akhir baris
print('baris 1. \nbaris 2.')#jadi dua baris dalam satu syntax, LF line feed -> unix, linux, macos
print('baris 3. \rbaris 4.')#CR carriage return, baris 3(hilang)-> commodore, acorn, lisp
print('baris 5. \r\nbaris 6.')#CRLF line feed carriage return-> windows

#string literal/raw
#contoh hati-hati
print('C:\new folder')#salah
#menggunakan raw string: dengan menambahkan r sebelum ''
print(r'C:\new folder, hallo jum')

#multiline literal string, dalam satu print("""bisa nulis bberapa baris""")
print("""
nama : ucup
kelas: E
nim  : 2306142
""")

#multiline literal string dan raw
print(r"""
C:\newm folder
website: www.ucup.com.\newid
""")

print('\n\nmateri operasi dan manipulasi string')
print('='*50)

#1. menyambung string
namapertama = 'Ucup'
namatengah = 'D'
namaakhir = 'venom'
nama = namapertama+" "+namatengah+"'"+namaakhir
print(nama)

#2. menghitung string
panjang = len(nama) #output len berupa integer
print('panjang dari '+nama+' = '+str(panjang))

#3. operator untuk string
#cek apakah ada komponen char/ string di string
u = "u"
status = u in nama
print(u+' ada di '+nama+' = '+str(status))

d = "d"
status = d not in nama
print(d+' tidak ada di '+nama+' = '+str(status))

#mengulang string
print('wk'*10)

#indexing (mulai dari 0)
print("index ke-0: "+nama[0])#0 tidak punya (+/-), jadi -0 dan 0 sama
print("index ke-(-1): "+nama[-1])#if minus(-) dimulai dari belakang
print("index [0:3]: "+nama[0:3])#output 3 tidak muncul, karena dibaca sebelum 3, tanda(:)=sampai
print("index [7:12]: "+nama[7:13])# + 1, untuk menampilkan kata yang kita inginkan

#item paling kecil pakai : min
print("paling kecil: "+min(nama))# output pasti spasi jika ada spasi
#item paling besar pakai : max
print("paling kecil: "+max(nama))# output terbesar diitung dari urutan abjad

#cek ascii code
ascii = ord("v")
print("ascii codenya adalah: "+str(ascii))

#4. operator dalam bentuk mthod:
data = "otong surotong pararotong"
jumlah = data.count("g")
print("jumlah g adalah: "+str(jumlah))


print("\n\nMateri string menggunakan operator method")
print("="*50)

#merubah case dari string
#1. merubah semua ke uper case/ huruf besar semua
salam = "hai!"
print("normal = ",salam)
salam = salam.upper() 
print("UPPER = ",salam)

#2. merubah semuake lower case/ hutuf kecil semua
alay = "haI aKu keCE aBIezZZZzzzz"
print("normalnya = ",alay)
alay = alay.lower()
print("lower nya = ",alay)

#3. pengecekan dengan isX method
#contohnya:  cara penulisan: (nama variabel).is(perintahya)
salam = "sist"
apakah = salam.islower()# cek huruf kecil semua atau besar semua, atau dll
print(salam," is lower = ",str(apakah))
apakah2 = salam.isupper()
print(salam," is upper = ",str(apakah2))
""""
1. isalpha()= untuk cek semua huruf
2. isalnum()= untuk cek huruf dan angka
3. isdecimal()= untuk cek angka saja
4. ispace()= untuk cek ada spasi, tab, newline
5. istitle()= semua kata dimulai dengan huruf besar

"""

judul = "It Is Okay Not To Be Orkay"
cekjudul = judul.istitle()# hasil bool
print("apakah kalimat: ",judul," adalah judul = ",str(cekjudul))
#print(str(cekjudul))

##cek komponen startswith(), endswith()
cek_start = "Hallo Ini Judul".startswith("Hallo")#cek apakah dimulai dengan kata "Hallo"
print("start = "+str(cek_start))

cek_end = "Hallo Ini Judul".endswith("Judul")#cek apakah diakhiri dengan kata "Judul"
print("end = "+str(cek_end))

##penggabungan komponen join()/gabung, split()/pisah
pisah = ["aku", "suka", "makan"]
gabung = " ".join(pisah)# jadi data dalam list gabung ((" ")untuk spasi)
print(pisah)
print(gabung)

gabungan ="akubsukabmakan"
print(gabungan.split("b"))# b nya jadi dihilangkan

## alokasi karakter(char): ada rjust()/kanan, ljust()/kiri, center()/tengah
print(5*"="+"data"+"="*5)
kanan = "kanan".rjust(20,"-")
print("'"+kanan+"'")

kiri = "kiri".ljust(20,"-")
print("'"+kiri+"'")

tengah = "tengah".center(20,"-")# supaya tidak spasi pakei argment lagi seletah 20 yaitu contoh: (,"-")
print("'"+tengah+"'")

#kebalikannya alokasi strip()
tengah = tengah.strip("-")#menghilangkan yang kosong/ tanda (-)
print("'"+tengah+"'")

""""
bisa cari internet untuk string method di internet serta kegunaannya
"""

print('\n\n\nMateri format string dengan f sbelum " ", (f" ")')
print("="*50)

#contoh generic
# string
nama = "marley"
#str = "hello " + nama
formatstr = f"hello {nama}"#menggunakan f sebelum(""), untuk variabel didalam({})
print(formatstr)


# boolean
boolean = True
formatstr= f"boolean = {boolean}"
print(formatstr)

# angka 
angka = 2005.5
#formatstr = "angka = "+str(angka)
formatstr = f"angka = {angka}" #jadi tidak perlu str(angka)
print(formatstr)

#bilangan bulat
angka = 15
formatstr = f"bilangan bulat = {angka:d}"# d untuk integer(bil bulat)
print(formatstr)

#bilangan ribuan/jutaan/milyaran
angka = 20000000000
formatstr = f"bilangan milyaran = {angka:,}"#tanda (,) untuk memcah nol menjadi sesuai yg kita inginkan(2,000)/dua ribu
print(formatstr)

#bilangan desimal
angka = 200.569876 #titik dihitung
formatstr = f"bilangan bulat = {angka:.2f}"# (.2f)= angka yg diambil 2 setelah koma
print(formatstr)

#menampilkan leading zero
angka = 200.569876 #titik dihitung
formatstr = f"bilangan bulat = {angka:07.2f}"# (07.2f)= 07 untuk menabahkan 0 didepan
print(formatstr)

#menampilkan tanda +/-
angkamin = -10
angkaplus = +10.2765
formatmin = f"minus = {angkamin}"#min selalu keluar
formatplus = f"plus = {angkaplus:+.2f}"#untuk plus tambahkan (+d), d(sesuai tipe data)/ +.2f(plus,lalu 2 angka dibelakang koma, f untuk float)

print(formatmin)
print(formatplus)

#meformat %(persen)
persen = 0.045
formatpersen = f"persen = {persen:.2%}"#angka dirubah jadi persenan dengan .2%, 2 untuk mau berapa angka setelah(.)
print(formatpersen)

#melakukan operasi operasi didalam {}/ kurung kurawa
harga = 10000
jumlah = 5
formatstr = f"harga total = {harga*jumlah:,}"
print(formatstr)

#format angka lain {binary, octal, hexadecimal}
angka = 255
formatbinary = f"binary = {bin(angka)}"#untuk biner
formatoctal = f"octal = {oct(angka)}"#untuk octal
formathex = f"hexadecimal = {hex(angka)}"#untuk hexadecimal
print(formatbinary)
print(formatoctal)
print(formathex)











