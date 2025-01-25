from tkinter import *
from tkinter import ttk

root = Tk()

root.title('Calculator')
root.geometry('500x250+700+390')

icon = PhotoImage(file='calc.png')
root.iconphoto(False, icon)

plus = '+'
minus = '-'
multiply = '*'
divide = '/'

sign = StringVar()

numbers1 = ttk.Entry()
numbers1.place(x=60, y=30, anchor=NW)
numbers2 = ttk.Entry()
numbers2.place(x=300, y=30, anchor=NW)
plus_btn = ttk.Radiobutton(text=plus, value=plus, variable=sign)
plus_btn.pack()
minus_btn = ttk.Radiobutton(text=minus, value=minus, variable=sign)
minus_btn.pack()
multiply_btn = ttk.Radiobutton(text=multiply, value=multiply, variable=sign)
multiply_btn.pack()
divide_btn = ttk.Radiobutton(text=divide, value=divide, variable=sign)
divide_btn.pack()


def calculate():
    num1 = float(numbers1.get())
    num2 = float(numbers2.get())
    operation = sign.get()

    if operation == plus:
        result_value = num1 + num2
    elif operation == minus:
        result_value = num1 - num2
    elif operation == multiply:
        result_value = num1 * num2
    elif operation == divide:
        result_value = num1 / num2
    else:
        result_value = 'Error'
    result.config(text=f'Результат: {result_value}')


calc_btn = ttk.Button(root, text="Посчитать", command=calculate, padding=5)
calc_btn.place(x=205, y=100)

result = ttk.Label(root, text='Результат: ')
result.place(x=205, y=140)

root.mainloop()
