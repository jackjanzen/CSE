import random
import string


def challenge1(first_name, last_name):
    return "%s %s" % (last_name, first_name)
def challenge2(a):
    if a % 2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")
def challenge3(base, height):
    return base * height * 1/2
def challenge4(numero):
    if numero > 0:
        print("%d is positive." % numero)
    elif numero == 0:
        
print("Easy:")
print(challenge1("Jack", "Janzen"))
print("***")

print(challenge2(1))
print(challenge2(2))
print("***")
print(challenge3(2, 2))
print("***")

