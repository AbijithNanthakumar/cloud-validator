import streamlit as st

from dashboard.components.layout import page_header
from dashboard.services.dashboard_service import get_dashboard_service


def show_ai_analysis():
    """
    Displays AI-generated security analysis
    and remediation recommendations.
    """

    page_header(
        "AI Analysis",
        "AI-powered remediation insights."
    )

    dashboard_service = get_dashboard_service()

    # AI is explicitly requested only on this page.
    dashboard_data = dashboard_service.load_dashboard(
        include_ai=True
    )

    ai_results = dashboard_data.ai_results

    if not ai_results:
        st.info("No AI analysis available.")
        return

    st.success(
        f"AI analysis generated for {len(ai_results)} finding(s)."
    )

    for index, result in enumerate(ai_results, start=1):

        finding = result.finding

        with st.expander(
            f"Finding {index} — {finding.check_id}",
            expanded=(index == 1)
        ):

            st.markdown("### 🔎 Security Finding")

            st.write(
                f"**Check:** {finding.check_name}"
            )

            st.write(
                f"**Severity:** {finding.severity}"
            )

            st.write(
                f"**Resource:** {finding.resource}"
            )

            st.divider()

            st.markdown("### 🧠 AI Analysis")

            st.write(result.explanation)

            st.markdown("### 🛠️ Recommended Remediation")

            st.write(result.remediation)

            st.markdown("### 🔧 Terraform Fix")

            st.code(
                result.terraform_fix,
                language="hcl"
            )

            st.markdown("### 📚 Best Practice")

            st.write(result.best_practice)