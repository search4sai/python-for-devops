import random

def play_guessing_game():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    # Ask the user to guess the number
    guess = int(input("Guess a number between 1 and 10: "))

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the number correctly!")
    elif guess < secret_number:
        print("Sorry, that's not the number. The number is higher.")
    elif guess > secret_number:
        print("Sorry, that's not the number. The number is lower.")        
    else:
        print("Sorry, that's not the number. The number was", secret_number)
import random

def play_guessing_game():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    attempts = 3  # Number of attempts allowed

    for _ in range(attempts):
        # Ask the user to guess the number
        guess = int(input("Guess a number between 1 and 10: "))

        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the number correctly!")
            break
        elif guess < secret_number:
            print("Sorry, that's not the number. The number is higher.")
        elif guess > secret_number:
            print("Sorry, that's not the number. The number is lower.")
    else:
        print("Sorry, you've used all your attempts. The number was", secret_number)

# Start the game
play_guessing_game()
# Start the game
play_guessing_game()
