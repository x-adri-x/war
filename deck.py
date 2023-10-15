from card import Card
import random

class Deck:

    suits = ["♠️", "♣️", "♦️", "♥️"]
    ranks = list(range(2, 15))
    
    def __init__(self):
        """ Initialise the deck. """
        self.cards = [Card(r, s) for s in self.suits for r in self.ranks]

    def deal_cards(self, player1, player2):
        """ Deal each player 26 cards from the shuffled deck. """
        self.shuffle()
        player1.cards = self.cards[1:27]
        player2.cards = self.cards[26:]
    
    def shuffle(self):
        random.shuffle(self.cards)