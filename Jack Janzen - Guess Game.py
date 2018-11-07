import random
print("Welcome to Guess Game!")
print("When prompted, please guess a number between 1 and 10")
print("You have 5 tries to guess the right number. If you don't, you lose!")
print("Good luck!")
turn = 0
number = (random.randint(1, 10))

while turn < 5:
    turn += 1
    print("Turn %d" % turn)
    guess = int(input("Guess a number:"))
    if guess == number:
        print("You Win!")
        turn = 10
    elif guess > number:
        if turn == 5:
            print("You Lost.")
        else:
            print("Lower.")

    else:
        if turn == 5:
            print("You Lost.")
        else:
            print("Higher.")

