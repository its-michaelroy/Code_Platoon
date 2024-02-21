# Make gameboard display with the typical 9 spaces
def gameboard_display(board):
    print(f"{board['top_left']} | {board['top_mid']} | {board['top_right']}")
    print("--|---|--")
    print(f"{board['mid_left']} | {board['mid_mid']} | {board['mid_right']}")
    print("--|---|--")
    print(f"{board['bot_left']} | {board['bot_mid']} | {board['bot_right']}")


# Base gameboard, to use
gameboard = {
    'top_left': ' ', 'top_mid': ' ', 'top_right': ' ',
    'mid_left': ' ', 'mid_mid': ' ', 'mid_right': ' ',
    'bot_left': ' ', 'bot_mid': ' ', 'bot_right': ' '
}

# Handle player input for gameboard
# When player puts in x || O & selects place > gameboard.place = X || O
if num_of_turns_taken == 0:
    user_letter_choice = input("Choose X or O for your letter: ")
    print(f"Your letter is {user_letter_choice}")
else:
    user_position_choice = input(
        "Choose a position to place your letter: top_left, top_mid, top_right, mid_left, mid_mid, mid_right, bot_left, bot_mid, bot_right: ")
    print(f"Your position is {user_position_choice}")

    if user_letter_choice == 'X':
        gameboard[user_position_choice] = 'X'
    elif user_letter_choice == 'O':
        gameboard[user_position_choice] = 'O'
    else:
        print("Invalid letter choice. Please choose X or O")
user_letter_choice = input("Choose X or O for your letter: ")
print(f"Your letter is {user_letter_choice}")

user_position_choice = input(
    "Choose a position to place your letter: top_left, top_mid, top_right, mid_left, mid_mid, mid_right, bot_left, bot_mid, bot_right: ")
print(f"Your position is {user_position_choice}")


print(gameboard_display(gameboard))


# handle player input for gameboard
# When player puts in x || O & selects place > gameboard.place = X || O
# place in for loop to bounce between computer and player


# check if someone won each round
# make sure to check inside the loops if someone won by checking a conditional statement to see if any three combos are true. If so then the player with x or O wins
