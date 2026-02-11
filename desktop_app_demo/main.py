#Modules
from tkinter import *
import tkinter.font as tkFont

#create window
window = Tk()

window.title("Desktop App Demo")
window.geometry('350x200')

#create label
font = tkFont.Font(family = "Helvetica", size = 50, weight = "bold")
lbl = Label(window, text="Hello World", font= font)
lbl.grid(column = 0, row = 0)

#create text entry
user_text = Entry(window, width = 10)
user_text.grid(column = 1, row = 0)

#button func
def clicked():
    res = "welcome to " + user_text.get()
    lbl.configure(text = res)
    btn.pack_forget()
    btn.grid_forget()
    

#create button
btn = Button(window, text = "Click me",bg = "white", fg = "blue", command = clicked)
btn.grid(column = 2, row = 0)



#start window
window.mainloop()

#notes
'''
1. To create a desktop application, we can use the Tkinter library in Python.
2. We can create a window using the Tk() function and set its title and geometry.
3. We can create a label using the Label() function and set its text and font.
4. We can create a text entry using the Entry() function and set its width.
5. We can create a button using the Button() function and set its text, background color, foreground color, and command.
6. We can define a function that will be called when the button is clicked.
7. We can start the window using the mainloop() function.
8. We can use the grid() method to position the widgets in the window.
9. We can use the configure() method to change the text of the label.
10. We can use the pack_forget() and grid_forget() methods to hide the button after it is clicked.
'''