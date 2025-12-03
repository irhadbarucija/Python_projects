import random
from art import logo

# Number of attempts - easy and hard
easy_level = 10
hard_level = 5

def set_difficulty():
    """Set number of attempts based on user choice of difficulty."""

    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()

        if level == "easy":
            return easy_level
        elif level == "hard":
            return hard_level
        else:
            print("\nInvalid input. Please enter 'easy' or 'hard' to choose difficulty.")


def random_number():
    """Generate random number between 1 and 100."""
    num = random.randint(1, 100)
    return num

def play_game():
    """Runs one full round of the game."""
    print(logo)
    print("Welcome to the Guess Number game!")
    print("I'm thinking of a number between 1 and 100. Try to guess it!")

    attempts = set_difficulty()
    number = random_number()

    # Continue to run as long as the player still has attempts left.
    # The loop stops when the number is guessed or attempts reach zero.
    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")

        # Validate input
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("\nInvalid input. Please enter a number.")
            continue

        if guess > number:
            print("\nToo high.\nGuess again.")
        elif guess < number:
            print("\nToo low.\nGuess again.")
        else:
            print(f"You got it! The answer was {number}!")
            return

        attempts -= 1
    
    print(f"You ran out of guesses. You lose. The number was {number}!")

# Keep running the game as long as the player chooses to continue.
while True:
    play_game()
    play_again = input("\nDo you want to play again? Type 'y'or 'n': ").lower()
    if play_again != 'y':
        print("\nGoodbye!")
        break
    else:
        print("\n" * 20)