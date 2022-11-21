import streamlit as st
import save_pdf
import time
import datetime


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
        gender = st.selectbox("جنس" , ("  ","مرد","عورت"), index=0) 
        name = st.text_input("نام")
        position =st.selectbox("عہدہ",
                                ("",
                                "اسسٹنٹ ایڈمن کم اکائونٹس",
                                "اسسٹنٹ ہارڈوئیر اینڈ نیٹ ورک",
                                "پروگرام مینجر(ایپلی کیشنز)",
                                "(بصری حروف شناسی)پروگرام مینجر",
                                "پروگرام مینجر(تحقیق و ترقی)",
                                "ٹیم ممبر (ایپلی کیشنز)",
                                "ٹیم ممبر (بصری حروف شناسی)",
                                "ٹیم ممبر (تحقیق و ترقی)",
                                "ٹیم ممبر (زبان)",
                                "ماہرِ زبان/لینگویج انجینئر",
                                "نائب قاصد"))
        dept = st.selectbox("مینجر" , ("  ","اپلیکیشنز","ایڈمِن","آئی ٹی","بصری حروف شناسی","تحقیق و ترقی","لسانیات"), index=0) 
        date1 = datetime.date.today()
        date2 = st.date_input("رخصٹ کے اختتام کی تاریخ", value=None , min_value=None , max_value=None , key=None)
        total_days = str((date2-date1).days+1)
        reason = st.text_input("رخصت کی وجہ")
        name_informant = st.text_input("خبر رساں کا نام")
        pdf_button=st.button("درخواست تیار کریں")
    with col1:
        st.write(" اطلاع برائے رخصت کا سامپل")
        st.image("src/sample_info-1.png")
    if pdf_button:
        # with st.spinner('برائے مہربانی انتظار کریں'):
        #     time.sleep(5)
        save_pdf.make_3rd_party_leave(name,position,dept,date1,date2,total_days,reason,gender,name_informant)
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

