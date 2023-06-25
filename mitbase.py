import datetime

import streamlit as st
import gdelt

st.title("MitBase")


def get_data(query: str):
    st.write(gdelt.articles)


query = st.text_input(label="query", placeholder="query", label_visibility="hidden")

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input(label="start_date", value=datetime.datetime.now())

with col2:
    end_date = st.date_input(label="end_date", value=datetime.datetime.now())

if st.button(label="Search", use_container_width=True):
    get_data(query)

