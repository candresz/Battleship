# Battleship Game 🎯

A simplified version of the classic Battleship game implemented in Python. This is a terminal-based game where the player tries to find and sink all ships on a 10x10 grid.

## 🚀 Features

- Random ship placement  
- Interactive text-based interface  
- Real-time feedback (HIT/MISS)  
- Game-over detection  
- Clean and easy-to-read code structure  

## 📜 Game Rules

- The game board is a 10x10 grid, initially filled with `.` to represent water.  
- 5 ships (`S`) are placed randomly on the board (not visible to the player during the game).  
- On each turn:  
  - The player enters a **row** and **column** number (0–9).  
  - If they hit a ship, it’s marked as `X` and prints **HIT**.  
  - If they miss, the cell is marked as `O` and prints **MISS**.  
- The game continues until all ships are hit (`X`).  
- When all ships are hit, the final board is shown and **"GAME OVER!"** is printed.

## 🧠 How It Works (Algorithm Summary)

1. Initialize board: A 10x10 grid filled with `"."`  
2. Place ships: 5 ships are placed at unique random positions  
3. Main loop:  
   - Display the board  
   - Prompt user input for row and column  
   - Evaluate hit or miss  
   - Repeat until all ships are found  
4. End game: Show final board and print `"GAME OVER!"`

## 📁 Files

- `project_02.py`: The main Python script that runs the game
- 
## ▶️ How to Run

Make sure you have Python installed, then run:

```bash
python project_02.py

...

📌 Requirements
Python 3.x

Standard library (random, sys)

🧑‍💻 Author
Carlos Zarate
GitHub: @candresz
