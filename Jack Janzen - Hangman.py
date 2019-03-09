import random
import string
disp_list = []
wordList = ["Wiebe", "tiger", "Edison", "Deus Vult!", "helicopter", "bookshelf", "pencil", "campus", "notebook", "desk"]
word = random.choice(wordList)
legalltrs = list(string.ascii_letters)
word_listform = list(word)
guesseslft = 8
prior_guesses = []
swapwordlist = list(word.swapcase())
totalword = swapwordlist + word_listform
for i in range(len(word)):
    if word_listform[i] in legalltrs:
        disp_list.append("_")
    else:
        disp_list.append(word_listform[i])
solve = False
num = 0
while guesseslft > 0 and solve is False and "_" in disp_list:
    print(' '.join(disp_list))
    print("Tries left: %d" % guesseslft)
    if "_" in disp_list and solve is False:
        guessltr = input("Guess a letter or the word:")
        if len(list(guessltr)) > 1:
            guesswrd = list(guessltr)
            if len(guesswrd) == len(word_listform):
                for i in range(len(word_listform)):
                    if guesswrd[i] == word_listform[i] or guesswrd[i] == swapwordlist[i]:
                        num += 1
                if num == len(word_listform):
                    solve = True
                else:
                    print("Incorrect.")
                    guesseslft -= 1
            else:
                print("Incorrect.")
                guesseslft -= 1
        elif guessltr not in prior_guesses and guessltr in legalltrs and guessltr in totalword:
            print("Correct!")
            for letter in range(len(word_listform)):
                if guessltr == word_listform[letter] or guessltr == swapwordlist[letter]:
                    disp_list[letter] = word_listform[letter]
                    prior_guesses.append(guessltr)
                    prior_guesses.append(guessltr.swapcase())
        elif guessltr not in legalltrs:
            print("That is not a valid letter. Please try again.")
        elif guessltr in prior_guesses:
            print("You already guessed that.")
        elif guessltr not in word_listform and guessltr in legalltrs and guessltr not in list(word.swapcase()):
            guesseslft -= 1
            print("Incorrect.")
            prior_guesses.append(guessltr)
if solve is True:
    disp_list = []
if guesseslft == 0:
    print("You ran out of turns. You Lose! The word was %s" % word)
if "_" not in disp_list:
    print("Congratulations! You guessed the word! The word was %s" % word)
