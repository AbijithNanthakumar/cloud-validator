import streamlit as st

from dashboard.components.metrics import metric_card


def show_kpis(metrics):
    """
    Displays dashboard KPI cards.
    """

    columns = st.columns(len(metrics))

    for col, metric in zip(columns, metrics):

        with col:
            metric_card(
                title=metric["title"],
                value=metric["value"],
                color=metric.get("color", "#2563EB"),
                icon=metric.get("icon", "📊"),
                subtitle=metric.get("subtitle", "")
            )