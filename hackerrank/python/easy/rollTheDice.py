import random


def rollTheDice():
    return random.randint(1, 6), random.randint(1, 6)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        response = input("Roll the dice (y/n): ")
        if response in ['y', 'Y']:
            print(rollTheDice())
        elif response in ['n', 'N']:
            print("Thanks for playing")
            break
        else:
            print("Invalid choice!")
