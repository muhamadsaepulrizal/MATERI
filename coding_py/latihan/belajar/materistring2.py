print("\n\nMateri string widht and alignment")
print("="*50)

#widht and multiline

#data
datanama = "Ucup Surucup"
dataumur = 20
datatinggi = 170.5
data_nomorsepatu = 42

#string standard
datastr = f"nama = {datanama}, umur = {dataumur}, tinggi = {datatinggi}, no.sepatu = {data_nomorsepatu}"
print(5*"="+"Data String Standard"+5*"=")
print(datastr)

#string multiline dengan enter/newline/(\n)
datastr = f"nama = {datanama}, \numur = {dataumur}, \ntinggi = {datatinggi}, \nno.sepatu = {data_nomorsepatu}"
print("\n"+5*"="+"Data String Multiline"+5*"=")
print(datastr)

#string multiline pakai kutip triplets("""""")/ menampilkan sesuai dengan yg kita ketik
datanama = "Ucup"
datastr = f"""nama      = {datanama:>5}
umur      = {dataumur}
tinggi    = {datatinggi}
no.sepatu = {data_nomorsepatu}
""" 
print("\n"+5*"="+"Data String Multiline dengan kutip triplets(kutip 2 3kali)"+5*"=")
print(datastr)



















