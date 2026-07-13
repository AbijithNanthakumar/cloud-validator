import streamlit as st


def render_sidebar():

    st.sidebar.image(
        "https://img.icons8.com/fluency/96/shield.png",
        width=70
    )

    st.sidebar.title("Psiddhi")

    st.sidebar.caption(
        "AI Cloud Validator"
    )

    st.sidebar.divider()

    page = st.sidebar.radio(

        "Navigation",

        [

            "Overview",

            "Findings",

            "AI Analysis",

            "Reports"

        ]

    )

    st.sidebar.divider()

    st.sidebar.success(
        "System Ready"
    )

    return page