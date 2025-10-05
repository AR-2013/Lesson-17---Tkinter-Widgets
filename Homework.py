import tkinter as tk
import random

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("300x250")

choices = ["Rock", "Paper", "Scissors"]

def play(player_choice):
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"You: {player_choice}\nComputer: {computer_choice}\n{result}")

rock_btn = tk.Button(window, text="Rock", width=10, command=lambda: play("Rock"))
paper_btn = tk.Button(window, text="Paper", width=10, command=lambda: play("Rock"))
scissors_btn = tk.Button(window, text="Scissors", width=10, command=lambda: play("Rock"))

rock_btn.pack()
paper_btn.pack()
scissors_btn.pack()

result_label = tk.Label(window, text="")
result_label.pack(pady=20)

window.mainloop()
