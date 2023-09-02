#@Author: kippari2
#@Help: Timanttiso
#@Date: 2.9.2023
#@Version: 1.0

import os
from tkinter import filedialog as fd
import tkinter.messagebox
from tkinter import *

root = Tk()
root.title("Mod Rename V1.0")
root.resizable(False, False)

#Changes to the proper directory so that icons can be found
#directory = os.path.realpath(os.path.dirname(__file__))
#os.chdir(directory)

l = Label(root, text="Rename mods")
l.pack()

root.iconbitmap("Icons/icon.ico")

canvas = Canvas(root, width = 300, height = 232)      
canvas.pack(fill = "both", expand = True)

img = PhotoImage(file = "Icons/bg.png")
canvas.create_image(0, 0, anchor=NW, image=img)
root.geometry("300x360+64+64")

srcpath = ""

def rename(srcpath):
    if srcpath == "" or srcpath == None:
        tkinter.messagebox.showinfo(title="Warning", message="No Directory Selected")
        return
    else:
        files = os.listdir(srcpath)
        if var.get() == 0 or var.get() == None or var.get == "":
            tkinter.messagebox.showinfo(title="Warning", message="No Type Selected")
        elif var.get() == 1:
            print("renameto09")
            for file in files:
                oldname = srcpath + "/" + file
                if "_" in file:
                    prefix = "LS09_"
                    newname = srcpath + "/" + prefix + file
                    print(oldname)
                    print(newname)
                    os.rename(oldname, newname)
                elif " " in file:
                    prefix = "LS09 "
                    newname = srcpath + "/" + prefix + file
                    print(oldname)
                    print(newname)
                    os.rename(oldname, newname)
                else:
                    prefix = "LS09" 
                    newname = srcpath + "/" + prefix + file
                    print(oldname)
                    print(newname)
                    os.rename(oldname, newname)
                
        elif var.get() == 2:
            print("renameto08")
            for file in files:
                oldname = srcpath + "/" + file
                if "_" in file:
                    prefix = "LS08_"
                    newname = srcpath + "/" + prefix + file
                    print(oldname)
                    print(newname)
                    os.rename(oldname, newname)
                elif " " in file:
                    prefix = "LS08 "
                    newname = srcpath + "/" + prefix + file
                    print(oldname)
                    print(newname)
                    os.rename(oldname, newname)
                else:
                    prefix = "LS08" 
                    newname = srcpath + "/" + prefix + file
                    print(oldname)
                    print(newname)
                    os.rename(oldname, newname)
        
def select_files():
    global srcpath
    srcpath = fd.askdirectory()

open_button = Button(
    root,
    text='Select directory',
    command=select_files
)
open_button.pack(expand=True)
  
var = IntVar()
R1 = Radiobutton(
    root, 
    text="LS09", 
    variable=var, 
    value=1)
R1.pack( anchor = W )

R2 = Radiobutton(
    root, 
    text="LS08", 
    variable=var, 
    value=2)
R2.pack( anchor = W )

ExecuteOrder = Button(
    root,
    text="Execute",
    command= lambda : rename(srcpath)
)
ExecuteOrder.pack(expand=True)
root.mainloop()