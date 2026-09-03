import streamlit as st

from dashboard.components.layout import page_header
from dashboard.services.dashboard_service import get_dashboard_service


def show_ai_analysis():
    """
    Displays AI-powered security analysis and remediation
    for the selected findings.
    """

    page_header(
        "AI Analysis",
        "AI-powered security analysis and Terraform remediation."
    )

    st.warning(
        "AI analysis uses external AI APIs and is limited to "
        "a small number of findings to control API usage."
    )

    dashboard_service = get_dashboard_service()

    # AI is explicitly requested only on this page.
    dashboard_data = dashboard_service.load_dashboard(
        include_ai=True
    )

    ai_results = dashboard_data.ai_results
    findings = dashboard_data.findings

    if not ai_results:

        if findings:
            st.error(
                "AI analysis is temporarily unavailable. "
                "The security scan completed successfully, but "
                "an external AI provider could not process the "
                "requested findings. Please try again later."
            )

            st.caption(
                f"{len(findings)} security finding(s) were detected "
                "by the validation engine."
            )

        else:
            st.info(
                "No security findings are available for AI analysis."
            )

        return

    st.success(
        f"AI analysis generated for "
        f"{len(ai_results)} finding(s)."
    )

    for index, result in enumerate(
        ai_results,
        start=1
    ):

        finding = result.finding

        with st.expander(
            f"Finding {index} — {finding.check_id}",
            expanded=(index == 1)
        ):

            # -------------------------------------------------
            # Security Finding
            # -------------------------------------------------

            st.markdown("### 🔎 Security Finding")

            col1, col2 = st.columns(2)

            with col1:
                st.write(
                    f"**Check ID:** {finding.check_id}"
                )
                st.write(
                    f"**Check:** {finding.check_name}"
                )
                st.write(
                    f"**Resource:** {finding.resource}"
                )

            with col2:
                st.write(
                    f"**File:** {finding.file_name}"
                )
                st.write(
                    f"**Severity:** {finding.severity}"
                )
                st.write(
                    f"**Source:** {finding.source}"
                )

            st.divider()

            # -------------------------------------------------
            # Groq Analysis
            # -------------------------------------------------

            st.markdown("### 🧠 AI Security Analysis")

            st.write(result.explanation)

            st.divider()

            # -------------------------------------------------
            # Gemini Remediation
            # -------------------------------------------------

            st.markdown(
                "### 🛠️ Recommended Remediation"
            )

            st.write(result.remediation)

            st.divider()

            # -------------------------------------------------
            # Terraform Fix
            # -------------------------------------------------

            st.markdown(
                "### 🔧 Terraform Remediation"
            )

            if result.terraform_fix:
                st.code(
                    result.terraform_fix,
                    language="hcl"
                )
            else:
                st.info(
                    "No Terraform remediation was generated."
                )

            st.divider()

            # -------------------------------------------------
            # Best Practice
            # -------------------------------------------------

            st.markdown(
                "### 📚 Best Practice"
            )

            st.info(result.best_practice)

            st.caption(
                f"AI Source: {result.source}"
            )