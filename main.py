#test

import tkinter as tk
from tkinter import ttk
import Flowsheet as fl

# from Flowsheet.Fowsheet import Course

# from tkinter import *

CourseList = []
# Cells = []
root = tk.Tk()

root.geometry("1000x600")
root.title('Main bit')
# root.configure")

class cell:
    def __init__(self, course= None, selected = False):
        self.course = course
        self.selected = selected
    
    def editframe(self):
        wind = tk.Tk()
        wind.title('Edit ' + self.course.CourseName)
        
    
    def createFrame(self):
        self.frame = tk.Frame(root,
                              background="red",
                              height = 10,
                              width = 10
                                )
        # self.frame.configure(border = '')
        self.frame.pack()
        # self.frame.bind("B1")

        self.Label = tk.Label(master = self.frame, text = self.course.CourseName, height = 5, font = 'Arial 36 bold', background='blue')
        self.Label.pack( side = 'left')


        # self.editbutton = tk.Button(master =self.frame, text='edit')

        # self.editbutton.pack(side ='right')
        edit1 = tk.Button(root, text = 'Edit', command = self.editframe)

        edit1.pack()

    def updatecourse(self, newcourse):
        CourseList.remove(self.course)
        CourseList.append(newcourse)
        self.course = newcourse

        





def createCourse():
    popup = tk.Tk()
    popup.title('Popup Thing')
    popup.geometry('500x500')


    label1 = tk.Label(popup, text = "Course Name: " )
    label1.pack()
    cname = tk.StringVar(popup)
    courseEnter1 = tk.Entry(popup, textvariable=cname)
    courseEnter1.pack()


    label2 = tk.Label(popup, text = "Part: " )
    label2.pack()
    Part_options = [ 'Part IA', 'Part IB', 'Part II', 'Part III']
    cpart = tk.StringVar(popup)
    cpart.set('Part IA')
    dropdown = tk.OptionMenu(popup, cpart, *Part_options)
    dropdown.pack()
    
    label3 = tk.Label(popup, text = "Term: " )
    label3.pack()
    Term_options = ['Mihcaelmas', 'Lent', 'Easter']
    cterm = tk.StringVar(popup)
    cterm.set('Michaelmas')
    dropdown2 = tk.OptionMenu(popup, cterm, *Term_options)
    dropdown2.pack()

    label4 = tk.Label(popup, text = "Number of lectures: " )
    label4.pack()
    lec_options = [16,24]
    clecs = tk.StringVar(popup)
    clecs.set(16)
    dropdown3 = tk.OptionMenu(popup, clecs, *lec_options)
    dropdown3.pack()
    
    prereqs = []
    label5 = tk.Label(popup, text = 'Prerequisites' )
    label5.pack()
    prereq_options = CourseList
    tk.Listbox(popup)








    def saveandclose():
        #Saving stuff
        newcourse = fl.Course(cname.get(),cpart.get(),cterm.get(),int(clecs.get()))
        newcell = cell(newcourse)
        newcell.createFrame()
        # Cells.append(newcell)
        CourseList.append(newcourse)
        popup.destroy()
        

    savebutton = tk.Button(popup, text= 'Save',command=saveandclose)
    savebutton.pack()


    #Now, when we make a new course, we want a corresponding cell in the flowchart
    newframe = tk.Frame(root, )
    
    popup.mainloop()

    







    


butt1 = tk.Button(root, text= 'Add Course', command= createCourse)
butt1.pack()



# c1 = fl.Course("Algebraic Topology", 'Part II',  'Michaelmas' , 24)

# cell1 = cell( c1)

# edit1 = tk.Button(root, text = 'Edit', command = cell1.editframe)

# edit1.pack()


root.mainloop()