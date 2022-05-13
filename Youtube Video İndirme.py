from cProfile import label
import fractions
from tkinter import *
from tkinter.filedialog import *
import tkinter as tk
from pytube import YouTube
from tkinter import messagebox


root = tk.Tk()
root.title('YouTube Dosya İndirme')
root.geometry("300x150")
root.resizable(width=0,height=0)
root.eval('tk::PlaceWindow . center')
def verial():
    path_save = askdirectory()    
    link=YouTube(yazi.get())
    stream=link.streams.get_highest_resolution()
    stream.download(path_save)
    var = messagebox.showinfo("Dogukan Kurnaz" , "Dosya İndirildi.")

yazi=Entry(root)
yazi.place(x=60,y=50,width=200)


button=Button(text="Gönder",command=verial)
button.place(x=130,y=80)

etiket=Label(text="dogukaN © 2022 ")
etiket.place(x=100,y=125)
etiket1=Label(text="YouTube Linki Giriniz ")
etiket1.place(x=100,y=15)

root.mainloop()
