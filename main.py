
import streamlit as st
from streamlit_option_menu import option_menu

import matplotlib.pyplot as plt
import datetime

import file_handler

## run app with >
## sudo streamlit run main.py

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

    # I dislike that it is done like this but streamlit requires you to create multiple session states in order to
    # update input widget values from an external function. I do not believe there is a better way.

    tab1, tab2 = st.tabs(["Today's Log", "Old Logs"])

    with tab1:

        def load_log(date):
            log = file_handler.get_individual_log(date)
            if(log != False):
                st.session_state['log_saved'] = True # Set log_saved status to true

                st.session_state['mood_metric_val'] = int(log[1])
                st.session_state['health_metric_val'] = int(log[2])
                st.session_state['mania_metric_val'] = int(log[3])
                st.session_state['depression_metric_val'] = int(log[4])
                st.session_state['anxiety_metric_val'] = int(log[5])

                st.session_state['wake_up_time_val'] = datetime.datetime.strptime(log[6], '%H:%M:%S').time()
                st.session_state['sleep_time_val'] = datetime.datetime.strptime(log[7], '%H:%M:%S').time()
                st.session_state['weight_val'] = float(log[8])

                st.session_state['screen_time_val'] = float(log[9])
                st.session_state['prn_count_val'] = int(log[10])
                st.session_state['herb_count_val'] = float(log[11])
                st.session_state['cigs_count_val'] = float(log[12])

                st.session_state['reading_time_val'] = float(log[13])
                st.session_state['piano_time_val'] = float(log[14])
                st.session_state['meditation_time_val'] = float(log[15])
                st.session_state['work_time_val'] = float(log[16])

                return True
            else:
                return False

        def initialize_log():
            st.session_state['log_saved'] = False

            st.session_state['mood_metric_val'] = 50
            st.session_state['health_metric_val'] = 50
            st.session_state['mania_metric_val'] = 50
            st.session_state['depression_metric_val'] = 50
            st.session_state['anxiety_metric_val'] = 50

            st.session_state['wake_up_time_val'] = datetime.time(7, 00)
            st.session_state['sleep_time_val'] = datetime.time(23, 00)
            st.session_state['weight_val'] = 0.0

            st.session_state['screen_time_val'] = 0.0
            st.session_state['prn_count_val'] = 0
            st.session_state['herb_count_val'] = 0.0
            st.session_state['cigs_count_val'] = 0.0

            st.session_state['reading_time_val'] = 0.0
            st.session_state['piano_time_val'] = 0.0
            st.session_state['meditation_time_val'] = 0.0
            st.session_state['work_time_val'] = 0.0


        if 'log_saved' not in st.session_state: # If log variables not initialized, initialize
            initialize_log()
            # Then try to load current log from file
            load_log(datetime.date.today())


        def change_log(): # Function is called when you change the date in order to load older logs
            initialize_log()
            if not load_log(st.session_state.date):
                initialize_log()

        def primary_form_callback(): # Save data
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
            if not st.session_state.log_saved:                          # If log is unsaved
                if file_handler.write_primary_log_file(log_data):   # Then try to save and mark the save in session
                    st.session_state.log_saved = True

        def mark_log_unsaved():
            st.session_state.log_saved = False


        st.markdown('<p class="header1">Logs</p>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<p class="header2">General</p>', unsafe_allow_html=True)
            mood = st.slider('Mood', 0, 100, st.session_state.mood_metric_val, on_change=mark_log_unsaved, key='mood_metric')
            health = st.slider('Health', 0, 100, st.session_state.health_metric_val, on_change=mark_log_unsaved, key='health_metric')
            mania = st.slider('Mania', 0, 100, st.session_state.mania_metric_val, on_change=mark_log_unsaved, key='mania_metric')
            depression = st.slider('Depression', 0, 100, st.session_state.depression_metric_val, on_change=mark_log_unsaved, key='depression_metric')
            anxiety = st.slider('Anxiety', 0, 100, st.session_state.anxiety_metric_val, on_change=mark_log_unsaved, key='anxiety_metric')

            st.markdown('<p class="header2">Bio</p>', unsafe_allow_html=True)
            cola, colb = st.columns(2)
            with cola:
                wakeup = st.time_input('Wake Up', st.session_state.wake_up_time_val, on_change=mark_log_unsaved, key='wake_up_time')
                sleep = st.time_input('Sleep', st.session_state.sleep_time_val, on_change=mark_log_unsaved, key='sleep_time')
            with colb:
                weight = st.number_input('Weight (lbs)', min_value=0., step=1.,value=st.session_state.weight_val, on_change=mark_log_unsaved, key='weight')
        with col2:

            st.markdown('<p class="header2"> Vice </p>', unsafe_allow_html=True)

            cola, colb = st.columns(2)
            with cola:
                screen_time = st.number_input('Screen Time (hrs)', min_value=0., step=1., value=st.session_state.screen_time_val, on_change=mark_log_unsaved, key='screen_time')
                prn = st.number_input('Prn', min_value=0, step=1, value=st.session_state.prn_count_val, on_change=mark_log_unsaved, key='prn_count')
            with colb:
                herb = st.number_input('Herb', min_value=0., step=1., value=st.session_state.herb_count_val, on_change=mark_log_unsaved, key='herb_count')
                cigs = st.number_input('Cigs', min_value=0., step=1., value=st.session_state.cigs_count_val, on_change=mark_log_unsaved, key='cigs_count')


            st.markdown('<p class="header2"> Virtue </p>', unsafe_allow_html=True)
            cola, colb = st.columns(2)
            with cola:
                reading_time = st.number_input('Reading (hrs)', min_value=0., step=1., value=st.session_state.reading_time_val, on_change=mark_log_unsaved, key='reading_time')
                piano_time = st.number_input('Piano (hrs)', min_value=0., step=1., value=st.session_state.piano_time_val, on_change=mark_log_unsaved, key='piano_time')
            with colb:
                meditation_time = st.number_input('Meditation (hrs)', min_value=0., step=1., value=st.session_state.meditation_time_val, on_change=mark_log_unsaved, key='meditation_time')
                work_time = st.number_input('Work (hrs)', min_value=0., step=1., value=st.session_state.work_time_val, on_change=mark_log_unsaved, key='work_time')

            date = st.date_input("Date", datetime.date.today(), on_change=change_log, key='date')

            colc, cold = st.columns(2)
            with colc:
                submit_button = st.button(label='Submit', on_click=primary_form_callback)
            with cold:
                if (st.session_state.log_saved):
                    st.success('Log Saved', icon="✅")
                else:
                    st.warning('Log Unsaved', icon="⚠️")


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
    tab1, tab2 = st.tabs(["Main Budget", "Old Logs"])

    with tab1:
        st.markdown('<p class="header1">Exercise</p>', unsafe_allow_html=True)

        col1, col2 = st.columns([2, 2])

        with col1:
            with st.form(key='workout_log'):
                st.markdown('<p class="header2">General Workout</p>', unsafe_allow_html=True)
                option = st.selectbox(
                    'Exercise Type',
                    ('Pushups', 'Crunches'))
                cola, colb = st.columns(2)
                with cola:
                    protein = st.number_input('Sets', min_value=0, step=1, key='protein')
                    carbs = st.number_input('Reps', min_value=0, step=1, key='carbs')
                with colb:
                    fat = st.number_input('Weight', min_value=0, step=1, key='fat')
                    calories = st.number_input('Calories', min_value=0, step=1, key='calories')

                with st.expander("Advanced"):
                    colc, cold = st.columns(2)
                    with colc:
                        date = st.date_input("Date", datetime.date.today(), key='date')
                    with cold:
                        dairy = st.checkbox('Dairy', key='dairy')
                        fruit = st.checkbox('Fruit', key='fruit')
                        vegetable = st.checkbox('Vegetable', key='vegetable')

                submit_button = st.form_submit_button(label='Submit')


        with col2:
            with st.form(key='running_log'):
                st.markdown('<p class="header2">Running</p>', unsafe_allow_html=True)
                cola, colb = st.columns(2)
                with cola:
                    distance = st.number_input('Distance (km)', min_value=0., step=1., key='distance')
                    run_date = st.date_input("Date", datetime.date.today(), key='run_date')
                with colb:
                    time = st.number_input('Time (hrs)', min_value=0., step=1., key='time')
                    st.markdown('<br>', unsafe_allow_html=True)
                    n_submit_button = st.form_submit_button(label='Submit')


elif choose == "Diet":

    st.markdown(""" 
        <style> 
            .itemSection {
                border: solid 1px black;
                padding: 5px 5px;
                margin: 3px 0px;
                border-radius: 10px;
                display: flex;
                align-items: center;
                justify-content: space-between;
            }
            
            .itemName {
                font-weight: bold;
            }
            .nutritionBox {
                
            }
            .addButton {
                width: 10%;
            }
        </style>
         """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Main Budget", "Old Logs"])

    with tab1:
        st.markdown('<p class="header1">Diet</p>', unsafe_allow_html=True)
        st.write("Nutrition Lookup: [link](https://nutritiondata.self.com/)")

        col1, col2 = st.columns([2, 2])


        def initialize_diet_form():
            st.session_state['food_name_val'] = ""

            st.session_state['protein_val'] = 0
            st.session_state['carbs_val'] = 0
            st.session_state['fat_val'] = 0
            st.session_state['calories_val'] = 0

        if 'food_name_val' not in st.session_state:  # If log variables not initialized, initialize
            initialize_diet_form()


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

        with col1:


            with st.form(key='diet_log'):
                name = st.text_input('Food Name', value=st.session_state.food_name_val, key='food_name')
                cola, colb = st.columns(2)
                with cola:
                    protein = st.number_input('Protein (g)', value=st.session_state.protein_val, min_value=0, step=1, key='protein')
                    carbs = st.number_input('Carbs (g)', value=st.session_state.carbs_val, min_value=0, step=1, key='carbs')
                with colb:
                    fat = st.number_input('Fat (g)', value=st.session_state.fat_val, min_value=0, step=1, key='fat')
                    calories = st.number_input('Calories', value=st.session_state.calories_val, min_value=0, step=1, key='calories')

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
            def selectFoodItem(item):
                st.session_state.food_name_val = item[1]
                st.session_state.protein_val = int(item[2])
                st.session_state.carbs_val = int(item[3])
                st.session_state.fat_val = int(item[4])
                st.session_state.calories_val = int(item[5])


            for item in file_handler.get_diet_item_list():
                cola, colb = st.columns([5,1])
                with cola:
                    st.markdown("<div class='itemSection'>"
                                "<div class='itemName'>" + item[1] + "</div> <div class='nameBox'> calories: " + item[
                                    5] + " | carbs: " + item[3] + " | fat: " + item[4] + " | protein: " + item[2] + "</div>",
                                unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                with colb:
                    st.button("add",key=item[1]+"button", on_click=selectFoodItem, args=(item,))


        st.write("TODO: Ideally there should be a system to add several smaller items together to create meal which itself is an item")
        st.write("Quantity system")
        st.write("Also the advanced expander is not being loaded from selected food items on the right (im lazy sry)")




