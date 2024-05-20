# Python Image Picker

How can I build this thing?

* Tkinter
* An edittext to get folder path
* Lazily load the images in current folder
* a list of valid image formats (jpg, jpeg, png, ... ...)
* Recyclerview / list view / grid view
* item click detection
* on item click, open get models metadata (file name, file abs path, ...)

/home/soumic/Pictures/Wallpapers

Python may ask you to install / upgrade "pillow" dependency.

    pip3 install pillow --upgrade

## How to run python from maxscript?

https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=MAXDEV_Python_executing_python_executing_python_from_maxscript_html

Looks like you need to add this line:

python.ExecuteFile @"C:\Program Files\Autodesk\3ds Max 2015\scripts\Python\demoBentCylinder.py"

So in this case,

python.ExecuteFile @"C:\Program Files\some\path\to\start_image_explorer.py"
