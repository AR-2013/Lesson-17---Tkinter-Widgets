from tkinter import *

root=Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("100x180")
    top.title("toplevel")
    mango = top(top, text="This is a toplevel window.")

    top.mainloop()

    orange = Label(root, text="This is a root window")
    btn = Button(root, text="Click here to open another window", command = topwin)

    orange.pack()
    btn.pack()