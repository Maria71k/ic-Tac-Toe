def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)
        row = int(input(f"Player {player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {player}, enter column (0, 1, 2): "))

        if board[row][col] != " ":
            print("This position is already taken. Try again.")
            continue

        board[row][col] = player
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Congratulations! Player {player} wins!")
            break

        player = "O" if player == "X" else "X"

        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    tic_tac_toe()
