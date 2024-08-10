import os
#kwargs berupa dictionary
'''**kwargs fungsinya untuk '''

def fungsi(nama,tinggi,berat):
    '''fungsi biasa'''
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
fungsi("ucup",170,55)

def fungsi(**kwargs):
    '''fungsi kwarg (kita bisa buat fungsi dengan keyword)'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    #print(kwargs)
fungsi(nama="ucup",tinggi=170,berat=55)

#studi kasus:

def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("tidaka ada operasi")

    return output


hasil = math(1,2,3,4,option="tambah")
print(f"hasil jumlah adalah {hasil}")    
hasil = math(1,2,3,4,option="kali")    
print(f"hasil kali adalah {hasil}")    











