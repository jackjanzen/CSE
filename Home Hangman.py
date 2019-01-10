import random
import string
wordList = ["Pancakes? No!"]
word = random.choice(wordList)
uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
asciilegal = string.ascii_lowercase + string.ascii_uppercase
legalltrs = list(asciilegal)
word_listform = list(word)
guesseslft = 8
prior_guesses = []
disp_list = []
swapwordlist = list(word.swapcase())
totalword = swapwordlist + word_listform
for i in range(len(word)):
    if word_listform[i] in legalltrs:
        disp_list.append("_")
    else:
        disp_list.append(word_listform[i])

while guesseslft > 0 and "_" in disp_list:
    print(' '.join(disp_list))
    print("Tries left: %d" % guesseslft)
    guessltr = input("Guess a letter:")
    if guessltr not in prior_guesses and guessltr in legalltrs and guessltr in totalword:
        for letter in range(len(word_listform)):
            if guessltr == word_listform[letter]:
                print("Correct!")
                disp_list[letter] = guessltr
                prior_guesses.append(guessltr)
    elif guessltr not in legalltrs:
        print("That is not a valid letter. Please try again.")
    elif guessltr in prior_guesses:
        print("You already guessed that.")
    if guessltr not in word_listform and guessltr in legalltrs and guessltr not in list(word.swapcase()):
        guesseslft -= 1
        print("Incorrect.")
        prior_guesses.append(guessltr)
if guesseslft == 0:
    print("You ran out of turns. You Lose! The word was %s" % word)
if "_" not in disp_list:
    print("Congratulations! You guessed the word! The word was %s" % word)
