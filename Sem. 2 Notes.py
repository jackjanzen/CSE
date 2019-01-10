import god
print("Hello world!")
# This is a single line comment.
cars = 5
driving = True
print("I have %d cars." % cars)
print("I have " + str(cars) + " cars.")
age = input("How old are you?")
print("%s?! You're ancient!" % age)
colors = ["Green", "Yellow", "Red", "Blue", "Purple"]
colors.append("Cyan")
print(colors)
colors.pop(0)
print(colors)
print(colors[2])















death = input("Would you like to call god? Type Yes or No.")
if death == "Y" or "Yes" or "yes" or "YES":
    god.call_god()
elif death == "N" or "No" or "NO" or "no":
    print("Maybe some other time.")
else:
    print("That was not a valid answer. Goodbye.")
