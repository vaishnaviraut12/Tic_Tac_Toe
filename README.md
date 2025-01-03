# Tic_Tac_Toe

```markdown
# 🎮 Tic-Tac-Toe Game in Python  

A simple and interactive **Tic-Tac-Toe** game implemented in Python. This game allows two players to compete against each other, taking turns to place their symbols (X or O) on a 3x3 grid.  

---

## ✨ Features  
- 🌀 **Interactive Gameplay**: Players take turns entering their moves.  
- 🔄 **Dynamic Board Display**: The game board updates after every move.  
- 🎯 **Win and Draw Detection**:  
  - Players win by aligning three symbols in a row, column, or diagonal.  
  - The game ends in a draw if the board is full and no player has won.  
- 🚫 **Validation**: Prevents invalid moves (e.g., placing a symbol in an occupied cell).  

## 🎮 How to Play  
1. **Start the Game**:  
   Run the script to begin.  

   ```bash  
   python tic_tac_toe.py  
   ```  
2. **Input Moves**:  
   Players take turns entering the row and column numbers (0, 1, or 2) where they want to place their symbol.  
3. **Game End**:  
   - The game announces the winner if a player aligns three symbols.  
   - The game ends in a draw if all cells are occupied and no one wins.  
4. **Restart**:  
   To play again, restart the script.  

## 📋 Features Overview  
- 🎴 **Dynamic Game Board**: A clear representation of the current state of the game.  
- 🎯 **Win Detection**: Checks rows, columns, and diagonals for a winning line.  
- 🚫 **Input Validation**: Ensures valid moves within the board's bounds and empty cells.  
- 🛡️ **Draw Detection**: Declares a draw if no moves are possible.  

## 🚀 Future Enhancements  
- 🖥️ **Graphical Interface**: Build a GUI using libraries like `tkinter` or `PyGame`.  
- 🤖 **AI Opponent**: Add an option to play against the computer using AI algorithms.  
- 🌐 **Online Multiplayer**: Enable online gameplay using sockets or APIs.  

## Sample Gameplay  
```plaintext  
Player X's turn:  
Enter row (0-2): 0  
Enter column (0-2): 1  

 | X |   
-----  
  |   |   
-----  
  |   |   

Player O's turn:  
Enter row (0-2): 1  
Enter column (0-2): 1  

 | X |   
-----  
  | O |   
-----  
  |   |   
```  

---

