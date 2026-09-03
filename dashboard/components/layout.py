import streamlit as st


def page_header(title: str, subtitle: str):
    """
    Displays a clean dashboard page header.
    """

    st.title(f"🛡️ {title}")

    st.caption(subtitle)

    st.divider()