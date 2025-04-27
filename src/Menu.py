
import networkx as nx
import Flowsheet as fl
#Let's just do a streamlit app - tkinter (if I recall correctly) annoyed me

import streamlit as st
import pandas as pd
from io import StringIO

#So we want to create a graph of courses essentially - then have some nice ways of viewing this.


st.title('Course Flowchart')


def new_graph():
    graph = fl.Graph()
    st.session_state['graph'] = graph

st.button('New Flowsheet',key = 'newButton', on_click=new_graph)


uploaded_file = st.file_uploader("Load a csv file")

if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    # st.write(dataframe)
    graph = fl.df_to_graph(dataframe)
    st.write('Dataframe successfully imported')
    st.session_state['graph'] = graph
    # st.session_state['df'] = dataframe



