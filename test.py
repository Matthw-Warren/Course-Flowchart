import tkinter as tk
import Flowsheet as fl
import os
import platform

import pickle


root = tk.Tk()
root.geometry('800x800+1000+30')



label1 = tk.Label(root, padx=200,pady=200,border= 1 , borderwidth=10,  bg='blue',text = 'test')
label1.pack()


c1 = fl.Course("Algebraic Topology", 'Part II',  'Michaelmas' , 24)
c2 = fl.Course("Algebraic Geometry",  'Part II','Lent', 24)
c3 = fl.Course("Algebraic Number Theory",  'Part III','Lent', 24)


CourseList = [c1,c2,c3]

prereqs = []
label5 = tk.Label(root, text = 'Prerequisites' )
label5.pack()
prereq_options = CourseList


listbox = tk.Listbox(root, width=50, selectmode='multiple')
listbox.pack()

listbox.insert(1,*CourseList)
# listbox.yview()



def listselected():
    coursesindex = listbox.curselection()

    print(coursesindex)
    for k in coursesindex:
        print(CourseList[k])



lisc = tk.Button(root, text = ' press', command = listselected)
lisc.pack()

root.mainloop()
