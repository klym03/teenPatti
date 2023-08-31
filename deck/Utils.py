# Author: Romikk
# Description: Utility functions for the deck package
# Date: 2021/02/10
# Version: 1.0
# Python version: 3.8
#
def get_winner_looser(combination_1, combination_2):
    if combination_1.points > combination_2.points:
        return combination_1, combination_2
    elif combination_1.points < combination_2.points:
        return combination_2, combination_1
    else:
        if combination_1.weight > combination_2.weight:
            return combination_1, combination_2
        elif combination_1.weight < combination_2.weight:
            return combination_2, combination_1
        else:
            return None, None


def get_high_card(cards):
    return max(cards[0].value, cards[1].value, cards[2].value)


def get_pair_card(cards):
    if cards[0].value == cards[1].value:
        pair_card_value = cards[0].value
    elif cards[0].value == cards[2].value:
        pair_card_value = cards[0].value
    elif cards[1].value == cards[2].value:
        pair_card_value = cards[1].value
    if pair_card_value == 1:
        return 14
    else:
        return pair_card_value


def get_set_card(cards):
    if cards[0].value == cards[1].value == cards[2].value:
        if cards[0].value == 1:
            return 14
        return cards[0].value


def has_ace(cards):
    return cards[0].value == 1 or cards[1].value == 1 or cards[2].value == 1


def has_king(cards):
    return cards[0].value == 13 or cards[1].value == 13 or cards[2].value == 13


def has_two(cards):
    return cards[0].value == 2 or cards[1].value == 2 or cards[2].value == 2
