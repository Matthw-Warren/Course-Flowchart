import sys, os

sys.path.insert(0, os.path.abspath("."))
import src.Flowsheet as fl
import streamlit as st
import pandas as pd



# graph = fl.Graph()
# course_0 = fl.Course(123, 'Algebraic Geometry', 2, 'Lent', 24, 'MWF-12')
# course_1 = fl.Course(234, 'Algebraic Toplogy', 3, 'Lent', 24, 'TTS-09' )
# graph.add_course(course_0)
# graph.add_course(course_1)
# df=  graph.graph_to_df()
# df.to_csv('src/saves/test.csv')
# print(df)

df = pd.read_csv('src/saves/test_withlink.csv')
print(df)
graph = fl.df_to_graph(df)
print(graph[123])

graph.link_pre_post(123,234)
#Let's say that all courses ids have to be int
print(graph[123].postreqs)

df = graph.graph_to_df()
print(df)
# df.to_csv('src/saves/test_withlink.csv')