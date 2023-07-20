import random


class GuessingGame:
    def __init__(self, max_guesses, min_number, max_number):
        if min_number >= max_number:
            raise ValueError("Invalid range. min_number must be less than max_number.")

        # Initialize constructor members.
        self.max_guesses = max_guesses
        self.min_number = min_number
        self.max_number = max_number
        self.number_to_guess = None

        # Initialize game messages.
        self.message_introduction = f"Welcome to the guessing game! You have {self.max_guesses} tries to guess the correct number ranging from {self.min_number} to {self.max_number}."
        self.message_try_again = "That is not the correct number. Try again!"
        self.message_victory = "Congratulations! You guessed the number correctly."
        self.message_defeat = "You have run out of guesses. Do you want to try again?"

    def generate_number(self):
        # Generate a random number within the specified range.
        self.number_to_guess = random.randint(self.min_number, self.max_number)

    def play(self):
        self.generate_number()
        remaining_guesses = self.max_guesses

        # Introduce user to the game.
        print(self.message_introduction)

        while remaining_guesses > 0:
            try:
                user_guess = int(input("Your guess: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue

            if self.number_to_guess is not None:
                if user_guess == self.number_to_guess:
                    # Player guessed correctly.
                    print(self.message_victory)
                    return
                else:
                    remaining_guesses -= 1
                    if remaining_guesses == 0:
                        # Player ran out of guesses.
                        print(self.message_defeat)
                        break
                    # Provide feedback and decrement remaining guesses.
                    print(self.message_try_again)
                    if user_guess < self.number_to_guess:
                        print("The actual number is higher.")
                    else:
                        print("The actual number is lower.")

        # Ask the player if they want to play again.
        start_again = input("Do you want to play again? (Y/N): ")
        if start_again.upper() == "Y":
            self.play()


game = GuessingGame(4, 1, 10)
game.play()
