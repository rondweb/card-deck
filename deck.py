from card import Card
import json
from random import sample

class Deck(Card):
    def __init__(self, id):
        self.id = id
        self.get_deck()

    def __str__(self):
        return f"id:{self.id} with: {len(self.cards)} cards with sequence: {', '.join([(x.suit+'-'+x.value) for x in self.cards])}"

    def object_decoder(self, card_data):
        return Card(**card_data)

    def get_deck(self):
        with open("deck_description.json") as f:
            json_data = json.load(f)
            self.cards = list(map(self.object_decoder, json_data))
    
    def shuffle_deck(self):
        self.cards = sample(self.cards,len(self.cards))       

# if __name__ == '__main__':
#     _deck = Deck('1')
#     print(str(_deck))
#     _deck.shuffle_deck()
#     print(str(_deck))
#     _deck.shuffle_deck()
#     print(str(_deck))

