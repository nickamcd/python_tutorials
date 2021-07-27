from tkinter import *

# constants for number button sizing
NUM_X_PADDING = 60
NUM_Y_PADDING = 30

root = Tk()
root.title("Calculator")

e = Entry(root, width=50, borderwidth=3)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def num_click(num):
  curr = e.get()
  e.delete(0, END)
  e.insert(0, str(curr) + str(num))

def function_click(op):
  num = e.get()

  global num_one
  num_one = int(num)

  global operand
  operand = op

  e.delete(0, END)

def equal_click():
  num = e.get()
  e.delete(0, END)

  num_two = int(num)

  if operand == '+':
    e.insert(0, num_one + num_two)
  elif operand == '-':
    e.insert(0, num_one - num_two)
  elif operand == '*':
    e.insert(0, num_one * num_two)
  elif operand == '/':
    e.insert(0, num_one / num_two)

def clear_click():
  e.delete(0, END)


# create numerical buttons for input
button_1 = Button(root, text='1', padx=NUM_X_PADDING, pady=NUM_Y_PADDING, command=lambda : num_click(1))
button_2 = Button(root, text='2', padx=NUM_X_PADDING, pady=NUM_Y_PADDING, command=lambda : num_click(2))
button_3 = Button(root, text='3', padx=NUM_X_PADDING, pady=NUM_Y_PADDING, command=lambda : num_click(3))
button_4 = Button(root, text='4', padx=NUM_X_PADDING, pady=NUM_Y_PADDING, command=lambda : num_click(4))
button_5 = Button(root, text='5', padx=NUM_X_PADDING, pady=NUM_Y_PADDING, command=lambda : num_click(5))
button_6 = Button(root, text='6', padx=NUM_X_PADDING, pady=NUM_Y_PADDING, command=lambda : num_click(6))
button_7 = Button(root, text='7', padx=NUM_X_PADDING, pady=NUM_Y_PADDING, command=lambda : num_click(7))
button_8 = Button(root, text='8', padx=NUM_X_PADDING, pady=NUM_Y_PADDING, command=lambda : num_click(8))
button_9 = Button(root, text='9', padx=NUM_X_PADDING, pady=NUM_Y_PADDING, command=lambda : num_click(9))
button_0 = Button(root, text='0', padx=NUM_X_PADDING, pady=NUM_Y_PADDING, command=lambda : num_click(0))

# create other buttons for functionality
button_add = Button(root, text='+', padx=NUM_X_PADDING, pady=NUM_Y_PADDING, command=lambda : function_click('+'))
button_sub = Button(root, text='-', padx=NUM_X_PADDING, pady=NUM_Y_PADDING, command=lambda : function_click('-'))
button_mul = Button(root, text='*', padx=NUM_X_PADDING, pady=NUM_Y_PADDING, command=lambda : function_click('*'))
button_div = Button(root, text='/', padx=NUM_X_PADDING, pady=NUM_Y_PADDING, command=lambda : function_click('/'))

button_equal = Button(root, text='=', padx=NUM_X_PADDING, pady=NUM_Y_PADDING, command=lambda : equal_click())
button_clear = Button(root, text='C', padx=NUM_X_PADDING, pady=NUM_Y_PADDING, command=lambda : clear_click())

# put buttons into grid
button_0.grid(row=4, column=0)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)

button_equal.grid(row=4, column=1)
button_clear.grid(row=4, column=2)


root.mainloop()