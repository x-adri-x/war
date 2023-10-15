import sys
import random
from tabulate import tabulate
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

    def shuffle_players(self, player1, player2):
        players = [player1, player2]
        random.shuffle(players)
        return players

    def play_game(self, player1, player2):
        while True:
        # while input() == "":
            is_war = False
            # a stack to store all the cards that were placed down during war
            cards_played_at_war = []
            # store the cards played by the players
            face_up_cards = [
                x.draw_card() if x.has_cards() else self.end_game(x, [player1, player2])
                for x in [player1, player2]
            ]
            # outcome stores the winning card object or the word "war"
            outcome = self.compare_cards(face_up_cards)
            if outcome == "war":
                is_war = True
                # if there is a war, add the two cards with equal rank to the war card stack
                cards_played_at_war.extend(face_up_cards)
            else:
                # if there is no war, add the two cards played to the winner's stack
                outcome.player.add_cards(face_up_cards)
                self.finish_round(face_up_cards, player1, player2, outcome)
            while is_war:
                self.print_war_round(face_up_cards, player1, player2)
                face_up_cards = []
                for player in [player1, player2]:
                    cards_drawn = (
                        player.draw_cards_at_war()
                        if player.has_cards()
                        else self.end_game(player, [player1, player2])
                    )
                    cards_played_at_war.extend(cards_drawn)
                    face_up_cards.append(cards_drawn.pop())
                outcome = self.compare_cards(face_up_cards)
                if outcome != "war":
                    is_war = False
                    outcome.player.add_cards(cards_played_at_war)
                    self.finish_round(face_up_cards, player1, player2, outcome)

    def compare_cards(self, cards: list[Card]) -> Union[Card, str]:
        if cards[0].rank > cards[1].rank:
            return cards[0]
        elif cards[1].rank > cards[0].rank:
            return cards[1]
        else:
            return "war"

    def end_game(self, player_lost, players):
        print(self.pretty_print(f"{player_lost.name} ran out of cards!"))
        winner = [x for x in players if x.name != player_lost.name][0]
        sys.exit(self.pretty_print(f"{winner.name} has won!"))

    @staticmethod
    def print_war_round(cards, player1, player2):
        text1 = f"{player1.name} played {cards[0]}"
        text2 = f"{player2.name} played {cards[1]}"
        print(tabulate([[text1,text2]], tablefmt="fancy_grid"))
        print(
            f"\n\t\t   {cards[0]} vs. {cards[1]}\n"
            f"\t\t\t   WAR!\n"
            f"\tPlace 1 card face down, and 1 face up.!\n"
            "====================================================\n"
        )

    @staticmethod
    def finish_round(cards, player1, player2, outcome):
        text1 = f"{player1.name} played {cards[0]}"
        text2 = f"{player2.name} played {cards[1]}"
        print(
            tabulate(
                [[text1,text2]],
                tablefmt="fancy_grid",
            )
        )
        print(
            f"\n\t\t   {cards[0]} vs. {cards[1]}\n"
            f"\t\t{outcome.player.name} has won this round!\n"
            "==================================================\n"
        )
        [print(f"{x.name} has {len(x.cards)} cards\n") for x in [player1, player2]]
        print("Hit enter to start a round!")

    @staticmethod
    def pretty_print(text):
        f = Figlet(font="ogre")
        return f.renderText(text)
