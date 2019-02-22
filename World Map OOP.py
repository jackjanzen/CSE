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


# Option 2 - Set all at once, modify controller
WOFPIT = Room("West of Pit", "x", 'NOFPIT', 'SOFPIT', 'EOFPIT', None, None, 'UPOFPIT', 'EDGEOFPIT')
NOFPIT = Room("North of Pit", "x", None, "SOFPIT", "EOFPIT", "WOFPIT", None, "UPOFPIT", 'EDGEOFPIT')
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
WBTURE = Room("Weiberture Science Laboratory", "x", 'LDLABS', None, None, None, None, None, None)
PEEC = Room("Popeye's", "x", None, None, None, None, None, None, None)
ECNHALL = Room("East Chamber | North Hall", "x", None, None, None, None, None, None, None)
ECWHALL = Room("East Chamber | West Hall", "x", None, None, None, None, None, None, None)
ECEHALL = Room("East Chamber | East Hall", "x", None, None, None, None, None, None, None)
ECSHALL = Room("East Chamber | South Hall", "x", None, None, None, None, None, None, None)
ECCENT = Room("East Chamber | Center", "x", None, None, None, None, None, None, None)
WCNHALL = Room("West Chamber | North Hall", "x", None, None, None, None, None, None, None)
WCWHALL = Room("West Chamber | West Hall", "x", None, None, None, None, None, None, None)
WCEHALL = Room("West Chamber | East Hall", "x", None, None, None, None, None, None, None)
WCSHALL = Room("West Chamber | South Hall", "x", None, None, None, None, None, None, None)
WCCENT = Room("West Chamber | Center", "x", None, None, None, None, None, None, None)

