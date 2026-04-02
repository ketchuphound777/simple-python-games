# --- Tic Tac Toe Game ---

# The game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Game control variables
game_still_going = True
winner = None
current_player = "X"


# --- Display the board ---
def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


# --- Main game function ---
def play_game():
    display_board()

    # Loop until game ends
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    # When loop ends, announce result
    if winner:
        print(f"{winner} wins! 🎉")
    else:
        print("It's a tie! 🤝")


# --- Handle a player turn ---
def handle_turn(player):
    print(f"{player}'s turn.")
    valid = False

    while not valid:
        position = input("Choose a position from 1-9: ")

        if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Invalid input. Pick a number between 1 and 9.")
            continue

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("That spot is taken. Try again.")

    board[position] = player
    display_board()


# --- Check if the game is over ---
def check_if_game_over():
    check_for_winner()
    check_for_tie()


# --- Check for winner ---
def check_for_winner():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    global game_still_going
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return None


def check_columns():
    global game_still_going
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        game_still_going = False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return None


def check_diagonals():
    global game_still_going
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"
    if diag1 or diag2:
        game_still_going = False
    if diag1:
        return board[0]
    elif diag2:
        return board[2]
    return None


# --- Check for a tie ---
def check_for_tie():
    global game_still_going
    if "-" not in board and winner is None:
        game_still_going = False


# --- Flip player ---
def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


# --- Start the game ---
play_game()
