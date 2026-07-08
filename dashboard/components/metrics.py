# import streamlit as st


# def metric_card(title, value, color="#2563EB"):

#     st.markdown(
#         f"""
#         <div class="metric-card">

#             <div class="metric-value"
#                  style="color:{color};">

#                 {value}

#             </div>

#             <div class="metric-label">

#                 {title}

#             </div>

#         </div>
#         """,
#         unsafe_allow_html=True
#     )

import streamlit as st


def metric_card(title, value, color="#2563EB"):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-value" style="color: {color};">
                {value}
            </div>
            <div class="metric-label">
                {title}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )