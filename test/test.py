

import tkinter as tk
from tkinter import ttk
import Flowsheet as fl
import pickle
from tkinter import filedialog


root = tk.Tk()

root.geometry("600x400")
root.title('Menu')
# root.configure"

frametest = tk.Frame(root)
for k in range(4): 
    frametest.grid_columnconfigure(k,weight=1, minsize=80)


frametest.grid_rowconfigure(0,weight=1)

frametest.pack(fill = 'both' , expand=True)

col1 = tk.Frame(frametest)
col1.grid(column=0 , row = 0, sticky='ns ew')
col2 = tk.Frame(frametest)
col2.grid(column=1, row = 0)
col3 = tk.Frame(frametest)
col3.grid(column=2, row = 0)
col4 = tk.Frame(frametest)
col4.grid(column=3, row = 0)

scrollbar = tk.Scrollbar(
    col1
)
scrollbar.pack(side = 'right', fill = 'y')

cellcol1 = tk.Canvas(col1, yscrollcommand=scrollbar.set)
cellcol1.pack(side='left')


for k in range(20):
    r = tk.Label(cellcol1, text = f'{k}')
    r.pack()

scrollbar.configure(command= cellcol1.yview)



root.mainloop()



 