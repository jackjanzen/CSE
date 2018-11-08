import random
guesslft = 6
wordlist = [["w", "i", "e", "b", "e"], ["t", "i", "g", "e", "r"], ["e", "d", "i", "s", "o", "n"]]
print("Welcome to Hangman!")
print("You have 6 guesses to figure out what the word is by guessing letters.")
print("When you guess a letter, it does not count as a guess.")
print("This means that if you get the letter right on the first try, you'll still have six guesses remaining.")
print("This works the same way for the whole game")
wordidx = random.randint(0, 2)
word = wordlist[wordidx]
while guesslft > 0:
    print("Guesses left: %d" % guesslft)
    guessltr = input("Guess a letter:")
    if guessltr in [word]:
        print("Correct!")
    else:
        print("Incorrect.")
        guesslft -= 1

