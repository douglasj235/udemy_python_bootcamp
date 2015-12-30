__author__ = 'Jerry'
# Global variables
board = [' '] * 10
game_state = True
announce = ''

def reset_board():
    global board, game_state
    board = [' '] * 10
    game_state = True

def display_board():
    print " "+board[7]+" |"+board[8]+" |"+board[9]+" "
    print "------------"
    print " "+board[4]+" |"+board[5]+" |"+board[6]+" "
    print "------------"
    print " "+board[1]+" |"+board[2]+" |"+board[3]+" "

# Find different ways player can win
def win_check(board, player):
    if (board[7]  == board[8] == board[9] == player) or \
        (board[4] == board[5] == board[6] == player) or \
        (board[1] == board[2] == board[3] == player) or \
        (board[7] == board[4] == board[1] == player) or \
        (board[8] == board[5] == board[2] == player) or \
        (board[9] == board[6] == board[3] == player) or \
        (board[7] == board[5] == board[3] == player) or \
        (board[9] == board[5] == board[1] == player):
        return True
    else:
        return False

# Check for full board
def full_board(board):
    if ' ' in board[1:]:
        return False
    else:
        return True

# Ask player where to place X or O mark, check validity of input
def ask_player(mark):
    global board
    req = 'Choose where to place your: '+ mark+'. Please input an integer between 1 - 9.'
    while True:
        try:
            choice = int(raw_input(req))
        except ValueError:
            print ("Sorry, please input an integer between 1-9.")
            continue

        if choice == 0 or choice > 9:
            print "Sorry, please select an integer between 1-9"
            continue

        if board[choice] == ' ':
            board[choice] = mark
            break
        else:
            print "That space isn't empty!"
            continue

def player_choice(mark):
    global board, game_state, announce
    announce = ''
    # Player input
    mark = str(mark)
    # Validate input
    ask_player(mark)

    display_board()

    # Check for tie
    if full_board(board):
        announce = "Players tie!"
        game_state = False

    # Check for player win
    if win_check(board,mark):
        announce = mark +" wins! Great Job"
        game_state = False


    return game_state, announce

def play_game():
    reset_board()
    global announce

    X = 'X'
    O = 'O'
    display_board()
    while True:
        # Player X turn
        player_choice(X)
        print announce
        if game_state == False:
            break

        # Player O turn
        player_choice(O)
        print announce
        if game_state == False:
            break

    # Ask if players want to continue
    rematch = raw_input('Would you like to play another game? y/n ')
    if rematch == 'y':
        play_game()
    else:
        print "Thanks for playing!"


play_game()