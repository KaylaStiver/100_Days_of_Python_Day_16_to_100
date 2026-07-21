from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
BACKGROUND_COLOR = "#B1DDC6"

#---------------------- UI Setup ------------------------#
#Card positioning
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)

canvas = Canvas(window, width=1000, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas.create_image(500, 300, image=front_img)
canvas.grid(row=0, column=1, columnspan= 2, sticky=EW)

#Card labels for title and word
title_label = Label(text="Title", font=("Ariel", 40, "italic"), bg="white")
title_label.place(x=450, y=150)

word_label = Label(text="Word", font=("Ariel", 60, "bold"), bg="white")
word_label.place(x=400, y=263)

#Buttons for wrong and right
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(row=1, column=1)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(row=1, column=2)

window.mainloop()