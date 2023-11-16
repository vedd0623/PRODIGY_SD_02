from tkinter import *
from random import *
from tkinter.messagebox import *

root=Tk()
root.title('Guessing Game')
root.geometry('500x500+50+50')
root.configure(bg='red')
f=('Arial',15)
f1=('Algerian',20,'underline')
f2=('Algerian',20)

a=randint(2,5)
print(a)

lab_guess=Label(root,text='GUESS THE NUMBER!',font=f1,bg='lightgreen')
lab_guess.pack(pady=30)
lab_guess1=Label(root,text='Enter your guess',font=f,bg='lightgreen')
lab_guess1.place(x=50,y=100)
ent_guess1=Entry(root,font=f,bg='lightgreen')
ent_guess1.place(x=220,y=100)

c=0

def check():
	global c
	try:
		b=int(ent_guess1.get())
	except:
		showerror('Issue','Enter valid entry')
		return

	c+=1

	if b==a:
		showinfo('Congratulations','Correct Guess! Total attempts:{}'.format(c))
		ent_guess1.config(state='disabled')
		btn_check.config(state='disabled')
	else:
		showerror('Oops','Wrong Guess!')
		return

btn_check=Button(root,text='CHECK',font=f2,command=check,bg='lightgreen')
btn_check.place(x=200,y=150)

root.mainloop()