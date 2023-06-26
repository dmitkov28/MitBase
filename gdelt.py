from datetime import datetime

import streamlit as st
from gdeltdoc import GdeltDoc, Filters

gd = GdeltDoc()


@st.cache_data
def get_data(data_type: str, query: str, start_date: datetime, end_date: datetime):
    start_date = start_date.strftime("%Y-%m-%d")
    end_date = end_date.strftime("%Y-%m-%d")
    f = Filters(
        keyword=query,
        start_date=start_date,
        end_date=end_date
    )

    data_types = {
        "articles": gd.article_search(f),
        "timelinevolraw": gd.timeline_search("timelinevolraw", f),
        "timelinetone": gd.timeline_search("timelinetone", f),
    }
    return data_types[data_type]
