
import tkinter as tk
from tkinter import ttk
import Flowsheet as fl
import pickle


# from Flowsheet.Fowsheet import Course

# from tkinter import *
#Maybe make courseList like a lookup dictionary, so you can look up the name of the Course and it returns the obj course
# Cells = []
root = tk.Tk()

root.geometry("600x400")
root.title('Menu')
# root.configure"






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
        
        label5 = tk.Label(wind, text = 'Prerequisites' )
        label5.pack()


        # #Could make it so can only choose prereqs from previous years.
        # prereq_options = 
        listbox = tk.Listbox(wind, selectmode='multiple')
        listbox.insert(1, *CourseList)       
        listbox.pack()

        
        def saveandclose():
            #Saving stuff
            # prereqs_index = listbox.curselection()
            # for k in pre


            self.updatecourse(cname.get(), cpart.get(), cterm.get(), int(clecs.get()))
            self.updatecell()
            wind.destroy()
        

        savebutton = tk.Button(wind, text= 'Save',command=saveandclose)
        savebutton.pack()

        



        
    
    def createFrame(self,window):
        self.frame = tk.Frame(window,
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


class editline:
    def __init__(self,course = None ,selected = False) -> None:
        self.course = course
    
    def createline(self):

        line = tk.Label(editroot, text = self.course.CourseName)
        line.pack()



def save_and_exit():
    # if cellroot_displayed:
    #     cellroot.destroy()
    # elif editroot_displayed:
    #     editroot.destroy()
    
    savescreen = tk.Tk()
    savescreen.geometry('600x400')
    savescreen.title('Save flowsheet')


    label = tk.Label(savescreen, text = "Filename:" )
    label.pack()

    filenamevar = tk.StringVar(savescreen)
    save_entry = tk.Entry(savescreen, textvariable=filenamevar)

    save_entry.pack()

    
    def exitcommand():
        filename = filenamevar.get()
        print(filename)
        with open(filename + '.pickle', 'wb') as handle:
            pickle.dump(CourseList, handle, protocol=pickle.HIGHEST_PROTOCOL)
        savescreen.destroy()
        exit()

    def discard():
        exit()


    savebutton = tk.Button(savescreen,text = 'Save', command = exitcommand)
    savebutton.pack()

    discardbutton = tk.Button(savescreen, text = 'Discard', command = discard)
    discardbutton.pack()

    savescreen.mainloop()




def createCourse():
    #viewtype is either 'cell' or 'edit'

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



    label5 = tk.Label(popup, text = 'Prerequisites' )
    label5.pack()


    # #Could make it so can only choose prereqs from previous years.
    # prereq_options = 
    listbox = tk.Listbox(popup, selectmode='multiple')
    listbox.insert(1, *CourseList)       
    listbox.pack()








    def saveandclose():
        #Saving stuff
        
        newcourse = fl.Course(cname.get(),cpart.get(),cterm.get(),int(clecs.get()))
        prereqs_indices = listbox.curselection()
        for k in prereqs_indices:
            newcourse.prereqs.append(CourseList[k])


        if cellroot_displayed:
            newcell = cell(newcourse)
            newcell.createFrame(cellroot)
        elif editroot_displayed:
            new_edit_line = editline(newcourse)
            new_edit_line.createLine(editroot)
        

        # Cells.append(newcell)
        CourseList.append(newcourse)
        popup.destroy()
        

    savebutton = tk.Button(popup, text= 'Save',command=saveandclose)
    savebutton.pack()

    popup.mainloop()

    

def load_cell_view():

    root.destroy()
    

    global cellroot 
    global cellroot_displayed 
    cellroot_displayed = True
    editroot_displayed = False
    cellroot = tk.Tk()
    cellroot.geometry("1000x600")
    cellroot.title('Main bit')
    for course in CourseList:
        newcell = cell(course)
        newcell.createFrame(cellroot)
            

    edit_view_button = tk.Button(cellroot, text='Enter Edit View', command = load_edit_view)
    edit_view_button.pack()
      
    add_course_button = tk.Button(cellroot, text= 'Add Course', command= createCourse)
    add_course_button.pack()


    # course_chekcer  = tk.Button(cellroot, text = 'Check courses', command= printcourses)
    # course_chekcer.pack(side='bottom')


    save_and_quit = tk.Button(cellroot, text = 'Save and Exit' , command = save_and_exit)
    save_and_quit.pack()

    cellroot.mainloop()




def load_edit_view():
    # root.quit()
    cellroot.destroy()

    global editroot 
    global editroot_displayed
    editroot_displayed = True
    cellroot_displayed = False
    editroot = tk.Tk()
    editroot.geometry('1000x600')
    editroot.title('Edit View')
    
    for course in CourseList:
        neweditline = editline(course)
        neweditline.createline()
    
    #then here put all the things on the editscreen
    # for course in CourseList:
    #     coursecell = cell(course, False)
    #     #this doesnt work since createFrame puts the cell into the root not the edit!
    #     coursecell.createFrame()



    returnbutton = tk.Button(editroot, text = 'Cell View', command = load_cell_view)
    returnbutton.pack()

    save_and_quit = tk.Button(editroot,text = 'Save and Exit', command= save_and_exit)
    save_and_quit.pack()
   

    editroot.mainloop()



# def printcourses():
#     if len(CourseList)==0:
#         print('no courses')
#     else:
#         for course in CourseList:
#             print(course)



CourseList=[]


def loadcourses():
    pass


new_project_button = tk.Button(root, text = 'New Project', command=load_cell_view)
#Work out how to save and load course information!
load_project_button = tk.Button(root, text  = 'Load Project', command=loadcourses)



new_project_button.pack()
load_project_button.pack()





root.mainloop()


 