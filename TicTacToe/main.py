import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Game Logic Functions
# -------------------------------

def check_winner():
    """Check all winning combinations and highlight the winner."""
    global winner
    winning_combos = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7],
    ]
    for combo in winning_combos:
        if (
            buttons[combo[0] - 1]["text"]
            == buttons[combo[1] - 1]["text"]
            == buttons[combo[2] - 1]["text"]
            != ""
        ):
            for i in combo:
                buttons[i - 1].config(bg="lightgreen")
            messagebox.showinfo("Tic Tac Toe", f"Player {buttons[combo[0] - 1]['text']} wins!")
            winner = True
            return

def toggle_player():
    """Switch current player between X and O."""
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s Turn")

# -------------------------------
# UI Interaction Functions
# -------------------------------

def button_click(index):
    """Handle player move when a button is clicked."""
    global winner
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

def restart_game():
    """Reset the game board and start again."""
    global winner, current_player
    for btn in buttons:
        btn.config(text="", bg="SystemButtonFace")
    current_player = "X"
    winner = False
    label.config(text=f"Player {current_player}'s Turn")

# -------------------------------
# UI Setup
# -------------------------------

root = tk.Tk()
root.title("Tic-Tac-Toe")

current_player = "X"
winner = False

# Label at top
label = tk.Label(root, text=f"Player {current_player}'s Turn", font=("normal", 16))
label.grid(row=0, column=0, columnspan=3, pady=5)

# Buttons (Game Board)
buttons = [
    tk.Button(root, text="", font=("normal", 25), width=6, height=2,
              command=lambda i=i: button_click(i))
    for i in range(9)
]

for i, button in enumerate(buttons):
    button.grid(row=(i // 3) + 1, column=i % 3)

# Restart Button
restart_btn = tk.Button(root, text="Restart Game", font=("normal", 12),
                        command=restart_game, bg="#ddd")
restart_btn.grid(row=4, column=0, columnspan=3, pady=10)

# -------------------------------
# Main Loop
# -------------------------------
root.mainloop()
