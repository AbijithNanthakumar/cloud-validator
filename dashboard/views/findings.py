import streamlit as st

from components.layout import page_header
from components.tables import findings_table

from dashboard.services.dashboard_service import DashboardService

def show_findings():
    """
    Displays all security findings.
    """

    page_header(
        "Security Findings",
        "Review all detected cloud security issues."
    )

    dashboard_data = DashboardService().load_dashboard()

    findings = dashboard_data.findings

    st.text_input(
        "🔍 Search Findings",
        placeholder="Search by Check ID, Resource or File..."
    )

    findings_table(findings)