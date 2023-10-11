import sys
from pyfiglet import Figlet
from player import Player
from card import Card
from typing import Union

class Game:

    def create_player(self, nr: int) -> Player:
        while True:
            try:
                player = Player(input(f"Type name for player {nr}: "))
            except ValueError:
                print("Please type your name in order to start the game.")
            else:
                return player
            
    def play_a_round(self, player1, player2):
        while input() == "":
            cards = []
            for player in [player1, player2]:
                try:
                    card = player.play_a_card()
                except IndexError:
                    print(self.pretty_print(f"{player.name} ran out of cards!"))
                    sys.exit()
                else:
                    cards.append(card)
            outcome = self.compare_cards(cards[0],cards[1])
            while outcome == "war":
                print("=======================================================\n"
                        f"\t\t\t   WAR!\n"
                        f"\tPlace 1 card face down, and 1 face up.!\n"
                        "=======================================================\n")
                cards = []
                for player in [player1, player2]:
                    try:
                        cards_at_war = player.play_cards_at_war()
                    except IndexError:
                        self.pretty_print(f"{player.name} ran out of cards!")
                        sys.exit()
                    else:
                        if len(cards_at_war) == 1:
                            cards.append(cards_at_war[0])
                        else:
                            cards.append(cards_at_war[1])
                outcome = self.compare_cards(cards[0],cards[1])
            else:
                print("=======================================================\n"
                        f"\t\t   {cards[0]} vs. {cards[1]}\n"
                        f"\t\t{outcome.player} has won this round!\n"
                        "=======================================================\n")
            print("Hit enter to start a round!")
            
    def compare_cards(self, card1: Card, card2: Card) -> Union[Card, str]:
        if card1.rank > card2.rank:
            return card1
        elif card2.rank > card1.rank:
            return card2
        else:
            return "war"

    @staticmethod        
    def pretty_print(text):
        f = Figlet(font='ogre')
        return f.renderText(text)
