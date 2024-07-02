from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def open_file():
    filepath = filedialog.askopenfilename(title="Please select a file",
                                          # initialdir=r"#The file path to desired directory(not nesseccarry)",
                                          filetypes=(("c files", "*.c"), ("python files", "*.py"), ("html files", "*.html")))
    file = open(filepath, 'r')
    file_contents = file.read()
    messagebox.showinfo(title="show info", message=file_contents)
    file.close()


window = Tk()

open_button = Button(window, text="open file", command=open_file)
open_button.pack()


window.mainloop()
