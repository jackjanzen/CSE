import random


class God(object):

    def __init__(self, mindsize, number, name):
        self.name = name
        self.mind = mindsize
        self.number = number
        self.age = 'Infinite'
        self.plane = 'Omniscient'

    def shake_god(self):
        if self.mind == 'small':
            answer_list = ['Yes', 'No', 'Maybe']
            input("What do you wish to ask the small-minded god?")
            return 'You vigorously shake the ' \
                   'small-minded god. He says ' + random.choice(answer_list) + '.'
        elif self.mind == 'vast':
            answer_list = ['Yes', 'No', 'Maybe', 'Probably', 'Probably Not']
            input("What do you wish to ask the vast-minded god?")
            return 'You vigorously ' \
                   'shake the vast-minded god. He says ' + random.choice(answer_list) + "."
        elif self.mind == 'infinite':
            answer_list = ['Yes', 'No', 'Maybe', 'Probably', 'Probably Not', 'It is up to you, my child.',
                           "I didn't hear you. Can you ask again, dear child?"]
            input("What do you wish to ask the god with the infinite mind?")
            return 'You vigorously shake the god ' \
                   'with the infinite mind. He says ' + random.choice(answer_list) + "."
        else:
            return "{} is not a valid mind size. Please try again.".format(self.mind)

    def call(self):
        numcorrect = False
        while numcorrect is False:
            numask = int(input("Please enter %s's number. >_" % self.name))
            if numask == self.number:
                return "This is where I would perform the function god.call_god."
            else:
                print("That was not the correct number. Please try again.")


smallgod = God('small', 333, "Small-minded God")
vastgod = God('vast', 222, "Vast-minded God")
infgod = God('infinite', 111, "God with the Infinite Mind")
alecks = God('very small', 420, "Alecks")
'''
print(smallgod.shake_god())
print(vastgod.shake_god())
print(infgod.shake_god())
print(alecks.shake_god())
'''
print(smallgod.call())
print(vastgod.call())
print(infgod.call())
print(alecks.call())
