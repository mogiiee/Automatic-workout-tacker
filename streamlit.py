import streamlit as st

counter = 0

def increment_counter():
    global counter
    counter += 1

st.set_page_config(page_title="Workout Counter", page_icon=":muscle:", layout="wide")
st.title("Workout Counter")
st.markdown("### Track your progress with this workout counter")

st.write("")
st.write("Current workout count: ", counter)

if st.button("Increment workout count"):
    increment_counter()

st.write("")
st.write("Stay motivated and keep up the good work!")
