import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.db_utils import fetch_all_tickets

st.set_page_config(page_title="Database Viewer", layout="wide")
st.title("Database Viewer")

all_tickets = fetch_all_tickets()

table_choice = st.selectbox("Select Department Table to View", list(all_tickets.keys()))

st.subheader(f"{table_choice}")
tickets = all_tickets.get(table_choice, [])

if tickets:
    st.dataframe(
        tickets,
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("No tickets available for this department.")
