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

    def print_desc(self):
        return self.desc


WOFPIT = Room("West of Pit", "You stand in a clearing with a pit in the center. Near the edge of the pit, "
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
SOFPIT = Room("South of Pit", "x", 'NOFPIT', None, "EOFPIT", "WOFPIT", None, 'UPOFPIT', 'EDGEOFPIT')
EOFPIT = Room("East of Pit", "x", 'NOFPIT', 'SOFPIT', None, "WOFPIT", None, 'UPOFPIT', 'EDGEOFPIT')
EDGEOFPIT = Room("Edge of Pit", "x", 'NOFPIT', 'SOFPIT', "EOFPIT", "WOFPIT", 'BOTOFPIT', 'UPOFPIT', None)
UPOFPIT = Room("Up of Pit", "x", 'NOFPIT', 'SOFPIT', "EOFPIT", "WOFPIT", None, None, 'EDGEOFPIT')
BOTOFPIT = Room("Bottom of Pit", "x", None, "SCNHALL", 'EQROOMPIT', 'PEPIT', None, None, None)
PEPIT = Room("Popeye's", "x", None, None, 'BOTOFPIT', None, None, None, None)
EQROOMPIT = Room("Equipment Room", "x", 'NCEHALL', None, None, 'BOTOFPIT', None, None, None)
SCNHALL = Room("South Chamber | North Hall", "x", 'BOTOFPIT', None, 'NCEHALL', 'NCWHALL', None, None, None)
SCWHALL = Room("South Chamber | West Hall", "x", 'SCNHALL', 'SCSHALL', None, None, None, None, None)
SCEHALL = Room("South Chamber | East Hall", "x", 'SCNHALL', 'SCSHALL', None, None, None, None, None)
SCSHALL = Room("South Chamber | South Hall", "x", 'SCCENT', None, 'SCEHALL', 'SCWHALL', None, None, None)
SCCENT = Room("South Chamber | Center", "x", None, 'SCSHALL', None, None, None, None, None)
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

current_location = NOFPIT
print(current_location.name)
print(current_location.desc)
