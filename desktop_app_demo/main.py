#Modules
from tkinter import *

#create window
window = Tk()
window.title("Desktop App Demo")

lbl = Label(window, text="Hello World")
lbl.grid(column=0, row=0)

window.mainloop()