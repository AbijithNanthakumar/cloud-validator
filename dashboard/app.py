import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st

from styles import load_styles
from components.sidebar import render_sidebar
from views.overview import show_overview
from views.findings import show_findings
from views.ai_analysis import show_ai_analysis
from views.reports import show_reports

import streamlit as st

from styles import load_styles

from components.sidebar import render_sidebar

from views.overview import show_overview
from views.findings import show_findings
from views.ai_analysis import show_ai_analysis
from views.reports import show_reports


st.set_page_config(
    page_title="Psiddhi AI Cloud Validator",
    page_icon="🛡️",
    layout="wide"
)

load_styles()

page = render_sidebar()

if page == "Overview":
    show_overview()

elif page == "Findings":
    show_findings()

elif page == "AI Analysis":
    show_ai_analysis()

elif page == "Reports":
    show_reports()