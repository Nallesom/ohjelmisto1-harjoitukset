import random

rolls = int(input("How many dice to roll: "))
dicesum = 0

for rolls in range(0, rolls):
    dicesum += random.randint(1, 6)

print(f"Sum of the dice: {dicesum}")