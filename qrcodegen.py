from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
root=Tk()

def generate():
    link_name=name_entry.get()
    link_add=link_entry.get()
    file_name=link_name + '.png'
    url=pyqrcode.create(link_add)
    url.png(file_name,scale=8)
    image=ImageTk.PhotoImage(Image.open(file_name))
    image_label=Label(image=image)
    image_label.image=image
    canvas.create_window(200,450,window=image_label)

canvas=Canvas(root,width=400,height=600)
canvas.pack()
app_label=Label(root,text='QR Code Generator',fg='red',font=('arial,30'))
canvas.create_window(200,50,window=app_label)
name_label=Label(root,text='Link name')
link_label=Label(root,text='Link')
canvas.create_window(100,110,window=link_label)
canvas.create_window(100,160,window=name_label)
name_entry=Entry(root)
link_entry=Entry(root)
canvas.create_window(200,110,window=link_entry)
canvas.create_window(200,160,window=name_entry)
button=Button(text='Generate QR code',command=generate)
canvas.create_window(200,200,window=button)

root.mainloop()
