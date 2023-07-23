class GameConfig:
    def __init__(self, max_guesses: int, min_number: int, max_number: int) -> None:
        if min_number > max_number:
            raise ValueError(
                "Minimum number cannot be greater than the maximum number."
            )

        # Initialize constructor members.
        self.max_guesses: int = max_guesses
        self.min_number: int = min_number
        self.max_number: int = max_number

        # Initialize game messages.
        self.MESSAGE_INTRODUCTION: str = f"Welcome to the guessing game! You have {max_guesses} tries to guess the correct number ranging from {min_number} to {max_number}."
        self.MESSAGE_TRY_AGAIN: str = "That is not the correct number. Try again!"
        self.MESSAGE_VICTORY: str = "Congratulations! You guessed the number correctly."
        self.MESSAGE_DEFEAT: str = "You have run out of guesses. Do you want to try again?"