
import tkinter as tk

current_number = ""
first_number = ""
operator = ""

def click(value):
    global current_number
    current_number = current_number + str(value)
    display.delete(0, tk.END)
    display.insert(0, current_number)

def set_operator(op):
    global first_number, operator, current_number

    first_number = current_number
    operator = op
    current_number = ""

def calculate():
    global first_number, operator, current_number

    second_number = current_number

    if first_number == "" or second_number == "":
        return

    num1 = float(first_number)
    num2 = float(second_number)

    if operator == "+":
        answer = num1 + num2

    elif operator == "-":
        answer = num1 - num2

    elif operator == "*":
        answer = num1 * num2

    elif operator == "/":
        if num2 == 0:
            display.delete(0, tk.END)
            display.insert(0, "Error")
            return

        answer = num1 / num2

    display.delete(0, tk.END)
    display.insert(0, str(answer))

    current_number = str(answer)

def clear():
    global current_number, first_number, operator

    current_number = ""
    first_number = ""
    operator = ""

    display.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

display = tk.Entry(root, font=("Arial",20))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

tk.Button(root,text="7",width=5,height=2,command=lambda:click(7)).grid(row=1,column=0)
tk.Button(root,text="8",width=5,height=2,command=lambda:click(8)).grid(row=1,column=1)
tk.Button(root,text="9",width=5,height=2,command=lambda:click(9)).grid(row=1,column=2)
tk.Button(root,text="/",width=5,height=2,command=lambda:set_operator("/")).grid(row=1,column=3)

tk.Button(root,text="4",width=5,height=2,command=lambda:click(4)).grid(row=2,column=0)
tk.Button(root,text="5",width=5,height=2,command=lambda:click(5)).grid(row=2,column=1)
tk.Button(root,text="6",width=5,height=2,command=lambda:click(6)).grid(row=2,column=2)
tk.Button(root,text="*",width=5,height=2,command=lambda:set_operator("*")).grid(row=2,column=3)

tk.Button(root,text="1",width=5,height=2,command=lambda:click(1)).grid(row=3,column=0)
tk.Button(root,text="2",width=5,height=2,command=lambda:click(2)).grid(row=3,column=1)
tk.Button(root,text="3",width=5,height=2,command=lambda:click(3)).grid(row=3,column=2)
tk.Button(root,text="-",width=5,height=2,command=lambda:set_operator("-")).grid(row=3,column=3)

tk.Button(root,text="0",width=5,height=2,command=lambda:click(0)).grid(row=4,column=0)
tk.Button(root,text="C",width=5,height=2,command=clear).grid(row=4,column=1)
tk.Button(root,text="=",width=5,height=2,command=calculate).grid(row=4,column=2)
tk.Button(root,text="+",width=5,height=2,command=lambda:set_operator("+")).grid(row=4,column=3)

root.mainloop()
