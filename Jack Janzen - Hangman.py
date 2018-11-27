import random
guesslft = 6
wordList = ["wiebe", "tiger", "edison", "school", "helicopter", "bookshelf", "pencil", "campus", "notebook", "desk"]
guessdltrs = []
print("Welcome to Hangman!")
print("You have 6 guesses to figure out what the word is by guessing letters.")
print("When you guess a letter, it does not count as a guess.")
print("This means that if you get the letter right on the first try, you'll still have six guesses remaining.")
print("This works the same way for the whole game")
word = random.choice(wordList)
word_listform = list(word)
guesseslft = 6
prior_guesses = []
disp_list = ["_"] * len(word)
wordidx = 0
letterslft = len(word)
while guesseslft > 0 and letterslft > 0:
    print(' '.join(disp_list))
    print("Guesses left: %d" % guesseslft)
    print("Letters left: %d" % letterslft)
    guessltr = input("Guess a letter:")
    if guessltr not in prior_guesses:
        for letter in range(len(word_listform)):
            if guessltr == word_listform[letter]:
                disp_list[letter] = guessltr
                letterslft -= 1
                prior_guesses.append(guessltr)
                print("Correct!")
    else:
        print("You already guessed that.")
    if guessltr not in word_listform:
        guesseslft -= 1
        print("Incorrect.")
        prior_guesses.append(guessltr)

if guesseslft == 0:
    print("You ran out of turns. You Lose!.")
    print("The actual word was %s" % word)
if letterslft == 0:
    print("Congratulations! You guessed the word!")
    print("The word was %s" % word)
