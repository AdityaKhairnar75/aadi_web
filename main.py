import streamlit as st 
import pandas as pd

name = st.text_input("Enter your name:")
fname = st.text_input("Enter your father's name:")
adress = st.text_area("Enter your address:")
classdata = st.selectbox("Select your class:", ["10th", "11th", "12th"])

button = st.button("Done")
if button:
    st.markdown(f"""
                Name: {name}
                Father's Name: {fname}
                Address: {adress}
                Class: {classdata}
""")
