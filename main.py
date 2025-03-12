import streamlit as st

st.set_page_config(page_title="ウィステリア用アプリ created by 三苫", page_icon="🎼")

top_page = st.Page(page="contents/home.py", title="ホーム", icon="🏠")
harmonic = st.Page(page="contents/harmonic_tone_visible.py", title="倍音見える君", icon="🎶")
#pdf_reader = st.Page(page="contents/pdf_reader.py", title="楽譜見える君", icon="🎶")
pg = st.navigation([top_page, harmonic])
pg.run()