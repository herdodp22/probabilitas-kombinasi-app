import tkinter
from tkinter import *
import math

def hitungprobabilitas():
    inputna = int(na.get())
    inputns = int(ns.get())
    
    hitungpa = inputna/inputns
    stringpa = str(hitungpa)
    labelstringpa.set(stringpa)

root = Tk()
root.title("aplikasi probabilitas")
root.geometry("300x300")
root.resizable(0,0)

menubar = Menu(root)
menu1 = Menu(menubar, tearoff=0)

menu1.add_command(label="tentang aplikasi")
menubar.add_cascade(label="about", menu=menu1)



judul = Label(root, text="Aplikasi ini dibuat untuk melakukan perhitungan \nprobabilitas")
judul.place(x=20, y=10)

kanvas = Canvas(root)
kanvas.create_line(0, 25, 300, 25)
kanvas.place(x=0, y=45)

judul1 = Label(root, text="-menghitung probabilitas-")
judul1.place(x=10, y=80)

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

tombolhasil = Button(root, text="hitung", command=hitungprobabilitas)
tombolhasil.place(x=120, y=240)








root.config(menu=menubar)
root.mainloop()