from game_service import GameService


class Game:
    def __init__(self, game_service: GameService):
        self.game_service: GameService = game_service

    # Starts the game loop and allow the user to play the guessing game.
    # The game continues until the player decides not to play again.
    def play(self):
        while True:
            self.game_service.play_round()
            if not self.game_service.ask_play_again():
                break
