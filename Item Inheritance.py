class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage, durability, dodge):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.durability = durability
        self.dodge = dodge


class Broadsword(Weapon):
    def __init__(self, desc):
        super(Broadsword, self).__init__("Steel Broadsword", 34, 30, 75)
        self.desc = desc
        

class TIBroadsword(Weapon):
    def __init__(self, desc):
        super(TIBroadsword, self).__init__("Tiger Iron Broadsword", 34, 40, 75)
        self.desc = desc
        

class BWBroadsword(Weapon):
    def __init__(self, desc):
        super(BWBroadsword, self).__init__("Bloodworked Broadsword", 50, 30, 75)
        self.desc = desc


class Longsword(Weapon):
    def __init__(self, desc):
        super(Longsword, self).__init__("Steel Longsword", 20, 50, 85)
        self.desc = desc


class TILongsword(Weapon):
    def __init__(self, desc):
        super(TILongsword, self).__init__("Tiger Iron Longsword", 20, 60, 85)
        self.desc = desc


class BWLongsword(Weapon):
    def __init__(self, desc):
        super(BWLongsword, self).__init__("Bloodworked Longsword", 30, 50, 85)
        self.desc = desc


class Greatsword(Weapon):
    def __init__(self, desc):
        super(Greatsword, self).__init__("Steel Greatsword", 50, 80, 65)
        self.desc = desc


class TIGreatsword(Weapon):
    def __init__(self, desc):
        super(TIGreatsword, self).__init__("Tiger Iron Greatsword", 50, 90, 65)
        self.desc = desc


class BWGreatsword(Weapon):
    def __init__(self, desc):
        super(BWGreatsword, self).__init__("Bloodworked Greatsword", 75, 80, 65)
        self.desc = desc
