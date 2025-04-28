import sys, os
sys.path.insert(0, os.path.abspath("."))
import streamlit as st
from src import Flowsheet as fl



# def add_course():
#     st.popover('Add course')

if 'graph' not in st.session_state.keys():
    graph = fl.Graph()

graph = st.session_state['graph']
course_ids = graph.keys()
df = graph.graph_to_df()
selected_only = False



def export_to_csv():
    pass

def reset():
    pass



with st.popover('Add course'):
    def id_check():
        if course_id in graph.keys():
            st.markdown('id already taken!')
    course_id = st.text_input('Course id', on_change=id_check)
    
    course_name = st.text_input('Course Name')
    course_year = st.selectbox('Year', [1,2,3,4])
    course_term = st.selectbox('Term', ['Michaelmas', 'Lent', 'Easter'])
    course_num_lecs = st.text_input('Number of lectures')
    course_days = st.selectbox('Days', ['MWF', 'TTS'])
    course_time_of_day = st.text_input('Time')
    course_time = course_days +'-' + course_time_of_day
    course_prereqs = st.multiselect('Prereqs',course_ids)
    course_postreqs = st.multiselect('Postreqs',course_ids)

    def add_course():
        newcourse = fl.Course(course_id,course_name, course_year,course_term,course_num_lecs, course_time )
        graph.add_course(newcourse)
        for course in course_prereqs:
            graph.link_pre_post(course ,course_id )
        for course in course_postreqs:
            graph.link_pre_post(course_id ,course)

    add_button = st.button('Enter', on_click=add_course)

    

# graph = st.session_state['graph']
# course_names = [course.course_name for course in graph.values()]
# df = graph.graph_to_df()


#Other buttons:  Export to CSV, Reset, Selected only, 


with st.container():
    b1,b2,b3 , b4= st.columns([2,1.1,2,5])
    with b1: save_csv_button = st.button('Export to CSV', on_click=export_to_csv)
    with b2: reset_button  = st.button('Reset', on_click=reset)
    with b3: selected_only = st.toggle('Selected Only')
        



def show_data(graph, selected ):
    df = graph.graph_to_df()
    df_to_show = df[cols_to_show]
    if selected:
        df_to_show = df_to_show.loc[df_to_show['Selected'] == True]
    st.data_editor(df_to_show, hide_index=True, column_config={
        'Selected': st.column_config.CheckboxColumn('Selected', disabled=False),
        'Year' : st.column_config.SelectboxColumn('Year', options=[1,2,3,4] ,disabled=False)
        })
    #We have a data_editor  -need edits to actually change our graph also.



cols_to_show = ['id', 'Name', 'Year', 'Term', 'Num lecs', 'Time', 'Selected']
st.title('List View')
show_data(graph, selected_only)
