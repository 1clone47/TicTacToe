def set_token():
    print("Do you play as 'X' or 'O'?")
    choose_token = input("Enter: ")
    if choose_token.lower() == "x":
        return "X"
    elif choose_token.lower() == "o":
        return "O"
    else:
        print("Please enter 'X' or 'O'!")
        set_token()


def set_computer_token(player_token):
    if player_token == "X":
        return "O"
    else:
        return "X"


ADMIN_PASSWORD = "admin"
PLAYER_TOKEN = set_token()
COMPUTER_TOKEN = set_computer_token(PLAYER_TOKEN)
EMPTY = ' '
FIELD = {'7': EMPTY, '8': EMPTY, '9': EMPTY,
         '4': EMPTY, '5': EMPTY, '6': EMPTY,
         '1': EMPTY, '2': EMPTY, '3': EMPTY}