import streamlit as st


def metric_card(
    title,
    value,
    color="#2563EB",
    icon="📊",
    subtitle=""
):
    """
    Displays a clean KPI metric card.
    """

    with st.container(border=True):

        st.markdown(f"### {icon} {title}")

        st.metric(
            label="",
            value=value
        )

        if subtitle:
            st.caption(subtitle)