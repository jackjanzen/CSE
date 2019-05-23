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
        self.hm = 0
        self.cp = 0
        self.lg = 0
        self.bt = 0
        self.armor = self.hm + self.cp + self.lg + self.bt
        self.helm = False
        self.chest = False
        self.leg = False
        self.boot = False
        self.weapon = None

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
        for gg in range(len(self.inventory)):
            if issubclass(type(self.inventory[gg]), Armor) is True:
                # Helmet
                if self.inventory[gg].part == 1 and self.helm is False:
                    self.hm = self.inventory[gg].hp
                    self.helm = True
                # Chestplate
                if self.inventory[gg].part == 2 and self.chest is False:
                    self.cp = self.inventory[gg].hp
                    self.chest = True
                # Leggings
                if self.inventory[gg].part == 3 and self.leg is False:
                    self.lg = self.inventory[gg].hp
                    self.leg = True
                # Boots
                if self.inventory[gg].part == 4 and self.boot is False:
                    self.bt = self.inventory[gg].hp
                    self.boot = True

    def take_damage(self, damage):
        self.armor_check()
        if self.armor > damage:
            self.armor -= damage
            print("The attack smashes into your armor! your armor has "
                  "%d health left." % self.armor)
        elif 0 < self.armor < damage:
            hadamage = damage - self.armor
            print("The attack breaks your armor! %d damage gets through." % hadamage)
            self.health -= hadamage
        elif self.armor <= 0:
            self.health -= damage
            print("The attack hit for %d damage!" % (damage - self.armor))
        if self.armor > 0:
            print("")
        print("You have %d health left." % self.health)

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


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage, durability, dodge):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.durability = durability
        self.dodge = dodge
        self.desc = str(name) + " || Damage: " + str(damage) + " || Durability: " + str(
            durability) + " || Accuracy: " + str(dodge)

    def desc_check(self):
        self.desc = "Name: " + str(self.name) + " || Damage: " + str(self.damage) + " || Durability: " + str(
            self.durability) + " || Accuracy: " + str(self.dodge)


class Broadsword(Weapon):
    def __init__(self):
        super(Broadsword, self).__init__("Steel Broadsword", 34, 30, 75)


class TIBroadsword(Weapon):
    def __init__(self):
        super(TIBroadsword, self).__init__("Tiger Iron Broadsword", 34, 40, 75)


class BWBroadsword(Weapon):
    def __init__(self):
        super(BWBroadsword, self).__init__("Bloodworked Broadsword", 50, 30, 75)


class Longsword(Weapon):
    def __init__(self):
        super(Longsword, self).__init__("Steel Longsword", 20, 50, 85)


class TILongsword(Weapon):
    def __init__(self):
        super(TILongsword, self).__init__("Tiger Iron Longsword", 20, 60, 85)


class BWLongsword(Weapon):
    def __init__(self):
        super(BWLongsword, self).__init__("Bloodworked Longsword", 30, 50, 85)


class Greatsword(Weapon):
    def __init__(self):
        super(Greatsword, self).__init__("Steel Greatsword", 50, 80, 65)


class TIGreatsword(Weapon):
    def __init__(self):
        super(TIGreatsword, self).__init__("Tiger Iron Greatsword", 50, 90, 65)


class BWGreatsword(Weapon):
    def __init__(self):
        super(BWGreatsword, self).__init__("Bloodworked Greatsword", 75, 80, 65)


class Bow(Weapon):
    def __init__(self, arrows):
        super(Bow, self).__init__("Wooden Longbow", 100, 100, 35)

        self.arrows = arrows


class TFBow(Weapon):
    def __init__(self, arrows):
        super(TFBow, self).__init__("True-Fire Longbow", 100, 100, 55)

        self.arrows = arrows


class MCBow(Weapon):
    def __init__(self, arrows):
        super(MCBow, self).__init__("Master-Crafted Longbow", 100, 110, 35)

        self.arrows = arrows


class Armor(Item):
    def __init__(self, name, hp, part, crit):
        super(Armor, self).__init__(name)
        self.hp = hp
        self.part = part
        self.crit = crit
        self.desc = str(self.name) + " || Hit Points: " + str(self.hp)


class Chestplate(Armor):
    def __init__(self):
        super(Chestplate, self).__init__("Steel Chestplate", 75, 2, True)


class TIChestplate(Armor):
    def __init__(self):
        super(TIChestplate, self).__init__("Tiger Iron Chestplate", 100, 2, True)


class Leggings(Armor):
    def __init__(self):
        super(Leggings, self).__init__("Steel Leggings", 75, 3, True)


class TILeggings(Armor):
    def __init__(self):
        super(TILeggings, self).__init__("Tiger Iron Leggings", 100, 3, True)


class Boots(Armor):
    def __init__(self):
        super(Boots, self).__init__("Steel Boots", 25, 4, True)


class TIBoots(Armor):
    def __init__(self):
        super(TIBoots, self).__init__("Tiger Iron Boots", 25, 4, True)


class Helmet(Armor):
    def __init__(self):
        super(Helmet, self).__init__("Steel Helmet", 25, 1, False)


class TIHelmet(Armor):
    def __init__(self):
        super(TIHelmet, self).__init__("Tiger Iron Helmet", 25, 1, False)


class Consumable(Item):
    def __init__(self, name, uses):
        super(Consumable, self).__init__(name)
        self.uses = uses


class Potion(Consumable):
    def __init__(self, name, effect):
        super(Potion, self).__init__(name, 1)
        self.effect = effect


class HPotion(Potion):
    def __init__(self):
        super(HPotion, self).__init__("Lesser Health Potion", 1)
        self.heal = 20


class H2Potion(Potion):
    def __init__(self):
        super(H2Potion, self).__init__("Greater Health Potion", 2)
        self.heal = 50


class Invis(Potion):
    def __init__(self):
        super(Invis, self).__init__("Invisibility Potion", 3)


class StartPage(Item):
    def __init__(self):
        super(StartPage, self).__init__("Welcome Page")
        self.script = '''
    Welcome to the world of Wiebalia, adventurer! Long ago, Dr. Wiebature invented 
a time machine deep underground. In an attempt to destroy his invention, take the blueprints,
and take credit for the construction, Dr. Wiebature's rival, Lord Heisenwiebe, caused the time
machine to melt down and created a rift in time. Through the use of this rift, Lord Heisenwiebe
met Al Capone and learned the ways of running the world through organized crime. Now, Lord
Heisenwiebe rules with an iron fist. I am Dr. Wiebature, and I need your help. When he took
over, I attempted to shut the rift to stop his advances, but by the time I succeeded, he
already learned enough to take over the planet. I know that he has hidden the key to stopping
him somewhere underground, but I am far too old to keep searching. Please brave adventurer,
finish what I could not, and take back the land that should be ruled with peace, not terror.
        Sincerely,
            D.W.
                      '''

    def read(self):
        print(self.script)


class Enemy(object):
    def __init__(self, name, health, weapon, armor, desc):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.desc = desc

    def take_damage(self, damage):
        if self.armor > damage:
            self.armor -= damage
            print("The attack smashes into %s's armor! %s's armor has "
                  "%d health left." % (self.name, self.name, self.armor))
        elif 0 < self.armor < damage:
            hadamage = damage - self.armor
            print("The attack breaks %s's armor! %d damage gets through." % (self.name, hadamage))
            self.health -= hadamage
        elif self.armor <= 0:
            self.health -= damage
            print("The attack hit for %d damage!" % (damage - self.armor))
        if self.armor > 0:
            print("")
        print("%s has %d health left." % (self.name, self.health))

    def attack(self, target):
        try:
            print("%s attacks you for %d damage" % (self.name, self.weapon.damage))
            if random.randint(1, 100) <= self.weapon.dodge:
                target.take_damage(self.weapon.damage)
                self.weapon.durability -= 1
                self.weapon.desc_check()
            else:
                print("The attack missed!")
        except AttributeError:
            print("%s cannot attack! They do not have a weapon." % self.name)


class Flat(Enemy):
    def __init__(self, num):
        super(Flat, self).__init__("", 50, tibroadsword, 0, None)
        self.name = "Flat Earther " + str(num)
        self.desc = "%s blocks your path." % self.name


class CCDeny(Enemy):
    def __init__(self, num):
        super(CCDeny, self).__init__("", 100, tilongsword, 0, None)
        self.name = "Climate Change Denier " + str(num)
        self.desc = "%s blocks your path." % self.name


class BenShap(Enemy):
    def __init__(self):
        super(BenShap, self).__init__("Ben Shapiro", 100, Greatsword(), 200, None)
        self.desc = "%s blocks your path. Fire leaps up around him as your heated " \
                    "debate begins. He shouts in a booming, lightning fast voice that facts don't care about" \
                    " your feelings." % self.name


class Igor(Enemy):
    def __init__(self, num):
        super(Igor, self).__init__("", 100, Longsword(), 0, None)
        self.name = "Igor " + str(num)
        self.desc = "%s blocks your path. He tells you to rob the bar cart." % self.name


class Mob(Enemy):
    def __init__(self, num):
        super(Mob, self).__init__("", 50, Broadsword(), 0, None)
        self.name = "Russian Mobster " + str(num)
        self.desc = "%s blocks your path. He says something in Russian. It didn't sound nice." % self.name


class Bert(Enemy):
    def __init__(self):
        super(Bert, self).__init__("The Machine", 100, BWGreatsword(), 125, None)
        self.desc = "A shirtless fat man blocks your path. His real name is Bert, but calling himself '%s'" \
                    " has been useful in befriending the Russians. \nHe drunkenly mutters something in Russian" \
                    " and begins the fight." % self.name


class Mobile(Enemy):
    def __init__(self, num):
        super(Mobile, self).__init__("", 25, Longsword(), 0, None)
        self.name = "Mobile Gamer " + str(num)
        self.desc = "%s blocks your path. He asks if you have games on your phone." % self.name


class GeoGamer(Enemy):
    def __init__(self):
        super(GeoGamer, self).__init__("Geometry Dash Gamer", 100, BWLongsword(), 50, None)
        self.desc = "An avid %s blocks your path. He's humming 'Stereo Madness'." % self.name


class Frostbite(Enemy):
    def __init__(self, num):
        super(Frostbite, self).__init__("", 50, Broadsword(), 0, None)
        self.name = "Frostbite " + str(num)
        self.desc = "%s blocks your path. It's what you get when you cross a vampire with a snowman." % self.name


class Untied(Enemy):
    def __init__(self, num):
        super(Untied, self).__init__("", 100, Longsword(), 0, None)
        self.name = "Untied Shoe " + str(num)
        self.desc = "%s blocks your path. I don't know what it's laced with, but it'll have you tripping" \
                    " all day." % self.name


class Kyle(Enemy):
    def __init__(self):
        super(Kyle, self).__init__("Kyle, King of Humor", 100, TILongsword(), 250, None)
        self.desc = "%s blocks your path. It's Bad Joke Friday, but his jokes are so bad, " \
                    "they'll send you back to Monday." % self.name


# inits

#   Items

#       Armor

boots = Boots()
chestplate = Chestplate()
helmet = Helmet()
leggings = Leggings()
tiboots = TIBoots()
tichestplate = TIChestplate()
tihelmet = TIHelmet()
tileggings = TILeggings()

#        Weapons

broadsword = Broadsword()
bwbroadsword = BWBroadsword()
bwgreatsword = BWGreatsword()
bwlongsword = BWLongsword()
greatsword = Greatsword()
longsword = Longsword()
tibroadsword = TIBroadsword()
tilongsword = TILongsword()
tigreatsword = TIGreatsword()

#        Potions

h2potion1 = H2Potion()
h2potion2 = H2Potion()
h2potion3 = H2Potion()
h2potion4 = H2Potion()
h2potion5 = H2Potion()
h2potion6 = H2Potion()
h2potion7 = H2Potion()
h2potion8 = H2Potion()
h2potion9 = H2Potion()
h2potion10 = H2Potion()
h2potion11 = H2Potion()
h2potion12 = H2Potion()
h2potion13 = H2Potion()
h2potion14 = H2Potion()
h2potion15 = H2Potion()
h2potion16 = H2Potion()
h2potion17 = H2Potion()
h2potion18 = H2Potion()
h2potion19 = H2Potion()
h2potion20 = H2Potion()
h2potion21 = H2Potion()
h2potion22 = H2Potion()
h2potion23 = H2Potion()
h2potion24 = H2Potion()
h2potion25 = H2Potion()
h2potion26 = H2Potion()
h2potion27 = H2Potion()
h2potion28 = H2Potion()
h2potion29 = H2Potion()
h2potion30 = H2Potion()

hpotion1 = HPotion()
hpotion2 = HPotion()
hpotion3 = HPotion()
hpotion4 = HPotion()
hpotion5 = HPotion()
hpotion6 = HPotion()
hpotion7 = HPotion()
hpotion8 = HPotion()
hpotion9 = HPotion()
hpotion10 = HPotion()
hpotion11 = HPotion()
hpotion12 = HPotion()
hpotion13 = HPotion()
hpotion14 = HPotion()
hpotion15 = HPotion()
hpotion16 = HPotion()
hpotion17 = HPotion()
hpotion18 = HPotion()
hpotion19 = HPotion()
hpotion20 = HPotion()
hpotion21 = HPotion()
hpotion22 = HPotion()
hpotion23 = HPotion()
hpotion24 = HPotion()
hpotion25 = HPotion()
hpotion26 = HPotion()
hpotion27 = HPotion()
hpotion28 = HPotion()
hpotion29 = HPotion()
hpotion30 = HPotion()

invis1 = Invis()
invis2 = Invis()
invis3 = Invis()

#        Papers

startpage = StartPage()

#        Enemies

# South Chamber
ccdeny1 = CCDeny(1)
ccdeny2 = CCDeny(2)
ccdeny3 = CCDeny(3)
ccdeny4 = CCDeny(4)

flat1 = Flat(1)
flat2 = Flat(2)
flat3 = Flat(3)
flat4 = Flat(4)

benshap = BenShap()

# North Chamber
mob1 = Mob(1)
mob2 = Mob(2)
mob3 = Mob(3)
mob4 = Mob(4)

igor1 = Igor(1)
igor2 = Igor(2)
igor3 = Igor(3)
igor4 = Igor(4)

bert = Bert()

# West Chamber

mobile1 = Mobile(1)
mobile2 = Mobile(2)
mobile3 = Mobile(3)
mobile4 = Mobile(4)
mobile5 = Mobile(5)
mobile6 = Mobile(6)
mobile7 = Mobile(7)
mobile8 = Mobile(8)
mobile9 = Mobile(9)
mobile10 = Mobile(10)
mobile11 = Mobile(11)
mobile12 = Mobile(12)
mobile13 = Mobile(13)
mobile14 = Mobile(14)
mobile15 = Mobile(15)
mobile16 = Mobile(16)
mobile17 = Mobile(17)
mobile18 = Mobile(18)
mobile19 = Mobile(19)
mobile20 = Mobile(20)
mobile21 = Mobile(21)
mobile22 = Mobile(22)
mobile23 = Mobile(23)

geogamer = GeoGamer()

# East Chamber

frostbite1 = Frostbite(1)
frostbite2 = Frostbite(2)
frostbite3 = Frostbite(3)
frostbite4 = Frostbite(4)

untied1 = Untied(1)
untied2 = Untied(2)
untied3 = Untied(3)
untied4 = Untied(4)

kyle = Kyle()

#        In Progress

# tfbow = TFBow(None, 50)
# mcbow = MCBow(None, 100)


# Characters

# Rooms


WOFPIT = Room("West of Pit", "You stand in a clearing with a pit in the center. Near the edge of the pit, "
                             "a camp sits. It seems it has been abandoned for a long"
                             " time. \nTo the far south, you can see"
                             " the dark spires of a castle. "
                             "\nOn the ground beside you there is a letter. You should probably "
                             "read it "
                             "before going further. (Dont read it. Doesn't work.)", [startpage], None, 'NOFPIT',
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
                                   "\nThere is a locked gate on the "
                                   "northern wall.", [helmet, chestplate, leggings, boots, broadsword, greatsword,
                                                      longsword],
                                   None, 'NCEHALL', None, None, 'BOTOFPIT', None, None, None)
SCNHALL = Room("South Chamber | North Hall", "You enter into a dark, damp room. Moss clings to the stone walls, and"
                                             " water drips from the ceiling.\nA fat droplet smacks your cheek."
                                             "To the East and West, there are two hallways. They curve to the south,"
                                             " but you can't see any "
                                             "light coming from "
                                             "there.", None, [ccdeny1, flat1], 'BOTOFPIT', None, 'SCEHALL', 'SCWHALL',
               None, None, None)
SCWHALL = Room("South Chamber | West Hall", "As you move through the halls, the rooms begin to get warmer. Guess your"
                                            " debates with all these idiots got pretty heated.\nNot my best joke.\n"
                                            "But in all seriousness, the incessant ceiling drip has begun to slow. "
                                            "It's almost as if it's evaporating before falling off the ceiling."
                                            "\nTo the North and the South, there are hallways."
                                            "", None, [ccdeny2, flat2], 'SCNHALL', 'SCSHALL', None, None, None, None,
               None)
SCEHALL = Room("South Chamber | East Hall", "As you move through the halls, the rooms begin to get warmer. Guess your"
                                            " debates with all these idiots got pretty heated.\nNot my best joke.\n"
                                            "But in all seriousness, the incessant ceiling drip has begun to slow. "
                                            "It's almost as if it's evaporating before falling off the ceiling."
                                            "\nTo the North and the South, there are hallways."
               , None, [ccdeny3, flat3], 'SCNHALL', 'SCSHALL', None,
               None, None, None, None)
SCSHALL = Room("South Chamber | South Hall", "A Climate Change"
                                             "denier and a Flat Earther block your path. Need I say more?"
                                             "\nTo the East, West, and North there are hallways."
                                             "", None, [ccdeny4, flat4], 'SCCENT', None, 'SCEHALL', 'SCWHALL',
               None, None, None)
SCCENT = Room("South Chamber | Center", "It's insanely hot in this room. You could use some water, but Jack didn't"
                                        " feel like adding in a thirst feature. \nOr water for that matter."
                                        "\nTo the South there is a hallway."
                                        "", [greatsword, tileggings], [benshap], None, 'SCSHALL', None, None, None,
              None, None)
NCEHALL = Room("North Chamber | East Hall", "x", None, [igor1, mob1], 'NCNHALL', 'NCSHALL', None, None, None,
               None, None)
NCNHALL = Room("North Chamber | North Hall", "x", None, [igor2, mob2], None, None, 'NCEHALL', 'NCWHALL', None,
               None, None)
NCSHALL = Room("North Chamber | South Hall", "x", None, [igor3, mob3], None, None, 'NCEHALL', 'NCWHALL', None,
               None, None)
NCWHALL = Room("North Chamber | West Hall", "x", None, [igor4, mob4], 'NCNHALL', 'NCSHALL', 'NCCENT', None,
               None, None, None)
NCCENT = Room("North Chamber | Center", "x", [bwlongsword, tiboots], [bert], None, 'PENC', 'LDLABS', 'NCWHALL',
              None, None, None)
PENC = Room("Popeye's", "x", None, None, 'NCCENT', None, None, None, None, None, None)
LDLABS = Room("Long's Drugs", "x", None, None, None, 'WBTURE', None, 'NCCENT', None, None, None)
WBTURE = Room("Weiberture Science Laboratory", "x", [tichestplate, tihelmet, invis1, invis2, invis3], None, 'LDLABS',
              None, 'ECNHALL', 'PEWC', None, None, None)
PEWC = Room("Popeye's", "x", None, None, None, 'WCNHALL', 'WBTURE', None, None, None, None)
ECNHALL = Room("East Chamber | North Hall", "x", [frostbite1, untied1], None, 'WBTURE', None, 'ECEHALL', 'ECWHALL',
               None, None, None)
ECWHALL = Room("East Chamber | West Hall", "x", [frostbite2, untied2], None, 'ECNHALL', 'ECSHALL',
               None, None, None, None, None)
ECEHALL = Room("East Chamber | East Hall", "x", [frostbite3, untied3], None, 'ECNHALL', 'ECSHALL',
               None, None, None, None, None)
ECSHALL = Room("East Chamber | South Hall", "x", [frostbite4, untied4], None, 'ECCENT', None, 'ECEHALL', 'ECWHALL',
               None, None, None)
ECCENT = Room("East Chamber | Center", "x", [tibroadsword], [kyle], None, 'ECSHALL', None, None, None, None, None)
WCNHALL = Room("West Chamber | North Hall", "x", None, [mobile1, mobile2, mobile3, mobile4, mobile5], 'PEWC',
               None, 'WCEHALL', 'WCWHALL', None, None, None)
WCWHALL = Room("West Chamber | West Hall", "x", None, [mobile6, mobile7, mobile8, mobile9, mobile10], 'WCNHALL',
               'WCSHALL', None, None, None, None, None)
WCEHALL = Room("West Chamber | East Hall", "x", None, [mobile11, mobile12, mobile13, mobile14, mobile15], 'WCNHALL',
               "WCSHALL", None, None, None, None, None)
WCSHALL = Room("West Chamber | South Hall", "x", None, [mobile16, mobile17, mobile18, mobile19, mobile20],
               'WCCENT', None, 'WCEHALL', 'WCWHALL', None, None, None)
WCCENT = Room("West Chamber | Center", "x", [tigreatsword], [geogamer, mobile21, mobile22, mobile23], None,
              'WCSHALL', None, None, None, None, None)

# Player
player = Player(WOFPIT)

current_location = player.current_location

# Controller
playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
misc_comm = ["to_pit"]
short_mc = ["pit"]
event = False
fighting = False
invisible = False
while playing:
    if event is False:
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
        if player.current_location.character is not None:
            fighting = True
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
                event = False
                try:
                    next_room = player.find_next_room(command.lower())
                    player.move(next_room)
                except KeyError:
                    print("I can't go that way.")
                    event = True
            else:
                print("I can't run, there is an enemy here.")
                event = True
# Take
        elif command.lower()[0:4] == "take":
            event = True
            command1 = "take"
            jac = command.lower().split()
            thing = " ".join(jac[1:])
            try:
                grabbed = False
                for i in range(len(player.current_location.item)):
                    if player.current_location.item[i - 1].name.lower() == thing.lower():
                        itemindex = i - 1
                        if issubclass(type(player.current_location.item[itemindex]), Weapon) is True:
                            if player.weapon is None:
                                player.weapon = player.current_location.item[itemindex]
                            else:
                                print("You dropped your %s." % player.weapon.name)
                                vary = player.weapon
                                player.weapon = player.current_location.item[itemindex]
                                player.current_location.item.append(vary)
                                player.inventory.remove(vary)
                        player.inventory.insert(0, player.current_location.item[itemindex])
                        print(player.current_location.item[itemindex].name + " has been added to your inventory.")
                        player.current_location.item.pop(itemindex)
                        grabbed = True
                if grabbed is False:
                    print("That item is not here.")
            except TypeError:
                print("There is nothing to pick up.")
# Inventory
        elif command.lower() == "inventory":
            event = True
            for i in range(len(player.inventory)):
                print(player.inventory[i].name)
# Describe
        elif command.lower() == "describe":
            event = False
# Attack
        elif command.lower()[0:6] == "attack":
            event = True
            attack_list = command.lower().split()
            targ = attack_list[1:]
            targ = " ".join(targ)
            targe = ""
            attacked = False
            for i in player.current_location.character:
                if i.name.lower() == targ:
                    targ = i
                    player.attack(targ)
                    attacked = True
                    if targ.health <= 0:
                        print(targ.name + " was killed!")
                        player.current_location.character.remove(targ)
                        if len(player.current_location.character) == 0:
                            player.current_location.character = None
                            fighting = False
                    else:
                        for x in player.current_location.character:
                            x.attack(player)
                            if player.health <= 0:
                                print("You died. Thanks for playing!")
                                playing = False
            if attacked is False:
                print("That enemy is not here.")
                event = True
        elif command.lower()[0:3] == "use":
            thang = command.lower().split()[1:]
            thang = " ".join(thang)
            for i in player.inventory:
                if thang == player.inventory[i].name.lower():



        else:
            event = True
            print("Command Not Found")
# ----------------------------------------------
# Skip Description
    else:
        if player.current_location.character is not None:
            fighting = True
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
                event = False
                try:
                    next_room = player.find_next_room(command.lower())
                    player.move(next_room)
                except KeyError:
                    print("I can't go that way.")
                    event = True
            else:
                print("I can't run, there is an enemy here.")
                event = True
        # Take
        elif command.lower()[0:4] == "take":
            event = True
            command1 = "take"
            jac = command.lower().split()
            thing = " ".join(jac[1:])
            try:
                grabbed = False
                for i in range(len(player.current_location.item)):
                    if player.current_location.item[i - 1].name.lower() == thing.lower():
                        itemindex = i - 1
                        if issubclass(type(player.current_location.item[itemindex]), Weapon) is True:
                            if player.weapon is None:
                                player.weapon = player.current_location.item[itemindex]
                            else:
                                print("You dropped your %s." % player.weapon.name)
                                vary = player.weapon
                                player.current_location.item.append(vary)
                                player.weapon = player.current_location.item[itemindex]
                                player.inventory.remove(vary)
                        player.inventory.insert(0, player.current_location.item[itemindex])
                        print(player.current_location.item[itemindex].name + " has been added to your inventory.")
                        player.current_location.item.pop(itemindex)
                        grabbed = True
                if grabbed is False:
                    print("That item is not here.")
            except TypeError:
                print("There is nothing to pick up.")
        # Inventory
        elif command.lower() == "inventory":
            event = True
            for i in range(len(player.inventory)):
                print(player.inventory[i].name)
        # Describe
        elif command.lower() == "describe":
            event = False
        # Attack
        elif command.lower()[0:6] == "attack":
            event = True
            attack_list = command.lower().split()
            targ = attack_list[1:]
            targ = " ".join(targ)
            targe = ""
            attacked = False
            for i in player.current_location.character:
                if i.name.lower() == targ:
                    targ = i
                    player.attack(targ)
                    attacked = True
                    if targ.health <= 0:
                        print(targ.name + " was killed!")
                        player.current_location.character.remove(targ)
                        if len(player.current_location.character) == 0:
                            player.current_location.character = None
                            fighting = False
                    else:
                        for x in player.current_location.character:
                            x.attack(player)
                            if player.health <= 0:
                                print("You died. Thanks for playing!")
                                playing = False
            if attacked is False:
                print("That enemy is not here.")
                event = True
        else:
            event = True
            print("Command Not Found")
