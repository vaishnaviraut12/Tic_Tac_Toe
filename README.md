# Tic_Tac_Toe

# Tic-Tac-Toe Game
Welcome to the Tic-Tac-Toe game! This is a simple implementation of the classic 3x3 grid game where two players take turns placing their respective marks (`X` or `O`) on the grid until one player wins or the game ends in a draw.

## Features
- **Grid System**: The game board is represented as a 3x3 grid.
- **Turn-Based Gameplay**: Two players alternate turns to place their marks (`X` or `O`).
- **Win Conditions**: The game checks for a win (horizontal, vertical, or diagonal) after every move.
- **Input Validation**: Players can only place their mark in an empty spot on the board.
- **Draw Detection**: The game checks for a draw if the board is full and no player has won.
- **Dynamic Player Switching**: The game alternates between Player X and Player O after each valid move.

## How to Play
1. **Start the Game**: When you run the program, Player X will be asked to make the first move.
2. **Make Moves**: Players take turns entering their move. You will be prompted to enter the row and column (from 0 to 2) where you want to place your mark.
   - Example input: `1 1` places your mark in the center of the board.
3. **Game Flow**: The game will continue until:
   - A player wins (three of their marks in a row, column, or diagonal).
   - The board is full and there is no winner (a draw).
4. **Game Outcome**: The winner is displayed when a player wins, or the game announces a draw when the board is full.

## Sample Gameplay:

```
Player X, enter row and column (0, 1, or 2) separated by space: 0 0

 |   |  
---------
 |   |  
---------
 |   |  

Player O, enter row and column (0, 1, or 2) separated by space: 1 1

X |   |  
---------
 | O |  
---------
 |   |  

Player X, enter row and column (0, 1, or 2) separated by space: 0 1

X | X |  
---------
 | O |  
---------
 |   |  

Player O, enter row and column (0, 1, or 2) separated by space: 2 0

X | X |  
---------
 | O |  
---------
O |   |  

Player X, enter row and column (0, 1, or 2) separated by space: 0 2

X | X | X
---------
 | O |  
---------
O |   |  

Player X wins!
```

## Game Board Layout:

The board is displayed as a 3x3 grid with the following format:

```
 |   |  
---------
 |   |  
---------
 |   |  
```

## How to Run

### Prerequisites

To run this game, you'll need Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

### Steps to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/tic-tac-toe.git
   ```

2. Navigate to the project folder:
   ```bash
   cd tic-tac-toe
   ```

3. Run the Python script:
   ```bash
   python tic_tac_toe.py
   ```

The game will start and you will be prompted to make your moves.

## Code Explanation
1. **Game Board**: The board is initialized as a 3x3 grid filled with empty spaces `' '`.
2. **Make Move**: Players can input their move as a row and column index (0, 1, or 2). If the selected cell is already occupied, the player will be asked to choose another cell.
3. **Win Check**: After every move, the game checks if the current player has won by checking all rows, columns, and diagonals.
4. **Draw Check**: If the board is full and no player has won, the game ends in a draw.
5. **Player Switching**: The game alternates between Player X and Player O.

### How to Use Symbols in Markdown

If you'd like to add more structure or improve the readability of the board, you could use **code blocks** with Markdown. For example, you can create a better-structured view of the board like this:

```markdown
Player X, enter row and column (0, 1, or 2) separated by space: 0 0

X |   |  
---------
  |   |  
---------
  |   |  

Player O, enter row and column (0, 1, or 2) separated by space: 1 1

X |   |  
---------
  | O |  
---------
  |   |  
```
