import tkinter
from tkinter import *
import math
import tempfile, base64, zlib


ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)
    
    
def clearprobabilitas():
    na.delete(0, END)
    ns.delete(0, END)
    labelstringpa.set("")

def clearkombinasi():
    nk.delete(0, END)
    kk.delete(0, END)
    

def hitungprobabilitas():
    inputna = float(na.get())
    inputns = float(ns.get())
    
    hitungpa = inputna/inputns
    stringpa = str(hitungpa)
    labelstringpa.set(stringpa)
    
    
def hitungkombinasi() :
    inputn = int(nk.get())
    inputk = int(kk.get())
    
    angkan = 1
    for n in range(1, inputn + 1):
        angkan *= n
    
        hasiln = float(angkan)
    
    angkak = 1
    for k in range(1, inputk + 1):
        angkak *= k
        
        hasilk = float(angkak)
    
    nkurangk = n - k
    angkakurang = 1
    for j in range(1, nkurangk + 1) :
        angkakurang *= j 
    
        hasilnkurangk = float(angkakurang)
    
    perhitungankombinasi = hasiln/(hasilk*hasilnkurangk)
    perhitunganfloat = float(perhitungankombinasi)
    
    perhitunganstring = str(perhitunganfloat)
    
    labelstringnk.set(perhitunganstring)
    
    
    

root = Tk()
root.title("Aplikasi hitung")
root.geometry("300x500")
root.resizable(0,0)
root.iconbitmap(default=ICON_PATH)
label = tkinter.Label(root, text="Window with transparent icon.")

menubar = Menu(root)
menu1 = Menu(menubar, tearoff=0)

menu1.add_command(label="tentang aplikasi")
menubar.add_cascade(label="about", menu=menu1)



judul = Label(root, text="Aplikasi ini dibuat untuk melakukan perhitungan \nprobabilitas dan kombinasi")
judul.place(x=20, y=10)

kanvas = Canvas(root)
kanvas.create_line(0, 25, 300, 25)
kanvas.place(x=0, y=45)

judul1 = Label(root, text="-menghitung probabilitas-")
judul1.place(x=80, y=80)

judulrumus = Label(root, text="rumus :")
judulrumus.place(x=10, y=110)

rumuspa = Label(root, text="P(A) = n(A)/n(S)")
rumuspa.place(x=100, y=120)

labelna = Label(root, text="n(A) : ")
labelna.place(x=10, y=150)

na = Entry(root)
na.place(x=50, y=153)

labelns = Label(root, text="n(S) : ")
labelns.place(x=10, y=180)

ns = Entry(root)
ns.place(x=50, y=183)

hasilpa = Label(root, text="P(A) yang didapat adalah ")
hasilpa.place(x=10, y=210)

labelstringpa = StringVar()
labelpa = Label(root, textvariable=labelstringpa, fg="red")
labelpa.place(x=150, y=210)

tombolhasil = Button(root, text="hitung", bg="green",fg="white",command=hitungprobabilitas)
tombolhasil.place(x=100, y=240)

tombolclearprobabilitas = Button(root, text="clear", bg="red", fg="white",command=clearprobabilitas)
tombolclearprobabilitas.place(x=150, y=240)




kanvas2 = Canvas(root)
kanvas2.create_line(0, 25, 300, 25)
kanvas2.place(x=0, y=265)







judul2 = Label(root, text="-menghitung kombinasi-")
judul2.place(x=80, y=295)

judulrumus2 = Label(root, text="rumus :")
judulrumus2.place(x=10, y=310)

rumuspermutasi = Label(root, text="nPk = n!/k!(n-k)!")
rumuspermutasi.place(x=100, y=320)

labeln = Label(root, text="n! : ")
labeln.place(x=10, y=345)

nk = Entry(root, width=5)
nk.place(x=50, y=345)

labelk = Label(root, text="k! : ")
labelk.place(x=10, y=375)

kk = Entry(root, width=5)
kk.place(x=50, y=375)

hasilpa = Label(root, text="nCk yang didapat adalah ")
hasilpa.place(x=10, y=400)

labelstringnk = StringVar()
labelnk = Label(root, textvariable=labelstringnk, fg="red")
labelnk.place(x=160, y=400)

tombolhasil = Button(root, text="hitung",bg="green", fg="white",command=hitungkombinasi)
tombolhasil.place(x=100, y=430)

tombolclearkombinasi = Button(root, text="clear", bg="red", fg="white",command=clearkombinasi)
tombolclearkombinasi.place(x=150, y=430)








root.config(menu=menubar)
root.mainloop()