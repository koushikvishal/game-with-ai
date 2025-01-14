import random

# Constants for the players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to print the current board
def print_board(board):
    for row in range(3):
        print(' | '.join(board[row]))
        if row < 2:
            print('-' * 5)
    print()

# Function to check for a winner
def check_winner(board):
    # Check rows, columns, and diagonals
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None

# Function to check if the game is a draw
def check_draw(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                return False
    return True

# Minimax algorithm to find the best move for AI
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == PLAYER_X:
        return -10 + depth  # If X wins, AI loses
    elif winner == PLAYER_O:
        return 10 - depth  # If O wins, AI wins
    elif check_draw(board):
        return 0  # Draw

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_O
                    score = minimax(board, depth + 1, False)
                    board[row][col] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_X
                    score = minimax(board, depth + 1, True)
                    board[row][col] = EMPTY
                    best_score = min(score, best_score)
        return best_score

# Function to get the best move for the AI
def get_best_move(board):
    best_score = float('-inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_O
                score = minimax(board, 0, False)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

# Function to play the game
def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human (Player X) move
        row, col = map(int, input("Enter your move (row col): ").split())
        if board[row][col] != EMPTY:
            print("Invalid move, try again.")
            continue
        board[row][col] = PLAYER_X
        print_board(board)
        
        # Check if Player X wins
        if check_winner(board) == PLAYER_X:
            print("Player X wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break
        
        # AI (Player O) move
        print("AI is making its move...")
        ai_move = get_best_move(board)
        board[ai_move[0]][ai_move[1]] = PLAYER_O
        print_board(board)
        
        # Check if AI wins
        if check_winner(board) == PLAYER_O:
            print("Player O (AI) wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()