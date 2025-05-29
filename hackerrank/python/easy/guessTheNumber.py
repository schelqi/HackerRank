import random

number_2_guess = random.randint(1, 100)

while True:
    response = input("Guess the number between 1 and 100: ")

    try:
        guessed_number = int(response)
        if guessed_number > number_2_guess:
            print("Too high!")
        elif guessed_number < number_2_guess:
            print("Too low!")
        else:
            print("Congrats!")
            break
    except ValueError:
        print("Please enter a valid number!")
