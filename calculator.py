from tkinter import *

root = Tk()
root.title("Calculator")

button_width = 3 

expression = ""

def key(user_input):
    global expression
    if user_input == "=":
        expression = str(eval(expression))
    elif user_input == "C":
        expression = ""
    elif user_input == "BACK":
        expression = expression[0:-1]
    else:
        expression += user_input

    expression_shown.set(expression)

expression_shown = StringVar()

expression_field = Entry(root, textvariable=expression_shown)
expression_field.grid(columnspan=4)

bt_one = Button(root, text = "1", command = lambda: key("1"),
                width = button_width)
bt_one.grid(row = 1,column=0)
bt_two = Button(root, text = "2", command = lambda: key("2"), 
                width = button_width)
bt_two.grid(row = 1, column=1)
bt_three = Button(root, text = "3", command = lambda: key("3"), 
                  width = button_width)
bt_three.grid(row = 1, column=2)
bt_minus = Button(root, text = "-", command = lambda: key("-"), 
                  width = button_width)
bt_minus.grid(row = 1, column=3)
bt_clear = Button(root, text = "BACK", command = lambda: key("BACK"),
                  width = button_width)
bt_clear.grid(row = 1, column=4)

bt_four = Button(root, text = "4", command = lambda: key("4"), 
                 width = button_width)
bt_four.grid(row = 2, column=0)
bt_five = Button(root, text = "5", command = lambda: key("5"), 
                 width = button_width)
bt_five.grid(row = 2, column=1)
bt_six = Button(root, text = "6", command = lambda: key("6"), 
                width = button_width)
bt_six.grid(row = 2, column=2)
bt_plus = Button(root, text = "+", command = lambda: key("+"), 
                 width = button_width)
bt_plus.grid(row = 2, column=3)
bt_clear = Button(root, text = "C", command = lambda: key("C"),
                  width = button_width)
bt_clear.grid(row = 2, column=4)

bt_seven = Button(root, text = "7", command = lambda: key("7"), 
                  width = button_width)
bt_seven.grid(row = 3, column=0)
bt_eight = Button(root, text = "8", command = lambda: key("8"), 
                  width = button_width)
bt_eight.grid(row = 3, column=1)
bt_nine = Button(root, text = "9", command = lambda: key("9"), 
                 width = button_width)
bt_nine.grid(row = 3, column=2)
bt_multiply = Button(root, text = "*", command = lambda: key("*"), 
                     width = button_width)
bt_multiply.grid(row = 3, column=3)
bt_openbracket = Button(root, text = "(", command = lambda: key("("),
                  width = button_width)
bt_openbracket.grid(row = 3, column=4)


bt_zero = Button(root, text = "0", command = lambda: key("0"), 
                 width = 10)
bt_zero.grid(row = 4, columnspan=2)
bt_equal = Button(root, text = "=", command = lambda: key("="), 
                  width = button_width)
bt_equal.grid(row = 4, column=2)
bt_divide = Button(root, text = "/", command = lambda: key("/"), 
                   width = button_width)
bt_divide.grid(row = 4, column=3)
bt_closebracket = Button(root, text = ")", command = lambda: key(")"),
                  width = button_width)
bt_closebracket.grid(row = 4, column=4)

root.mainloop()