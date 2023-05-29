import tkinter as tk

calculation = ""


def operation(num):
    global calculation  # rendo calculation richiamabile fuori dalla funzione
    calculation += str(num)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def equals():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.delete(1.0, "Error")


def clear():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()  # to create the object
root.title("Crazy Calculator")
root.geometry("375x500")
text_result = tk.Text(root, height=2.5, width=14, font=("Arial", 37))
text_result.grid(columnspan=5)

btn_1 = tk.Button(
    root, text=1, command=lambda: operation(1), width=5, font=("Arial", 20)
)
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(
    root, text=2, command=lambda: operation(2), width=5, font=("Arial", 20)
)
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(
    root, text=3, command=lambda: operation(3), width=5, font=("Arial", 20)
)
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(
    root, text=4, command=lambda: operation(4), width=5, font=("Arial", 20)
)
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(
    root, text=5, command=lambda: operation(5), width=5, font=("Arial", 20)
)
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(
    root, text=6, command=lambda: operation(6), width=5, font=("Arial", 20)
)
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(
    root, text=7, command=lambda: operation(7), width=5, font=("Arial", 20)
)
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(
    root, text=8, command=lambda: operation(8), width=5, font=("Arial", 20)
)
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(
    root, text=9, command=lambda: operation(9), width=5, font=("Arial", 20)
)
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(
    root, text=0, command=lambda: operation(0), width=5, font=("Arial", 20)
)
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(
    root, text="+", command=lambda: operation("+"), width=5, font=("Arial", 20)
)
btn_plus.grid(row=2, column=4)

btn_div = tk.Button(
    root, text="/", command=lambda: operation("/"), width=5, font=("Arial", 20)
)
btn_div.grid(row=5, column=4)

btn_minus = tk.Button(
    root, text="-", command=lambda: operation("-"), width=5, font=("Arial", 20)
)
btn_minus.grid(row=3, column=4)

btn_mul = tk.Button(
    root, text="*", command=lambda: operation("*"), width=5, font=("Arial", 20)
)
btn_mul.grid(row=4, column=4)

btn_mul = tk.Button(
    root, text="*", command=lambda: operation("*"), width=5, font=("Arial", 20)
)
btn_mul.grid(row=4, column=4)

btn_open = tk.Button(
    root, text="(", command=lambda: operation("("), width=5, font=("Arial", 20)
)
btn_open.grid(row=5, column=1)

btn_close = tk.Button(
    root, text=")", command=lambda: operation(")"), width=5, font=("Arial", 20)
)
btn_close.grid(row=5, column=3)

btn_clear = tk.Button(root, text="C", command=clear, width=10, font=("Arial", 20))
btn_clear.grid(row=6, column=1, columnspan=2)

btn_equals = tk.Button(root, text="=", command=equals, width=10, font=("Arial", 20))
btn_equals.grid(row=6, column=3, columnspan=2)


root.mainloop()  # keep the object running
