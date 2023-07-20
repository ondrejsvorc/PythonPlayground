import random
from game_config import GameConfig


class GameService:
    NO_MORE_GUESSES: int = 0

    def __init__(self, game_config: GameConfig) -> None:
        self.game_config: GameConfig = game_config
        self.number_to_guess: int = None
        self.remaining_guesses: int = game_config.max_guesses

    # Checks if user is out of guesses.
    def is_out_of_guesses(self) -> bool:
        return self.remaining_guesses == GameService.NO_MORE_GUESSES

    # Decreases the remaining number of guesses by 1.
    def decrement_remaining_guesses(self) -> None:
        self.remaining_guesses -= 1

    # Generates a random number within the given range.
    def generate_number(self) -> None:
        return random.randint(self.game_config.min_number, self.game_config.max_number)

    # Starts a new round of the guessing game.
    def play_round(self) -> None:
        self.number_to_guess = self.generate_number()
        print(self.game_config.MESSAGE_INTRODUCTION)
        self.remaining_guesses = self.game_config.max_guesses

        while not self.is_out_of_guesses():
            user_guess = self.get_user_guess()
            if user_guess == self.number_to_guess:
                print(self.game_config.MESSAGE_VICTORY)
                return
            else:
                self.decrement_remaining_guesses()
                if self.is_out_of_guesses():
                    print(self.game_config.MESSAGE_DEFEAT)
                    break
                self.print_feedback(user_guess)

    # Gets the user's guess from the input.
    def get_user_guess(self) -> int:
        while True:
            try:
                return int(input("Your guess: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Provides feedback to the user based on their guess.
    def print_feedback(self, user_guess: int) -> None:
        print(self.game_config.MESSAGE_TRY_AGAIN)
        if user_guess < self.number_to_guess:
            print("The actual number is higher.")
        else:
            print("The actual number is lower.")

    # Asks the user if they want to play again.
    def ask_play_again(self) -> bool:
        start_again = input("Do you want to play again? (Y/N): ")
        return start_again.upper() == "Y"
