from random import randint

#This is a simple game of battleship, played in console mode.
#In version 2.0 I'll implement standart 10x10 playboard and different
#types of ships.

#Initialization of a playboard
board = []
for x in range(10):
    board.append(["O"] * 10)

#Initialization of a ships
boats = []
barges = []
cruisers = []
manowar = []

Creating ships
def new_boat(boat):
    global boats
    coordinates = [randint(0, len(board) - 1), randint(0, len(board) - 1)]
    


#Global variables
game_is_running = True

#printing gameboard
def print_board(board):
    for row in board:
        print " ".join(row)

#Game start
print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print "Enemy ship coordinates:", ship_row, ship_col


while game_is_running:
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
        print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
        print "You guessed that one already."
    elif guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        game_is_running = False
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
    # Print (turn + 1) here!
    print_board(board)

