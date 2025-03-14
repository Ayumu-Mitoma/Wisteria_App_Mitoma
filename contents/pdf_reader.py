import streamlit as st
from pdf_reader import pdf_processing as pp

st.header("楽譜見える君")
st.text("自分のスマホにある楽譜のpdfファイルを選択してね")

score = st.file_uploader("楽譜のpdfファイルを選択")

# 画像リスト
images = ["image1.jpg", "image2.jpg", "image3.jpg"]

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
    </style>

    <div class="image-container">
        <img src="{current_image}" alt="画像">
        <div class="left-overlay" onclick="window.parent.postMessage('prev', '*')"></div>
        <div class="right-overlay" onclick="window.parent.postMessage('next', '*')"></div>
    </div>
    """.replace("{current_image}", images[st.session_state.image_index]),
    unsafe_allow_html=True
)

# JavaScriptからのメッセージを処理
message = st.query_params().get('message', [''])[0]

if message == 'next':
    st.session_state.image_index = (st.session_state.image_index + 1) % len(images)
elif message == 'prev':
    st.session_state.image_index = (st.session_state.image_index - 1) % len(images)