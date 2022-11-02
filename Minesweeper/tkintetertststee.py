from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!", background="white").grid(column=0, row=0)
root['background'] = 'white'
root.mainloop()