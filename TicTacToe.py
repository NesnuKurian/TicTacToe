BOARD_SIZE = 9

def print_board(board):
    for i in range(0, BOARD_SIZE, 3):
        print("|" + "|".join(board[i:i+3]) + "|")

def check_win(board):
    # Check rows, columns, and diagonals for a win
    for i in range(0, BOARD_SIZE, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] in ["X", "O"]:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] in ["X", "O"]:
            return True
    if ((board[0] == board[4] == board[8] or board[2] == board[4] == board[6])
        and (board[4] in ["X", "O"])):
        return True
    return False

def input_data():
    result = "y"
    player_symbols = {"X", "O"}
    while result == "y":
        board = [str(i) for i in range(BOARD_SIZE)]
        turn = "X"
        print("We have two symbols - X and O. We'll start with X")
        while True:
            print_board(board)
            print(f"Player {turn}, enter the desired location (0-{BOARD_SIZE-1}): ")
            try:
                location = int(input())
            except ValueError:
                print("Invalid entry. Please enter a number.")
                continue
            if 0 <= location < BOARD_SIZE and board[location] not in player_symbols:
                board[location] = turn
                if check_win(board):
                    result = input(f"Player {turn} won! Do you want to continue playing? (y/n): ")
                    break
                elif all(cell in player_symbols for cell in board):
                    result = input("Board filled completely. Do you want to start over? (y/n): ")
                    break
                turn = "O" if turn == "X" else "X"
            else:
                print("Invalid position. Please choose an available position.")

        if result.lower() != 'y':
            break

if __name__ == "__main__":
    input_data()
