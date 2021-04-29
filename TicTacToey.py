import random
winning_combos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
potential_wins = {1:[[2,3], [4,7], [5,9]],
                  2:[[1,3], [5,8]],
                  3:[[1,2], [6,9], [5,7]],
                  4:[[5,6], [1,7]],
                  5:[[4,6], [2,8], [1,9], [3,7]],
                  6:[[4,5], [3,9]],
                  7:[[8,9], [1,4], [3,5]],
                  8:[[7,9], [2,5]],
                  9:[[7,8], [3,6], [1,5]]
                  }

print('''$$$$$$$$\ $$\                 $$$$$$$$\                        $$$$$$$$\                        
\__$$  __|\__|                \__$$  __|                       \__$$  __|                       
   $$ |   $$\  $$$$$$$\          $$ | $$$$$$\   $$$$$$$\          $$ | $$$$$$\   $$$$$$\        
   $$ |   $$ |$$  _____|         $$ | \____$$\ $$  _____|         $$ |$$  __$$\ $$  __$$\       
   $$ |   $$ |$$ /               $$ | $$$$$$$ |$$ /               $$ |$$ /  $$ |$$$$$$$$ |      
   $$ |   $$ |$$ |               $$ |$$  __$$ |$$ |               $$ |$$ |  $$ |$$   ____|      
   $$ |   $$ |\$$$$$$$\          $$ |\$$$$$$$ |\$$$$$$$\          $$ |\$$$$$$  |\$$$$$$$\       
   \__|   \__| \_______|         \__| \_______| \_______|         \__| \______/  \_______|      ''')
def take_turn(player, guesses_left, marker, x, o):
    if player == "AI":
        guess=ai_logic(guesses_left, x, o)
        print(guess)
        return guess
    if player == "hooman":
        valid= False
        while not valid:
            guess = int(input(f"Which square would {marker} like to take?\n"))
            if guess in guesses_left:
                return guess
            else:
                print("Oops! That square's already taken!")


def ai_logic(guesses_left, x, o):
    if 5 in guesses_left:
        return 5
    else:
        for keys in potential_wins:
            for values in potential_wins[keys]:
                potential_x = all(elem in x for elem in values)
                potential_o = all(elem in o for elem in values)
                if potential_x or potential_o:
                    if keys in guesses_left:
                        return keys
                    else:
                        return random.choice(guesses_left)
        return random.choice(guesses_left)


def player_select():
    players = int(input("1 or 2 players?\n"))
    if players == 2:
        return 2
    elif players == 1:
        player = input("Do you want X or O?\n").lower()
        if player == "x":
            return 1
        if player == "o":
            return 0
        else:
            print("Sorry, that wasn't a valid choice. Try again!")
            player_select()

def play_game():
    valid_guesses = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x_player = "hooman"
    o_player = "hooman"
    x = []
    o = []
    game_is_over = False
    game_key = '''       |   |   
     1 | 2 | 3 
    ___|___|___
       |   |
     4 | 5 | 6 
    ___|___|___
       |   |
     7 | 8 | 9 
       |   |'''
    active_game_board = '''       |   |   
     1 | 2 | 3 
    ___|___|___
       |   |
     4 | 5 | 6 
    ___|___|___
       |   |
     7 | 8 | 9 
       |   |'''

    markers = ["X", "O"]
    state = player_select()
    if state == 1:
        o_player = "AI"
    elif state == 0:
        x_player = "AI"
    print(game_key)
    while not game_is_over:
        for marker in markers:
            if not valid_guesses:
                print("Tie Game! Well played.")
                more = input("Play again? Y or N\n").lower()
                if more == "n":
                    exit("Thanks for playing!")
                if more == "y":
                    valid_guesses = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    play_game()

            if marker == "X":
                guess = take_turn(x_player, valid_guesses, marker, x, o)
                if guess in valid_guesses:
                    valid_guesses.remove(guess)
                    active_game_board = active_game_board.replace(str(guess), marker)
                x.append(guess)

                for list in winning_combos:
                    result = all(elem in x for elem in list)
                    if result:
                        print(active_game_board)
                        print("X WINS BABY")
                        more = input("Play again? Y or N\n").lower()
                        if more == "n":
                            exit("Thanks for playing!")
                        if more == "y":
                            valid_guesses = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                            play_game()
            if marker == "O":
                guess = take_turn(o_player, valid_guesses, marker, x, o)
                if guess in valid_guesses:
                    valid_guesses.remove(guess)
                    active_game_board = active_game_board.replace(str(guess), marker)
                o.append(guess)
                for list in winning_combos:
                    result = all(elem in o for elem in list)
                    if result:
                        print(active_game_board)
                        print("O WINS BABY")
                        more = input("Play again? Y or N\n").lower()
                        if more == "n":
                            exit("Thanks for playing!")
                        if more == "y":
                            game_key = '''       |   |   
                                 1 | 2 | 3 
                                ___|___|___
                                   |   |
                                 4 | 5 | 6 
                                ___|___|___
                                   |   |
                                 7 | 8 | 9 
                                   |   |'''
                            active_game_board = '''       |   |   
                                 1 | 2 | 3 
                                ___|___|___
                                   |   |
                                 4 | 5 | 6 
                                ___|___|___
                                   |   |
                                 7 | 8 | 9 
                                   |   |'''
                            valid_guesses = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                            play_game()
            print(active_game_board)
play_game()
