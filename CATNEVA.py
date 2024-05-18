import tkinter as tk
from PIL import Image, ImageTk
import time

#Create image groupings
idle = [0,1]
gonnasleep = [2,3,4,5,6,7,8]


# Create window
root = tk.Tk()
root.geometry("150x150+1300+700")
root.attributes('-topmost', True) 

# Load images
image_paths = [
    "images/Idle1.png",
    "images/Idle2.png",
    "images/gonnasleep1.png",
    "images/gonnasleep2.png",
    "images/gonnasleep3.png",
    "images/gonnasleep4.png",
    "images/gonnasleep5.png",
    "images/gonnasleep6.png",
    "images/gonnasleep7.png",
]

images = []
for path in image_paths:
    img = Image.open(path)
    images.append(ImageTk.PhotoImage(img))


# Set background transparent
root.config(highlightbackground='green')
root.overrideredirect(True)
root.wm_attributes('-transparentcolor','green')

# Create label
label = tk.Label(root, bd=0, bg='green')
label.config(width=150, height=150)
label.pack()

#Decide next event
def event_decide(last_event):
    match last_event[0]:
        case 0:
            return gonnasleep
        case 2:
            return idle

#Run event
def event_run(event):

    for frame in event:
        label.config(image=images[frame])
        root.update()
        time.sleep(1)

    event_run(event_decide(event))
    
# Start main loop
event_run(idle)
root.mainloop()
