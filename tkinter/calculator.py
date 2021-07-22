from tkinter import *

# constants for number button sizing
NUM_X_PADDING = 60
NUM_Y_PADDING = 30

root = Tk()
root.title("Calculator")

e = Entry(root, width=50, borderwidth=3)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_add():
  pass


# create numerical buttons for input
button_1 = Button(root, text="1", padx=NUM_X_PADDING, pady=NUM_Y_PADDING)
button_2 = Button(root, text="2", padx=NUM_X_PADDING, pady=NUM_Y_PADDING)
button_3 = Button(root, text="3", padx=NUM_X_PADDING, pady=NUM_Y_PADDING)
button_4 = Button(root, text="4", padx=NUM_X_PADDING, pady=NUM_Y_PADDING)
button_5 = Button(root, text="5", padx=NUM_X_PADDING, pady=NUM_Y_PADDING)
button_6 = Button(root, text="6", padx=NUM_X_PADDING, pady=NUM_Y_PADDING)
button_7 = Button(root, text="7", padx=NUM_X_PADDING, pady=NUM_Y_PADDING)
button_8 = Button(root, text="8", padx=NUM_X_PADDING, pady=NUM_Y_PADDING)
button_9 = Button(root, text="9", padx=NUM_X_PADDING, pady=NUM_Y_PADDING)
button_0 = Button(root, text="0", padx=NUM_X_PADDING, pady=NUM_Y_PADDING)

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


root.mainloop()