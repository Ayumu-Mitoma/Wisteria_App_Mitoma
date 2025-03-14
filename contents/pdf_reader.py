import streamlit as st
from pdf_reader import pdf_processing as pp

st.header("楽譜見える君")
st.text("自分のスマホにある楽譜のpdfファイルを選択してね")

score = st.file_uploader("楽譜のpdfファイルを選択")

