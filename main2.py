
from tkinter import *
from tkinter.ttk import *
from os import listdir
from os.path import isfile, join


root = Tk()
root.geometry("300x300")
root.title(" Q&A ")

def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    onlyfiles = [f for f in listdir(INPUT) if isfile(join(INPUT, f))]
    print(onlyfiles)
    first_image = INPUT + "/" + "scared_muppets.png" # onlyfiles[0]

    photo = PhotoImage(file = first_image)
    imageview = Canvas(root)
    imageview.create_image( (0,0), image = photo)
    
    imageview.pack()

    Tk.update_idletasks(root)
    


     
l = Label(text = "What is 24 * 5 ? ")
inputtxt = Text(root, height = 1,
                width = 100,
                bg = "light yellow")
 
Output = Text(root, height = 5, 
              width = 25, 
              bg = "light cyan")
 
Display = Button(root,
                 width = 20, 
                 text ="Show",
                 command = lambda:Take_input())
 
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
 
mainloop()
