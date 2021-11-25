from fastapi import FastAPI
from game import Game

app = FastAPI()


def init_game():
    _game = Game()
    _game.add_deck()
    _game.add_deck()
    _game.add_player("player1")
    _game.add_player("player2")
    _game.add_player("player3")
    # _game.give_cards_to_players(5)
    # _game.get_decks()
    # _game.get_players_and_cards()

    return _game


@app.get("/decks")
def decks():
    game = init_game()
    cnt, deck = game.get_decks()
    return {"len": cnt, "original_decks": deck}


@app.get("/players")
def players():
    game = init_game()
    game.give_cards_to_players(5)
    return {"cards_player": game.get_players_and_cards()}


@app.get("/decks-missing")
def players():
    game = init_game()
    game.give_cards_to_players(5)
    cnt, deck = game.get_decks()
    return {"len": cnt, "decks_after_players": deck}
