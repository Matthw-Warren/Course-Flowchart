import sys, os
sys.path.insert(0, os.path.abspath("."))
import streamlit as st
from src import Flowsheet as fl


graph = st.session_state['graph']
df = graph.graph_to_df()


cols_to_show = ['id', 'Name', 'Year', 'Term', 'Num lecs', 'Time']
st.title('List View')
st.dataframe(df[cols_to_show], hide_index=[0])
