from tkinter import *

#entry
str1 = ""

#=====================================
# button click, clear, equals


# too much exceptions, just gave up after these
# universal "Invalid input" Error message as a response is further

def diff_shenanigans(sym,str1):
    if len(str1) > 0:
        if (str1[-1] == '(' and sym == ')') or (str1[-1] == ')' and sym == '('):
            return 1
        else:
            return 0

    if len(str1) == 0:
        if sym == ')':
            return 1
        else:
            return 0

# too much exceptions, just gave up after these
# universal "Invalid input" Error message as a response is further


def click(sym):
    global str1
    if not diff_shenanigans(sym, str1):
        str1 = str1 + str(sym)
        txt_input.set(str1)


def clear():
    global str1
    str1 = ""
    txt_input.set("")

def clear1():
    global str1
    str1 = str1[0:-1]
    txt_input.set(str1)

def equals():
    global str1
    try:
        res = str(eval(str1))
    except (SyntaxError, NameError):
        txt_input.set("Invalid Input")
        str1 = ""
    except ZeroDivisionError:
        txt_input.set("Infinity(zero division)")
        str1 = ""

    else:
        txt_input.set(res)
        str1 = ""


#GUI START

root = Tk()
root.title("Calculator")
txt_input = StringVar()



display = Entry(root, font = ('helvetica', 25),textvariable = txt_input, bd = 15,insertwidth=10, bg = "white", justify = 'right').grid(columnspan = 4)

#=====================================
# buttons placement and initialization

bracket1 = Button (root, padx = 15, bd = 10, fg = "black", font = ('helvetica', 25), text = "(", command = lambda:click( '('  )).grid(row = 1, column = 0)
bracket2 = Button (root, padx = 15, bd = 10, fg = "black", font = ('helvetica', 25), text = ")", command = lambda:click( ')' )).grid(row = 1, column = 1)
cl = Button (root, padx = 15, bd = 10, fg = "black", font = ('helvetica', 25), text = "←", command = lambda:clear1()).grid(row = 1, column = 2)
ac = Button (root, padx = 0, bd = 10, fg = "black", font = ('helvetica', 25), text = "AC",  command = lambda:clear()).grid(row = 1, column = 3)

b7 = Button (root, padx = 15, bd = 10, fg = "black", font = ('helvetica', 25), text = "7", command = lambda:click(7)).grid(row = 2, column = 0)
b8 = Button (root, padx = 15, bd = 10, fg = "black", font = ('helvetica', 25), text = "8", command = lambda:click(8)).grid(row = 2, column = 1)
b9 = Button (root, padx = 15, bd = 10, fg = "black", font = ('helvetica', 25), text = "9", command = lambda:click(9)).grid(row = 2, column = 2)
divide = Button (root, padx = 18, bd = 10, fg = "black", font = ('helvetica', 25), text = "/",  command = lambda:click('/')).grid(row = 2, column = 3)

b4 = Button (root, padx = 15, bd = 10, fg = "black", font = ('helvetica', 25), text = "4", command = lambda:click(4)).grid(row = 3, column = 0)
b5 = Button (root, padx = 15, bd = 10, fg = "black", font = ('helvetica', 25), text = "5", command = lambda:click(5)).grid(row = 3, column = 1)
b6 = Button (root, padx = 15, bd = 10, fg = "black", font = ('helvetica', 25), text = "6", command = lambda:click(6)).grid(row = 3, column = 2)
multiply = Button (root, padx = 12, bd = 10, fg = "black", font = ('helvetica', 25), text = "X",  command = lambda:click('*')).grid(row = 3, column = 3)

b1 = Button (root, padx = 15, bd = 10, fg = "black", font = ('helvetica', 25), text = "1",command = lambda:click(1)).grid(row = 4, column = 0)
b2 = Button (root, padx = 15, bd = 10, fg = "black", font = ('helvetica', 25), text = "2", command = lambda:click(2)).grid(row = 4, column = 1)
b3 = Button (root, padx = 15, bd = 10, fg = "black", font = ('helvetica', 25), text = "3", command = lambda:click(3)).grid(row = 4, column = 2)
minus = Button (root, padx = 15, bd = 10, fg = "black", font = ('helvetica', 25), text = "-",  command = lambda:click('-')).grid(row = 4, column = 3)

b0 = Button (root, padx = 15, bd = 10, fg = "black", font = ('helvetica', 25), text = "0", command = lambda:click(0)).grid(row = 5, column = 0)
point = Button (root, padx = 15, bd = 10, fg = "black", font = ('helvetica', 25), text = ".", command = lambda:click('.')).grid(row = 5, column = 1)
equal = Button (root, padx = 15, bd = 10, fg = "black", font = ('helvetica', 25), text = "=", command = lambda:equals()).grid(row = 5, column = 2)
plus = Button (root, padx = 12, bd = 10, fg = "black", font = ('helvetica', 25), text = "+",  command = lambda:click('+')).grid(row = 5, column = 3)

root.mainloop()








"""
class calculator:

    def add(x, y):
        print(x+y)
        return x + y


    def subtract(x, y):
        return x - y


    def divide(x, y):
        return x / y


    def multiply(x, y):
        return x * y


a = calculator
a.add(2,3)
"""
