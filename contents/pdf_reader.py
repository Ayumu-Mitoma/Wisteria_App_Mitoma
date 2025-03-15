import streamlit as st
from pdf_reader import pdf_processing as pp

st.header("楽譜見える君")
st.text("自分のスマホにある楽譜のpdfファイルを選択してね")

st.session_state["visible"] = False
score_file = st.file_uploader("楽譜のpdfファイルを選択", type=["pdf"])

if score_file is not None:
    file_name = score_file.name.lower()
    if file_name.endswith(".pdf"):
        images = pp.pdf_to_images(score_file.read())
        st.text(len(images))
        if len(images) != 0:
            st.session_state["visible"] = True
    else:
        st.error("対応しているファイルはpdfのみです")
        st.stop()

if st.session_state["visible"] == True:
    pass