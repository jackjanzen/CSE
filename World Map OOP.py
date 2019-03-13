class Room(object):
    def __init__(self, name, desc, north=None, south=None, east=None, west=None, down=None, up=None, to_pit=None):
        self.name = name
        self.desc = desc
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.down = down
        self.up = up
        self.to_pit = to_pit
        self.characters = []

    def print_desc(self):
        return self.desc


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

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


class PeLady(object):
    def __init__(self, desc=None, dialogue=None, ):
        self.name = "Deidrie Henry"
        self.desc = desc
        self.dialogue = dialogue


WOFPIT = Room("West of Pit", "Welcome to 14 Qyzpn at Chili's: A Choose Your Own Adventure game! "
                             "You stand in a clearing with a pit in the center. Near the edge of the pit, "
                             "a camp sits. It seems it has been abandoned for a long"
                             " time. \nTo the far south, you can see"
                             " the dark spires of a castle. "
                             "\nOn the ground beside you there is a letter. You should probably "
                             "read it "
                             "before going further.", 'NOFPIT', 'SOFPIT', 'EOFPIT', None, None, 'UPOFPIT', 'EDGEOFPIT')
NOFPIT = Room("North of Pit", "You can see more of the castle now. A large insignia is visible with the letters "
                              '"HW". \nColumns of smoke rise from the area behind the castle. They are extra'
                              " visible against the "
                              "orange sunset sky.", None, "SOFPIT", "EOFPIT", "WOFPIT", None, "UPOFPIT", 'EDGEOFPIT')
SOFPIT = Room("South of Pit", "The smell of steel and oil combined with the feeling that an awful"
                              " artist is near dissuades you from going "
                              "further south.", 'NOFPIT', None, "EOFPIT", "WOFPIT", None, 'UPOFPIT', 'EDGEOFPIT')
EOFPIT = Room("East of Pit", "You can see the camp more clearly now. A lantern sits on top of a chest, the contents"
                             " of which are unknown.", 'NOFPIT', 'SOFPIT', None, "WOFPIT", None, 'UPOFPIT', 'EDGEOFPIT')
EDGEOFPIT = Room("Edge of Pit", "There is a chest here with a lantern "
                                "sitting on top. It appears to \nbe unlocked. "
                                "The pit before you is deep. If you jump down, you"
                                "\nprobably won't be able to"
                                " get back up.", 'NOFPIT', 'SOFPIT', "EOFPIT", "WOFPIT", 'BOTOFPIT', 'UPOFPIT', None)
UPOFPIT = Room("Up of Pit", "What?", 'NOFPIT', 'SOFPIT', "EOFPIT", "WOFPIT", None, None, 'EDGEOFPIT')
UP2OFPIT = Room("Up Up of Pit", "No, really, what's "
                                "the goal here?", 'NOFPIT', 'SOFPIT', "EOFPIT", "WOFPIT", None, None, 'EDGEOFPIT')
UP3OFPIT = Room("Up Up Up of Pit", "Dude, "
                                   "stop. Seriously.", 'NOFPIT', 'SOFPIT', "EOFPIT", "WOFPIT", None, None, 'EDGEOFPIT')
UP4OFPIT = Room("Up Up Up Up of Pit", "Can you please just do the quest? You know, I may be an omnipotent narrator, "
                                      "but I have to move "
                                      "to follow you.", 'NOFPIT', 'SOFPIT', "EOFPIT", "WOFPIT", None, None, 'EDGEOFPIT')
UP5OFPIT = Room("5(Up) of Pit", "What could you possibly want to go all the way up here? If you keep going, "
                                "I'll have no choice "
                                "but to call god.", 'NOFPIT', 'SOFPIT', "EOFPIT", "WOFPIT", None, None, 'EDGEOFPIT')
UP6OFPIT = Room("I'm getting tired of writing all these Ups.",
                "Listen. This is Jack speaking. Yeah, THE Jack Elliot Janzen. The guy who made you and"
                " put you here."
                " The guy that made the world around you.\nIf you keep going, "
                "I'm gonna have to send you back to West"
                " of Pit. Neither of us want that, do we? So, I'll cut"
                " you a deal. You go back NOW, or I'll send you "
                "back by force.", 'NOFPIT', 'SOFPIT', "EOFPIT", "WOFPIT", None, None, 'EDGEOFPIT')
BOTOFPIT = Room("Bottom of Pit", "You land on the wet stone floor at the bottom of the pit. "
                                 "It was stupid to jump that far down and everything hurts."
                                 " If we're being realistic you'd be dead right now."
                                 " \nBut, for the plot's sake, you lived. "
                                 "\nTo the west there is a bustling restaraunt with a sign over the door"
                                 " that reads, 'Popeye's'. \nTo the south there is a dark room with strange noises"
                                 " coming from it. It would be wise to have a light with you before entering."
                                 " \nTo the east, there is a room with various pieces of "
                                 "battle-ready equipment.", None, "SCNHALL", 'EQROOMPIT', 'PEPIT', None, None, None)
PEPIT = Room("Popeye's", "The fluorescent lights on the ceiling make the restaurant impressively bright."
                         "\nThe smell of fried chicken fills the air. A nice lady is standing behind the counter."
                         " Perhaps you should ask her "
                         "about the nature of this whimsical place.", None, None, 'BOTOFPIT', None, None, None, None)
EQROOMPIT = Room("Equipment Room", "There are various racks and armor stands arranged about the room."
                                   " Three swords are hung on one of the racks: a greatsword, a broadsword, and "
                                   "a longsword. \nYes, I use the Oxford "
                                   "Comma.\nThere is an armor stand. It has armor on it. "
                                   "\nThere is a locked gate on the "
                                   "northern wall.", 'NCEHALL', None, None, 'BOTOFPIT', None, None, None)
SCNHALL = Room("South Chamber | North Hall", "Some guy that puts milk in before cereal blocks your path."
                                             " No one knows why he does this, he just"
                                             " does, and will argue with anyone that disagrees.\n"
                                             "To the East and West, there are two hallways. They curve to the south,"
                                             " but you can't see any "
                                             "light coming from "
                                             "there.", 'BOTOFPIT', None, 'NCEHALL', 'NCWHALL', None, None, None)
SCWHALL = Room("South Chamber | West Hall", "Two Flat Earthers block your path. As soon as you walk into the room,"
                                            " they tell you about themselves. It's a married vegan couple named"
                                            " Marge and Ethan, \nwho have two children. \nWho are, of course,"
                                            " unvaccinated.\nAfter getting into a heated debate with them"
                                            " on the SHAPE OF THE EARTH, they begin to instigate a battle."
                                            "\nTo the North and the South, there are hallways."
                                            "", 'SCNHALL', 'SCSHALL', None, None, None, None, None)
SCEHALL = Room("South Chamber | East Hall", "Two Flat Earthers block your path. As soon as you walk into the room,"
                                            " they tell you about themselves. \nIt's a married couple named"
                                            " John and Katherine, who have three children. Who are, of course,"
                                            " unvaccinated. \nKatherine says that crystal therapy"
                                            " is the only safe alternative to vaccines."
                                            "\nWhat an idiot.\nAfter getting into a heated debate with them"
                                            " on the SHAPE OF THE EARTH, they begin to instigate a battle."
                                            "\nTo the North and the South, there are "
                                            "hallways.", 'SCNHALL', 'SCSHALL', None, None, None, None, None)
SCSHALL = Room("South Chamber | South Hall", "A Climate Change"
                                             "denier and a Flat Earther block your path. Need I say more?"
                                             "\nTo the East, West, and North there are hallways."
                                             "", 'SCCENT', None, 'SCEHALL', 'SCWHALL', None, None, None)
SCCENT = Room("South Chamber | Center", "Ben Shapiro himself blocks your path."
                                        "\n Rumor has it he ate 50,000 liberals in one sitting.\nWith his sharp wit,"
                                        "he dumbfounds you with pure FACTS and LOGIC, and begins to instigate a battle"
                                        ".\nTo the South there is a hallway."
                                        "", None, 'SCSHALL', None, None, None, None, None)
NCEHALL = Room("North Chamber | East Hall", "x", 'NCNHALL', 'NCSHALL', 'EQROOMPIT', None, None, None, None)
NCNHALL = Room("North Chamber | North Hall", "x", None, None, 'NCEHALL', 'NCWHALL', None, None, None)
NCSHALL = Room("North Chamber | South Hall", "x", None, None, 'NCEHALL', 'NCWHALL', None, None, None)
NCWHALL = Room("North Chamber | West Hall", "x", 'NCNHALL', 'NCSHALL', 'NCCENT', None, None, None, None)
NCCENT = Room("North Chamber | Center", "x", None, 'PENC', 'LDLABS', 'NCWHALL', None, None, None)
PENC = Room("Popeye's", "x", 'NCCENT', None, None, None, None, None, None)
LDLABS = Room("Long's Drugs", "x", None, 'WBTURE', None, 'NCCENT', None, None, None)
WBTURE = Room("Weiberture Science Laboratory", "x", 'LDLABS', None, 'ECNHALL', 'PEWC', None, None, None)
PEWC = Room("Popeye's", "x", None, 'WCNHALL', 'WBTURE', None, None, None, None)
ECNHALL = Room("East Chamber | North Hall", "x", 'WBTURE', None, 'ECEHALL', 'ECWHALL', None, None, None)
ECWHALL = Room("East Chamber | West Hall", "x", 'ECNHALL', 'ECSHALL', None, None, None, None, None)
ECEHALL = Room("East Chamber | East Hall", "x", 'ECNHALL', 'ECSHALL', None, None, None, None, None)
ECSHALL = Room("East Chamber | South Hall", "x", 'ECCENT', None, 'ECEHALL', 'ECWHALL', None, None, None)
ECCENT = Room("East Chamber | Center", "x", None, 'ECSHALL', None, None, None, None, None)
WCNHALL = Room("West Chamber | North Hall", "x", 'PEWC', None, 'WCEHALL', 'WCWHALL', None, None, None)
WCWHALL = Room("West Chamber | West Hall", "x", 'WCNHALL', 'WCSHALL', None, None, None, None, None)
WCEHALL = Room("West Chamber | East Hall", "x", 'WCNHALL', "WCSHALL", None, None, None, None, None)
WCSHALL = Room("West Chamber | South Hall", "x", 'WCCENT', None, 'WCEHALL', 'WCWHALL', None, None, None)
WCCENT = Room("West Chamber | Center", "x", None, 'WCSHALL', None, None, None, None, None)

current_location = SCSHALL
print(current_location.name)
print(current_location.desc)
player = Player(WOFPIT)
'''
# Controller
playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
# short_directions = ['n', 's', 'e', 'w', 'u', 'd']
# misc_comm = ["to pit"]
# short_mc = ["pit"]
while playing:
    print(player.current_location.name)
    print(player.current_location.desc)
    command = input(">_")
    # if command.lower() in short_directions:
    #     index = short_directions.index(command.lower)
    #     command = directions[index]
    # elif command.lower() in short_mc:
    #     index = short_mc.index(command.lower())
    #     command = misc_comm[index]
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:  # or command.lower() in misc_comm:
        try:
            next_room = player.find_next_room(command.lower())
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command Not Found")
'''
