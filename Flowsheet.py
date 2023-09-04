

import tkinter as tk
from tkinter import ttk
#Is there a better way to store all of these properties of the class??

class Course:
    def __init__(self, courseName: str, part:str   ,term: str, Numlecs: int, areas=[], prereqs=[], postreqs=[], selected = False):
        #The prereqs and post reqs will be an array containing other courses, the general is for general info
        #  such as which term, how many courses, the lecturer. References could contain like books and lecture notes and stuff
        self.CourseName = courseName
        self.areas = areas
        #We may want to differentiate between 'essential', 'useful' and so on.
        #Also, we could add a list of 'good to be accompanied by' 
        self.prereqs = prereqs
        self.postreqs = postreqs
        # self.general = general
        # self.references = references
        self.term = term
        self.Numlecs = Numlecs
        self.selected = selected
        self.part = part



    def addprereq(self, newprereq):
        self.prereqs.append(newprereq)
    def addpostreq(self, newpr):
        self.postreqs.append(newpr)


    def __str__(self) -> str:
        return self.part + " : " + self.CourseName + ', ' + str(self.Numlecs) + " lectures in "  + self.term 

    def getfamilty(self):
        #This is going to get all of the courses that the current course is connected to, eg its anscestors and descendants, (see that the structure here is essentialy a tree)
        pass

    

    
class Area:
    def __init__(self,name,tagcolour=None):
        self.name = name
        self.colour = tagcolour


c1 = Course("Algebraic Topology", 'Part II',  'Michaelmas' , 24)
c2 = Course("Algebraic Geometry",  'Part II','Lent', 24)



# def CreateCourse():
#     print('Course Name : ')
#     cname = input()
#     print('Enter course year (Part 1A, Part 1B, Part II, Part III) : ')
#     cpart = input()
#     print('Enter term : ')
#     cterm = input()
#     print('Number of lectures : ') 
#     clecs = input()
#     return Course(cname,cpart,cterm, clecs)



