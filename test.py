import tkinter as tk
import Flowsheet as fl
import os
import platform

import pickle
from tkinter import filedialog


root = tk.Tk()


def openf():
    filepath = filedialog.askopenfilename()
    print(filepath)
    
    with open(filepath, 'rb') as handle:
        CourseList = pickle.load(handle)

    print(CourseList)



button = tk.Button(root, text = 'get file', command = openf)
button.pack()


root.mainloop()


