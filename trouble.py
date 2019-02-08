

def turn():
    die = int(input("Enter roll amount:"))
    if die == 1:
        yesno = input("Is it possible to take a piece out of home? Type Y for yes and N for no.")
        if yesno == "N":
            yesno = input("Can you move a piece into the finish? Type Y for yes and N for no.")
            if yesno == "N":
                yesno = input("Can you take an enemy piece? Type Y for yes and N for no.")
                if yesno == "N":
                    print("Move piece closest to finish.")
                elif yesno == "Y":
                    print("Take enemy piece")
            elif yesno == "Y":
                print("Move piece into the finish")
        elif yesno == "Y":
            print("Take piece out of home.")
    elif die == 6:
        yesno = input("Is it possible to take a piece out of home? Type Y for yes and N for no.")
        if yesno == "N":
            yesno = input("Can you move a piece into the finish? Type Y for yes and N for no.")
            if yesno == "N":
                yesno = input("Can you take an enemy piece? Type Y for yes and N for no.")
                if yesno == "N":
                    print("Move piece closest to finish.")
                    print("Roll again.")
                elif yesno == "Y":
                    print("Take enemy piece.")
                    print("Roll again.")
            elif yesno == "Y":
                print("Move piece into the finish.")
                print("Roll again.")
        elif yesno == "Y":
            print("Take piece out of home.")
            print("Roll again.")
    else:
        yesno = input("Can you move a piece into the finish? Type Y for yes and N for no.")
        if yesno == "N":
            yesno = input("Can you take an enemy piece? Type Y for yes and N for no.")
            if yesno == "N":
                print("Move piece closest to finish.")
            elif yesno == "Y":
                print("Take enemy piece")
        elif yesno == "Y":
            print("Move piece into the finish")


turn()
gameend = False
gover = "N"
while gameend is False:
    gover = input("Is the game over? Type Y for yes and N for no.")
    if gover == "Y":
        print("Thanks for playing!")
        gameend = True
    elif gover == "N":
        turn()
