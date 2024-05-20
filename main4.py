from tkinter import *
import os
from PIL import ImageTk, Image
from scrolled_frame import ScrolledFrame
# from tkscrolledframe import ScrolledFrame


root = Tk()
root.geometry("500x500")
root.title(" main4 ")

# Create a ScrolledFrame widget
sf = ScrolledFrame(root, width=640, height=480)
# Bind the arrow keys and scroll wheel
sf.bind_arrow_keys(root)
sf.bind_scroll_wheel(root)

# Create a frame within the ScrolledFrame
inner_frame = sf.display_widget(Frame)

img_list=[]


def Take_input(some_inner_frame):  
  #img_list = []
  path = "/home/soumic/Pictures/Wallpapers" # my folder
  n_row = 0
  n_col = 0
  index = 0
  x = IntVar()
  for f in os.listdir(path):
      img_list.append(ImageTk.PhotoImage(Image.open(os.path.join(path,f))))
      n_col +=1
      index +=1
      if n_col > 9:
          n_row +=1
          n_col = 1
      # radio_button = Label(some_inner_frame, width=100, height=60) # 
      radio_button = Radiobutton(some_inner_frame, image=img_list[index-1], indicatoron=0, bd=2, variable = x, value = index, width=100, height = 60)
      radio_button.grid(row=n_row, column = n_col)
      # radio_button.configure(image= img_list[index-1] )
  # root.update()
  pass
     
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
                 command = lambda:Take_input(some_inner_frame=inner_frame))
 
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()





sf.pack(side="top", expand=1, fill="both")






root.mainloop()
