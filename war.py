import sys
from deck import Deck
from game import Game

def main():
    try:
        game = Game()
        player_1 = game.create_player(1)
        player_2 = game.create_player(2)

        deck = Deck()
        deck.deal_cards(player_1, player_2)
        print("\nThe game is starting ...\n"
            "The deck is being shuffled ...\n")
        print(game.pretty_print("Let's play!"))
        game.play_game(player_1, player_2)
    except (EOFError, KeyboardInterrupt):
        sys.exit("\nExited Game of War! Sorry to see you go :(")


if __name__ == "__main__":
    main()
