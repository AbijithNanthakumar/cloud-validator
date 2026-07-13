import streamlit as st

def page_header(title: str, subtitle: str):
    st.markdown(
        f"""
        <div style="margin-bottom:25px;">
            <h1 style="
                color:#2563EB;
                margin-bottom:0;
                font-size:42px;
                font-weight:700;
            ">
                🛡️ {title}
            </h1>

            <p style="
                color:#64748B;
                font-size:18px;
                margin-top:6px;
            ">
                {subtitle}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()