import random


class Room(object):
    def __init__(self, name, desc, item, character, north=None, south=None,
                 east=None, west=None, down=None, up=None, to_pit=None):
        self.name = name
        self.desc = desc
        self.item = item
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.down = down
        self.up = up
        self.to_pit = to_pit
        self.character = character

    def print_desc(self):
        return self.desc


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []
        self.health = 100
        self.helm = None
        self.chest = None
        self.leg = None
        self.boot = None
        self.weapon = None
        self.armor = 0

    def attack(self, target):
        try:
            print("You attack %s for %d damage." % (target.name, self.weapon.damage))
            if random.randint(1, 100) <= self.weapon.dodge:
                target.take_damage(self.weapon.damage)
                self.weapon.durability -= 1
                self.weapon.desc_check()
            else:
                print("The attack missed!")
        except AttributeError:
            print("You cannot attack! You do not have a weapon.")

    def armor_check(self):
        # Helmet
        if self.helm is None:
            pass
        else:
            if self.helm.hp <= 0:
                self.helm = None
                print("Your helmet broke.")
            self.armor += self.helm.hp
        # Chestplate
        if self.chest is None:
            pass
        else:
            if self.chest.hp <= 0:
                self.chest = None
                print("Your chestplate broke.")
            self.armor += self.chest.hp
        # Leggings
        if self.leg is None:
            pass
        else:
            if self.leg.hp <= 0:
                self.leg = None
                print("Your leggings broke.")
            self.armor += self.leg.hp
        # Boots
        if self.boot is None:
            pass
        else:
            if self.boot.hp <= 0:
                self.boot = None
                print("Your boots broke.")
            self.armor += self.boot.hp

    def take_damage(self, damage):
        self.armor_check()
        damaged = False
        # Helmet
        if self.helm is None:
            pass
        elif damaged is False:
            self.helm.hp -= damage
            damaged = True
            self.armor_check()
            print("The attack smashes into your helmet. Your helmet has %d HP left." % self.helm.hp)
        # Boots
        if self.boot is None:
            pass
        elif damaged is False:
            self.boot.hp -= damage
            damaged = True
            self.armor_check()
            print("The attack smashes into your boots. Your boots have %d HP left." % self.boot.hp)
        # Leggings
        if self.leg is None:
            pass
        elif damaged is False:
            self.leg.hp -= damage
            damaged = True
            self.armor_check()
            print("The attack smashes into your leggings. Your leggings have %d HP left." % self.leg.hp)
        # Chestplate
        if self.chest is None:
            pass
        elif damaged is False:
            self.chest.hp -= damage
            damaged = True
            self.armor_check()
            print("The attack smashes into your chestplate. Your chestplate has %d HP left." % self.chest.hp)
        if damaged is False and self.helm is None and self.chest is None and self.leg is None and self.boot is None:
            self.health -= damage
            print("You took %d damage. You are at %d health" % (damage, self.health))

    def move(self, new_location):
        """This moves the player to a new room.

        :param new_location: The room object of which you are going to.
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """

        :param direction: The direction that you want to move to.
        :return: The Room object if it exists, or None if it does not.
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


WOFPIT = Room("West of Pit", "You stand in a clearing with a pit in the center. Near the edge of the pit, "
                             "a camp sits. It seems it has been abandoned for a long"
                             " time. \nTo the far south, you can see"
                             " the dark spires of a castle. "
                             "\nOn the ground beside you there is a letter. You should probably "
                             "read it "
                             "before going further. (Type 'pit' to go to the pit)", [], None, 'NOFPIT',
              'SOFPIT', 'EOFPIT', None, None,
              'UPOFPIT', 'EDGEOFPIT')
NOFPIT = Room("North of Pit", "You can see more of the castle now. A large insignia is visible with the letters "
                              '"HW". \nColumns of smoke rise from the area behind the castle. They are extra'
                              " visible against the "
                              "orange sunset sky.", None, None, None, "SOFPIT", "EOFPIT", "WOFPIT", None, "UPOFPIT",
              'EDGEOFPIT')
SOFPIT = Room("South of Pit", "The smell of steel and oil combined with the feeling that an awful"
                              " artist is near dissuades you from going "
                              "further south.", None, None, 'NOFPIT', None, "EOFPIT", "WOFPIT", None, 'UPOFPIT',
              'EDGEOFPIT')
EOFPIT = Room("East of Pit", "You can see the camp more clearly now. A lantern sits on top of a chest, the contents"
                             " of which are unknown.", None, None, 'NOFPIT', 'SOFPIT', None, "WOFPIT", None, 'UPOFPIT',
              'EDGEOFPIT')
EDGEOFPIT = Room("Edge of Pit", "The pit before you is deep. If you jump down, you"
                                "\nprobably won't be able to"
                                " get back up.", None, None, 'NOFPIT', 'SOFPIT', "EOFPIT", "WOFPIT", 'BOTOFPIT',
                 'UPOFPIT', None)
UPOFPIT = Room("Up of Pit", "What?", None, None, 'NOFPIT', 'SOFPIT', "EOFPIT", "WOFPIT", None, 'UP2OFPIT', 'EDGEOFPIT')
UP2OFPIT = Room("Up Up of Pit", "No, really, what's "
                                "the goal here?", None, None, 'NOFPIT', 'SOFPIT', "EOFPIT", "WOFPIT", None, 'UP3OFPIT',
                'EDGEOFPIT')
UP3OFPIT = Room("Up Up Up of Pit", "Dude, "
                                   "stop. Seriously.", None, None, 'NOFPIT', 'SOFPIT', "EOFPIT", "WOFPIT", None,
                'UP4OFPIT', 'EDGEOFPIT')
UP4OFPIT = Room("Up Up Up Up of Pit", "Can you please just do the quest? You know, I may be an omnipotent narrator, "
                                      "but I have to move "
                                      "to follow you.", None, None, 'NOFPIT', 'SOFPIT', "EOFPIT", "WOFPIT", None,
                'UP5OFPIT', 'EDGEOFPIT')
UP5OFPIT = Room("5(Up) of Pit", "What could you possibly want to go all the way up here? If you keep going, "
                                "I'll have no choice "
                                "but to call god.", None, None, 'NOFPIT', 'SOFPIT', "EOFPIT", "WOFPIT", None,
                'UP6OFPIT', 'EDGEOFPIT')
UP6OFPIT = Room("I'm getting tired of writing all these Ups.",
                "Listen. This is Jack speaking. Yeah, THE Jack Elliot Janzen. The guy who made you and"
                " put you here."
                " The guy that made the world around you.\nIf you keep going, "
                "I'm gonna have to send you back to West"
                " of Pit. Neither of us want that, do we? So, I'll cut"
                " you a deal. You go back NOW, or I'll send you "
                "back by force.", None, None, 'NOFPIT', 'SOFPIT', "EOFPIT", "WOFPIT", None, 'WOFPIT', 'EDGEOFPIT')
BOTOFPIT = Room("Bottom of Pit", "You land on the wet stone floor at the bottom of the pit. "
                                 "It was stupid to jump that far down and everything hurts."
                                 " If we're being realistic you'd be dead right now."
                                 " \nBut, for the plot's sake, you lived. "
                                 "\nTo the south there is a dark room with strange noises"
                                 " coming from it."
                                 " \nTo the east, there is a room with various pieces of "
                                 "battle-ready equipment.", None, None, None, "SCNHALL", 'EQROOMPIT', None,
                None, None, None)
PEPIT = Room("Popeye's", "The fluorescent lights on the ceiling make the restaurant impressively bright."
                         "\nThe smell of fried chicken fills the air. A sign on the wall reads:\n   Welcome to Popeye's"
                         "", None, None, None, None, None, None, None, None, None)
EQROOMPIT = Room("Equipment Room", "There are various racks and armor stands arranged about the room."
                                   " Three swords are hung on one of the racks: a greatsword, a broadsword, and "
                                   "a longsword. \nYes, I use the Oxford "
                                   "Comma.\nThere is an armor stand. It has armor on it. "
                                   "\nThere is an open gate on the "
                                   "northern wall.", [],
                 None, 'NCEHALL', None, None, 'BOTOFPIT', None, None, None)
SCNHALL = Room("South Chamber | North Hall", "You enter into a dark, damp room. Moss clings to the stone walls, and"
                                             " water drips from the ceiling.\nA fat droplet smacks your cheek."
                                             "To the East and West, there are two hallways. They curve to the south,"
                                             " but you can't see any "
                                             "light coming from "
                                             "there.", None, [], 'BOTOFPIT', None, 'SCEHALL', 'SCWHALL',
               None, None, None)
SCWHALL = Room("South Chamber | West Hall", "As you move through the halls, the rooms begin to get warmer. Guess your"
                                            " debates with all these idiots got pretty heated.\nNot my best joke.\n"
                                            "But in all seriousness, the incessant ceiling drip has begun to slow. "
                                            "It's almost as if it's evaporating before falling off the ceiling."
                                            "\nTo the North and the South, there are hallways."
                                            "", [], [], 'SCNHALL', 'SCSHALL', None, None, None, None,
               None)
SCEHALL = Room("South Chamber | East Hall", "As you move through the halls, the rooms begin to get warmer. Guess your"
                                            " debates with all these idiots got pretty heated.\nNot my best joke.\n"
                                            "But in all seriousness, the incessant ceiling drip has begun to slow. "
                                            "It's almost as if it's evaporating before falling off the ceiling."
                                            "\nTo the North and the South, there are hallways.", [], 'SCNHALL',
               'SCSHALL', None,
               None, None, None, None)
SCSHALL = Room("South Chamber | South Hall", "It's getting very hot now. You press your hand against the back of the"
                                             " North door. It seems like the heat is coming from there."
                                             "\nTo the East, West, and North there are hallways."
                                             "", None, [], 'SCCENT', None, 'SCEHALL', 'SCWHALL',
               None, None, None)
SCCENT = Room("South Chamber | Center", "It's insanely hot in this room. You could use some water, but Jack didn't"
                                        " feel like adding in a thirst feature. \nOr water for that matter."
                                        "\nTo the South there is a hallway."
                                        "", [], None, 'SCSHALL', None, None, None,
              None, None)
NCEHALL = Room("North Chamber | East Hall", "You can faintly hear Rasputin by Boney M."
                                            " playing off in the distance."
                                            "\nWhat an amazing song. Absolute masterpiece. You just want to dance"
                                            " your heart out. Too bad you're trying to save the world."
                                            "\nTo the North and South, there are hallways.", [], [],
               'NCNHALL', 'NCSHALL', 'EQROOMPIT', None, None,
               None, None)
NCNHALL = Room("North Chamber | North Hall", "Rasputin is getting louder the farther you advance through"
                                             "the chamber. It's a great song, but its starting to get annoying."
                                             "\nYou can also see increasing amounts of broken vodka"
                                             " bottles on the ground.\nOh, those Russians. \nTo the "
                                             "East and West, there are hallways.", None,
               [], None, None, 'NCEHALL', 'NCWHALL', None,
               None, None)
NCSHALL = Room("North Chamber | South Hall", "Rasputin is getting louder the farther you advance through"
                                             " the chamber. It's a great song, but its starting to get annoying."
                                             "\nYou can also see increasing amounts of broken vodka"
                                             " bottles on the ground.\nOh, those Russians. \nTo the "
                                             "East and West, there are hallways.", None, [], None,
               None, 'NCEHALL', 'NCWHALL', None,
               None, None)
NCWHALL = Room("North Chamber | West Hall", "Moskau is playing VERY loudly now. Funnily enough, Moskau is by a German"
                                            " band. Strange, huh?\nIf hearing damage were programmed in to this "
                                            "game then I'd tell you "
                                            "to bring earplugs before going in the room in front of you. "
                                            "\nTo the North and South there are hallways.",
               None, [], 'NCNHALL', 'NCSHALL', 'NCCENT', None,
               None, None, None)
NCCENT = Room("North Chamber | Center", "Russian Hardbass has started blasting out of two massive subwoofers "
                                        "in opposite corners of the room. "
                                        "\nIt hurts to listen to, but you have the sudden "
                                        "urge to slav squat. \nTo the East there is a hallway.",
              [], [], None, 'PENC', 'LDLABS', 'NCWHALL',
              None, None, None)

player = Player(WOFPIT)

current_location = player.current_location

# Controller
playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
misc_comm = ["to_pit"]
short_mc = ["pit"]

fighting = False
invisible = False
invisibility = 0
while playing:
    print(player.current_location.name)
    print(player.current_location.desc)
    # --------------DEBUG--------------
    try:
        if len(player.current_location.item) is 0:
            player.current_location.item = None
    except TypeError:
        pass
    if player.current_location.item is None:
        print("There are no items here.")
    else:
        try:
            x = False
            for i in range(len(player.current_location.item)):
                if x is False:
                    x = True
                    print("Items:")
                try:
                    print(player.current_location.item[i].desc)
                except AttributeError:
                    print(player.current_location.item[i].name)
            x = False
        except TypeError:
            pass
    try:
        if len(player.current_location.character) is 0:
            player.current_location.character = None
    except TypeError:
        pass
    if player.current_location.character is None:
        print("There is nobody here.")
    else:
        try:
            x = False
            for i in range(len(player.current_location.character)):
                if x is False:
                    x = True
                try:
                    print(player.current_location.character[i].desc)
                except AttributeError:
                    print(player.current_location.character[i].name)
            x = False
        except TypeError:
            pass
    # ---------------------------------
    firstchecker = False
    if invisibility <= 0:
        invisible = False
        if firstchecker:
            print("Your invisiblity wore off.")
            firstchecker = False
    else:
        invisibility -= 1
        if invisibility <= 0:
            firstchecker = True
        print("Your invisibility has %d turns left." % invisibility)
        invisible = True
    if player.current_location.character is not None and invisible is False:
        fighting = True
    elif invisible:
        fighting = False
    command = input(">_")
    # Short Command Converter
    if command.lower() in short_directions:
        index = short_directions.index(command.lower())
        command = directions[index]
    # Misc Short Command Converter
    elif command.lower() in short_mc:
        index = short_mc.index(command.lower())
        command = misc_comm[index]
    # Quit
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    # Move
    elif command.lower() in directions or command.lower() in misc_comm:
        if not fighting:

            try:
                next_room = player.find_next_room(command.lower())
                player.move(next_room)
            except KeyError:
                print("I can't go that way.")

        else:
            print("I can't run, there is an enemy here.")

    else:
        print("Command Not Found.")
