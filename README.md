# Project Deck
## Simple card deck and actors

## Classes and Methods:


|CLASS           |ATTRIBUTES                     |METHODS                      |
|----------------|-------------------------------|-----------------------------|
|Card            |ref (int), suit (string), value (string) | get_ref(),get_value(),get_suit()            |
|Deck            |id (string),cards (Card collection)      |object_decoder(), get_deck(), shuffle_deck()          |
|Player          | name (string), cards (Card collection)  |set_cards(),get_cards() |
|Game            | players (Players collection), cards (Card collection)  |add_player(), get_decks(), give_cards_to_players()|


## Web API

- For the WEB API it was choosed the Framework FAST API with python 3.9
- For the enviroment it was choosed Miniconda 3
