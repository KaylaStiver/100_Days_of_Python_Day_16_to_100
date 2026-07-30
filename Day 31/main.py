from tkinter import *
from random import choice, randint, shuffle

import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_word = ""
to_learn = {}
#---------------------- Card Functionality ------------------------#

try:
    data = pandas.read_csv("./data/french_words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    words_dict = data.to_dict(orient="records")
else:
    to_learn = pandas.read_csv("./data/french_words.csv")
    words_dict = to_learn.to_dict(orient="records")

def new_card():
    global current_word, timer
    window.after_cancel(timer)
    chosen_word = choice(words_dict)
    canvas.itemconfig(bg_img, image=front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=chosen_word.get("French"), fill="black")
    current_word = chosen_word

    timer = window.after(3000, flip_card)


def flip_card():
    translated_word = ""
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(bg_img, image=back_img)
    for i in words_dict:
        if i.get("French") == current_word.get("French"):
            translated_word = i.get("English")
    canvas.itemconfig(word_text, text=translated_word, fill="white")

def is_known():
    words_dict.remove(current_word)
    new_card()
    data = pandas.DataFrame(words_dict)
    data.to_csv("./data/french_words_to_learn.csv", index=False)

#---------------------- UI Setup ------------------------#
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)

timer = window.after(3000, new_card)

front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")

canvas = Canvas(window, width=1000, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
bg_img = canvas.create_image(500, 300, image=front_img)
title_text = canvas.create_text(495, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(490, 300, text="Word", font=("Ariel", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2, sticky=EW)

#Buttons for wrong and right
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=new_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)


window.mainloop()