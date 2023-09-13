#test

import tkinter as tk
from tkinter import ttk
import Flowsheet as fl

# from Flowsheet.Fowsheet import Course

# from tkinter import *
#Maybe make courseList like a lookup dictionary, so you can look up the name of the Course and it returns the obj course
CourseList = []
# Cells = []
root = tk.Tk()

root.geometry("1000x600")
root.title('Main bit')
# root.configure")



#I think that we should begin with an intro screen, where you can select to make a 'new Project' etc 
















class cell:
    def __init__(self, course= None, selected = False):
        self.course = course
        self.selected = selected
    
    def editframe(self):
        wind = tk.Tk()
        wind.title('Edit ' + self.course.CourseName)
        wind.geometry('500x500')

        label1 = tk.Label(wind, text = "Course Name: " )
        label1.pack()
        cname = tk.StringVar(wind)
        cname.set(self.course.CourseName)
        courseEnter1 = tk.Entry(wind, textvariable=cname)
        courseEnter1.pack()


        label2 = tk.Label(wind, text = "Part: " )
        label2.pack()
        Part_options = [ 'Part IA', 'Part IB', 'Part II', 'Part III']
        cpart = tk.StringVar(wind)
        cpart.set(self.course.part)
        dropdown = tk.OptionMenu(wind, cpart, *Part_options)
        dropdown.pack()
        
        label3 = tk.Label(wind, text = "Term: " )
        label3.pack()
        Term_options = ['Mihcaelmas', 'Lent', 'Easter']
        cterm = tk.StringVar(wind)
        cterm.set(self.course.term)
        dropdown2 = tk.OptionMenu(wind, cterm, *Term_options)
        dropdown2.pack()

        label4 = tk.Label(wind, text = "Number of lectures: " )
        label4.pack()
        lec_options = [16,24]
        clecs = tk.StringVar(wind)
        clecs.set(self.course.Numlecs)
        dropdown3 = tk.OptionMenu(wind, clecs, *lec_options)
        dropdown3.pack()
        
        # prereqs = []
        # label5 = tk.Label(wind, text = 'Prerequisites' )
        # label5.pack()
        # prereq_options = CourseList
        # tk.Listbox(wind)
        
        def saveandclose():
            #Saving stuff
            self.updatecourse(cname.get(), cpart.get(), cterm.get(), int(clecs.get()))
            self.updatecell()
            wind.destroy()
        

        savebutton = tk.Button(wind, text= 'Save',command=saveandclose)
        savebutton.pack()

        



        
    
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

        self.label2 = tk.Label(self.frame,text = self.course.term + ', ' + self.course.part + ', ' + str(self.course.Numlecs))
        self.label2.pack()

        # self.editbutton = tk.Button(master =self.frame, text='edit')

        # self.editbutton.pack(side ='right')
        edit1 = tk.Button(self.frame, text = 'Edit', command = self.editframe)

        edit1.pack()

        closebutton = tk.Button(self.frame, text = 'Delete', command = self.deletecell )
        closebutton.pack()

    def updatecourse(self, newname, newpart, newterm, newlecs):
        self.course.updatename(newname)
        self.course.updatepart(newpart)
        self.course.updateterm(newterm)
        self.course.updatelecs(newlecs)
       
    def updatecell(self):
        self.Label.configure(text = self.course.CourseName)
        self.label2.configure(   text = self.course.term + ', ' + self.course.part + ', ' + str(self.course.Numlecs)) 

    def deletecell(self):
        CourseList.remove(self.course)
        self.frame.destroy()



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

    







    


add_course_button = tk.Button(root, text= 'Add Course', command= createCourse)
add_course_button.pack()



class editline():
    def __init__(self,course,selected) -> None:
        self.course = course
    
    def createline(self):
        pass


def cellview():
    mainroot = tk.Tk()
    mainroot.geometry("1000x600")
    mainroot.title('Main bit')

    for course in CourseList:
        pass


    mainroot.mainloop()


    pass





def editview():
    # root.quit()
    root.destroy()
    editview = tk.Tk()
    editview.geometry('1000x600')
    editview.title('Edit View')
    
    #then here put all the things on the editscreen
    # for course in CourseList:
    #     coursecell = cell(course, False)
    #     #this doesnt work since createFrame puts the cell into the root not the edit!
    #     coursecell.createFrame()


    def saveandclose():
        editview.destroy()
        root.mainloop()

       

    returnbutton = tk.Button(editview, text = 'save', command = saveandclose)
    returnbutton.pack()

   

    editview.mainloop()

    


edit_view_button = tk.Button(root, text='Enter Edit View', command = editview)
edit_view_button.pack()


# c1 = fl.Course("Algebraic Topology", 'Part II',  'Michaelmas' , 24)

# cell1 = cell( c1)

# edit1 = tk.Button(root, text = 'Edit', command = cell1.editframe)

# edit1.pack()


def printcourses():
    if len(CourseList)==0:
        print('no courses')
    else:
        for course in CourseList:
            print(course)

course_chekcer  = tk.Button(root, text = 'Check courses', command= printcourses)
course_chekcer.pack(side='bottom')



root.mainloop()


 