
# ----------------GLOBAL VARIABLES-------------------------------------
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]

game_still_going = True

winner = None

player = "X"

computer = "O"

# ---------------------------------------------------------------------

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# ---------------------------------------------------------------------

def insert_letter(letter, position): # x, 0
    board[position] = letter
    if letter == computer:
        display_board()
        

    if game_still_going == True:
        check_win()
        check_tie()

    if check_tie():
        print("Tie!")
        exit()
    elif winner == "X":
        print("Player wins!")
    elif winner == "O":
        print("Computer wins!")
    return

# ----------------------------------------------------------------------

def check_win(): # returns  winner | changes  game_still_going
    global winner
    global game_still_going

    row_winner = check_row()
    column_winner = check_column()
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
        game_still_going = False
    elif column_winner:
        winner = column_winner
        game_still_going = False
    elif diagonal_winner:
        winner = diagonal_winner
        game_still_going = False
    else:
        winner = None
    return

def check_row():
    global game_still_going
    
    if board[0] == board[1] == board[2] != "-":
        game_still_going = False
        return board[0]
    elif board[3] == board[4] == board[5] != "-":
        game_still_going = False
        return board[3]
    elif board[6] == board[7] == board[8] != "-":
        game_still_going = False
        return board[6]
    return

def check_column():
    global game_still_going
    
    if board[0] == board[3] == board[6] != "-":
        game_still_going = False
        return board[0]
    elif board[1] == board[4] == board[7] != "-":
        game_still_going = False
        return board[1]
    elif board[2] == board[5] == board[6] != "-":
        game_still_going = False
        return board[2]
    return

def check_diagonal():
    global game_still_going
    
    if board[0] == board[4] == board[8] != "-":
        game_still_going = False
        return board[0]
    elif board[2] == board[4] == board[6] != "-":
        game_still_going = False
        return board[2]
    return

def check_tie():
    if "-" in board:
        return False # not a tie because "-" in board
    return True # tie because "-" in board

# ----------------------------------------------------------------------

# To check which symbol won from minimaxing (use "symbol" instead of "letter" since "letter" already used)

def check_if_symbol_win(symbol):
    if board[0] == board[1] == board[2] == symbol:
        return True
    elif board[3] == board[4] == board[5] == symbol:
        return True
    elif board[6] == board[7] == board[8] == symbol:
        return True
    elif board[0] == board[3] == board[6] == symbol:
        return True
    elif board[1] == board[4] == board[7] == symbol:
        return True
    elif board[2] == board[5] == board[8] == symbol:
        return True
    elif board[2] == board[4] == board[6] == symbol:
        return True
    elif board[0] == board[4] == board[8] == symbol:
        return True
    else:
        return False

# ----------------------------------------------------------------------

def player_move():
    if game_still_going == False:
        exit()
    while True: # checks if valid input else asks for new input
        try:
            position = int(input("Choose position for X from 1-9: "))
            assert 1 <= position <= 9
            position -= 1
            assert board[position] == "-"
        except:
            print("Invalid input or Already taken\n")
            continue
        else:
            break
    insert_letter(player, position)

def comp_move():
    best_score = -1000
    best_move = 0

    for i, key in enumerate(board):
        if key == "-":
            board[i] = computer
            score = minimax(board, False)
            board[i] = "-"
            if score > best_score:
                best_score = score
                best_move = i
    
    insert_letter(computer, best_move)
    return

def minimax(board, is_maximizing):
    if check_if_symbol_win(computer):   # these three check if the current node has a winner or tie from board being full
        return 1
    elif check_if_symbol_win(player):
        return -1
    elif check_tie():
        return 0        # if no winner/tie then continue with if statements below
    
    if is_maximizing:
        best_score = -1000
        for i, key in enumerate(board):
            if key == "-":
                board[i] = computer
                score = minimax(board, False)
                board[i] = "-"
                if score > best_score:
                    best_score = score
        return best_score

    else:
        best_score = 1000
        for i, key in enumerate(board):
            if key == "-":
                board[i] = player
                score = minimax(board, True)
                board[i] = "-"
                if score < best_score:
                    best_score = score
        return best_score


# ----------------------------------------------------------------------

if __name__ == '__main__':
    while game_still_going == True:
        player_move()
        comp_move()
