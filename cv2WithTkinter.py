import numpy as np
import cv2
import Tkinter as tk
from PIL import Image, ImageTk
import time
from Tkinter import Text, END, DISABLED, NORMAL

x = 0.0
y = 0.0
tim = time.time()
t = time.time() - tim

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Digital Microscope")
#window.config(background="#FFFFFF")

#Graphics window
imageFrame = tk.Frame(window, width=320, height=240)
imageFrame.grid(row=4, column=0, padx=10, pady=2)

textField1 = tk.Text(window, height=1, width=30)
print(textField1)
textField1.grid(row=0, column=1, padx=10, pady=1)
textField2 = tk.Text(window, height=1, width=30)
textField2.grid(row=1, column=1, padx=10, pady=1)
textField3 = tk.Text(window, height=1, width=30)
textField3.grid(row=2, column=1, padx=10, pady=1)

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)

cap.set(3, 320)
cap.set(4, 240)
def show_frame():
    global x, y, tim, t
    t = time.time() - tim
    textField1.config(state=NORMAL)
    textField1.delete(1.0,END)
    textField1.insert(END, ("Time: " + str(t)))
    print(textField1)
    textField1.config(state=DISABLED)
    textField2.config(state=NORMAL)
    textField2.delete(1.0,END)
    textField2.insert(END, (str(x)))
    textField2.config(state=DISABLED)
    textField3.config(state=NORMAL)
    textField3.delete(1.0,END)
    textField3.insert(END, (str(y)))
    textField3.config(state=DISABLED)
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    x += 0.1
    y += 0.0345
    lmain.after(2, show_frame)

#Slider window (slider controls stage position)
#sliderFrame = tk.Frame(window, width=600, height=100)
#sliderFrame.grid(row = 600, column=0, padx=10, pady=2)


show_frame()  #Display 2
window.mainloop()  #Starts GUI
