import streamlit as st


def load_styles():
    """
    Loads custom CSS styling for the dashboard.
    """

    st.markdown(
        """
        <style>

        /* Main App */
        .main{
            background-color:#F8FAFC;
        }

        /* Header */
        .main-title{
            font-size:36px;
            font-weight:700;
            color:#0F172A;
            margin-bottom:0px;
        }

        .subtitle{
            color:#64748B;
            font-size:16px;
            margin-top:-10px;
        }

        /* Metric Cards */

        .metric-card{

            background:white;

            padding:20px;

            border-radius:12px;

            border:1px solid #E2E8F0;

            box-shadow:0px 1px 5px rgba(0,0,0,.05);

            text-align:center;

        }

        .metric-value{

            font-size:32px;

            font-weight:bold;

            color:#2563EB;

        }

        .metric-label{

            color:#64748B;

            font-size:14px;

        }

        </style>
        """,
        unsafe_allow_html=True
    )