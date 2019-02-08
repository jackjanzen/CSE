import random
import string
wordList = ["wiebe", "tiger", "edison", "school", "folder", "bookshelf", "pencil", "campus", "notebook", "desk"]
word = random.choice(wordList)
asciilegal = string.ascii_lowercase
legalltrs = list(asciilegal)
word_listform = list(word)
guesseslft = 6
prior_guesses = []
disp_list = ["_"] * len(word)
while guesseslft > 0 and "_" in disp_list:
    print(' '.join(disp_list))
    print("Tries left: %d" % guesseslft)
    guessltr = input("Guess a letter:")
    if guessltr not in prior_guesses and guessltr in legalltrs:
        for letter in range(len(word_listform)):
            if guessltr == word_listform[letter]:
                print("Correct!")
                disp_list[letter] = guessltr
                prior_guesses.append(guessltr)
    elif guessltr not in legalltrs:
        print("That is not a valid letter. Please try again.")
    else:
        print("You already guessed that.")
    if guessltr not in word_listform and guessltr in legalltrs:
        guesseslft -= 1
        print("Incorrect.")
        prior_guesses.append(guessltr)
if guesseslft == 0:
    print("You ran out of turns. You Lose! The word was %s" % word)
if "_" not in disp_list:
    print("Congratulations! You guessed the word! The word was %s" % word)
