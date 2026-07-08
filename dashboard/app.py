import streamlit as st

from styles import load_styles
from views.overview import show_overview

st.set_page_config(
    page_title="Psiddhi AI Cloud Validator",
    page_icon="🛡️",
    layout="wide"
)

load_styles()

show_overview()