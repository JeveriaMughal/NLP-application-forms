import streamlit as st
import save_pdf
import time


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def app():
    local_css("src/style.css")
    st.image("src/left-1 - Copy.jpg")
    st.markdown('<h1 class="urdu-font-big">درخواست کی پی ڈی ایف ڈاون لوڈ کریں</h1>', unsafe_allow_html=True)
    st.write("براہ کرم درج ذیل تفصیلات درج کریں۔")
    col1, col2 = st.columns(2)
    with col2:
        name = st.text_input("نام")
        position =st.text_input("عہدہ")
        dept = st.selectbox("شعبہ" , ("  ","اپلیکیشن","اڈمِن","آئی ٹی","بصری حروف شناسی","تحقیق و ترقی"), index=0) 
        date1 = st.date_input("رخصٹ کے اغاز کی تاریخ", value=None , min_value=None , max_value=None , key=None)
        date2 = st.date_input("رخصت کے اِختتام کی تاریخ", value=None , min_value=None , max_value=None , key=None)
        total_days = str((date2-date1).days))
        reason = st.text_input("رخصت کی وجہ")
        address = st.text_input("دوران رخصت پتہ ")
        pdf_button=st.button("درخواست تیار کریں")
    with col1:
        st.write(" درخواست فارم برائے اتفاقیہ رخصت کا سامپل")
        st.image("src/black_casual_leave-1.png")
    if pdf_button:
        # with st.spinner('برائے مہربانی انتظار کریں'):
        #     time.sleep(5)
        save_pdf.make_pdf_leave(name,position,dept,str(date1),str(date2),total_days,reason,address)
        st.write("درخواست ڈوں لوڈ کے لیے تیار ہے")
    with open("Application.pdf", "rb") as file:
        btn = st.download_button(
             label="درخواست حاصل کریں",
             data=file,
             file_name="Application.pdf",
             mime="image/png"
           )
        if btn:
            st.balloons()
            st.success("درخواست کی ڈاؤن لوڈ کردہ کاپی آپ کے سسٹم پر موجود ہے۔")

