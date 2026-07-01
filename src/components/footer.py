import streamlit as st

def footer_home():
    st.markdown("""
        <div style="
            margin-top:2rem;
            text-align:center;
            color:black;
            font-size:20px;
            font-weight:500;
            letter-spacing:0.5px;
        ">
            © 2026 SnapClass AI • Developed by
            <span style="
                color:#FFD43B;
                font-weight:800;
            ">
                Saif Chogle
            </span>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="
            margin-top:2.5rem;
            text-align:center;
            color:#444;
            font-size:30px;
            font-weight:700;
            letter-spacing:0.5px;
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