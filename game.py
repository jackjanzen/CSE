import trouble
trouble.turn()
gameend = False
gover = "N"
while gameend is False:
    gover = input("Is the game over? Type Y for yes and N for no.")
    if gover == "Y":
        print("Thanks for playing!")
        gameend = True
    elif gover == "N":
        trouble.turn()
