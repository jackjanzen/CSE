class Room(object):
    def __init__(self, name, desc, north=None, south=None, east=None, west=None, down=None, up=None):
        self.name = name
        self.desc = desc
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.down = down
        self.up = up


# Option 2 - Set all at once, modify controller
R19A = Room("Mr. Wiebe's Room", 'parking_lot')
parking_lot = Room("Parking Lot", None, "R19A")
