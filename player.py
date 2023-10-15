from card import Card


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError
        else:
            self._name = name

    def draw_card(self) -> Card:
        card = self.cards.pop(0)
        card.player = self
        return card
    
    def has_cards(self) -> bool:
        return len(self.cards) != 0
        
    def add_cards(self, cards_to_add):
        """ Adds the cards won to the player's deck. """
        for card in cards_to_add:
            self.cards.append(card)

    def draw_cards_at_war(self) -> list[Card]:
        cards = []
        cards.append(self.draw_card())
        if self.has_cards():
            cards.append(self.draw_card())
        return cards
