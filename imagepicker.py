from tkinter import *


if __name__ == "__main__":
  root = Tk()

  label1 = Label(root, text="Name")
  label2 = Label(root, text="Password")

  label1.grid(row=0, column=0)
  label1.grid(row=1, column=0)

  entry1 = Entry(root)
  entry2 = Entry(root)

  entry1.grid(row=0, column=1)
  entry2.grid(row=1, column=1)

  root.mainloop()
  pass
