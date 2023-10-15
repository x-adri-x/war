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
    
    def shuffle_players(self, players):
        random.shuffle(players)
        return players

    def play_game(self, player1, player2):
        rounds = 0
        players = [player1, player2]
        while True:
            is_war = False
            # a stack to store all the cards that were placed down during war
            cards_played_at_war = []
            self.shuffle_players(players)
            # store the cards played by the players in a round
            face_up_cards = [
                x.draw_card() if x.has_cards() else self.end_game(x, players, rounds)
                for x in players
            ]
            # outcome stores the winning card object or the word "war"
            outcome = self.compare_cards(face_up_cards)
            rounds += 1
            if outcome == "war":
                is_war = True
                # if there is a war, add the two cards with equal ranks to the war card stack
                cards_played_at_war.extend(face_up_cards)
            else:
                # if there is no war, add the two cards played to the winning player's stack
                outcome.player.add_cards(face_up_cards)
                self.finish_round(face_up_cards, player1, player2, outcome)
            while is_war:
                self.print_war_round(face_up_cards, player1, player2)
                face_up_cards = []
                self.shuffle_players(players)
                for player in players:
                    # draw cards if the players have enough, or end the game if one of them runs out
                    cards_drawn = (
                        player.draw_cards_at_war()
                        if player.has_cards()
                        else self.end_game(player, players, rounds)
                    )
                    cards_played_at_war.extend(cards_drawn)
                    face_up_cards.append(cards_drawn.pop())
                outcome = self.compare_cards(face_up_cards)
                if outcome != "war":
                    rounds += 1
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

    def end_game(self, player_lost, players, rounds):
        """ When one of the players runs out of cards, finish the game 

        Parameters:
            player_lost: class Player, the player who ran out of cards
            players: list of class Player, the players of the game
            round: int, counting the played rounds of game
        """
        print(self.pretty_print(f"{player_lost.name} ran out of cards!"))
        # get the winning Player object
        winner = [x for x in players if x.name != player_lost.name][0]
        print(f"A total of {rounds} rounds were played.")
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

    @staticmethod
    def pretty_print(text):
        f = Figlet(font="contessa")
        return f.renderText(text)
