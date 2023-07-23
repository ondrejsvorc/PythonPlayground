from game_service import GameService
from game_config import GameConfig
from game import Game


def main() -> None:
    # Define game constants.
    MAX_GUESSES: int = 5
    MIN_NUMBER: int = 1
    MAX_NUMBER: int = 10

    # Prepare game service with game configuration.
    game_config: GameConfig = GameConfig(MAX_GUESSES, MIN_NUMBER, MAX_NUMBER)
    game_service: GameService = GameService(game_config)

    # Start game.
    game: Game = Game(game_service)
    game.play()


if __name__ == "__main__":
    main()
