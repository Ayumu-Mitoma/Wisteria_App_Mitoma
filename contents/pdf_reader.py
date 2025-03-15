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

    img_base64 = pp.get_image_base64(images[current_page])
    js_code = f"""
    <script>
        var clickCount = 0;
        function changePage(event){{
            var x = event.clientX;
            var width = window.innerWidth;
            
            clickCount += 1;
            var streamlit = window.parent || window;
            streamlit.postMessage({type: "updateClickCount", count: Clickcount}, "*");

            if (x < width / 2){{
                //左半分をクリック
                if(window.currentPage > 0){{
                    window.currentPage -= 1;
                }}
            }}else{{
                //右半分をクリック
                if(window.currentPage < {total_pages - 1}) {{
                    window.currentPage += 1;
                }}
            }}
            //ページ変更を反映
            var streamlit = window.parent || window;
            streamlit.postMessage({{type: "setCurrentPage", page: window.currentPage}}, "*");
        }}

        document.addEventListener("DOMContentLoaded", function(){{
            window.currentPage = {current_page}; //初期ページ
            var img = document.getElementById("pdf-image");
            img.addEventlistener("click", changePage);
        }});
    </script>
    """
    #画像のHTMLコード
    img_html = f"""
    <img id="pdf-image" src="data:image/png;base64,{img_base64}"
        style="width:100%; cursor:pointer;" />
    """

    st.markdown(js_code, unsafe_allow_html=True)
    st.markdown(img_html, unsafe_allow_html=True)

    st.session_state.current_page = st.query_params.get("page", [current_page])[0]