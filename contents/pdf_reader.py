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
        if len(images) != 0:
            st.session_state["visible"] = True
    else:
        st.error("対応しているファイルはpdfのみです")
        st.stop()

if st.session_state["visible"] == True:
    if "current_page" not in st.session_state:
        st.session_state.current_page = 0

    total_pages = len(images)
    current_page = st.session_state.current_page

    img_io = images[current_page]
    st.image(img_io, caption=f"{current_page+1}/{total_pages} ページ")

    cols = st.columns([1,1])
    with cols[0]:
        if st.button("前のページ", key="prev") and current_page > 0:
            st.session_state.current_page -= 1
            st.rerun()
    with cols[1]:
        if st.button("次のページ", key="next") and current_page < total_pages -1:
            st.session_state.current_page += 1
            st.rerun()