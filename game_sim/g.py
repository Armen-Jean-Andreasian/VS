games = {}


def construct_table():
    num = 0
    while True:
        game = input("Enter a game name or type b\n")
        if game == "b":
            break
        else:
            games[game] = num


