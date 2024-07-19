import tkinter as tk
from PIL import Image, ImageTk
import time
import random

x = 1300

#Obtain screen resolution [x, y]
roo = tk.Tk()
roo.update_idletasks()
roo.attributes('-fullscreen', True)
roo.state('iconic')
geometry = roo.winfo_geometry()
roo.destroy()
screen_res = geometry.split("+")[0].split("x")

#Create image groupings
idle = [1,[0,1]]
gonnasleep = [0.75,[2,3,4,5,6,7,8]]
sleeping = [0.5,[9,10,11,12]]
wakeup = [0.75,[13,14,15,16,17]]
walkleft = [0.6,[18,19,20,21]]
walkright = [0.2,[22,23,24,25]]


# Create window
root = tk.Tk()
root.geometry("150x150+"+str(x)+"+675")
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
    "images/sleeping1.png",
    "images/sleeping2.png",
    "images/sleeping3.png",
    "images/sleeping4.png",
    "images/wakeup1.png",
    "images/wakeup2.png",
    "images/wakeup3.png",
    "images/wakeup4.png",
    "images/wakeup5.png",
    "images/walkleft1.png",
    "images/walkleft2.png",
    "images/walkleft3.png",
    "images/walkleft4.png",
    "images/walkright1.png",
    "images/walkright2.png",
    "images/walkright3.png",
    "images/walkright4.png"
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
    match last_event[1][0]:
        
        case 0: #idle
            decider = random.randint(0,3)
            match decider:
                case 0:
                    return idle
                case 1:
                    return gonnasleep
                case 2:
                    return walkleft
                case 3:
                    return walkright
        
        case 2: #gonnasleep
            return sleeping
        
        case 9: #sleeping
            decider = random.randint(0,1)
            match decider:
                case 0:
                    return sleeping
                case 1:
                    return wakeup
        
        case 13: #wakeup
            return idle
        
        case 18: #walkleft
            return idle
        
        case 22: #walkright
            return idle


#Run event
def event_run(event):
    global x
    global screen_res
    
    if event[1][0] == 18: #walkleft
        
        #Pick Random destination to left
        left_limit = max(0, x - 300)
        new_x =(random.randint(left_limit,x))
        increment = (x-new_x)//4

        for frame in event[1]:
            label.config(image=images[frame])
            x -= increment
            root.geometry("150x150+"+str(x)+"+675")
            root.update()
            time.sleep(event[0])
        
        
    elif event[1][0] == 22: #walkright

        #Pick Random destination to left
        right_limit = min(screen_res[1], x + 300)
        new_x =(random.randint(right_limit,x))
        increment = (x+new_x)//4

        for frame in event[1]:
            label.config(image=images[frame])
            x += increment
            root.geometry("150x150+"+str(x)+"+675")
            root.update()
            time.sleep(event[0])
    
    else: #events with no movements
        for frame in event[1]:
            label.config(image=images[frame])
            root.update()
            time.sleep(event[0])
            
    #Recurison used for next event
    event_run(event_decide(event))
    
# Start main loop
event_run(idle)
root.mainloop()
