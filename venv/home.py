# import module from tkinter for UI
from tkinter import *

import os
from datetime import datetime;
from tkinter import filedialog
# creating instance of TK
root = Tk()

root.configure(background="white")

# root.geometry("300x300")

def function1():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Image files", "*.jpg*"), ("all files", "*.*")))



def function2():
    os.system("py train_mask_detector.py")


def function3():
    os.system("py detect_mask_video.py")



def function5():
    os.system("py detect_mask_video.py")



def function6():
    root.destroy()




# stting title for the window
root.title("Face Mask Detector")

# creating a text label
Label(root, text="Face Mask Detection Using Deep Learning", font=("times new roman", 20), fg="white", bg="#795548",
      height=2).grid(row=0, rowspan=2, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating first button
Button(root, text="Face Mask Detection", font=('times new roman', 20), bg="#bcaaa4", fg="#3e2723", command=function3).grid(
    row=7, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)


Button(root, text="Exit", font=('times new roman', 20), bg="#795548", fg="white", command=function6).grid(row=8,
                                                                                                         columnspan=2,
                                                                                                         sticky=N + E + W + S,
                                                                                                         padx=5, pady=5)

root.mainloop()
