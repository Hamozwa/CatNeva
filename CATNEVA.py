import tkinter as tk
from PIL import Image, ImageTk
import time


# Create window
root = tk.Tk()
root.geometry("150x150+1300+700")
root.attributes('-topmost', True) 

# Load images
image_paths = ["images/Idle1.png", "images/Idle2.png"]
images = [ImageTk.PhotoImage(Image.open(path)) for path in image_paths]

# Set background transparent
root.config(highlightbackground='green')
root.overrideredirect(True)
root.wm_attributes('-transparentcolor','green')

# Create label
label = tk.Label(root, bd=0, bg='green')
label.pack()

def update_image(index):
    label.config(image=images[index])
    root.after(1000, update_image, (index + 1) % len(images))
    
# Start main loop
update_image(0)
root.mainloop()
