from tkinter import *
root = Tk()
root.title("Calculator App")
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def btn_clear():
    e.delete(0, END)

def btn_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "subtract":
        e.insert(0, f_num - int(second_number))
    elif math == "multiply":
        e.insert(0, f_num * int(second_number))
    elif math == "divide":
        e.insert(0, f_num / int(second_number))

def btn_operation(op):
    first_num = e.get()
    global f_num
    global math
    math = op
    f_num = int(first_num)
    e.delete(0, END)

btn1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
btn2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
btn3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
btn4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
btn5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
btn6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
btn7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
btn8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
btn9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
btn0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
# Define operation buttons
btn_add = Button(root, text="+", padx=39, pady=20, command=lambda: btn_operation("addition"))
btn_subtract = Button(root, text="-", padx=41, pady=20, command=lambda: btn_operation("subtract"))
btn_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: btn_operation("multiply"))
btn_divide = Button(root, text="/", padx=41, pady=20, command=lambda: btn_operation("divide"))
btn_equal = Button(root, text="=", padx=91, pady=20, command=btn_equal)
btn_clear = Button(root, text="Clear", padx=79, pady=20, command=btn_clear)

# Place buttons on the grid
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btn0.grid(row=4, column=0)

btn_add.grid(row=5, column=0)
btn_subtract.grid(row=6, column=0)
btn_multiply.grid(row=6, column=1)
btn_divide.grid(row=6, column=2)

btn_equal.grid(row=5, column=1, columnspan=2)
btn_clear.grid(row=4, column=1, columnspan=2)

root.mainloop()