class Card:
    def __init__(self, rank, suit, player=None):
        self.rank = rank
        self.suit = suit
        self.player = player

    def __str__(self):
        if self.rank == 11:
            name = "Jack"
        elif self.rank == 12:
            name = "Queen"
        elif self.rank == 13:
            name = "King"
        elif self.rank == 14:
            name = "Ace"
        else:
            name = self.rank
        return f"{name} of {self.suit}"