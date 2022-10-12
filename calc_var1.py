from tkinter import *
import math
import tkinter.messagebox
root = Tk()
root.title("õÉËÉÐÅÄÉÑ Å ÍÎÏÇÏÅÚÉÞÎÁ ÅÌÅËÔÒÏÎÎÁ ÅÎÃÉËÌÏÐÅÄÉÑ")
root.configure(background = 'blanched almond')
root.resizable(width=False, height=False)
root.geometry("1000x1000")
calc = Frame(root)
calc.grid()
class Calc():
	def __init__(self):
		self.total=0
		self.current=''
		self.input_value=True
		self.check_sum=False
		self.op=''
		self.result=False
	def vvod(self, num):
		self.result=False
		firstnum=calct.get()
		secondnum=str(num)
		if self.input_value:
			self.current = secondnum
			self.input_value=False
		else:
			if secondnum == '.':
				if secondnum in firstnum:
					return
			self.current = firstnum+secondnum
		self.display(self.current)
	def sum_of_total(self):
		self.result=True
		self.current=float(self.current)
		if self.check_sum==True:
			self.valid_function()
		else:
			self.total=float(calct.get())
	def display(self, value):
		calct.delete(0, END)
		calct.insert(0, value)
	def valid_function(self):
		if self.op == "add":
			self.total += self.current
		if self.op == "min":
			self.total -= self.current
		if self.op == "umn":
			self.total += self.current
		if self.op == "del":
			self.total %= self.current
		if self.op == "delsost":
			self.total /= self.current
		self.input_value=True
		self.check_sum=False
		self.display(self.total)
	def operation(self, op):
		self.current = float(self.current)
		if self.check_sum:
			self.valid_function()
		elif not self.result:
			self.total=self.current
			self.input_value=True
		self.check_sum=True
		self.op=op
		self.result=False
	def Clear_Entry(self):
		self.result = False
		self.current = "0"
		self.display(0)
		self.input_value=True
	def All_Clear_Entry(self):
		self.Clear_Entry()
		self.total=0
	def pi(self):
		self.result = False
		self.current = math.pi
		self.display(self.current)
	def tau(self):
		self.result = False
		self.current = math.tau
		self.display(self.current)
	def e(self):
		self.result = False
		self.current = math.e
		self.display(self.current)
	def mathPM(self):
		self.result = False
		self.current = -(float(calct.get()))
		self.display(self.current)
	def squared(self):
		self.result = False
		self.current = math.sqrt(float(calct.get()))
		self.display(self.current)
	def cos(self):
		self.result = False
		self.current = math.cos(math.radians(float(calct.get())))
		self.display(self.current)
	def cosh(self):
		self.result = False
		self.current = math.cosh(math.radians(float(calct.get())))
		self.display(self.current)
	def tan(self):
		self.result = False
		self.current = math.tan(math.radians(float(calct.get())))
		self.display(self.current)
	def tanh(self):
		self.result = False
		self.current = math.tanh(math.radians(float(calct.get())))
		self.display(self.current)
	def sin(self):
		self.result = False
		self.current = math.sin(math.radians(float(calct.get())))
		self.display(self.current)
	def sinh(self):
		self.result = False
		self.current = math.sinh(math.radians(float(calct.get())))
		self.display(self.current)
	def log(self):
		self.result = False
		self.current = math.log(float(calct.get()))
		self.display(self.current)
	def exp(self):
		self.result = False
		self.current = math.exp(float(calct.get()))
		self.display(self.current)
	def acosh(self):
		self.result = False
		self.current = math.acosh(float(calct.get()))
		self.display(self.current)
	def asinh(self):
		self.result = False
		self.current = math.asinh(float(calct.get()))
		self.display(self.current)
	def expm1(self):
		self.result = False
		self.current = math.expm1(float(calct.get()))
		self.display(self.current)
	def lgamma(self):
		self.result = False
		self.current = math.lgamma(float(calct.get()))
		self.display(self.current)
	def degrees(self):
		self.result = False
		self.current = math.degrees(float(calct.get()))
		self.display(self.current)
	def log2(self):
		self.result = False
		self.current = math.log2(float(calct.get()))
		self.display(self.current)
	def log10(self):
		self.result = False
		self.current = math.log10(float(calct.get()))
		self.display(self.current)
	def log1p(self):
		self.result = False
		self.current = math.log1p(float(calct.get()))
		self.display(self.current)
added_value = Calc()
calct = Entry(calc, font=('Arial Black',18,'bold'),
				bg='pink',fg='white')
calct.grid(row=0,column=0, columnspan=4, pady=1)
calct.insert(0,"0")
numberpad = "123456789"
i=0
btn = []
for j in range(2,5):
	for k in range(3):
		btn.append(Button(calc, width=6, height=2,
						bg='pink',fg='white',
						font=('Arial Black',18,'bold'),
						text=numberpad[i]))
		btn[i].grid(row=j, column= k, pady = 0)
		btn[i]["command"]=lambda x=numberpad[i]:added_value.vvod(x)
		i+=1
	
Och = Button(calc, text=chr(67),width=6,
				height=2,bg='blanched almond',
				font=('Arial Black',18,'bold')
				, command=added_value.Clear_Entry
				).grid(row=2, column= 3, pady = 0)
OchVse = Button(calc, text=chr(67)+chr(69),
					width=6, height=2,
					bg='blanched almond',
					font=('Arial Black',18,'bold'),
					
					command=added_value.All_Clear_Entry
					).grid(row=1, column= 3, pady = 0)
kn = Button(calc, text="\u221A",width=6, height=2,
			bg='blanched almond', font=('Arial Black',
									18,'bold'),
			command=added_value.squared
			).grid(row=1, column= 2, pady = 0)
dobavit = Button(calc, text="+",width=6, height=2,
				bg='blanched almond',
				font=('Arial Black',18,'bold'),
				command=lambda:added_value.operation("add")
				).grid(row=1, column= 0, pady = 0)
ss = Button(calc, text="-",width=6,
				height=2,bg='blanched almond',
				font=('Arial Black',18,'bold'),
				command=lambda:added_value.operation("sub")
				).grid(row=1, column= 1, pady = 0)
umn = Button(calc, text="x",width=6,
				height=2,bg='blanched almond',
				font=('Arial Black',18,'bold'),
				command=lambda:added_value.operation("multi")
				).grid(row=3, column= 3, pady = 0)
delit = Button(calc, text="/",width=6,
				height=2,bg='blanched almond',
				font=('Arial Black',18,'bold'),
				command=lambda:added_value.operation("divide")
				).grid(row=4, column= 3, pady = 0)
zero = Button(calc, text="0",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=lambda:added_value.vvod(0)
				).grid(row=5, column= 0, pady = 0)
Tochka = Button(calc, text=".",width=6,
				height=2,bg='blanched almond',
				font=('Arial Black',18,'bold'),
				command=lambda:added_value.vvod(".")
				).grid(row=5, column= 1, pady = 0)
modul = Button(calc, text="|n|",width=6,
			height=2,bg='blanched almond', font=('Arial Black',18,'bold'),
			command=added_value.mathPM
			).grid(row=5, column= 2, pady = 0)
ravno = Button(calc, text="=",width=6,
				height=2,bg='blanched almond',
				font=('Arial Black',18,'bold'),
				command=added_value.sum_of_total
				).grid(row=5, column= 3, pady = 0)
knopkapi = Button(calc, text="π",width=6,
			height=2,bg='pink',fg='white',
			font=('Arial Black',18,'bold'),
			command=added_value.pi
			).grid(row=1, column= 5, pady = 0)
cosinus = Button(calc, text="cos",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=added_value.cos
			).grid(row=1, column= 4, pady = 0)
tangens = Button(calc, text="tan",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=added_value.tan
			).grid(row=1, column= 7, pady = 0)
sinus = Button(calc, text="sin",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=added_value.sin
			).grid(row=1, column= 6, pady = 0)
knopka2pi = Button(calc, text="2π",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=added_value.tau
			).grid(row=2, column= 5, pady = 0)
cosinush = Button(calc, text="cosh",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=added_value.cosh
				).grid(row=2, column= 4, pady = 0)
tangensh = Button(calc, text="tanh",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=added_value.tanh
				).grid(row=2, column= 7, pady = 0)
sinush = Button(calc, text="sinh",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=added_value.sinh
				).grid(row=2, column= 6, pady = 0)
logarifm = Button(calc, text="log",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=added_value.log
			).grid(row=3, column= 5, pady = 0)
btnExp = Button(calc, text="exp",width=6, height=2,
				bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=added_value.exp
			).grid(row=3, column= 4, pady = 0)
btnMod = Button(calc, text="mod",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=lambda:added_value.operation("mod")
				).grid(row=3, column= 7, pady = 0)
btnE = Button(calc, text="e",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=added_value.e
			).grid(row=3, column= 6, pady = 0)
logarifm10 = Button(calc, text="log10",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=added_value.log10
				).grid(row=4, column= 5, pady = 0)
cosinus = Button(calc, text="log1n",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=added_value.log1p
				).grid(row=4, column= 4, pady = 0)
eee = Button(calc, text="expm1",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=added_value.expm1
				).grid(row=4, column= 7, pady = 0)
gamma1 = Button(calc, text="gamma",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=added_value.lgamma
				).grid(row=4, column= 6, pady = 0)
logarifm2 = Button(calc, text="log2",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=added_value.log2
				).grid(row=5, column= 5, pady = 0)
degres = Button(calc, text="deg",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=added_value.degrees
			).grid(row=5, column= 4, pady = 0)
btnacosh = Button(calc, text="acosh",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=added_value.acosh
				).grid(row=5, column= 7, pady = 0)
btnasinh = Button(calc, text="asinh",width=6,
				height=2,bg='pink',fg='white',
				font=('Arial Black',18,'bold'),
				command=added_value.asinh
				).grid(row=5, column= 6, pady = 0)
CalcDis = Label(calc, text = "õÉËÉÐÅÄÉÑ Å ÍÎÏÇÏÅÚÉÞÎÁ ÅÌÅËÔÒÏÎÎÁ ÅÎÃÉËÌÏÐÅÄÉÑ", fg="pink",
				font=('Arial Black',25,'bold'))
CalcDis.grid(row=0, column= 4,columnspan=4)
def Vihod():
	Vihod = tkinter.messagebox.askyesno("õÉËÉÐÅÄÉÑ Å ÍÎÏÇÏÅÚÉÞÎÁ ÅÌÅËÔÒÏÎÎÁ ÅÎÃÉËÌÏÐÅÄÉÑ", "Ð£ÐžÐºÐžÐ¿ÐµÐŽÐžÑ Ðµ ÑÐ²ÐŸÐ±ÐŸÐŽ ÐŒÐœÐŸÐ?")
	if Vihod>0:
		root.destroy()
		return
def Engeener():
	root.resizable(width=False, height=False)
	root.geometry("950x520")
def Standart():
	root.resizable(width=False, height=False)
	root.geometry("445x520")
menubar = Menu(calc)
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Опции', menu = filemenu)
filemenu.add_command(label = "Обычный", command = Standart)
filemenu.add_command(label = "Инженерный", command = Engeener)
filemenu.add_separator()
filemenu.add_command(label = "Выход", command = Vihod)
root.config(menu=menubar)
root.mainloop()
