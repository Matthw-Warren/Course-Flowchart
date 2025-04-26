import sys, os

sys.path.insert(0, os.path.abspath("."))
import src.Flowsheet as fl
import streamlit as st
import pandas as pd



graph = fl.Graph('CamMaths')
course_0 = fl.Course(123, 'Algebraic Geometry', 2, 'Lent', 24, [12,'MonWedFri'])
graph.add_course(course_0)
df=  graph.graph_to_df()
print(df)

reverse = fl.df_to_graph(df, 'reversal')
print(reverse)