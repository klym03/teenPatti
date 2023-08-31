import random
deck = []
for i in range(1, 5):
    for j in range(2, 15):
        deck.append((i, j))


def get_combination(combination):
    while True:
        random.shuffle(deck)
        player = []
        for i in range(0, 3):
            player.append(deck[i])
        pair = player[0][1] == player[1][1] or player[0][1] == player[2][1] or player[1][1] == player[2][1]
        set = player[0][1] == player[1][1] == player[2][1]
        flash = player[0][0] == player[1][0] == player[2][0]
        straight = player[0][1] == player[1][1] - 1 == player[2][1] - 2
        straight_flash = player[0][1] == player[1][1] - 1 == player[2][1] - 2 and player[0][0] == player[1][0] == \
                         player[2][0]

        if combination == "pair":
            if pair:
                deck.remove(player[0])
                deck.remove(player[1])
                deck.remove(player[2])
                rang = 1
                return player,rang
        elif combination == "set":
            if set:
                deck.remove(player[0])
                deck.remove(player[1])
                deck.remove(player[2])
                rang = 3
                return player,rang
        elif combination == "flash":
            if flash:
                deck.remove(player[0])
                deck.remove(player[1])
                deck.remove(player[2])
                rang = 2
                return player,rang
        elif combination == "straight":
            if straight:
                deck.remove(player[0])
                deck.remove(player[1])
                deck.remove(player[2])
                rang = 4
                return player,rang
        elif combination == "straight_flash":
            if straight_flash:
                deck.remove(player[0])
                deck.remove(player[1])
                deck.remove(player[2])
                rang = 5
                return player,rang
        elif combination == "none_combination":
            if not pair and not set and not flash and not straight and not straight_flash:
                deck.remove(player[0])
                deck.remove(player[1])
                deck.remove(player[2])
                rang = 0
                return player,rang


comb = ["pair", "set", "flash", "straight", "straight_flash","none_combination"]
random.shuffle(comb)
# print(comb)
combination1 = random.choice(comb)
player_1 = get_combination(combination1)
combination2 = random.choice(comb)
player_2 = get_combination(combination2)
winner = " "
# print(player_1)
# print(player_2)
if player_1[1] > player_2[1]:
    print("player_1 win")
    winner = "player_1"
    print(player_1[0])
    print(player_2[0])
elif player_1[1] < player_2[1]:
    print("player_2 win")
    winner = "player_2"
    print(player_1[0])
    print(player_2[0])
else:
    t = player_1[0][0][1]-player_2[0][0][1]
    print(player_1[0])
    print(player_2[0])
    print(combination1)
    print(combination2)
    if combination1 == "straight_flash" or combination2 == "straight":
        if t > 0:
            print("player_1 win")
            winner = "player_1"
        elif t < 0:
            print("player_2 win")
            winner = "player_2"
        else:
            print("draw")
    if combination1 == 'pair':
#print number that duplicate in player_1
        if player_1[0][0][1] == player_1[0][1][1]:
            t1 = player_1[0][0][1]
        elif player_1[0][0][1] == player_1[0][2][1]:
            t1 = player_1[0][0][1]
        elif player_1[0][1][1] == player_1[0][2][1]:
            t1 = player_1[0][1][1]
#print number that duplicate in player_2
        if player_2[0][0][1] == player_2[0][1][1]:
            t2 = player_2[0][0][1]
        elif player_2[0][0][1] == player_2[0][2][1]:
            t2 = player_2[0][0][1]
        elif player_2[0][1][1] == player_2[0][2][1]:
            t2 = player_2[0][1][1]
        if t1 > t2:

            print("player_1 win")
        elif t1 < t2:
            print("player_2 win")
    if combination1 == 'flush':
#max nunber in player_1
        if player_1[0][0][1] > player_1[0][1][1] and player_1[0][0][1] > player_1[0][2][1]:
            t1 = player_1[0][0][1]
        elif player_1[0][1][1] > player_1[0][0][1] and player_1[0][1][1] > player_1[0][2][1]:
            t1 = player_1[0][1][1]
        elif player_1[0][2][1] > player_1[0][0][1] and player_1[0][2][1] > player_1[0][1][1]:
            t1 = player_1[0][2][1]
#max nunber in player_2
        if player_2[0][0][1] > player_2[0][1][1] and player_2[0][0][1] > player_2[0][2][1]:
            t2 = player_2[0][0][1]
        elif player_2[0][1][1] > player_2[0][0][1] and player_2[0][1][1] > player_2[0][2][1]:
            t2 = player_2[0][1][1]
        elif player_2[0][2][1] > player_2[0][0][1] and player_2[0][2][1] > player_2[0][1][1]:
            t2 = player_2[0][2][1]
        if t1 > t2:
            print("player_1 win")
        elif t1 < t2:
            print("player_2 win")
    if combination1 == 'none_combination':
        if player_1[0][0][1] > player_1[0][1][1] and player_1[0][0][1] > player_1[0][2][1]:
            t1 = player_1[0][0][1]
        elif player_1[0][1][1] > player_1[0][0][1] and player_1[0][1][1] > player_1[0][2][1]:
            t1 = player_1[0][1][1]
        elif player_1[0][2][1] > player_1[0][0][1] and player_1[0][2][1] > player_1[0][1][1]:
            t1 = player_1[0][2][1]
        # max nunber in player_2
        if player_2[0][0][1] > player_2[0][1][1] and player_2[0][0][1] > player_2[0][2][1]:
            t2 = player_2[0][0][1]
        elif player_2[0][1][1] > player_2[0][0][1] and player_2[0][1][1] > player_2[0][2][1]:
            t2 = player_2[0][1][1]
        elif player_2[0][2][1] > player_2[0][0][1] and player_2[0][2][1] > player_2[0][1][1]:
            t2 = player_2[0][2][1]
        if t1 > t2:
            print("player_1 win")
        elif t1 < t2:
            print("player_2 win")
    if combination1 == 'set':
        if t > 0:
            print("player_1 win")
        elif t < 0:
            print("player_2 win")
        else:
            print("draw")

