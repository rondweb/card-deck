from deck import Deck
from player import Player
from random import sample


class Game(Deck, Player):
    def __init__(self):
        self.decks = []
        self.players = []

    def add_deck(
        self,
    ):
        new_deck = Deck(len(self.decks) + 1)
        new_deck.shuffle_deck()
        self.decks.append(new_deck)

    def add_player(self, name):
        new_player = Player(name)
        self.players.append(new_player)

    def get_decks(
        self,
    ):
        return len(self.decks), self.decks
        # for d in self.decks:
        #     print(str(d))

    def give_cards_to_players(self, number_cards):
        for p in self.players:
            deck = sample(self.decks, 1)
            p_cards = sample(deck[0].cards, 5)  # cards to player
            deck[0].cards = set(deck[0].cards) - set(p_cards)  # new deck

            p.set_cards(p_cards)

    def get_players_and_cards(
        self,
    ):
        return self.players
        # for p in self.players:
        #     print(f"Name:{p.name} with cards: {', '.join([(x.suit+'-'+x.value) for x in p.get_cards()])}")


# if __name__ == '__main__':
#     _game = Game()
#     _game.add_deck()
#     _game.add_deck()
#     _game.add_player('player1')
#     _game.add_player('player2')
#     _game.add_player('player3')
#     _game.give_cards_to_players(5)
#     _game.get_decks()
#     _game.get_players_and_cards()
