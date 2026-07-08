# import streamlit as st

# from dashboard.components.metrics import metric_card


# def show_overview():

#     st.markdown(
#         """
#         <div class="main-title">
#             🛡️ Psiddhi AI Cloud Validator
#         </div>

#         <div class="subtitle">
#             AI Powered Cloud Infrastructure Security Platform
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

#     st.divider()

#     col1, col2, col3, col4 = st.columns(4)

#     with col1:
#         metric_card(
#             "Security Score",
#             "36%",
#             "#2563EB"
#         )

#     with col2:
#         metric_card(
#             "Compliance",
#             "Non-Compliant",
#             "#EF4444"
#         )

#     with col3:
#         metric_card(
#             "Resources",
#             "3",
#             "#10B981"
#         )

#     with col4:
#         metric_card(
#             "Failed Checks",
#             "16",
#             "#F59E0B"
#         )


import streamlit as st

from components.metrics import metric_card


def show_overview():

    st.markdown(
        """
        <div class="main-title">
            🛡️ Psiddhi AI Cloud Validator
        </div>

        <div class="subtitle">
            AI Powered Cloud Infrastructure Security Platform
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card(
            "Security Score",
            "36%",
            "#2563EB"
        )

    with col2:
        metric_card(
            "Compliance",
            "Non-Compliant",
            "#EF4444"
        )

    with col3:
        metric_card(
            "Resources",
            "3",
            "#10B981"
        )

    with col4:
        metric_card(
            "Failed Checks",
            "16",
            "#F59E0B"
        )