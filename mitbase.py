import datetime

import streamlit as st

import gdelt
from cloud import create_wordcloud

st.title("MitBase")

with st.sidebar:
    query = st.text_input(label="query", placeholder="query", label_visibility="hidden")
    if len(query) <= 5:
        query = query + " " * (5 - len(query))

    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input(label="start date", value=datetime.datetime.now())

    with col2:
        end_date = st.date_input(label="end date", value=datetime.datetime.now())

    button = st.button(label="Search", use_container_width=True)

col1, col2 = st.columns(2, gap="large")

if button:
    articles = gdelt.get_data("articles", query, start_date, end_date).to_dict(orient="records")
    timeline = gdelt.get_data("timelinevolraw", query, start_date, end_date)
    timeline_tone = gdelt.get_data("timelinetone", query, start_date, end_date)

    with col1:
        st.line_chart(data=timeline, x='datetime', y='Article Count')
        st.line_chart(data=timeline_tone, x="datetime")
        headlines = [item.get("title") for item in articles]
        wordcloud_chart = create_wordcloud(st, headlines)
        st.pyplot(wordcloud_chart)

    with col2:
        for article in articles:
            st.write(article.get("title"))
            if article.get("socialimage"):
                st.image(article.get("socialimage"))
            if article.get("url"):
                st.write(article.get("url"))
            st.divider()
