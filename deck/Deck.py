# Author: Romikk
# Description: Deck class with 3 cards
# Date: 2021/02/10
# Version: 1.0
# Python version: 3.8
#


import random

from deck.Card import Card
from deck.Combination import Combination


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in [1, 2, 3, 4]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def get_random_combination(self):
        random.shuffle(self.cards)
        cards = []
        for i in range(0, 3):
            cards.append(self.cards[i])
        combination = Combination(cards)
        self.__remove_cards(cards)
        return combination.get_combination()

    def get_none(self):
        while True:
            random.shuffle(self.cards)
            cards = []
            for i in range(0, 3):
                cards.append(self.cards[i])
            combination = Combination(cards)
            if combination.is_none():
                self.__remove_cards(cards)
                return combination.get_combination()

    def get_pair(self):
        while True:
            random.shuffle(self.cards)
            cards = []
            for i in range(0, 3):
                cards.append(self.cards[i])
            combination = Combination(cards)
            if combination.is_pair():
                self.__remove_cards(cards)
                return combination.get_combination()

    def get_set(self):
        while True:
            random.shuffle(self.cards)
            cards = []
            for i in range(0, 3):
                cards.append(self.cards[i])
            combination = Combination(cards)
            if combination.is_set():
                self.__remove_cards(cards)
                return combination.get_combination()

    def get_flash(self):
        while True:
            random.shuffle(self.cards)
            cards = []
            for i in range(0, 3):
                cards.append(self.cards[i])
            combination = Combination(cards)
            if combination.is_flash():
                self.__remove_cards(cards)
                return combination.get_combination()

    def get_straight(self):
        while True:
            random.shuffle(self.cards)
            cards = []
            for i in range(0, 3):
                cards.append(self.cards[i])
            combination = Combination(cards)
            if combination.is_straight():
                self.__remove_cards(cards)
                return combination.get_combination()

    def get_straight_flash(self):
        while True:
            random.shuffle(self.cards)
            cards = []
            for i in range(0, 3):
                cards.append(self.cards[i])
            combination = Combination(cards)
            if combination.is_straight_flash():
                self.__remove_cards(cards)
                return combination.get_combination()

    def __remove_cards(self, cards):
        for card in cards:
            self.cards.remove(card)
