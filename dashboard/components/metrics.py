import streamlit as st


def metric_card(title, value, color="#2563EB", icon="📊", subtitle=""):

    st.markdown(
        f"""
        <div style="
            background:white;
            border-radius:14px;
            padding:20px;
            border:1px solid #E2E8F0;
            box-shadow:0px 3px 10px rgba(0,0,0,.05);
            height:170px;
        ">

            <div style="
                font-size:28px;
                margin-bottom:10px;
            ">
                {icon}
            </div>

            <div style="
                font-size:34px;
                font-weight:700;
                color:{color};
            ">
                {value}
            </div>

            <div style="
                font-size:15px;
                color:#475569;
                margin-top:8px;
            ">
                {title}
            </div>

            <div style="
                margin-top:18px;
                color:#94A3B8;
                font-size:13px;
            ">
                {subtitle}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )