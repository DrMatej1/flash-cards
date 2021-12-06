from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    datad = original_data.to_dict(orient="records")
else:
    datad = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(datad)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=cardf)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=cardb)


def is_known():
    datad.remove(current_card)
    done = pandas.DataFrame(datad)
    done.to_csv("data/words_to_learn.csv", index=False)
    next_card()


#UI
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
cardf = PhotoImage(file="images/card_front.png")
cardb = PhotoImage(file="images/card_back.png")
righti = PhotoImage(file="images/right.png")
wrongi = PhotoImage(file="images/wrong.png")
right = Button(image=righti, highlightthickness=0, command=is_known)
wrong = Button(image=wrongi, highlightthickness=0, command=next_card)
card_background = canvas.create_image(400, 263, image=cardf)
canvas.grid(row=0, column=0, columnspan=2)
right.grid(row=1, column=0)
wrong.grid(row=1, column=1)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

next_card()

window.mainloop()
