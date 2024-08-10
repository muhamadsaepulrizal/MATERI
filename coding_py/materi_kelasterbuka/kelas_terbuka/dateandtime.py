#date and time
import datetime as dt #menambahkan

hariini = dt.date.today() #keluar tanggal sekarang dengan .date.today()
print(hariini)
print(f"hari ini adalah hari {hariini:%A}")# :%A untuk cek tanggal secra spesifik

tanggal = dt.date(2004,12,10)
print(tanggal)
print(f"ultah saya {tanggal} hari: {tanggal:%A}")# :%A untuk cek tanggal secra spesifik(hari saat saya lahir)

print("Masukan Tanggal, Bulan, Dan Tahun lahir anda!")
print("-"*50)
tanggal = int(input("Masukan Tangal lahir anda: "))
bulan   = int(input("Masukan Bulan Lahir anda : "))
tahun   = int(input("Masukan Tahun lahir anda : "))
print("----------")
lengkap = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda : {lengkap}")
print(f"Harinya adalah hari: {lengkap:%A}")
#hitung umur
hariini = dt.date.today()
umurhari = hariini-lengkap #inisialisasi usia dengan hariini dikurang lengkap(tanggal lahir)
umurtahun = umurhari.days // 365 #inisialisasi umue hari ketahun dng dibagi 365
umur_bulansisa = (umurhari.days % 365) // 30 #inisialisasi setahun lebih berapa bulan umur anda(19tahun lebih 4bulan)
print(f"Usia anda sekarang : {umurtahun}, lebih {umur_bulansisa} bulan")

 







