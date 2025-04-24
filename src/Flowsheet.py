import networkx as nx


part_to_int = {
    "Part IA" : 1,
    "Part IB" : 2,
    "Part II" : 3,
    "Part III" : 4
}



class Graph(dict):
    def __init__(self, name):
        self.name = name

    def add_course(self,course):
        pass




class Course:
    def __init__(self, id, course_name: str, year ,term: str , number_lecs: int, prereqs:set, postreqs:set, coreqs:set, selected = False):
        #The prereqs and post reqs will be an array containing other courses, the general is for general info
        #  such as which term, how many courses, the lecturer. References could contain like books and lecture notes and stuff

        #Note to self, This is a graph - so the prereqs are going to be only the immediate ones - we dont need to go crazy and add all of the prereqs in
        self.id = id
        self.course_name = course_name
        self.prereqs = prereqs
        self.posreqs = postreqs
        self.coreqs = coreqs 
        self.term = term
        self.number_lecs
        self.selected = selected
        self.year = year
        self.direct_connections  = self.prereqs+ self.postreqs + self.coreqs


    def __str__(self) -> str:
        return 'Year {} {}, Term: {}, Number of lectures: {}'.format(self.year, self.course_name, self.term, self.number_lecs)


    def addprereq(self, newprereq):
        self.prereq.append(newprereq)
        self.connections  = self.prereqs+ self.postreqs + self.coreqs

    def addpostreq(self, newpostreq):
        self.postreqs.append(newpostreq)
        self.connections  = self.prereqs+ self.postreqs + self.coreqs

    def addcoreq(self,newcoreq):
        self.coreq.append(newcoreq)
        self.connections  = self.prereqs+ self.postreqs + self.coreqs

    def remove_prereq(self, id):
        self.prereqs.remove(id)
        
    def remove_postreq(self, id):
        self.postreqs.remove(id)

    def remove_coreq(self, id):
        self.coreqs.remove(id)


    def get_deep_prereqs(self, Graph):
        #Graph will be a dict from id to the node
        output = self.prereqs
        digging = True
        while digging:
            size = len(output)
            for k in output:
                output = output.union(Graph[k.id].prereqs)
            if len(output) == size:
                digging = False
        return output     

    def get_deep_postreqs(self, Graph):
        #Graph will be a dict from id to the node
        output = self.postreqs
        digging = True
        while digging:
            size = len(output)
            for k in output:
                output = output.union(Graph[k.id].postreqs)
            if len(output) == size:
                digging = False
        return output     
        
    def get_all_connections(self,Graph):
        return self.get_deep_postreqs.union(self.get_deep_prereqs)


    def updatename(self, newname):
        self.course_name = newname
    
    def updateterm(self, newterm):
        self.term = newterm

    def updateyear(self, year):
        self.year = year
  
    def updatelecs(self, newlecs):
        self.number_lecs = newlecs



