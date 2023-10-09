from deck import Deck
from player import Player

def main():
    deck = Deck()
    player_1 = Player("Joe")
    player_2 = Player("Susan")
    deck.deal_cards(player_1, player_2)
    print(player_1.cards)


if __name__ == "__main__":
    main()
