import streamlit as st


def footer_home():
    st.markdown("""
    <div style="
        margin-top:2rem;
        padding-bottom:1rem;
        text-align:center;
        font-size:16px;
        font-weight:500;
        color:white;
        letter-spacing:0.3px;
        opacity:0.95;
    ">
        © 2026 SnapClass AI • Built by
        <span style="
            color:#FFD43B;
            font-weight:700;
        ">
            Saif Chogle
        </span>
    </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
    <div style="
        margin-top:2rem;
        padding-bottom:1rem;
        text-align:center;
        font-size:16px;
        font-weight:500;
        color:#555555;
        letter-spacing:0.3px;
    ">
        © 2026 SnapClass AI • Built by
        <span style="
            color:#4F5DFF;
            font-weight:700;
        ">
            Saif Chogle
        </span>
    </div>
    """, unsafe_allow_html=True)