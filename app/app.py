import streamlit as st

from pathlib import Path

st.title("Hello world - just testing!")


password = "12345"

user_password = st.text_input(label="User password")

if user_password == password:
    st.header("Secret information")
