# Python program to create
# a pdf file

def make_pdf_short_leave(name,position,dept,date,time1,time2,reason,prev_leaves):
	from fpdf import FPDF

	import arabic_reshaper
	from bidi.algorithm import get_display

	# save FPDF() class into a
	# variable pdf
	pdf = FPDF()

	# Add a page
	pdf.add_page()
	pdf.image("src/logo.jpeg", x =15, y = 5, w = 180, h = 40, type = 'JPG', link = '')
	# set style and size of font
	# that you want in the pdf
	# pdf.add_font('Jameel Noori Nastaleeq', '', '/home/j-mughal/Documents/fonts/all_fonts/PakType-Naskh-Basic.ttf', uni=True)
	pdf.add_font('Naskh', '', 'src/DTNASKH0.TTF', uni=True)
	# pdf.set_font("Jameel Noori Nastaleeq",style='U', size = 25)

	# create a cell

	pdf.set_font("Naskh",style='', size = 15)
	pdf.cell(70, 15, txt = "     ",border=0,ln = 1, align = 'R')
	pdf.set_font("Naskh",style='U', size = 35)
	reshaped_text=arabic_reshaper.reshape("درخواست فارم برائے مختصر رخصت ")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(200, 55, txt = reshaped_word,border=0,ln = 1, align = 'C')
	# pdf.set_font("Jameel Noori Nastaleeq",style='', size = 15) 
	pdf.set_font("Naskh",style='', size = 15)
	#line 1
	reshaped_text=arabic_reshaper.reshape(name)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(150, 20, txt =reshaped_word,border=0,ln = 0, align = 'R')

	reshaped_text=arabic_reshaper.reshape("نام: ")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0, 20, txt = reshaped_word,border=0,ln = 1, align = 'R')

	#line 2
	reshaped_text=arabic_reshaper.reshape(position)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(150, 20, txt =reshaped_word,border=0,ln = 0, align = 'R')

	reshaped_text=arabic_reshaper.reshape("عہدہ: ")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0, 20, txt = reshaped_word,border=0,ln = 1, align = 'R')
	#line 3
	reshaped_text=arabic_reshaper.reshape(dept)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(150, 20, txt =reshaped_word,border=0,ln = 0, align = 'R')

	reshaped_text=arabic_reshaper.reshape("شعبہ: ")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0, 20, txt = reshaped_word,border=0,ln = 1, align = 'R')
    #line 4 
	# reshaped_text=arabic_reshaper.reshape(str(date.strftime("%d-%m-%Y")))
	# reshaped_word=get_display(reshaped_text)
	pdf.cell(150, 20, txt = str(date.strftime("%d-%m-%Y")),border=0,ln = 0, align = 'R')

	reshaped_text=arabic_reshaper.reshape("تاریخ:",)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0, 20, txt = reshaped_word,border=0,ln = 1, align = 'R')

	#line 5
	reshaped_text=arabic_reshaper.reshape(time2)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(55, 20, txt =reshaped_word,border=0,ln = 0, align = 'R')

	reshaped_text=arabic_reshaper.reshape("تا")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(20, 20, txt =reshaped_word,border=0,ln = 0, align = 'R')

	reshaped_text=arabic_reshaper.reshape(time1)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(55, 20, txt =reshaped_word,border=0,ln = 0, align = 'R')

	reshaped_text=arabic_reshaper.reshape(":دورانیہ مختصر رخصت از")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0, 20, txt = reshaped_word,border=0,ln = 1, align = 'R')
    #line 6
	reshaped_text=arabic_reshaper.reshape(reason)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(150, 20, txt = reshaped_word,border=0,ln = 0, align = 'R')

	reshaped_text=arabic_reshaper.reshape("رخصت کی وجوہات:")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0, 20, txt = reshaped_word,border=0,ln = 1, align = 'R')

    #line 7&8
	pdf.cell(70, 15, txt = "     ",border=0,ln = 1, align = 'R')
	pdf.cell(40, 2, txt = "----------------",border=0,ln = 1, align = 'R')
	reshaped_text=arabic_reshaper.reshape("دستخط: درخواست گزار",)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(40,20, txt = reshaped_word,border=0,ln = 0, align = 'R')

    #line 9
	pdf.cell(70, 15, txt = "     ",border=0,ln = 1, align = 'R')
	reshaped_text=arabic_reshaper.reshape(prev_leaves)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(120, 20, txt = reshaped_word,border=0,ln = 0, align = 'R')

	reshaped_text=arabic_reshaper.reshape("قبل ازیں کی گئی رخصت کی تعداد:")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0, 20, txt = reshaped_word,border=0,ln = 1, align = 'R')
	#line 10
	# pdf.cell(70, 15, txt = "     ",border=0,ln = 1, align = 'R')
	pdf.cell(90, 20, txt = "------------------------------",border=0,ln = 0, align = 'R')
	reshaped_text=arabic_reshaper.reshape("منظوری برائے نائب ناظم/ سربراہ شعبہ: ",)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0,20, txt = reshaped_word,border=0,ln = 0, align = 'R')

	# save the pdf with name .pdf
	filename= "Application.pdf"
	pdf.output(filename)



# name="جویریہ مغل "
# date="اگست 23، 2022"
# reason="طبیعت ناساز"
# make_pdf(name,date,reason)
def make_pdf_leave(name,position,dept,date1,date2,total_days,reason,address):
	from fpdf import FPDF

	import arabic_reshaper
	from bidi.algorithm import get_display

	# save FPDF() class into a
	# variable pdf
	pdf = FPDF()

	# Add a page
	pdf.add_page()
	pdf.image("src/logo.jpeg", x =15, y = 5, w = 180, h = 40, type = 'JPG', link = '')
	# set style and size of font
	# that you want in the pdf
	pdf.add_font('Naskh', '', 'src/DTNASKH0.TTF', uni=True)
	# pdf.set_font("Jameel Noori Nastaleeq",style='U', size = 25)

	# create a cell

	pdf.set_font("Naskh",style='', size = 15)
	pdf.cell(70, 15, txt = "     ",border=0,ln = 1, align = 'R')
	pdf.set_font("Naskh",style='U', size = 35)
	reshaped_text=arabic_reshaper.reshape("درخواست فارم برائے رخصت اتفاْقیہ ")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(200, 55, txt = reshaped_word,border=0,ln = 1, align = 'C')
	# pdf.set_font("Jameel Noori Nastaleeq",style='', size = 15) 
	pdf.set_font("Naskh",style='', size = 15)
	#line 1
	reshaped_text=arabic_reshaper.reshape(name)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(150, 10, txt =reshaped_word,border=0,ln = 0, align = 'R')

	reshaped_text=arabic_reshaper.reshape("نام: ")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0, 10, txt = reshaped_word,border=0,ln = 1, align = 'R')

	#line 2
	reshaped_text=arabic_reshaper.reshape(position)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(150, 10, txt =reshaped_word,border=0,ln = 0, align = 'R')

	reshaped_text=arabic_reshaper.reshape("عہدہ: ")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0, 10, txt = reshaped_word,border=0,ln = 1, align = 'R')
	#line 3
	reshaped_text=arabic_reshaper.reshape(dept)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(150, 10, txt =reshaped_word,border=0,ln = 0, align = 'R')

	reshaped_text=arabic_reshaper.reshape("شعبہ: ")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0, 10, txt = reshaped_word,border=0,ln = 1, align = 'R')
    #line 4 
	# reshaped_text=arabic_reshaper.reshape(date2)
	# reshaped_word=get_display(reshaped_text)
	pdf.cell(55, 10, txt = str(date2.strftime("%d-%m-%Y")),border=0,ln = 0, align = 'R')

	reshaped_text=arabic_reshaper.reshape("تا")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(20, 10, txt =reshaped_word,border=0,ln = 0, align = 'R')

	# reshaped_text=arabic_reshaper.reshape(date1)
	# reshaped_word=get_display(reshaped_text)
	pdf.cell(55, 10, txt = str(date1.strftime("%d-%m-%Y")),border=0,ln = 0, align = 'R')

	reshaped_text=arabic_reshaper.reshape("رخصت کا دورانیہ:")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0, 10, txt = reshaped_word,border=0,ln = 1, align = 'R')
    #line 5
	reshaped_text=arabic_reshaper.reshape("دن")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(110, 10, txt = reshaped_word,border=0,ln = 0, align = 'R') 

	reshaped_text=arabic_reshaper.reshape(total_days)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(20, 10, txt = reshaped_word,border=0,ln = 0, align = 'R')

	reshaped_text=arabic_reshaper.reshape("رخصت کا کل دورانیہ:")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0, 10, txt = reshaped_word,border=0,ln = 1, align = 'R')

    #line 6
	reshaped_text=arabic_reshaper.reshape(reason)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(150, 10, txt = reshaped_word,border=0,ln = 0, align = 'R')

	reshaped_text=arabic_reshaper.reshape("رخصت کی وجوہات:")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0, 10, txt = reshaped_word,border=0,ln = 1, align = 'R')

    #line 7
	reshaped_text=arabic_reshaper.reshape(address)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(150, 10, txt = reshaped_word,border=0,ln = 0, align = 'R')

	reshaped_text=arabic_reshaper.reshape("دورانِ رخصت پتہ:")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0, 10, txt = reshaped_word,border=0,ln = 1, align = 'R')
    #line 8&9
	pdf.cell(70, 15, txt = "     ",border=0,ln = 1, align = 'R')
	pdf.cell(40, 2, txt = "----------------",border=0,ln = 1, align = 'R')
	reshaped_text=arabic_reshaper.reshape("دستخط: درخواست گزار",)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(40,10, txt = reshaped_word,border=0,ln = 1, align = 'R')
	#line 10
	pdf.cell(70, 15, txt = "     ",border=0,ln = 1, align = 'R')
	pdf.cell(150, 10, txt = "--------------------------------------------------",border=0,ln = 0, align = 'R')
	reshaped_text=arabic_reshaper.reshape("تفصیل استحقاق رخصت:",)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0,10, txt = reshaped_word,border=0,ln = 1, align = 'R')
	#line 11
	pdf.cell(80, 10, txt = "------------------------------",border=0,ln = 0, align = 'L')
	reshaped_text=arabic_reshaper.reshape("تصدیق کنندہ:",)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0,10, txt = reshaped_word,border=0,ln = 1, align = 'L')
	#line 12
	pdf.cell(150, 10, txt = "--------------------------------------------------",border=0,ln = 0, align = 'R')
	reshaped_text=arabic_reshaper.reshape("منظور کنندہ:",)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0,10, txt = reshaped_word,border=0,ln =1, align = 'R')

	# save the pdf with name .pdf
	filename= "Application.pdf"
	pdf.output(filename)

def make_3rd_party_leave(name,position,dept,date1,date2,total_days,reason,gender,name_informant):
	from fpdf import FPDF

	import arabic_reshaper
	from bidi.algorithm import get_display
	from datetime import date 
	no_of_days = str((date2-date1).days+1)
	
	if gender == "مرد":
		gender_pronoun="محترم "
	else:
		gender_pronoun="محترمہ "
	
	# save FPDF() class into a
	# variable pdf
	pdf = FPDF()

	# Add a page
	pdf.add_page()
	pdf.image("src/logo.jpeg", x =15, y = 5, w = 180, h = 40, type = 'JPG', link = '')
	# set style and size of font
	# that you want in the pdf
	# pdf.add_font('Jameel Noori Nastaleeq', '', 'src/PakType-Naskh-Basic.ttf', uni=True)
	pdf.add_font('Naskh', '', 'src/Amiri-Regular.ttf', uni=True)
	# pdf.set_font("Jameel Noori Nastaleeq",style='U', size = 25)

	# create a cell

	pdf.set_font("Naskh",style='', size = 15)
	pdf.cell(70, 15, txt = "     ",border=0,ln = 1, align = 'R')
	pdf.set_font("Naskh",style='U', size = 35)
	reshaped_text=arabic_reshaper.reshape("اطلاع برائے رخصت ")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(200, 55, txt = reshaped_word,border=0,ln = 1, align = 'C')
	# pdf.set_font("Jameel Noori Nastaleeq",style='', size = 15) 
	pdf.set_font("Naskh",style='', size = 15)
	reshaped_text=arabic_reshaper.reshape(str(date1))
	date=get_display(reshaped_text)
	if date1==date2:
		sentence=[gender_pronoun+name,
					" ( ",
					position,
					" ) نے",
					" بذریعہ ٹیلی فون",
					" اطلاع دی ہے",
					" کہ وہ  ",
					date,
					" کو ",
					reason,
					" کے باعث",
					" دفتر حاضر",
					" ہونے سے",
					" قاصر ہیں۔",
					"لہذا ایک",
					" یوم کی رخصت ",
					"عنایت فرمائیں۔ "]
	else:
		sentence=[gender_pronoun+name,
					" ( ",
					position,
					" ) نے بذریعہ ٹیلی فون",
					" اطلاع دی ہے کہ وہ  ",
					str(date1),
					" تا ",
					str(date2),
					" کو ",
					reason,
					" کے باعث ",
					"دفتر حاضر ",
					"ہونے سے ",
					"قاصر ہ۔ ",
					"لہذا ",
					no_of_days,
					" ایام ",
					"کی رخصت ",
					"عنایت فرمائیں۔"]
	max_len=80
	sub_sen1=""
	sub_sen2=""
	sub_sen3=""
	line1=0
	line2=0
	for element in sentence:
		if line1==0 and len(sub_sen1)+len(element) < max_len:
			sub_sen1= sub_sen1 + element
		else:
			line1=1
			if line2==0 and len(sub_sen2)+len(element) < max_len:
				sub_sen2 = sub_sen2 + element
			else:
				line2=1
				sub_sen3=sub_sen3+element
	#line 1
	text=sub_sen1
	if line1 ==1:
		text=text+"\n"+sub_sen2
	if line2==1:
		text=text+"\n"+sub_sen3
	
	# 	text=gender_pronoun+name+" ( "+position+" ) نے بذریعہ ٹیلی فون اطلاع دی ہے کہ وہ  "+""+date+" کو "+"\n"+reason+" کے باعث دفتر حاضر ہونے سے قاصر ہیں۔لہذا ایک یوم کی رخصت عنایت فرمائیں۔ "
	# else:
	# 	text=gender_pronoun+name+" ( "+position+" ) نے بذریعہ ٹیلی فون اطلاع دی ہے کہ وہ  "+str(date1)+" تا "+str(date2)+"\n"+" کو "+reason+" کے باعث دفتر حاضر ہونے سے قاصر ہیں۔لہذا  "+no_of_days+" ایام کی رخصت عنایت فرمائیں۔"
	reshaped_text=arabic_reshaper.reshape(text)
	reshaped_word=get_display(reshaped_text)
	pdf.multi_cell(0, 15, txt =reshaped_word ,border=0, align = 'R')

	#line 2 
	pdf.cell(70, 15, txt = "     ",border=0,ln = 1, align = 'R')
	pdf.cell(40, 2, txt = "----------------",border=0,ln = 1, align = 'C')
	reshaped_text=arabic_reshaper.reshape(name_informant)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(40,10, txt = reshaped_word,border=0,ln = 1, align = 'C')
	reshaped_text=arabic_reshaper.reshape("(اطلاع دینے والے کا نام)")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(40,10, txt = reshaped_word,border=0,ln = 1, align = 'C')
	pdf.cell(40,10, txt =str( date1.strftime("%d-%m-%Y")) ,border=0,ln = 1, align = 'C')
	#line 10
	pdf.cell(140, 10, txt = "--------------------------------------------------",border=0,ln = 0, align = 'R')
	reshaped_text=arabic_reshaper.reshape("تفصیل استحقاق رخصت:",)
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0,10, txt = reshaped_word,border=0,ln = 1, align = 'R')
	#line 3
	if (dept == "اپلیکیشن" or dept =="بصری حروف شناسی" or dept=="تحقیق و ترقی"):
		pdf.cell(70, 15, txt = "     ",border=0,ln = 1, align = 'R')
		pdf.cell(0, 10, txt = "--------------------------------------------------",border=0,ln = 1, align = 'R')
		reshaped_text=arabic_reshaper.reshape(" پروگرام مینجر "+dept)
		reshaped_word=get_display(reshaped_text)
		pdf.cell(0,10, txt = reshaped_word,border=0,ln = 1, align = 'R')
	#line 4
	pdf.cell(70, 15, txt = "     ",border=0,ln = 1, align = 'R')
	pdf.cell(0, 10, txt = "--------------------------------------------------",border=0,ln = 1, align = 'R')
	reshaped_text=arabic_reshaper.reshape("  جناب پرنسپل انوسٹیگیٹر ")
	reshaped_word=get_display(reshaped_text)
	pdf.cell(0,10, txt = reshaped_word,border=0,ln = 1, align = 'R')


	# save the pdf with name .pdf
	filename= "Application.pdf"
	pdf.output(filename)
