import streamlit as st
import time

options = ("male", "female")

a = st.empty()

value = a.radio("gender", options, 0)

st.write(value)

time.sleep(2)

value = a.radio("gender", options, 1)

st.write(value)

st.button("Yo")