import streamlit as st

from components.layout import page_header
from dashboard.services.dashboard_service import DashboardService

def show_ai_analysis():
    """
    Displays AI-generated security analysis
    and remediation recommendations.
    """

    page_header(
        "AI Analysis",
        "AI-powered remediation insights."
    )

    dashboard_data = DashboardService().load_dashboard()

    ai_results = dashboard_data.ai_results

    if not ai_results:
        st.info("No AI analysis available.")
        return

    for index, result in enumerate(ai_results, start=1):

        with st.expander(f"Finding {index}"):

            st.markdown("### 🧠 AI Analysis")

            st.write(result.analysis)

            st.markdown("### 🛠️ Recommended Remediation")

            st.write(result.remediation)