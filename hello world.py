'''
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
#  This is a comment with no effect on code
# But I can:
# 1. Make notes to myself
# 2. Comment pieces of code that do not work
# 3. Make my code easier to read
print("Look at what happens here. Is there any space?")
print()
print()
print("There should be a couple of blank lines here.")
yoink = 2
yeet = 2

# Math
print(3+5)
print(5-2)
print(3*4)
print(6/2)
print()
print("Figure this out...")
print(6//2)
print(5//2)
print(9//4)
print()
print(6%2)
print(5%2)
print(11%4) # Modulus (Remainder)
print()


# variables for text


name = input("What is your name?")
print("Hello %s" % name)
age = input("How old are you? >_")
print("%s?!? You belong in a museum." % age)
print("%s is really old. They are %s years old." % (name,age))

car_name = "free candy and puppies inside"
car_type = "white van"
car_cylinders = 16
car_mpg = 0.01

print("I have a car with %s! It is a %s. Want to ride?" % (car_name, car_type))
print()
print()
print("Hello, I'm Chris Hansen, and welcome to To Catch a Predator Episode 9.")

# recasting


real_age = int(input("How old are you again?"))
hidden_age = real_age+10
print("This is your real age: %d" % hidden_age)
print("The camera adds ten years.")
input("Do you want to know why? Type something, anything to learn.")
print("I AM ALWAYS WATCHING.")

print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")
print("I AM ALWAYS WATCHING.")

print()
print()
print("Now back to your regularly scheduled program.")
'''
"""
# functions


def say_it():
    print("Hello World!")


say_it()
say_it()
say_it()

print("Slope-Intercept Formula:")


def f(x):
    print(2 * x + 3)


f(1)
f(5)
f(5000)
print("Distance:")


def distance(x1, y1, x2, y2):
    dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    print(dist)


distance(0, 0, 3, 4)
distance(0, 0, 5, 12)



# functions


def say_it():
    print("That's pretty lit")


say_it()
say_it()
say_it()

# For Loops

for i in range(10000):
    say_it()
for i in range(1000000):
    print(i+1)



# While Loops
a = 1
while a < 2048:
    print(a)
    a += 2

at the moment you start the loop:
For loops- use when you know exactly how many iterations
While loops - Use when you done know how many iterations


# if statements

sunny = False
if sunny:
    print("Go outside")


def grade_calc (percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


yourgrade = grade_calc(82)
print(yourgrade)


# Equality Statements
print(5 > 3)
print(5 >= 3)
print(3 == 3)
print(3 != 4)


a = 3 # A is set to 3
a == 3 # Is a equal to 3?
"""

colors = ["blue", "turquoise", "pink"]
print(colors)
lol = 0
sevlist = ["there", "are", "seven", "items", "in", "this", "list"]
sevlist[2] = "7"
print(sevlist[2])
print("The last thing in the list is %s." % sevlist[len(sevlist) - 1])
print(sevlist[1:3])

foodlist = ["tacos", "salad", "chocolate", "pie", "apples", "apple pie", "peach cobbler", "yogurt",
            "chips", "ice (for those with an iron deficiency)", "mac n' cheese",
            "pear", "ice cream", "popsicles", "lolipops", "maple syrup", "rocks",
            "fettuccine", "pizza", "turkey"]
print(len(foodlist))
foodlist.append("bacon")
foodlist.append("eggs")
print(foodlist)

foodlist.insert(1, "eggo waffles")
print(foodlist)

foodlist.remove("salad")
print(foodlist)

threelist = ["Wow!", "Three", "items"]
print(threelist)
threelist.append("exactly!")
threelist[1] = "Four"
print(threelist)
threelist.remove("Wow!")
threelist[0] = "Three"
print(threelist)

# pop is the insert version of removing things
print(foodlist)
foodlist.pop(0)
print(foodlist)

string1 = "turquoise"
list1 = list(string1)
print(list1)
print("".join(list1))
for i in range(len(list1)):
    if list1[i] == "u":
        list1.pop(i)
        list1.insert(i, "*")
print("".join(list1))

"""
for character is list1:
    if character == "u":
        # replace with a *
        currentindex = list1.index(character)
        list1.pop(currentindex)
        list1.insert(currentindex, "*"
"""

