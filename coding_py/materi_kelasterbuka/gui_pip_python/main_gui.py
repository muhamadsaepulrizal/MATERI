'''tkinter (bisa dipelajari di python interface to Tcl/Tk)
GUI (graphical user interface)
adapun untuk mempelajari package yaitu wb pypi
'''

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#__init__
window = tk.Tk() #awal body
window.configure(bg="red") #untuk warna
window.geometry("300x200") #untuk ukuran layar/monitor/dll
window.resizable(False,False)#supaya gui tidak bisa digerakkan (berukuran tetap)
window.title("program belajar GUI")#untuk judul atau header program

#variabel dan fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_klik():
    '''fungsi ini akan dipanggil oleh tombol'''
    pesan = f"hallo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, kenapa??"
    showinfo(title="whazzup!", message=pesan) #u/ mengeluarkan info

#frame input
input_frame = ttk.Frame(window)

#penempatan: grid, pack, place
input_frame.pack(padx=10, pady=10, fill="x",expand=True)

#komponen komponen
#1. label u/ nama depan
namadepan_label = ttk.Label(input_frame,text="nama depan")
namadepan_label.pack(padx=10,fill="x",expand=True)

#2. entry nama depan
namadepan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
namadepan_entry.pack(padx=10,fill="x",expand=True)

#3. label u/ nama belakang
namabelakang_label = ttk.Label(input_frame,text="nama belakang")
namabelakang_label.pack(padx=10,fill="x",expand=True)

#4. entry nama belakang
namabelakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
namabelakang_entry.pack(padx=10,fill="x",expand=True)

#5. tombol
tombol_sapa = ttk.Button(input_frame, text="sapa",command=tombol_klik)
tombol_sapa.pack(fill='x',expand=True, padx=10, pady=10)


#mainloop window
window.mainloop() #akhir body



