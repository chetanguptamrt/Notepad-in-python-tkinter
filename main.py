from tkinter import *
from tkinter.filedialog import askopenfiles,asksaveasfile
from tkinter.messagebox import askyesno
import os

def New():
    global f
    f=None
    root.title("Untitled - Notepad")
    textarea.delete(1.0,END)
def Open():
    global f
    if not (textarea.get(0.0,END)=='\n'):
        x=askyesno('Save','Do you want to save data?')
        if x==True:
            Save()
    file_path=askopenfiles(defaultextension=".txt", mode="r",filetypes=(("Text documents","*.txt"),('All files','*.*')))
    textarea.delete(0.0,END)
    root.title(os.path.basename(file_path[0].name)+" - Notepad")
    textarea.insert(0.0,file_path[0].read())
    f=file_path[0].name

def Save():
    global textarea,f
    if f==None:
        Saveas()
    else:
        with open(f,mode='w') as file_save:
            file_save.write(textarea.get(0.0,END))

def Saveas():
    global textarea,f
    file_path=asksaveasfile(defaultextension=".txt", mode="w",filetypes=(("Text documents","*.txt"),('All files','*.*')))
    if not (file_path==None):
        file_path.write(textarea.get(0.0,END))
        root.title(os.path.basename(file_path.name)+" - Notepad")
        f=file_path.name
        print(file_path,f)

def Cut():
    textarea.event_generate(("<<Cut>>"))
def Copy():
    textarea.event_generate(("<<Copy>>"))
def Paste():
    textarea.event_generate(("<<Paste>>"))
def Help():
    tsmg.showinfo("Help","You can write any thing in this notepad.")
def contactus():
    tsmg.showinfo("Contact us","Contact me on twitter @chetanguptamrt")
def About():
    tsmg.showinfo("About","Notepad - 1.0 \n By Chetan Gupta")
#----------------------------------------------------------
root=Tk()
root.geometry("600x400")
root.title("Untitled - Notepad")
f=None
#-------------------------------------------------------
mainmenubar=Menu(root)
m1=Menu(mainmenubar,tearoff=0)
m1.add_command(label="New file",command=New)
m1.add_command(label="Open file",command=Open)
m1.add_command(label="save file",command=Save)
m1.add_command(label="save as file",command=Saveas)
m1.add_separator()
m1.add_command(label="exit",command=quit)
mainmenubar.add_cascade(label="File",menu=m1)
m2=Menu(mainmenubar,tearoff=0)
m2.add_command(label="Cut",command=Cut)
m2.add_command(label="Copy",command=Copy)
m2.add_command(label="Paste",command=Paste)
mainmenubar.add_cascade(label="Edit",menu=m2)
m3=Menu(mainmenubar,tearoff=0)
m3.add_command(label="Help",command=Help)
m3.add_command(label="About",command=About)
m3.add_command(label="Contact us",command=contactus)
mainmenubar.add_cascade(label="About",menu=m3)
root.config(menu=mainmenubar)
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=BOTH)
textarea=Text(root,font="lucida 15 ",padx=5,pady=5)
textarea.pack(fill=BOTH,padx=5,pady=5,expand=TRUE)
textarea.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=textarea.yview)
root.mainloop()
