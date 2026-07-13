import streamlit as st
import pandas as pd
import plotly.express as px


def severity_chart(findings):
    """
    Displays findings grouped by severity.
    """

    rows = []

    for finding in findings:
        rows.append(
            {
                "Severity": finding.severity
            }
        )

    df = pd.DataFrame(rows)

    if df.empty:
        st.info("No findings available.")
        return

    counts = (
        df.groupby("Severity")
        .size()
        .reset_index(name="Count")
    )

    fig = px.pie(
        counts,
        names="Severity",
        values="Count",
        hole=0.65,
        title="Findings by Severity"
    )

    fig.update_layout(
        height=380,
        margin=dict(
            l=10,
            r=10,
            t=50,
            b=10
        ),
        legend_title=""
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )