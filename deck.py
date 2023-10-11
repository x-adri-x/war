from card import Card
import random

class Deck:

    suits = ["♠️", "♣️", "♦️", "♥️"]
    ranks = list(range(2, 15))

    def __init__(self):
        self.cards = []

    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, cards):
        self._cards = self.initialize(cards)

    def initialize(self, cards):
        for suit in self.suits:
            for rank in self.ranks:
                card = Card(rank, suit)
                cards.append(card)
        return cards

    def __str__(self):
        return self.cards[3]

    def deal_cards(self, player1, player2):
        self.shuffle()
        player1.cards = self.cards[1:27]
        player2.cards = self.cards[26:]
    
    def shuffle(self):
        random.shuffle(self.cards)