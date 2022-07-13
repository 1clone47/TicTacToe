import sys
import random

PASSWORD = "admin"
PLAYER_TOKEN = 'X'
COMPUTER_TOKEN = 'O'
EMPTY = ' '
field = {'7': EMPTY, '8': EMPTY, '9': EMPTY,
         '4': EMPTY, '5': EMPTY, '6': EMPTY,
         '1': EMPTY, '2': EMPTY, '3': EMPTY}


def playing_field(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def play():
    turn = PLAYER_TOKEN

    while True:
        available = possible_moves(field)
        playing_field(field)
        if not available:
            print(">>> Draw! <<<")
            with open("../log.txt", "a") as log:
                log.write(f"\n--> Draw!")
            return False
        if turn == PLAYER_TOKEN:
            print("It's your turn! " + turn + ". Please choose a field position: ")
        if turn == COMPUTER_TOKEN:
            move = computer_move(field)
        else:
            move = input()
            if input_check(move, turn):
                continue
        if field[move] == EMPTY:
            field[move] = turn
            print(f"--> Player {turn} has picked {move}...")
            with open("../log.txt", "a") as log:
                log.write(f"--> {turn} has picked {move}...\n")
        else:
            print("This field is already occupied.\nPlease choose another field.")
            continue
        if check_win(field):
            playing_field(field)
            print(f">>>> {turn} has won! <<<<")
            with open("../log.txt", "a") as log:
                log.write(f"\n--> {turn} has won! \n-->Moves needed: {move}")
            sys.exit(0)
        if turn == PLAYER_TOKEN:
            turn = COMPUTER_TOKEN
        else:
            turn = PLAYER_TOKEN


def check_win(board):
    if board['7'] == board['8'] == board['9'] != EMPTY:
        return True
    if board['4'] == board['5'] == board['6'] != EMPTY:
        return True
    if board['1'] == board['2'] == board['3'] != EMPTY:
        return True
    if board['1'] == board['5'] == board['9'] != EMPTY:
        return True
    if board['3'] == board['5'] == board['7'] != EMPTY:
        return True
    if board['7'] == board['4'] == board['1'] != EMPTY:
        return True
    if board['8'] == board['5'] == board['2'] != EMPTY:
        return True
    if board['9'] == board['6'] == board['3'] != EMPTY:
        return True
    return False


def possible_moves(board):
    return [k for k, v in board.items() if v == EMPTY]


def input_check(insert, turn):
    if insert.lower() == 'end':
        print(f"Game has been ended by Player {turn}")
        with open("../log.txt", "a") as log:
            log.write(f"\n--> Game has been ended by Player {turn}")
        sys.exit(0)
    elif insert.lower() == "clear":
        clear_logs()
    elif insert.lower() == "admin-login":
        admin = input("Bitte geben sie das Passwort ein: ")
        if admin == PASSWORD:
            print("$ Welcome Admin...")
    try:
        int(insert)
    except ValueError:
        print("Please enter a number!")
        return True
    if int(insert) < 1 or int(insert) > 9:
        print("Please enter a number from 1 to 9!")
        return True
    return False


def computer_move(board):
    copy_field = board.copy()
    # Kontrolle ob Computer eine Chance zum Siegen hat.
    for k, v in board.items():
        if v == EMPTY:
            copy_field[k] = COMPUTER_TOKEN
            if check_win(copy_field):
                move = k
                return move
            else:
                copy_field[k] = EMPTY
    # Bei keiner Chance zum Sieg, Rückgabe von zufällig generierter Zahl.
    return computer_defend(board)


def computer_defend(board):
    copy_field = board.copy()
    for k, v in board.items():
        if v == EMPTY:
            copy_field[k] = PLAYER_TOKEN
            if check_win(copy_field):
                move = k
                return move
            else:
                copy_field[k] = EMPTY
    return str(random.choice(possible_moves(board)))


def clear_logs():
    progress = True
    while progress:
        confirm_deletion = input("Are you sure you want to delete the logs? no [n] yes [y]: ")
        if confirm_deletion.lower() == "y":
            with open("../log.txt", "w") as log:
                pass
            print("The Logs have been deleted...")
            return
        elif confirm_deletion.lower() == "n":
            print("Progress has been stopped...")
            return
        else:
            print("Please enter either [n] for no or [y] for yes...")


while True:
    with open("../log.txt", "a") as log:
        log.write("\n\n >>> NEW-GAME <<< \n\n")
    play()
