import streamlit as st
import pdf_generate
import form_leave_app
import inform_leave_third_party

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("src/style.css")
PAGES = {"درخواست برائے مختصر رخصت": pdf_generate,
"درخواست برائے رخصت اتفاقیہ": form_leave_app,
"اطلاع برائے رخصت": inform_leave_third_party}
st.sidebar.title("NLP-L \n Application Form")
st.sidebar.image("logo-white_old.png")
selection = st.sidebar.radio("صفحہ",list (PAGES.keys()))
page= PAGES[selection]
page.app()
