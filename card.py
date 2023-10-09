class Card:
    def __init__(self, name, rank, suit, player=None):
        self.name = name
        self.rank = rank
        self.suit = suit
        self.player = player