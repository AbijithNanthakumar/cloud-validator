import streamlit as st


def load_styles():
    """
    Loads dashboard styling.
    
    Streamlit's native components are used for
    the main dashboard UI.
    """

    st.markdown(
        """
        <style>
        [data-testid="stMetric"] {
            padding: 8px;
        }

        [data-testid="stDataFrame"] {
            border-radius: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )