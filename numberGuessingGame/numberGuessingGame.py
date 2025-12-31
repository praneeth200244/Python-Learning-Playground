import random

def number_guessing_game():
    secret_number = random.randint(0, 100)
    attempts = 0

    print("I'm thinking of a number between 0 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 0 or guess > 100:
                print("Please enter a number between 0 and 100.")
                continue

        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            return attempts


if __name__ == "__main__":
    tries = number_guessing_game()
    print("Game finished. Attempts:", tries)
