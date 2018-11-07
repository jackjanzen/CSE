import random
cbal = 15
maxbal = 15
dice1 = 0
dice2 = 0
turn = 0
print("Welcome to Lucky 7's, the gambling game where you are destined to lose!")
print("Two 6 sided dice will be rolled, and if the sum equals 7, you win!")
print("You bet a $1 each round, and you start out at $15.")
print("If you win, then you get your bet back plus $4!")
print("If you lose, then you lose your bet.")
"""input("Input anything here to start:")"""

while cbal > 0:
    turn += 1
    print("Turn: %d" % turn)
    cbal -= 1
    print("Current Balance:")
    print(cbal)
    dice1 = (random.randint(1,6))
    dice2 = (random.randint(1,6))
    print("Dice 1:")

    print(dice1)
    print("Dice 2:")
    print(dice2)
    roll = dice1 + dice2
    print("Roll:")
    print(roll)
    if roll == 7:
        cbal += 5
    if cbal > maxbal:
        maxbal = cbal
print("You Lost!")
print("Highest balance: %d" % maxbal)

