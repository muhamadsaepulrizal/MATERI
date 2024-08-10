'''Tutorial menulis file ekxternal (.txt)'''

#1. mode write harus ada tambhan encoding=""
#   untuk write dia akan membuka file baru jika tidak ada si file (.txt) nya
#   lalu akan menimpa atau overwrite isinya
with open("data1.txt",mode="w",encoding="utf-8") as file:
    file.write("alucard orang tasik")

#ini akan menimpa yang diatas
with open("data1.txt",mode="w",encoding="utf-8") as file:
    file.write("zilong orang garut nimpa alucard orang garut")
#bagaimana jika ingin menambahkan? = pakai append

#2. Mode append
with open("data2.txt",mode="w",encoding="utf-8") as file:
    file.write("argus orang garut\n")
#   "w" diganti dengan "a" supaya akan menambah isi filenya/ menyambungkan
with open("data2.txt",mode="a",encoding="utf-8") as file:
    file.write("bambang orang kidul\n")
with open("data2.txt",mode="a",encoding="utf-8") as file:
    file.write("ini hasil append")

#3. mode r+
# untuk menimpa yang mau kita rubah



#kesimpulannya jika ingin menggandakan data mka diawal paka "a" kebawahnya juga "a"
#jika ingin menimpa pakai "w" saja maka isi sebelumny akan kehapus
#jika "w" lalu "a" seterusnya itu akan membuat file baru dengan "w" dan ditambah tanpa menimpa dengan "a"




