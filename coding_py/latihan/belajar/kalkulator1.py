judul = "PROGRAM KALKULATOR SEDERHANA".center(50,"-")
print("\n"+judul)
print("="*50)

note = """PANDUAN PROGRAM: 
1. masukan angka lalu enter
2. masukan operator lalu enter
3. masukan angka lalu enter
4. hasil operasi yang anda lakukan akan muncul
silahkan Mencoba!!
"""
print(note)
print("-"*50)
angka1 = float(input("Masukan angka pertama          : "))
operator = input("Masukan operator(+, -, x, /)   : ")
angka2 = float(input("Masukan angka kedua            : "))

if operator == "+":
    hasil = angka1+angka2
    print(f"hasil dari {angka1} + {angka2}        = {hasil:,.2f}")
elif operator == "-":
    hasil = angka1-angka2
    print(f"hasil dari {angka1} - {angka2}        = {hasil:,.2f}")
elif operator == "x":
    hasil = angka1*angka2
    print(f"hasil dari {angka1} * {angka2}        = {hasil:,.2f}")
elif operator == "/":
    hasil = angka1/angka2
    print(f"hasil dari {angka1} / {angka2}        = {hasil:,.2f}")
else:
    print("Operator yang anda masukan salah, mohon perhatikan")
    print("+(tambah), -(kurang), x(kali), /(bagi)")
print("="*50)    
akhir = "Terima kasih".center(50,"-")
print(akhir)


