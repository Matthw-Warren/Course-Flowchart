import sys, os

sys.path.insert(0, os.path.abspath("."))

import streamlit as st
from src import Flowsheet as fl


graph = fl.Graph()
course_0 = fl.Course(123, 'Algebraic Geometry', 2, 'Lent', 24, 'MWF-12')
graph.add_course(course_0)
df=  graph.graph_to_df()


cols_to_show = ['id', 'Name', 'Year', 'Term', 'Num lecs', 'Time']
st.write(df[cols_to_show])
