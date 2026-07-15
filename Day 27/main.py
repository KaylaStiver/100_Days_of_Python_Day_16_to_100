import tkinter as tk
FONT = "Calibri 10"

# Base window, unadjustable
window = tk.Tk()
window.title("Mi to Km Calculator")
window.minsize(200, 100)
window.maxsize(200, 100)
window.configure(padx= "10", pady="15")

# Entry for user input
user_input = tk.Entry(width=10, font=FONT)
user_input.grid(row=0, column=1)

# Text widgets, in order of grid placement
mi_label = tk.Label(text="Miles", font=FONT)
mi_label.grid(row=0, column=2)

is_equal_label = tk.Label(text="is equal to", font=FONT)
is_equal_label.grid(row=1, column=0)

calc_label = tk.Label(text="0", font=FONT)
calc_label.grid(row=1, column=1)

km_label = tk.Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)

# Button and its function
def calculate():
    #get user input and round to 2 decimals and change label text
    miles = user_input.get()
    miles = float(miles)
    km = miles * 1.609344
    km = round(km,2)
    calc_label.config(text=str(km))

button = tk.Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()


