import random

def roll_dice(dice_sides):
    return random.randint(1,dice_sides)

maxroll = int(input("How many sides in dice: "))
diceroll = 0
while diceroll != maxroll:
    diceroll = roll_dice(maxroll)
    print(diceroll)