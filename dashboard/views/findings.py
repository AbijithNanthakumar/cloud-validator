import streamlit as st

from dashboard.components.layout import page_header
from dashboard.components.tables import findings_table

from dashboard.services.dashboard_service import get_dashboard_service


def show_findings():
    """
    Displays all detected security findings.
    """

    page_header(
        "Security Findings",
        "Review all detected cloud security issues."
    )

    dashboard_service = get_dashboard_service()

    # Findings page only loads validation data.
    # No Groq or Gemini API calls are made here.
    dashboard_data = dashboard_service.load_dashboard(
        include_ai=False
    )

    findings = dashboard_data.findings

    search_query = st.text_input(
        "🔍 Search Findings",
        placeholder="Search by Check ID, Resource or File..."
    )

    if search_query:
        query = search_query.lower()

        filtered_findings = [
            finding
            for finding in findings
            if (
                query in str(finding.check_id).lower()
                or query in str(finding.check_name).lower()
                or query in str(finding.resource).lower()
                or query in str(finding.file_name).lower()
                or query in str(finding.severity).lower()
            )
        ]
    else:
        filtered_findings = findings

    st.caption(
        f"Showing {len(filtered_findings)} of {len(findings)} findings"
    )

    if not filtered_findings:
        st.warning("No findings match your search.")
        return

    findings_table(filtered_findings)