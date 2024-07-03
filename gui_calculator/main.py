import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))        
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:  
        clear_field()
        text_result.insert(1.0, "Error")  
      


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("400x400")
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(row=0, column=0, columnspan=5)

btn_1 = tk.Button(root, text="1", height=2, width=5, command=lambda: add_to_calculation(1))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", height=2, width=5, command=lambda: add_to_calculation(2))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", height=2, width=5, command=lambda: add_to_calculation(3))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", height=2, width=5, command=lambda: add_to_calculation(4))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", height=2, width=5, command=lambda: add_to_calculation(5))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", height=2, width=5, command=lambda: add_to_calculation(6))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", height=2, width=5, command=lambda: add_to_calculation(7))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", height=2, width=5, command=lambda: add_to_calculation(8))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", height=2, width=5, command=lambda: add_to_calculation(9))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", height=2, width=5, command=lambda: add_to_calculation(0))
btn_0.grid(row=5, column=2)
btn_plus = tk.Button(root, text="+", height=2, width=5, command=lambda: add_to_calculation("+"))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", height=2, width=5, command=lambda: add_to_calculation("-"))
btn_minus.grid(row=3, column=4)
btn_mul = tk.Button(root, text="*", height=2, width=5, command=lambda: add_to_calculation("*"))
btn_mul.grid(row=4, column=4)
btn_div = tk.Button(root, text="/", height=2, width=5, command=lambda: add_to_calculation("/"))
btn_div.grid(row=5, column=4)
btn_open = tk.Button(root, text="(", height=2, width=5, command=lambda: add_to_calculation("("))
btn_open.grid(row=5, column=1)
btn_close = tk.Button(root, text=")", height=2, width=5, command=lambda: add_to_calculation(")"))
btn_close.grid(row=5, column=3)
btn_clear = tk.Button(root, text="C", height=2, width=14, command=clear_field)
btn_clear.grid(row=6, column=3, columnspan=2)
btn_equals = tk.Button(root, text="=", height=2, width=14, command=evaluate_calculation)
btn_equals.grid(row=6, column=1, columnspan=2)

root.mainloop()


