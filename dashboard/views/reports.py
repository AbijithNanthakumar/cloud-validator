# import streamlit as st

# from components.layout import page_header
# from dashboard.services.dashboard_service import DashboardService

# def show_reports():
#     """
#     Displays dashboard summary report.
#     """

#     page_header(
#         "Reports",
#         "Generate security validation reports."
#     )

#     dashboard_data = DashboardService().load_dashboard()

#     summary = dashboard_data.summary

#     st.subheader("📋 Validation Summary")

#     col1, col2 = st.columns(2)

#     with col1:
#         st.metric(
#             "Passed Checks",
#             summary.passed
#         )

#         st.metric(
#             "Resources",
#             summary.resources
#         )

#     with col2:
#         st.metric(
#             "Failed Checks",
#             summary.failed
#         )

#         st.metric(
#             "Security Score",
#             f"{summary.security_score}%"
#         )

#     st.divider()

#     st.info(
#         "📄 PDF and CSV export functionality will be added in the next sprint."
#     )


import streamlit as st

from dashboard.components.layout import page_header
from dashboard.services.dashboard_service import DashboardService


def show_reports():
    """
    Displays dashboard summary report.
    """

    page_header(
        "Reports",
        "Generate security validation reports."
    )

    dashboard_data = DashboardService().load_dashboard()

    summary = dashboard_data.summary

    st.subheader("📋 Validation Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Passed Checks",
            summary.passed
        )

        st.metric(
            "Resources",
            summary.resources
        )

    with col2:
        st.metric(
            "Failed Checks",
            summary.failed
        )

        st.metric(
            "Security Score",
            f"{summary.security_score}%"
        )

    st.divider()

    st.info(
        "📄 PDF and CSV export functionality will be added in the next sprint."
    )