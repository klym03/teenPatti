# Author: Romikk
# Description: Card class
# Date: 2021/02/10
# Version: 1.0
# Python version: 3.8
#

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        return "{}{}".format(self.convert_value(), self.convert_suit())

    def convert_value(self):
        if self.value == 14:
            self.value = "A"
        elif self.value == 11:
            self.value = "J"
        elif self.value == 12:
            self.value = "Q"
        elif self.value == 13:
            self.value = "K"
        return self.value

    def convert_suit(self):
        if self.suit == 1:
            self.suit = "♠"
        elif self.suit == 2:
            self.suit = "♥"
        elif self.suit == 3:
            self.suit = "♦"
        elif self.suit == 4:
            self.suit = "♣"
        return self.suit
