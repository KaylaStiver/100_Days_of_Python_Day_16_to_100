import tkinter as tk
import random
import pyperclip
from tkinter import EW, messagebox
from tkinter import messagebox as mbox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Function to generate a random password for the user. Also copies to clipboard.
def generate_password():

    #Clear previous password before generating new one
    password_input.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for char in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for sym in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for num in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

#Function to save entered data to a file and clear entries.
def save():

    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    data = f"{website},{username},{password}\n"

    if website == "" or username == "" or password == "":
        messagebox.showerror("Error", "Please enter all required information")
    else:
        is_ok = mbox.askokcancel(title="Confirm", message="Do you want to save this information?")

        if is_ok:
            with open("data.text", "a") as file:
                file.write(data)

            website_input.delete(0, "end")
            username_input.delete(0, "end")
            password_input.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #

#Basic UI sizing and logo set up
window = tk.Tk()
window.title("Password Manager")
window.configure(padx = 50, pady = 50)

logo_img = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(window, width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, sticky=EW)

#Labels for entries
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = tk.Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0, sticky=EW)

#Entry boxes
website_input = tk.Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky=EW)
website_input.focus()

username_input = tk.Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2, sticky=EW)
username_input.insert(0, "useremail@gmail.com")
password_input = tk.Entry(width=21)
password_input.grid(row=3, column=1, sticky=EW)

#Buttons
generate_button = tk.Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky=EW)

add_button = tk.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1,  columnspan=2, sticky=EW)

window.mainloop()