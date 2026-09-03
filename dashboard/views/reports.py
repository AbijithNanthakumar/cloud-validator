import streamlit as st
import pandas as pd

from dashboard.components.layout import page_header
from dashboard.services.dashboard_service import get_dashboard_service


def show_reports():
    """
    Displays dashboard summary and provides CSV report export.
    """

    page_header(
        "Reports",
        "Generate and export security validation reports."
    )

    dashboard_service = get_dashboard_service()

    # Reports page must not trigger AI analysis
    dashboard_data = dashboard_service.load_dashboard(include_ai=False)

    summary = dashboard_data.summary
    findings = dashboard_data.findings

    # ---------------------------------------------------------
    # Validation Summary
    # ---------------------------------------------------------

    st.subheader("📋 Validation Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Security Score",
            f"{summary.security_score}%"
        )

    with col2:
        st.metric(
            "Passed Checks",
            summary.passed
        )

    with col3:
        st.metric(
            "Failed Checks",
            summary.failed
        )

    with col4:
        st.metric(
            "Resources",
            summary.resources
        )

    st.divider()

    # ---------------------------------------------------------
    # Findings Report
    # ---------------------------------------------------------

    st.subheader("🔍 Findings Report")

    rows = []

    for finding in findings:
        rows.append({
            "Check ID": finding.check_id,
            "Check Name": finding.check_name,
            "Resource": finding.resource,
            "File": finding.file_name,
            "Severity": finding.severity,
        })

    findings_df = pd.DataFrame(rows)

    if findings_df.empty:
        st.success("No security findings detected.")
    else:
        st.dataframe(
            findings_df,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        # ---------------------------------------------------------
        # CSV Export
        # ---------------------------------------------------------

        st.subheader("📥 Export Report")

        csv_data = findings_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇️ Download Findings CSV",
            data=csv_data,
            file_name="psiddhi_security_findings.csv",
            mime="text/csv",
            use_container_width=False
        )

    # ---------------------------------------------------------
    # Report Status
    # ---------------------------------------------------------

    st.divider()

    st.caption(
        "Psiddhi AI Cloud Validator • Security validation report"
    )