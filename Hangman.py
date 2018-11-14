import random
guesslft = 6
wordlist = ["wiebe", "tiger", "edison", "school", "death", "underworld", "class", "prison", "help", "pain"]
wordlist.append("donuts")
guessdltrs = []
print("Welcome to Hangman!")
print("You have 6 guesses to figure out what the word is by guessing letters.")
print("When you guess a letter, it does not count as a guess.")
print("This means that if you get the letter right on the first try, you'll still have six guesses remaining.")
print("This works the same way for the whole game")
word = random.choice(wordlist)
word_listform = list(word)
letterlft = len(word_listform)
print(word)
print(word_listform)
disp_list = "_ " * len(word)
print(disp_list)
while guesslft > 0 and letterlft > 0:
    print("Guesses left: %d" % guesslft)
    print("Letters left: %d" % letterlft)
    guessltr = input("Guess a letter:")

    if guessltr in word_listform:
        print("Correct!")
        letterlft -= 1
    else:
        print("Incorrect.")
        guesslft -= 1

if guesslft <= 0:
    print("You Lose!")
if letterlft <= 0:
    print("You Won!")

print("The word was: %s" % word)
