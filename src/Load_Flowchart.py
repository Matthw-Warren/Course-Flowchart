
import networkx as nx
import Flowsheet as fl
#Let's just do a streamlit app - tkinter (if I recall correctly) annoyed me

import streamlit as st


#So we want to create a graph of courses essentially - then have some nice ways of viewing this.


st.title('Course Flowchart')
st.write('')

st.cache_data(fl.Graph())