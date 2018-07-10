#QUES1-->
from tkinter import *
root=Tk()
hwL=Label(root,text="Hello World!!")
hwL.pack()
exitB=Button(root,text="Exit",width=25,command=root.destroy,)
exitB.pack(side=BOTTOM)
root.mainloop()

#QUES2--->
from tkinter import *
def write():
    p=Label(text="Tkinter is easy to use!")
    p.pack()
    p.mainloop()
root=Tk()
frame=Frame(root)
frame.pack()
hwL=Label(frame,text="Hello World!!")
hwL.pack()
b1=Button(frame,text="INFORMATION",width=25,command=write)
b1.pack(side=LEFT)
exitB=Button(root,text="Exit",width=25,command=root.destroy,)
exitB.pack(side=BOTTOM)
root.mainloop()

#QUES3-->
from tkinter import *
root=Tk()
text=0
def text_change():
    global text
    text += 1
    if text > 4:
        text = 1
    print("changed to:", text)
    b1.config(text=text)
def text_print():
    print("current:", text)

hwL=Label(root,text="Hello World!!")
hwL.pack()
b1=Button(text="CURRENT INFORMATION",width=25,command=text_print)
b1.pack()
b2 = Button(text="INFORMATION CHANGED", width=25, command=text_change)
b2.pack()
exitB=Button(text="Exit",width=25,command=root.destroy,)
exitB.pack(side=BOTTOM)
root.mainloop()

#QUES4-->
from tkinter import *
root=Tk()
def write():
    name=uP+uL
    print("Your Name is:",name)

root.title("DETAILS:")
frame=Frame(root)
frame.pack()
uL=Label(frame,text="First Name:")
uL.pack()
#uL.grid(row=0,column=0,sticky="e")
uP=Label(frame,text="Last Name:")
uP.pack()
#uP.grid(row=1,column=0,sticky="e")
eB=Entry(root,bd=5)
#eB.grid(row=1,column=0,sticky="E")
eB.pack()
eP=Entry(root,bd=5)
#eP.grid(row=1,column=0,sticky="e")
eP.pack()
b=Button(text="SUBMIT",width=25,command=write)
b.pack()
root.mainloop()

