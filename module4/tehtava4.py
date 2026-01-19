import random

random_num = random.randint(1, 10)
input_num = int(input("Guess a number (1-10): "))
while input_num != random_num:
    if input_num > random_num:
        print("Too high!")
    elif input_num < random_num:
        print("Too low!")
    input_num = int(input("Guess a number (1-10): "))

print("Correct")