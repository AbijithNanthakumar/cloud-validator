import streamlit as st

from components.layout import page_header
from components.kpi_section import show_kpis
from components.tables import findings_table
from components.charts import severity_chart

from dashboard.services.dashboard_service import DashboardService

def show_overview():
    """
    Displays the Overview dashboard.
    """

    dashboard_data = DashboardService().load_dashboard()

    summary = dashboard_data.summary

    page_header(
        "Psiddhi AI Cloud Validator",
        "AI Powered Cloud Infrastructure Security Platform"
    )

    metrics = [
        {
            "title": "Security Score",
            "value": f"{summary.security_score}%",
            "color": "#2563EB",
            "icon": "🛡️",
            "subtitle": "Overall security posture"
        },
        {
            "title": "Compliance",
            "value": summary.compliance,
            "color": "#EF4444",
            "icon": "⚠️",
            "subtitle": "Current compliance status"
        },
        {
            "title": "Resources",
            "value": summary.resources,
            "color": "#10B981",
            "icon": "☁️",
            "subtitle": "Infrastructure scanned"
        },
        {
            "title": "Failed Checks",
            "value": summary.failed,
            "color": "#F59E0B",
            "icon": "❌",
            "subtitle": "Requires immediate attention"
        }
    ]

    show_kpis(metrics)

    st.markdown("## 📊 Security Analytics")

    left, right = st.columns(2)

    with left:
        severity_chart(dashboard_data.findings)

    with right:
        st.info(
            "Resource distribution chart will be added next."
        )

    st.markdown("## 🔍 Latest Findings")

    findings_table(dashboard_data.findings)