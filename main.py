import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/english_words.csv")
# word_list = data.to_dict(orient="records")
current_word = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/english_words.csv")
    word_list = original_data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")


def next_card():
    global current_word
    current_word = random.choice(word_list)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_word["English"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    windows.after(4000, func=hindi_card)


def hindi_card():
    global current_word
    canvas.itemconfig(card_title, text="Hindi", fill="white")
    canvas.itemconfig(card_word, text=current_word["Hindi"], fill="white")
    canvas.itemconfig(card_background, image=back_image)
    windows.after(4000, func=next_card)


def remove_word():
    global current_word
    word_list.remove(current_word)
    data = pandas.DataFrame(word_list)
    data.to_csv("data/words_to_learn.csv", index=False)
    words_left.config(text=f"Words Remaining : {len(word_list)}")


windows = Tk()
windows.title("Flashy")
windows.config(bg=BACKGROUND_COLOR, pady=20, padx=20)

# windows.after(5000, func=hindi_card)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_background = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="", font=("ariel", 50, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("ariel", 60, "bold"))
canvas.grid(row=1, column=1)

right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, highlightthickness=0, command=remove_word)
right.grid(row=2, column=1)

information = Label()
information.config(text="Press ✔ if you know the word, It won't be repeated again")
information.config(background=BACKGROUND_COLOR, font=("ariel", 15, "normal"), fg="sea green", pady=10)
information.grid(row=3, column=1)

words_left = Label()
words_left.config(text=f"Words Remaining : {len(word_list)}")
words_left.config(background=BACKGROUND_COLOR, font=("ariel", 15, "normal"), fg="sea green", pady=10)
words_left.grid(row=0, column=1)

next_card()

windows.mainloop()


