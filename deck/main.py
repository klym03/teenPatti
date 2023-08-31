# Author: Romikk
# Description: Main file for the deck package
# Date: 2021/02/10
# Version: 1.0
# Python version: 3.8
#

from deck.Deck import Deck
from deck.Utils import get_winner_looser

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()

    player_1 = deck.get_random_combination()
    print(f"Player_1: {player_1.show()}")

    player_2 = deck.get_random_combination()
    print(f"Player_2: {player_2.show()}")

    print("------------------------------------------------")

    winner, looser = get_winner_looser(player_1, player_2)
    print(f"Winner: {winner.show()}")
    print(f"Looser: {looser.show()}")
