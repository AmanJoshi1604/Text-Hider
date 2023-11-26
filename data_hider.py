from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb #pip install stegano

root=Tk()
root.title("Steganography Project...")
root.geometry("700x500+250+180")
root.resizable(False,False)
root.configure(bg="#2f4155")

def Showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='Select Image File',
                                        filetype=(("PNG File","*.png"),
                                                  ("JPG File","*.jpg"),
                                                  ("All File","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    ibl.configure(image=img,width=250,height=250)
    ibl.image=img

def Hide():
    global secret
    message=text1.get(1.0,END)
    secret=lsb.hide(str(filename),message)

def Show():
    clear_message=lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clear_message)

def Save():
    secret.save("Hidden.png")
    

#icon
image_icon=PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file="logo1.png")
Label(root,image=logo,bg="#2f4155").place(x=10,y=10)

Label(root,text="Add Your Image",bg="#2d4155",fg="white",font="arieal 25 bold").place(x=100,y=20)

#First Frame
f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)

ibl=Label(f,bg="black")
ibl.place(x=40,y=10)

#Second Frame
frame2=Frame(root,bd=3,width=340,height=280,bg="white",relief=GROOVE)
frame2.place(x=350,y=80)

text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#Third Frame
frame3=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=370)

Button(frame3,text="Open Image",width=10,height=2,font="arial 14 bold",command=Showimage).place(x=20,y=30)
Button(frame3,text="Save Image",width=10,height=2,font="arial 14 bold",command=Save).place(x=180,y=30)
Label(frame3,text="Picture, Image, Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)


#Fourth Frame
frame4=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame4.place(x=360,y=370)

Button(frame4,text="Hide Data",width=10,height=2,font="arial 14 bold",command=Hide).place(x=20,y=30)
Button(frame4,text="Show Data",width=10,height=2,font="arial 14 bold",command=Show).place(x=180,y=30)
Label(frame4,text="Picture, Image, Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)



root.mainloop()
