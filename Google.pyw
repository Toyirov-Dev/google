from tkinter import*
import  webbrowser


# Dastur oynasi:
root = Tk()
root.title("Google clone!")
root.geometry('500x300')
root.config(bg='#19497C')

def dastur_vzfsi():
	webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % Search_input.get())

# Sarlavha:
Sarlavha = Label(root, text="Google-ga asoslangan\nqidiruv dasturi!",
	fg='Black',
	font=('Times', 17, 'bold'),
	bg='#19497C')
Sarlavha.place(x=140, y=20)


# input-ga tavfsif:
input_tvf = Label(root, text=" Qidirmoqchi bo'lgan malumotingizni yozing: ",
	fg='Black',
	font=('Times', 10, 'italic'),
	bg='#19497C',
	relief=SOLID,
	bd=1)
input_tvf.place(x=130, y=100)


# Search input:
Search_input = Entry(root, bg='#DFDFDF',
	fg = 'black',
	font = ('Times', 10, 'italic'),
	relief = SOLID,
	width = 35)
Search_input.place(x=135, y=130)


# Enter button:
S_button = Button(root, text='ENTER',
	bg='#1ECBE1',
	fg='black',
	font=('Times', 10, 'bold'),
	relief=SOLID,
	cursor='hand2',
	width=20,
	command=dastur_vzfsi)
S_button.place(x=183, y=175)


# inputga bezak:
input_bezak = Label(root, text=">>>",
	fg='Black',
	font=('Times', 10, 'bold'),
	bg='#19497C')
input_bezak.place(x=95, y=130)

input_bezak2 = Label(root, text="<<<",
	fg='Black',
	font=('Times', 10, 'bold'),
	bg='#19497C')
input_bezak2.place(x=390, y=130)


# Dasturchi:
Dasturchi = Label(root, text=" Dastur 'Toyirov Ziyodullo' tomonidan yaratildi! ",
	fg='Black',
	font=('Times', 10, 'italic'),
	bg='#19497C',
	relief=SOLID,
	bd=1)
Dasturchi.place(x=125, y=280)






root.mainloop()
