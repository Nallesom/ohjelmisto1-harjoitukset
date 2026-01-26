import random


def roll_dice():
    return random.randint(1, 6)


diceroll = 0
while diceroll != 6:
    diceroll = roll_dice()
    print(diceroll)