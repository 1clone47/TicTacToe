# A game TicTac Toe
# Author: Iclone47
# Version: 0.0.7
# Release: 27.06.2022
# Updated: 09.07.2022

import random

field_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def create_table(dict):
    print(dict[7] + " | " + dict[8] + " | " + dict[9])
    print(f"---------")
    print(dict[4] + " | " + dict[5] + " | " + dict[6])
    print(f"---------")
    print(dict[1] + " | " + dict[2] + " | " + dict[3])


def get_user_input():
    while True:
        user_move = input("Please Select the Field: ")
        if user_move in field_numbers:
            return user_move
        else:
            print("Please enter a Number from 1 to 9...")


def computer_move(dict):
    computer = True
    while computer:
        move = random.randint(1, 9)
        if dict[move] == "":
            return move


def block_user(field):
    computer = True
    while computer:
        player_1 = "X"
        if field[1] == player_1 and field[2] == player_1:
            return 3
        elif field[1] == player_1 and field[7] == player_1:
            return 4
        elif field[1] == player_1 and field[4] == player_1:
            return 7
        elif field[1] == player_1 and field[3] == player_1:
            return 2
        elif field[1] == player_1 and field[5] == player_1:
            return 9
        elif field[1] == player_1 and field[9] == player_1:
            return 5

        elif field[2] == player_1 and field[1] == player_1:
            return 3
        elif field[2] == player_1 and field[3] == player_1:
            return 1
        elif field[2] == player_1 and field[8] == player_1:
            return 5
        elif field[2] == player_1 and field[5] == player_1:
            return 8

        elif field[3] == player_1 and field[1] == player_1:
            return 2
        elif field[3] == player_1 and field[2] == player_1:
            return 1
        elif field[3] == player_1 and field[9] == player_1:
            return 6
        elif field[3] == player_1 and field[6] == player_1:
            return 9
        elif field[3] == player_1 and field[5] == player_1:
            return 7
        elif field[3] == player_1 and field[7] == player_1:
            return 5

        elif field[4] == player_1 and field[1] == player_1:
            return 7
        elif field[4] == player_1 and field[7] == player_1:
            return 1
        elif field[4] == player_1 and field[6] == player_1:
            return 5
        elif field[4] == player_1 and field[5] == player_1:
            return 6

        elif field[5] == player_1 and field[1] == player_1:
            return 9
        elif field[5] == player_1 and field[4] == player_1:
            return 6
        elif field[5] == player_1 and field[7] == player_1:
            return 3
        elif field[5] == player_1 and field[2] == player_1:
            return 8
        elif field[5] == player_1 and field[8] == player_1:
            return 2
        elif field[5] == player_1 and field[3] == player_1:
            return 7
        elif field[5] == player_1 and field[6] == player_1:
            return 4
        elif field[5] == player_1 and field[9] == player_1:
            return 1

        elif field[6] == player_1 and field[3] == player_1:
            return 9
        elif field[6] == player_1 and field[9] == player_1:
            return 3
        elif field[6] == player_1 and field[5] == player_1:
            return 4
        elif field[6] == player_1 and field[4] == player_1:
            return 5

        elif field[7] == player_1 and field[8] == player_1:
            return 9
        elif field[7] == player_1 and field[9] == player_1:
            return 8
        elif field[7] == player_1 and field[5] == player_1:
            return 3
        elif field[7] == player_1 and field[3] == player_1:
            return 5
        elif field[7] == player_1 and field[4] == player_1:
            return 1
        elif field[7] == player_1 and field[1] == player_1:
            return 4

        elif field[8] == player_1 and field[7] == player_1:
            return 9
        elif field[8] == player_1 and field[9] == player_1:
            return 7
        elif field[8] == player_1 and field[5] == player_1:
            return 2
        elif field[8] == player_1 and field[2] == player_1:
            return 5

        elif field[9] == player_1 and field[7] == player_1:
            return 8
        elif field[9] == player_1 and field[8] == player_1:
            return 7
        elif field[9] == player_1 and field[6] == player_1:
            return 3
        elif field[9] == player_1 and field[3] == player_1:
            return 6
        elif field[9] == player_1 and field[5] == player_1:
            return 1
        elif field[9] == player_1 and field[1] == player_1:
            return 5
        else:
            move = random.randint(1, 9)
            if field[move] == "":
                return move


def check_for_win(dict, moves):
    player_1 = "X"
    player_2 = "O"
    if moves >= 10:
        print("Tie! Nobody has won")
    elif dict[7] == player_1 and dict[4] == player_1 and dict[1] == player_1:
        print(f"{player_1} has won! Congrats")
        return False
    elif dict[8] == player_1 and dict[5] == player_1 and dict[2] == player_1:
        print(f"{player_1} has won! Congrats")
        return False
    elif dict[9] == player_1 and dict[6] == player_1 and dict[3] == player_1:
        print(f"{player_1} has won! Congrats")
        return False
    elif dict[9] == player_1 and dict[8] == player_1 and dict[7] == player_1:
        print(f"{player_1} has won! Congrats")
        return False
    elif dict[6] == player_1 and dict[5] == player_1 and dict[4] == player_1:
        print(f"{player_1} has won! Congrats")
        return False
    elif dict[1] == player_1 and dict[2] == player_1 and dict[3] == player_1:
        print(f"{player_1} has won! Congrats")
        return False
    elif dict[1] == player_1 and dict[5] == player_1 and dict[9] == player_1:
        print(f"{player_1} has won! Congrats")
        return False
    elif dict[7] == player_1 and dict[5] == player_1 and dict[3] == player_1:
        print(f"{player_1} has won! Congrats")
        return False

    elif dict[7] == player_2 and dict[4] == player_2 and dict[1] == player_2:
        print(f"{player_2} has won! Congrats")
        return False
    elif dict[8] == player_2 and dict[5] == player_2 and dict[2] == player_2:
        print(f"{player_2} has won! Congrats")
        return False
    elif dict[9] == player_2 and dict[6] == player_2 and dict[3] == player_2:
        print(f"{player_2} has won! Congrats")
        return False
    elif dict[9] == player_2 and dict[8] == player_2 and dict[7] == player_2:
        print(f"{player_2} has won! Congrats")
        return False
    elif dict[6] == player_2 and dict[5] == player_2 and dict[4] == player_2:
        print(f"{player_2} has won! Congrats")
        return False
    elif dict[1] == player_2 and dict[2] == player_2 and dict[3] == player_2:
        print(f"{player_2} has won! Congrats")
        return False
    elif dict[1] == player_2 and dict[5] == player_2 and dict[9] == player_2:
        print(f"{player_2} has won! Congrats")
        return False
    elif dict[7] == player_2 and dict[5] == player_2 and dict[3] == player_2:
        print(f"{player_2} has won! Congrats")
        return False
    else:
        return True


def write_log(player, move):
    if player == 2:
        with open("log.txt", "a") as log:
            log.write(f"--> Computer has picked {move}... \n")
    else:
        with open("log.txt", "a") as log:
            log.write(f"--> Player {player} has picked {move}... \n")


def create_header(move):
    with open("log.txt", "a") as log:
        log.write("\n\n >>> NEW-GAME <<< \n")


def clear_logs():
    progress = True
    while progress:
        confirm_deletion = input("Are you sure you want to delete the logs? no [n] yes [y]: ")
        if confirm_deletion.lower() == "y":
            with open("log.txt", "w") as log:
                pass
            print("The Logs have been deleted...")
            return
        elif confirm_deletion.lower() == "n":
            print("Progress has been stopped...")
            return
        else:
            print("Please enter either [n] for no or [y] for yes...")


def log_moves(moves):
    with open("log.txt", "a") as log:
        log.write(f"\n--> Moves needed: {moves} \n")


def game():
    moves = 0
    player = 1
    table = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
    if moves <= 0:
        create_table(table)
        create_header(moves)
    while check_for_win(table, moves):
        if player == 1:
            user_move = get_user_input()
            if user_move.lower() == "clear":
                clear_logs(user_move)
            else:
                if table[int(user_move)] == "":
                    if player == 1:
                        table[int(user_move)] = "X"
                        write_log(player, user_move)
                        player = 2
                        moves += 1
        elif player == 2:
            com_move = block_user(table)
            table[com_move] = "O"
            write_log(player, com_move)
            player = 1
            moves += 1
            print(f"Computer picks {com_move}...")
        else:
            print("This Field has already been selected...")
        create_table(table)
    log_moves(moves)


while True:
    ask_for_start = input("Press [n] to start a new Game: ")
    if ask_for_start.lower() == "n":
        game()
    elif ask_for_start.lower() == "clear":
        clear_logs()
    else:
        print("Please press the [n]-Button to start the new Game...")