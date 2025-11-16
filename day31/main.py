"""
Flashcard Learning App (French → English)

This program loads vocabulary words from CSV files and displays them as flashcards.
Users can mark words they already know, and the program saves the remaining words
to 'words_to_learn.csv', allowing progress tracking across sessions.

Features:
- Random flashcards
- Automatic card flipping after 3 seconds
- Saves progress (words removed once marked as known)
- Graphical UI using Tkinter
"""

from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# Global variables to store the current card and list of remaining cards
current_card = {}
to_learn = {}

# ---------------------------- DATA LOADING ---------------------------- #
"""
Load the list of words.

Priority:
1. Load 'words_to_learn.csv' (progress file)
2. If missing, load the original 'french_words.csv'
"""
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ---------------------------- FUNCTIONS ------------------------------- #
def next_card():
    """
    Select and display the next flashcard.

    Steps:
    1. Cancel the previous flip timer.
    2. Choose a random card.
    3. Display the French side.
    4. Schedule a flip in 3 seconds.
    """
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """Flip the flashcard to show the English translation."""
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    """
    Remove the current card from the review list
    and save updated progress to 'words_to_learn.csv'.
    """
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Timer for flipping cards
flip_timer = window.after(3000, func=flip_card)

# Canvas for card images/text
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# Start the first card
next_card()

window.mainloop()
