import random
import string
import math
import god
vow = ["a", "e", "i", "o", "u"]

def challenge1(first_name, last_name):
    return "%s %s" % (last_name, first_name)


def challenge2(a):
    if a % 2 == 0:
        return "Your number is even"
    else:
        return "Your number is odd"


def challenge3(base, height):
    return base * height * 1/2


def challenge4(numero):
    if numero > 0:
        return "%d is positive." % numero
    elif numero == 0:
        return "%d is 0" % numero
    else:
        return "%d is negative." % numero


def challenge5(radius):
    return radius ** 2 * math.pi


def challenge6(radius):
    return 4/3 * radius ** 3 * math.pi


def challenge7(n):
    return n + n ** 2 + n ** 3


def challenge8(x):
    if x in range(1850, 2150) or x in range(2850, 3150):
        return True
    else:
        return False


def challenge9(vow_guess):
    if vow_guess in vow:
        return "%s is a vowel" % vow_guess
    else:
        return "%s is not a vowel" % vow_guess

digit_string = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
def challenge10(p):
    if p in digit_string:
        return "%s is a number" % p
    else:
        return "%s is not a number" % p
print("Easy:")
print(challenge1("Jack", "Janzen"))
print("***")

print(challenge2(1))
print(challenge2(2))
print("***")
print(challenge3(2, 2))
print("***")
print(challenge4(1))
print(challenge4(0))
print(challenge4(-1))
print("Medium:")
print(challenge5(2))
print("***")
print(challenge6(2))
print("***")
print(challenge7(3))
print("***")
print(challenge8(2999))
print(challenge8(2500))
print("***")
print(challenge9("f"))
print(challenge9("e"))
print("***")
print(challenge10("4"))
print(challenge10("e"))