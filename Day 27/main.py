import tkinter as tk

# window = tk.Tk()
# window.title("First GUI")
# window.minsize(500, 300)
#
# tk.Label(text="First GUI").pack()
#
#
# window.mainloop()

def add(*args):
    arg_sum = 0
    for arg in args:
        arg_sum += arg
    return arg_sum