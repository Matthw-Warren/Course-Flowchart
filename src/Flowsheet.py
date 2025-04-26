import networkx as nx
import pandas as pd


part_to_int = {
    "Part IA" : 1,
    "Part IB" : 2,
    "Part II" : 3,
    "Part III" : 4
}







class Graph(dict):
    def __init__(self):
        pass

    def add_course(self,course):
        if course.id in self.keys():
            return 'Id already taken'
        self[course.id] = course
        

    def remove_course(self, course_id):
        self.pop(course_id)

    def get_hours_per_week(self):
        return sum([x.number_lecs for x in self.values()])
    

    def get_course_names(self):
        return [x.course_name for x in self.values()]



    def graph_to_df(self):
        cols = ['id', 'Name', 'Year', 'Term', 'Num lecs', 'Time', 'Prereqs', 'Postreqs', 'Coreqs' ]
        df = pd.DataFrame(columns=cols)
        for i, course in enumerate(self.values()):
            df.loc[i] = course.course_to_list()
        return df
    

    def graph_to_csv(self,name):
        df= self.graph_to_df()
        df.to_csv('src/saves'+name +'.csv')


class Course:
    def __init__(self, id, course_name: str, year ,term: str , number_lecs: int, timeandday ,  prereqs:set = set(), postreqs:set = set(), coreqs:set=set(), selected = False):
        #The prereqs and post reqs will be an array containing other courses, the general is for general info
        #  such as which term, how many courses, the lecturer. References could contain like books and lecture notes and stuff

        #Note to self, This is a graph - so the prereqs are going to be only the immediate ones - we dont need to go crazy and add all of the prereqs in
        self.id = id
        self.course_name = course_name
        self.prereqs = prereqs
        self.postreqs = postreqs
        self.coreqs = coreqs 
        self.term = term
        self.number_lecs = number_lecs
        self.selected = selected
        self.year = year
        self.timeandday = timeandday
        self.direct_connections  = self.prereqs.union(self.postreqs .union(self.coreqs))


    def __str__(self) -> str:
        return 'Year {} {}, Term: {}, Number of lectures: {}'.format(self.year, self.course_name, self.term, self.number_lecs)

    def course_to_list(self):
        return [self.id, self.course_name, self.year, self.term, self.number_lecs, self.timeandday, self.prereqs, self.postreqs, self.coreqs]



    def addprereq(self, newprereq):
        self.prereq.append(newprereq)
        self.direct_connections  = self.prereqs.union(self.postreqs .union(self.coreqs))

    def addpostreq(self, newpostreq):
        self.postreqs.append(newpostreq)
        self.direct_connections  = self.prereqs.union(self.postreqs .union(self.coreqs))

    def addcoreq(self,newcoreq):
        self.coreq.append(newcoreq)
        self.direct_connections  = self.prereqs.union(self.postreqs .union(self.coreqs))

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


def df_to_graph(df):
    cols_check = ['id', 'Name', 'Year', 'Term', 'Num lecs', 'Time', 'Prereqs', 'Postreqs', 'Coreqs' ]
    if list(df.columns) != cols_check:
        print('Improper columns') 
        return
    graph = Graph()
    graph_keys = df['id']
    graph_vals = df[cols_check[1:]]
    for k in range(len(df)):
        row = graph_vals.iloc[k]
        graph[graph_keys.iloc[k]]  = Course(tuple(row))
    return graph
