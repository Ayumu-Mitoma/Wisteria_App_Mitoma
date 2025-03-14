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
    #楽譜の表示と切り替え
    # 現在のインデックスをセッション状態で管理
    if "image_index" not in st.session_state:
        st.session_state.image_index = 0

    # JavaScriptで画像の左右クリックイベントを検出
    st.markdown(
        """
        <style>
        .image-container {
            position: relative;
            display: inline-block;
            width: 100%;
        }
        .image-container img {
            width: 100%;
        }
        .left-overlay, .right-overlay {
            position: absolute;
            top: 0;
            bottom: 0;
            width: 50%;
            cursor: pointer;
        }
        .left-overlay {
            left: 0;
            background: rgba(0, 0, 0, 0.2);
        }
        .right-overlay {
            right: 0;
            background: rgba(0, 0, 0, 0.2);
        }
        .full-width-image{
            width:100%;
            height:auto;
        }
        </style>

        <div class="image-container">
            <img src="{current_image}" alt="楽譜">
            <div class="left-overlay" onclick="window.parent.postMessage('prev', '*')"></div>
            <div class="right-overlay" onclick="window.parent.postMessage('next', '*')"></div>
        </div>
        """.replace("{current_image}", images[st.session_state.image_index]),
        unsafe_allow_html=True
    )

    # JavaScriptからのメッセージを処理
    message = st.query_params.get('message', [''])[0]

    if message == 'next':
        st.session_state.image_index = (st.session_state.image_index + 1) % len(images)
    elif message == 'prev':
        st.session_state.image_index = (st.session_state.image_index - 1) % len(images)