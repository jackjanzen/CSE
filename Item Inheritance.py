import random


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
    def __init__(self, name, door):
        super(Key, self).__init__(name, 1)
        self.door = door


class EQKey(Key):
    def __init__(self, desc):
        super(EQKey, self).__init__("Equipment Room Key", EQDoor)
        self.desc = desc


class NCHAMKey(Key):
    def __init__(self, desc):
        super(NCHAMKey, self).__init__("North Chamber Key", NCHAMDoor)
        self.desc = desc


class Door(Item):
    def __init__(self, name, lockstatus):
        super(Door, self).__init__(name)
        self.lockstatus = lockstatus


class Character(object):
    def __init__(self, name, health, weapon, helm, chest, leg, boot):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.helm = helm
        self.chest = chest
        self.leg = leg
        self.boot = boot
        self.armor = helm + chest + leg + boot

    def take_damage(self, damage: int):
        if self.armor.hp > damage:
            print("No damage is done to %s!" % self.name)
            print("%s's armor takes %d damage." % (self.name, damage))
        elif self.armor.hp > 0:
            print("%s has armor, but some damage gets through!")
        else:
            self.health -= damage - self.armor.hp
            print("The attack hit for %d damage!" % (damage - self.armor.hp))
        print("%s has %d health left." % (self.name, self.health))

    def attack(self, target):
        try:
            print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
            if random.randint(1, 100) <= self.weapon.dodge:
                target.take_damage(self.weapon.damage)
                self.weapon.durability -= 1
            else:
                print("The attack missed!")
        except AttributeError:
            print("%s cannot attack! They do not have a weapon." % self.name)


sword = Weapon("Sword", 10, 1000, 50)
canoe = Weapon("Canoe", 42, 1000, 1)
wiebe_armor = Armor("Armor of the gods", 5792, 1, 1)

flat_earther1 = Character("Katherine", 1000, sword, Armor("Generic Armor", 2, 1, 1))
flat_earther2 = Character("John", 10000, canoe, wiebe_armor)
flat_earther3 = Character("Marge", 10000, canoe, wiebe_armor)
flat_earther4 = Character("Ethan", 10000, canoe, wiebe_armor)

flat_earther1.attack(flat_earther2)
flat_earther1.attack(flat_earther2)

