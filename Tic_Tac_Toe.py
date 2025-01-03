# Tic-Tac-Toe Game in Python

# Function to print the game board
def print_board(board):
    """
    Function to print the current state of the game board.
    """
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

# Function to check if a player has won
def check_win(board, player):
    """
    Function to check if the given player has won.
    It checks rows, columns, and diagonals.
    """
    # Check rows for a win
    for row in board:
        if all([cell == player for cell in row]):
            return True
    
    # Check columns for a win
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check the diagonal (top-left to bottom-right)
    if all([board[i][i] == player for i in range(3)]):
        return True

    # Check the anti-diagonal (top-right to bottom-left)
    if all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

# Function to check if the board is full
def board_full(board):
    """
    Function to check if the board is full (no empty spaces).
    """
    for row in board:
        if " " in row:
            return False
    return True

# Main function to play the game
def play_game():
    """
    Main function that controls the flow of the game.
    It alternates turns between player X and player O.
    """
    # Initialize the game board with empty spaces
    board = [[" " for _ in range(3)] for _ in range(3)]  # 3x3 board
    current_player = "X"  # Player X always starts
    
    while True:
        # Print the current state of the board
        print_board(board)
        
        # Ask the current player for their move
        print(f"Player {current_player}'s turn:")
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            
            # Check if the move is valid (within bounds and on an empty spot)
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid position. Please choose between 0 and 2 for row and column.")
                continue
            if board[row][col] != " ":
                print("Cell already occupied. Choose another cell.")
                continue

            # Place the current player's symbol on the board
            board[row][col] = current_player
            
            # Check if the current player has won
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            
            # Check if the board is full (draw condition)
            if board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            
            # Switch player for the next turn
            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Invalid input. Please enter integers for row and column.")
            continue

# Start the game when the script is executed
if __name__ == "__main__":
    play_game()
