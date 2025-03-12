import streamlit as st

with st.sidebar:
    st.page_link("main.py", label="ホーム", icon="🏠")
    st.page_link("pages/harmonic_tone_visible.py", label="倍音見える君", icon="🎶")
    st.page_link("pages/pdf_reader.py", label="楽譜読める君", icon="🎶")