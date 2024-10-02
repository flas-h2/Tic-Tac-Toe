import random
import time

# Tech Stuff


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class spaces:
    X_SPACE = bcolors.OKCYAN + bcolors.BOLD + \
        bcolors.UNDERLINE + "X" + bcolors.ENDC
    O_SPACE = bcolors.FAIL + bcolors.BOLD + bcolors.UNDERLINE + "O" + bcolors.ENDC


def typetext(str, end="\n"):
    for character in str:
        time.sleep(.05)
        print(character, end="", flush=True)
    print(end, end="")


def get_valid_response(prompt, valid_response):

    while True:
        typetext(prompt)
        response = input().lower().strip()
        if response not in valid_response:
            print("Not valid")
        else:
            break

    return valid_response.index(response)


def restart():
    while True:
        response = str(
            input("Do you want to play again? [Yes/No]\n")).lower().strip()
        if response == "yes":
            play_game()
            break
        elif response == "no":
            exit()
        else:
            print("Not valid response. Try again!")


# Game


# Create and return a new list representing the board with indices 0 to 8.


def initialize_board():
    num_index = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return num_index

# Display the current state of the board, showing 'X' or 'O' in place of the numbers.


def print_board(board):
    one, two, three, four, five, six, seven, eight, nine = board
    print(f"""{one} | {two} | {
          three}\n---------\n{four} | {five} | {six}\n---------\n{seven} | {eight} | {nine}""")


# Place the player's symbol ('X' or 'O') at the specified index on the board.
def make_move(board, index, player):
    board[index] = player
    print_board(board)


# Determine if there is a winner. Return the winning symbol ('X' or 'O') or None if there is no winner yet.


def check_winner(board):
    if board[0] == spaces.X_SPACE and board[1] == spaces.X_SPACE and board[2] == spaces.X_SPACE:
        return [True, "Player"]
    elif board[3] == spaces.X_SPACE and board[4] == spaces.X_SPACE and board[5] == spaces.X_SPACE:
        return [True, "Player"]
    elif board[6] == spaces.X_SPACE and board[7] == spaces.X_SPACE and board[8] == spaces.X_SPACE:
        return [True, "Player"]
    elif board[0] == spaces.X_SPACE and board[3] == spaces.X_SPACE and board[6] == spaces.X_SPACE:
        return [True, "Player"]
    elif board[1] == spaces.X_SPACE and board[4] == spaces.X_SPACE and board[7] == spaces.X_SPACE:
        return [True, "Player"]
    elif board[2] == spaces.X_SPACE and board[5] == spaces.X_SPACE and board[8] == spaces.X_SPACE:
        return [True, "Player"]
    elif board[0] == spaces.X_SPACE and board[4] == spaces.X_SPACE and board[8] == spaces.X_SPACE:
        return [True, "Player"]
    elif board[2] == spaces.X_SPACE and board[4] == spaces.X_SPACE and board[6] == spaces.X_SPACE:
        return [True, "Player"]
    elif board[0] == spaces.O_SPACE and board[1] == spaces.O_SPACE and board[2] == spaces.O_SPACE:
        return [True, "Computer"]
    elif board[3] == spaces.O_SPACE and board[4] == spaces.O_SPACE and board[5] == spaces.O_SPACE:
        return [True, "Computer"]
    elif board[6] == spaces.O_SPACE and board[7] == spaces.O_SPACE and board[8] == spaces.O_SPACE:
        return [True, "Computer"]
    elif board[0] == spaces.O_SPACE and board[3] == spaces.O_SPACE and board[6] == spaces.O_SPACE:
        return [True, "Computer"]
    elif board[1] == spaces.O_SPACE and board[4] == spaces.O_SPACE and board[7] == spaces.O_SPACE:
        return [True, "Computer"]
    elif board[2] == spaces.O_SPACE and board[5] == spaces.O_SPACE and board[8] == spaces.O_SPACE:
        return [True, "Computer"]
    elif board[0] == spaces.O_SPACE and board[4] == spaces.O_SPACE and board[8] == spaces.O_SPACE:
        return [True, "Computer"]
    elif board[2] == spaces.O_SPACE and board[4] == spaces.O_SPACE and board[6] == spaces.O_SPACE:
        return [True, "Computer"]
    else:
        return False


# Determine if the game is a draw (i.e., the board is full and there is no winner).


def check_draw(board):
    if check_winner(board) != [True, "Player"] and check_winner(board) != [True, "Computer"] and "1" not in board and "2" not in board and "3" not in board and "4" not in board and "5" not in board and "6" not in board and "7" not in board and "8" not in board and "9" not in board:
        print("There was a draw")
        restart()
        return True
    else:
        return False

# Handle the move of the human player, including input validation.


def player_move(board):
    player_input = get_valid_response("Input a number 1-9: ", board)

    return player_input

    # board[player_input] = spaces.X_SPACE

# Handle the move of the computer, using a basic strategy like random moves.


def computer_move(board):
    move_by_comp = ""
    while True:
        move_by_comp = random.randint(0, 8)
        move_by_comp = str(move_by_comp)
        check_winner(board)
        check_draw(board)
        if move_by_comp in board:
            print(f"Computer plays at: {move_by_comp}")
            return board.index(move_by_comp)
        # elif "1" not in board and "2" not in board and "3" not in board and "4" not in board and "5" not in board and "6" not in board and "7" not in board and "8" not in board and "9" not in board:


# Manage the game loop, alternating between the player and computer, checking for a win or draw, and announcing the result.


def play_game():
    board = initialize_board()
    print_board(board)
    while check_winner(board) == False and check_draw(board) == False:
        move = player_move(board)
        make_move(board, move, spaces.X_SPACE)
        if check_winner(board) or check_draw(board):
            break
        move_computer = computer_move(board)
        make_move(board, move_computer, spaces.O_SPACE)

    if check_winner(board) == [True, "Player"]:
        print("Player won!")
        restart()
    elif check_winner(board) == [True, "Computer"]:
        print("Computer won!")
        restart()
    else:
        print("It was a draw")
        restart()


if __name__ == '__main__':
    play_game()
