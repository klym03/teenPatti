# Author: Romikk
# Description: Combination class
# Date: 2021/02/10
# Version: 1.0
# Python version: 3.8
#

from deck.Utils import Utils


class Combination:
    def __init__(self, cards):
        self.cards = cards
        self.points = 0
        self.weight = 0

    def show(self):
        return f"{self.cards[0].show()} {self.cards[1].show()} {self.cards[2].show()} Points: {self.points} Weight: {self.weight}"

    def is_none(self):
        return not self.is_pair() and not self.is_set() and not self.is_flash() and not self.is_straight() and not self.is_straight_flash()

    def is_pair(self):
        return (self.cards[0].value == self.cards[1].value or self.cards[0].value == self.cards[2].value or self.cards[
            1].value ==
                self.cards[2].value) and not (self.cards[0].value == self.cards[1].value == self.cards[2].value)

    def is_set(self):
        return self.cards[0].value == self.cards[1].value == self.cards[2].value

    def is_flash(self):
        return self.cards[0].suit == self.cards[1].suit == self.cards[2].suit

    def is_straight(self):
        return self.cards[0].value == self.cards[1].value - 1 == self.cards[2].value - 2

    def is_straight_flash(self):
        return self.cards[0].value == self.cards[1].value - 1 == self.cards[2].value - 2 and self.cards[0].suit == \
            self.cards[1].suit == self.cards[2].suit

    def __get_points(self):
        if self.is_none():
            self.points = 1
        elif self.is_pair():
            self.points = 2
        elif self.is_set():
            self.points = 3
        elif self.is_flash():
            self.points = 4
        elif self.is_straight():
            self.points = 5
        elif self.is_straight_flash():
            self.points = 6
        return self.points

    def __get_weight(self):
        if self.is_none() or self.is_flash() or self.is_straight():
            self.weight = Utils.get_high_card(self.cards)
        elif self.is_pair():
            self.weight = Utils.get_pair_card(self.cards)
        elif self.is_set():
            self.weight = Utils.get_set_card(self.cards)
        elif self.is_straight() or self.is_straight_flash():
            if Utils.has_ace(self.cards):
                if Utils.has_two(self.cards):
                    self.weight = 1
                elif Utils.has_king(self.cards):
                    self.weight = 14
            else:
                self.weight = Utils.get_high_card(self.cards)

    def get_combination(self):
        self.__get_points()
        self.__get_weight()
        return self

# Points
#
# 1. None combination - 1 point
# 2. Pair - 2 points
# 3. Set - 3 points
# 4. Flash - 4 points
# 5. Straight - 5 points
# 6. Straight flash - 6 points
#
# Weight of cards
# 1. Ace - 1 / 14
# 2. 2 - 2
# 3. 3 - 3
# 4. 4 - 4
# 5. 5 - 5
# 6. 6 - 6
# 7. 7 - 7
# 8. 8 - 8
# 9. 9 - 9
# 10. 10 - 10
# 11. Jack - 11
# 12. Queen - 12
# 13. King - 13
#
