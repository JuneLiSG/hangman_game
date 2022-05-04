from dealer_class import Dealer
from player_class import Player

print("Welcome to the game")

while True:
    #dealer sets up the game by setting mystery word
    player = Player()
    dealer = Dealer()

    word = dealer.set_mystery_word()
    pass