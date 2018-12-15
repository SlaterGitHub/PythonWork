import cv2
import numpy as np
import os
from PIL import Image, ImageTk
import Tkinter as tk
import lz4.frame

window = tk.Tk()
window.wm_title("Camera Feed")

imageFrame = tk.Frame(window, width=1000, height=1000)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)

def show_frame():
    global frames, front, back
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    frame = lz4.frame.compress(frame)
    if (front - 1) == back or (front+1) == back:
        frames[front] = frame
        front += 1
        back += 1
    else:
        frames[front] = [frame]
        back += 1
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(2, show_frame)

    sliderFrame = tk.Frame(window, width=600, height=100)
    sliderFrame.grid(row = 600, column=0, padx=10, pady=2)


frames = [None]*5
front = 0
back = 0

show_frame()
window.mainloop()
for x in range(len(frames)):
    frames[x] =(np.fromstring(lz4.frame.decompress(frames[x]), dtype = "uint8"))
print(frames)
