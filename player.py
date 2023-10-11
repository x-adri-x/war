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

    def play_a_card(self):
        if len(self.cards) == 0:
            raise IndexError
        else:
            card = self.cards.pop(0)
            card.player = self.name
            return card
        
    def add_cards(self, cards_to_add):
        ...
        
    def play_cards_at_war(self):
        cards = []
        face_down_card = self.play_a_card()
        try:
            face_up_card = self.play_a_card()
        except IndexError:
            cards.append(face_down_card)
        else:
            cards.append(face_down_card)
            cards.append(face_up_card)
        return cards