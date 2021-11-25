from card import Card


class Player(Card):
    def __init__(self, name):
        self.name = name
        self.cards = []

    def set_cards(self, cards):
        self.cards.extend(cards)

    def get_cards(
        self,
    ):
        return self.cards
