import tkinter as tk
import random

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("600x600")
window.resizable(False, False)

choices = ["Rock", "Paper", "Scissors"]

player_choice = tk.StringVar()

player_score = 0
computer_score = 0


def play():
    global player_score, computer_score

    player = player_choice.get()
    computer = random.choice(choices)

    if player == "":
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Choose Rock, Paper or Scissors")
        return

    if player == computer:
        result = "Draw!"

    elif (
        (player == "Rock" and computer == "Scissors")
        or
        (player == "Paper" and computer == "Rock")
        or
        (player == "Scissors" and computer == "Paper")
    ):
        result = "You win!"
        player_score += 1

    else:
        result = "Computer wins!"
        computer_score += 1

    result_entry.delete(0, tk.END)
    result_entry.insert(
        0,
        f"You: {player} | Computer: {computer} | {result}"
    )

    score_label.config(
        text=f"Player: {player_score}    |    Computer: {computer_score}"
    )


def Reset():
    global player_score, computer_score

    player_score = 0
    computer_score = 0

    player_choice.set("")

    result_entry.delete(0, tk.END)
    result_entry.insert(0, "Choose Rock, Paper or Scissors")

    score_label.config(
        text="Player: 0    |    Computer: 0"
    )


def Exit():
    window.destroy()


title_label = tk.Label(
    window,
    text="Rock Paper Scissors",
    font=("Arial", 28, "bold")
)
title_label.pack(pady=30)

instruction_label = tk.Label(
    window,
    text="Choose Rock, Paper or Scissors",
    font=("Arial", 16)
)
instruction_label.pack(pady=20)

rock_button = tk.Radiobutton(
    window,
    text="Rock",
    variable=player_choice,
    value="Rock",
    font=("Arial", 14)
)
rock_button.pack(pady=5)

paper_button = tk.Radiobutton(
    window,
    text="Paper",
    variable=player_choice,
    value="Paper",
    font=("Arial", 14)
)
paper_button.pack(pady=5)

scissors_button = tk.Radiobutton(
    window,
    text="Scissors",
    variable=player_choice,
    value="Scissors",
    font=("Arial", 14)
)
scissors_button.pack(pady=5)

result_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=50,
    justify="center"
)
result_entry.pack(pady=15)

result_entry.insert(
    0,
    "Choose Rock, Paper or Scissors"
)

play_button = tk.Button(
    window,
    text="PLAY",
    font=("Arial", 16, "bold"),
    width=15,
    command=play
)
play_button.pack(pady=10)

reset_button = tk.Button(
    window,
    text="RESET",
    font=("Arial", 14),
    width=15,
    command=Reset
)
reset_button.pack(pady=5)

exit_button = tk.Button(
    window,
    text="EXIT",
    font=("Arial", 14),
    width=15,
    command=Exit
)
exit_button.pack(pady=5)

score_label = tk.Label(
    window,
    text="Player: 0    |    Computer: 0",
    font=("Arial", 14, "bold")
)
score_label.pack(pady=10)

window.mainloop()