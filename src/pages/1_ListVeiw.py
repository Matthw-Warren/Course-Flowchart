import streamlit as st
from src import flowsheet as fl


current_graph = fl.graph()
current_df = current_graph.graph_to_df()


st.write(current_df)
