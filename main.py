import tkinter as tk
import random

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("600x600")
window.configure(bg="lightblue")

choices = ["rock", "paper", "scissors"]

player_choice = tk.StringVar()

title_label = tk.Label(
    window,
    text="Rock Paper Scissors",
    font=("Arial", 28, "bold"),
    bg="lightblue"
)
title_label.pack(pady=30)

instruction_label = tk.Label(
    window,
    text="Choose rock, paper, or scissors:",
    font=("Arial", 16),
    bg="lightblue"
)
instruction_label.pack(pady=10)

choice_entry = tk.Entry(
    window,
    textvariable=player_choice,
    font=("Arial", 16),
    width=20
)
choice_entry.pack(pady=10)

comp_pick = random.choice(choices)