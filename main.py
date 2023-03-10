
import streamlit as st
from streamlit_option_menu import option_menu

import matplotlib.pyplot as plt
import datetime

import file_handler




st.set_page_config(layout="wide")

st.markdown(""" 
    <style> 
        .header1 {
            font-size:35px ;
            font-family: 'Cooper Black'; 
            color: #FF9633;
            text-align: center;
            text-decoration: underline;
        } 
        .header2 {
            margin-top: 20px;
            font-size:20px ;
            font-family: 'Cooper Black'; 
            color: #FF9633;
            text-align: center;
            text-decoration: underline;
        } 
    </style>
     """, unsafe_allow_html=True)

with st.sidebar:
    choose = option_menu(None, ["Home",       "Logs",              "Budget",    "Exercise",     "Diet",       "ToDo"],
                         icons=['house-fill','journal-arrow-down', 'cash-coin', 'input-cursor', 'cup-straw', 'kanban'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#826f8f"},
    })


if choose == "Home":
    st.markdown('<p class="font">Home</p>', unsafe_allow_html=True)
    st.write("Please Eat My Bees")


elif choose == "Logs":

    tab1, tab2 = st.tabs(["Today's Log", "Old Logs"])

    with tab1:

        def primary_form_callback():
            log_data = {
                "date": st.session_state.date,

                "mood_metric": st.session_state.mood_metric,
                "health_metric": st.session_state.health_metric,
                "mania_metric": st.session_state.mania_metric,
                "depression_metric": st.session_state.depression_metric,
                "anxiety_metric": st.session_state.anxiety_metric,

                "wake_up_time": st.session_state.wake_up_time,
                "sleep_time": st.session_state.sleep_time,
                "weight": st.session_state.weight,

                "screen_time": st.session_state.screen_time,
                "prn_count": st.session_state.prn_count,
                "herb_count": st.session_state.herb_count,
                "cigs_count": st.session_state.cigs_count,

                "reading_time": st.session_state.reading_time,
                "piano_time": st.session_state.piano_time,
                "meditation_time": st.session_state.meditation_time,
                "work_time": st.session_state.work_time,
            }
            file_handler.write_primary_log_file(log_data)

        st.markdown('<p class="header1">Logs</p>', unsafe_allow_html=True)

        with st.form(key='primary_log'):
            col1, col2 = st.columns(2)

            with col1:
                st.markdown('<p class="header2">General</p>', unsafe_allow_html=True)
                mood = st.slider('Mood', 0, 100, 50, key='mood_metric')
                health = st.slider('Health', 0, 100, 50, key='health_metric')
                mania = st.slider('Mania', 0, 100, 50, key='mania_metric')
                depression = st.slider('Depression', 0, 100, 50, key='depression_metric')
                anxiety = st.slider('Anxiety', 0, 100, 50, key='anxiety_metric')

                st.markdown('<p class="header2">Bio</p>', unsafe_allow_html=True)
                cola, colb = st.columns(2)
                with cola:
                    wakeup = st.time_input('Wake Up', datetime.time(7, 00), key='wake_up_time')
                    sleep = st.time_input('Sleep', datetime.time(23, 00), key='sleep_time')
                with colb:
                    weight = st.number_input('Weight (lbs)', min_value=0., step=1., key='weight')

            with col2:

                st.markdown('<p class="header2"> Vice </p>', unsafe_allow_html=True)

                cola, colb = st.columns(2)
                with cola:
                    screen_time = st.number_input('Screen Time (hrs)', min_value=0., step=1., key='screen_time')
                    prn = st.number_input('Prn', min_value=0., step=1., key='prn_count')
                with colb:
                    herb = st.number_input('Herb', min_value=0., step=1., key='herb_count')
                    cigs = st.number_input('Cigs', min_value=0., step=1., key='cigs_count')


                st.markdown('<p class="header2"> Virtue </p>', unsafe_allow_html=True)
                cola, colb = st.columns(2)
                with cola:
                    reading_time = st.number_input('Reading (hrs)', min_value=0., step=1., key='reading_time')
                    piano_time = st.number_input('Piano (hrs)', min_value=0., step=1., key='piano_time')
                with colb:
                    meditation_time = st.number_input('Meditation (hrs)', min_value=0., step=1., key='meditation_time')
                    work_time = st.number_input('Work (hrs)', min_value=0., step=1., key='work_time')

                date = st.date_input("Date", datetime.date.today(), key='date')
                submit_button = st.form_submit_button(label='Submit', on_click=primary_form_callback)

    with tab2:
        st.markdown('<p class="font">Old</p>', unsafe_allow_html=True)


elif choose == "Budget":
    tab1, tab2 = st.tabs(["Main Budget", "Old Logs"])

    with tab1:
        st.markdown('<p class="header1">Budget</p>', unsafe_allow_html=True)

        col1, col2 = st.columns([3,2])

        with col2:
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
            sizes = [15, 30, 5, 50]
            explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            st.pyplot(fig1)


elif choose == "Exercise":
    st.markdown('<p class="header1">Exercise</p>', unsafe_allow_html=True)

elif choose == "Diet":
    tab1, tab2 = st.tabs(["Main Budget", "Old Logs"])

    with tab1:
        st.markdown('<p class="header1">Diet</p>', unsafe_allow_html=True)


        col1, col2 = st.columns([2, 2])

        with col1:
            def diet_form_callback():
                diet_data = {
                    "date": st.session_state.date,
                    "food_name": st.session_state.food_name,

                    "protein": st.session_state.protein,
                    "carbs": st.session_state.carbs,
                    "fat": st.session_state.fat,
                    "calories": st.session_state.calories,

                    "dairy": st.session_state.dairy,
                    "fruit": st.session_state.fruit,
                    "vegetable": st.session_state.vegetable,
                }
                file_handler.write_diet_log_file(diet_data)


            with st.form(key='diet_log'):
                name = st.text_input('Food Name', key='food_name')
                cola, colb = st.columns(2)
                with cola:
                    protein = st.number_input('Protein (g)', min_value=0, step=1, key='protein')
                    carbs = st.number_input('Carbs (g)', min_value=0, step=1, key='carbs')
                with colb:
                    fat = st.number_input('Fat (g)', min_value=0, step=1, key='fat')
                    calories = st.number_input('Calories (g)', min_value=0, step=1, key='calories')

                with st.expander("Advanced"):
                    colc, cold = st.columns(2)
                    with colc:
                        date = st.date_input("Date", datetime.date.today(), key='date')
                    with cold:
                        dairy = st.checkbox('Dairy', key='dairy')
                        fruit = st.checkbox('Fruit', key='fruit')
                        vegetable = st.checkbox('Vegetable', key='vegetable')

                submit_button = st.form_submit_button(label='Submit', on_click=diet_form_callback)
        with col2:
            st.write("Yeet yeet")
            st.write("Nutrition Lookup: [link](https://nutritiondata.self.com/)")


