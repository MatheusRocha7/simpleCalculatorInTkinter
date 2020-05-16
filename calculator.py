from tkinter import *



expression = ""



def inputNumber(number, equation):
	global expression
	expression = expression + str(number)
	equation.set(expression)
	
	
	
def clearInputField(equation):
	global expression
	expression = ""
	equation.set("")
	
	
	
def evaluate(equation):
	global expression
	
	try:
		result = str(eval(expression))
		equation.set(result)
		expression = ""
		
	except:
		expression = ""
		
		
		

gui = Tk()
gui["bg"] = "black"
gui.title("Calculator")
gui.geometry("300x300")

equation = StringVar()
	
inputField = Entry(gui, textvariable = equation)
inputField.place(x = 0, y = 0)

bt1 = Button(gui, text = "1", command = lambda: inputNumber("1", equation))
bt2 = Button(gui, text = "2", command = lambda: inputNumber("2", equation))
bt3 = Button(gui, text = "3", command = lambda: inputNumber("3", equation))
bt4 = Button(gui, text = "4", command = lambda: inputNumber("4", equation))
bt5 = Button(gui, text = "5", command = lambda: inputNumber("5", equation))
bt6 = Button(gui, text = "6", command = lambda: inputNumber("6", equation))
bt7 = Button(gui, text = "7", command = lambda: inputNumber("7", equation))
bt8 = Button(gui, text = "8", command = lambda: inputNumber("8", equation))
bt9 = Button(gui, text = "9", command = lambda: inputNumber("9", equation))
bt0 = Button(gui, text = "0", command = lambda: inputNumber("0", equation))
btPlus = Button(gui, text = "+", command = lambda: inputNumber("+", equation))
btMinus = Button(gui, text = "-", command = lambda: inputNumber("-", equation))
btMultiplication = Button(gui, text = "x", command = lambda: inputNumber("x", equation))
btDivision = Button(gui, text = "÷", command = lambda: inputNumber("÷", equation))
btEqual = Button(gui, text = "=", command = lambda: evaluate(equation))
btClear = Button(gui, text = "C", command = lambda: clearInputField(equation))
btExit = Button(gui, text = "Exit", command = gui.destroy)

bt7.place(x = 0, y = 50)
bt4.place(x = 0, y = 120)
bt1.place(x = 0, y = 190)
bt0.place(x = 0, y = 260)

bt8.place(x = 100, y = 50)
bt5.place(x = 100, y = 120)
bt2.place(x = 100, y = 190)
btClear.place(x = 100, y = 260)

bt9.place(x = 200, y = 50)
bt6.place(x = 200, y = 120)
bt3.place(x = 200, y = 190)
btEqual.place(x = 200, y = 260)

btPlus.place(x = 300, y = 50)
btMinus.place(x = 300, y = 120)
btMultiplication.place(x = 300, y = 190)
btDivision.place(x = 300, y = 260)

btExit.place(x = 600, y = 0)

gui.mainloop()