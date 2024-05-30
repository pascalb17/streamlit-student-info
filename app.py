import streamlit as st

st.title("Student Information")

name = st.text_input("Enter your name")

age = st.slider("Select your age")

def click_button():
        st.write("Your name is ",name,"and your age is ",age)

if st.button("Submit"):
        st.write("Your name is ",name,"and your age is ",age)

