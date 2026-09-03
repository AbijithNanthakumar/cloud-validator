import pandas as pd
import plotly.express as px
import streamlit as st


SEVERITY_ORDER = [
    "Critical",
    "High",
    "Medium",
    "Low",
    "Unknown",
]


def severity_chart(findings):
    """
    Displays the distribution of security findings by severity.

    The chart always uses a consistent severity order so that
    dashboard reporting remains predictable across scans.
    """

    if not findings:
        st.info("No findings available.")
        return

    rows = [
        {
            "Severity": finding.severity or "Unknown"
        }
        for finding in findings
    ]

    df = pd.DataFrame(rows)

    # Normalize severity values
    df["Severity"] = (
        df["Severity"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    # Keep only supported severity classifications
    df.loc[
        ~df["Severity"].isin(SEVERITY_ORDER),
        "Severity"
    ] = "Unknown"

    # Count each severity
    counts = (
        df["Severity"]
        .value_counts()
        .reindex(
            SEVERITY_ORDER,
            fill_value=0
        )
        .reset_index()
    )

    counts.columns = [
        "Severity",
        "Count"
    ]

    # Remove zero-count categories from the chart
    chart_data = counts[counts["Count"] > 0]

    if chart_data.empty:
        st.info("No severity data available.")
        return

    fig = px.pie(
        chart_data,
        names="Severity",
        values="Count",
        hole=0.65,
        title="Findings by Severity",
        category_orders={
            "Severity": SEVERITY_ORDER
        },
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Findings: %{value}<br>"
            "Percentage: %{percent}"
            "<extra></extra>"
        ),
    )

    fig.update_layout(
        height=380,
        margin=dict(
            l=10,
            r=10,
            t=50,
            b=10
        ),
        legend_title="Severity",
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )