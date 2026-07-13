import pandas as pd
import streamlit as st


def findings_table(findings):
    """
    Displays security findings in a table.
    """

    rows = []

    for finding in findings:
        rows.append(
            {
                "Check ID": finding.check_id,
                "Check Name": finding.check_name,
                "Resource": finding.resource,
                "File": finding.file_name,
                "Severity": finding.severity,
            }
        )

    df = pd.DataFrame(rows)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )