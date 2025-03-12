import streamlit as st

with st.sidebar:
    st.page_link("main.py", label="ホーム", icon="🏠")
    st.page_link("harmonic_tone_visible.py", label="倍音見える君", icon="1")
    st.page_link("pdf_reader.py", label="楽譜読める君", icon="2")