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

g_img_list=[]


user_selected_image_absolute_path = ""

def on_radio_button_click(path):
  global user_selected_image_absolute_path
  user_selected_image_absolute_path = path
  print(f"on radio clicked {user_selected_image_absolute_path}")
  Output.delete('1.0', END)  
  Output.insert(END, user_selected_image_absolute_path)
  pass


def take_input(some_inner_frame):
  image_ext = [".jpg", ".png"]

  img_list = []
  path = inputtxt.get("1.0", "end-1c")
  hardcoded_path = "/home/soumic/Pictures/Wallpapers" # my folder
  n_row = 0
  n_col = 0
  index = 0
  x = IntVar()
  for f in os.listdir(path):      
      image_path = os.path.join(path,f)
      is_actually_image = False
      for ext in image_ext:
        if image_path.endswith(ext):
           is_actually_image = True
           break

      if not is_actually_image:
         continue   
      
      original_img = Image.open(image_path)
      resized = original_img.resize(( 100, 60 ))

      img_list.append(ImageTk.PhotoImage(resized))
      n_col +=1
      index +=1
      if n_col > 9:
          n_row +=1
          n_col = 1 
      # radio_button = Label(some_inner_frame, width=100, height=60) # 
      radio_button = Radiobutton(some_inner_frame, image=img_list[index-1], 
                                value = index, indicatoron=0, bd=2, variable = x,  width=100, height = 60,
                                command=lambda  m = image_path: on_radio_button_click(m)
                                )
      radio_button.grid(row=n_row, column = n_col)
        # radio_button.configure(image= img_list[index-1] )
  # root.update()
  global g_img_list
  g_img_list = img_list
  pass
     
l = Label(text = "What is 24 * 5 ? ")
inputtxt = Text(root, height = 1,
                width = 100,
                bg = "light yellow")
 
Output = Text(root, height = 5, 
              width = 100, 
              bg = "light cyan")
 
Display = Button(root,
                 width = 20, 
                 text ="Show",
                 command = lambda:take_input(some_inner_frame=inner_frame))
 
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()





sf.pack(side="top", expand=1, fill="both")






root.mainloop()
