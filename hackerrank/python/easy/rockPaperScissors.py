import random
import emoji

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

def your_choice_emoji(choice):
    if choice == PAPER:
        return emoji.emojize(':roll_of_paper:')
    if choice == SCISSORS:
        return emoji.emojize(':scissors:')
    return emoji.emojize(':rock:')


def find_the_winner(computer_choice, user_choice):

    print("Your choice: ", your_choice_emoji(user_choice))
    print("Computer choice: ", your_choice_emoji(computer_choice))

    winner_combinations = [(ROCK, SCISSORS), (PAPER, ROCK), (SCISSORS, PAPER)]
    if user_choice == computer_choice:
        print("No winner")
    elif (user_choice, computer_choice) in winner_combinations:
        print("You won")
    else:
        print("Computer won")


if __name__ == '__main__':
    game_choices = (ROCK, PAPER, SCISSORS)

    while True:
        computer_choice = random.choice(game_choices)
        user_choice = input("Rock, paper or scissors (r/p/s): ").lower()

        if user_choice not in game_choices:
            print("Invalid choice!")
            continue

        find_the_winner(computer_choice, user_choice)

        continue_playing = input("Continue (y/n): ").lower()
        if continue_playing != 'y':
            break
