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


class Bow(Weapon):
    def __init__(self, desc, arrows):
        super(Bow, self).__init__("Wooden Longbow", 100, 100, 35)
        self.desc = desc
        self.arrows = arrows


class TFBow(Weapon):
    def __init__(self, desc, arrows):
        super(TFBow, self).__init__("True-Fire Longbow", 100, 100, 55)
        self.desc = desc
        self.arrows = arrows


class MCBow(Weapon):
    def __init__(self, desc, arrows):
        super(MCBow, self).__init__("Master-Crafted Longbow", 100, 110, 35)
        self.desc = desc
        self.arrows = arrows


class Armor(Item):
    def __init__(self, name, hp, part, crit):
        super(Armor, self).__init__(name)
        self.hp = hp
        self.part = part
        self.crit = crit


class Chestplate(Armor):
    def __init__(self, desc):
        super(Chestplate, self).__init__("Steel Chestplate", 75, 2, True)
        self.desc = desc


class TIChestplate(Armor):
    def __init__(self, desc):
        super(TIChestplate, self).__init__("Tiger Iron Chestplate", 100, 2, True)
        self.desc = desc


class Leggings(Armor):
    def __init__(self, desc):
        super(Leggings, self).__init__("Steel Leggings", 75, 3, True)
        self.desc = desc


class TILeggings(Armor):
    def __init__(self, desc):
        super(TILeggings, self).__init__("Tiger Iron Leggings", 100, 3, True)
        self.desc = desc


class Boots(Armor):
    def __init__(self, desc):
        super(Boots, self).__init__("Steel Boots", 25, 4, True)
        self.desc = desc


class TIBoots(Armor):
    def __init__(self, desc):
        super(TIBoots, self).__init__("Tiger Iron Boots", 25, 4, True)
        self.desc = desc


class Helmet(Armor):
    def __init__(self, desc):
        super(Helmet, self).__init__("Steel Helmet", 25, 1, False)
        self.desc = desc


class TIHelmet(Armor):
    def __init__(self, desc):
        super(TIHelmet, self).__init__("Tiger Iron Helmet", 25, 1, False)
        self.desc = desc


class Consumable(Item):
    def __init__(self, name, uses):
        super(Consumable, self).__init__(name)
        self.uses = uses


<<<<<<< HEAD
class HPotion(Consumable):
    def __init__(self, restvalue, desc):
        super(HPotion, self).__init__("Lesser Health Potion", 1)
        self.restvalue = restvalue
        self.desc = desc
=======
class Potion(Consumable):
    def __init__(self, name, effect):
        super(Potion, self).__init__(name, 1)
        self.effect = effect


class HPotion(Potion):
    def __init__(self, desc):
        super(HPotion, self).__init__("Lesser Health Potion", 1)
        self.desc = desc


class H2Potion(Potion):
    def __init__(self, desc):
        super(H2Potion, self).__init__("Greater Health Potion", 2)
        self.desc = desc


class Invis(Potion):
    def __init__(self, desc):
        super(Invis, self).__init__("Invisibility Potion", 3)
        self.desc = desc


class Key(Consumable):
    
>>>>>>> fc1b51814e8847f15e800d0ced30e83018fc6652
