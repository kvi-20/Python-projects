import tkinter as tk
from tkinter import *
import random

win = tk.Tk()
win.geometry("800x600")
win.title("Number Guessing Game")

# Set background color
win.configure(bg="#f2f2f2")

# Generate a random number
num = random.randint(1, 10)

# Variables
hint = StringVar()
score = IntVar()
final_score = IntVar()
guess = StringVar()

hint.set("Guess a number between 1 to 10")
score.set(5)
final_score.set(score.get())

# Functionality
def fun():
    try:
        x = int(guess.get())
    except ValueError:
        hint.set("Please enter a valid number!")
        return

    final_score.set(score.get())
    if score.get() > 0:
        if x < 1 or x > 50:
            hint.set("Out of range! You lost 1 chance.")
            score.set(score.get() - 1)
            final_score.set(score.get())
        elif num == x:
            hint.set("🎉 Congratulations! YOU WON!!! 🎉")
            score.set(score.get() - 1)
            final_score.set(score.get())
        elif num > x:
            hint.set("Too low! Guess higher.")
            score.set(score.get() - 1)
            final_score.set(score.get())
        elif num < x:
            hint.set("Too high! Guess lower.")
            score.set(score.get() - 1)
            final_score.set(score.get())
    else:
        hint.set("❌ Game Over! You Lost. ❌")

def reset_game():
    global num
    num = random.randint(1, 50)
    score.set(5)
    hint.set("Guess a number between 1 to 50")
    guess.set("")
    final_score.set(score.get())

# Title
Label(win, text="Number Guessing Game", font=("Helvetica", 30, "bold"), bg="#f2f2f2", fg="#333").pack(pady=20)

# Input Field
Entry(win, textvariable=guess, width=3, font=('Helvetica', 50), justify='center', relief=GROOVE).place(relx=0.5, rely=0.3, anchor=CENTER)

# Hint Box
Label(win, textvariable=hint, width=50, font=('Helvetica', 16), bg="#ffe0b3", fg="#333", relief=GROOVE).place(relx=0.5, rely=0.6, anchor=CENTER)

# Score Display
Label(win, text="Score:", font=("Helvetica", 18), bg="#f2f2f2", fg="#333").place(relx=0.4, rely=0.8, anchor=CENTER)
Label(win, textvariable=final_score, font=("Helvetica", 24, "bold"), bg="#f2f2f2", fg="#333").place(relx=0.5, rely=0.8, anchor=CENTER)

# Buttons
Button(win, width=8, text='CHECK', font=('Helvetica', 18, 'bold'), command=fun, bg='#4CAF50', fg='white', relief=GROOVE).place(relx=0.4, rely=0.7, anchor=CENTER)
Button(win, width=8, text='RESET', font=('Helvetica', 18, 'bold'), command=reset_game, bg='#f44336', fg='white', relief=GROOVE).place(relx=0.6, rely=0.7, anchor=CENTER)

win.mainloop()
