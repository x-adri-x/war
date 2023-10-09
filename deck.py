from card import Card

class Deck:

    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    ranks = [range(2, 14)]

    def __init__(self):
        self.cards = []
    
    def initialize(self, cards):
        
        for suit in self.suits:
            for rank in self.ranks:
                card = Card(suit, rank)
                cards.append(card)
        return cards

    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, cards):
        self._cards = self.initialize(cards)

    def deal_cards(self):
        ...
    
    def shuffle(self):
        ...