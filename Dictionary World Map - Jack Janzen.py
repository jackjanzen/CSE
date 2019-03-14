
world_map = {
    'W_OF_PIT': {
        'NAME': "West of Pit",
        'DESC': "Welcome to 14 Qyzpn at Chili's: A Choose Your Own Adventure game! "
                "You stand in a clearing with a pit in the center. Near the edge of the pit, "
                "a camp sits. It seems it has been abandoned for a long"
                " time. \nTo the far south, you can see"
                " the dark spires of a castle. "
                "\nOn the ground beside you there is a letter. You should probably "
                "read it "
                "before going further.",
        'PATHS': {
            'NORTH': "N_OF_PIT",
            'TO PIT': "EDGE_OF_PIT",
            'EAST': "E_OF_PIT",
            'SOUTH': "S_OF_PIT",
            'UP': "UP_OF_PIT"
        }
    },
    'N_OF_PIT': {
        'NAME': "North of Pit",
        'DESC': "You can see more of the castle now. A large insignia is visible with the letters "
                '"HW". \nColumns of smoke rise from the area behind the castle. They are extra'
                " visible against the "
                "orange sunset sky.",
        'PATHS': {
            'SOUTH': 'S_OF_PIT',
            'TO PIT': 'EDGE_OF_PIT',
            'EAST': 'E_OF_PIT',
            'WEST': 'W_OF_PIT',
            'UP': 'UP_OF_PIT'
        }
    },
    'S_OF_PIT': {
        'NAME': "South of Pit",
        'DESC': "The smell of steel and oil combined with the feeling that an awful"
                " artist is near dissuades you from going "
                "further south.",
        'PATHS': {
            'NORTH': 'N_OF_PIT',
            'TO PIT': 'EDGE_OF_PIT',
            'EAST': 'E_OF_PIT',
            'WEST': 'W_OF_PIT',
            'UP': 'UP_OF_PIT'
        }
    },
    'E_OF_PIT': {
        'NAME': "East of Pit",
        'DESC': "You can see the camp more clearly now. A lantern sits on top of a chest, the contents"
                " of which are unknown.",
        'PATHS': {
            'NORTH': 'N_OF_PIT',
            'TO PIT': 'EDGE_OF_PIT',
            'WEST': 'W_OF_PIT',
            'UP': 'UP_OF_PIT',
            'SOUTH': 'S_OF_PIT'
        }
    },
    'UP_OF_PIT': {
        'NAME': "Up of Pit",
        'DESC': "What?",
        'PATHS': {
            'NORTH': 'N_OF_PIT',
            'SOUTH': 'S_OF_PIT',
            'EAST': 'E_OF_PIT',
            'WEST': 'W_OF_PIT',
            'TO PIT': 'EDGE_OF_PIT',
            'UP': 'UP_UP_OF_PIT'
        }
    },
    'UP_UP_OF_PIT': {
        'NAME': "Up Up of Pit",
        'DESC': "No, really, what's the goal here?",
        'PATHS': {
            'NORTH': 'N_OF_PIT',
            'SOUTH': 'S_OF_PIT',
            'EAST': 'E_OF_PIT',
            'WEST': 'W_OF_PIT',
            'TO PIT': 'EDGE_OF_PIT',
            'UP': 'UP_UP_UP_OF_PIT'
        }
    },
    'UP_UP_UP_OF_PIT': {
        'NAME': "Up Up Up of Pit",
        'DESC': "Dude, stop. Seriously.",
        'PATHS': {
            'NORTH': 'N_OF_PIT',
            'SOUTH': 'S_OF_PIT',
            'EAST': 'E_OF_PIT',
            'WEST': 'W_OF_PIT',
            'TO PIT': 'EDGE_OF_PIT',
            'UP': 'UP4_OF_PIT'
        }
    },
    'UP4_OF_PIT': {
        'NAME': "Up Up Up Up of Pit",
        'DESC': "Can you please just do the quest? You know, I may be an omnipotent narrator, but I have to move "
                "to follow you.",
        'PATHS': {
            'NORTH': 'N_OF_PIT',
            'SOUTH': 'S_OF_PIT',
            'EAST': 'E_OF_PIT',
            'WEST': 'W_OF_PIT',
            'TO PIT': 'EDGE_OF_PIT',
            'UP': 'UP5_OF_PIT'
        }
    },
    'UP5_OF_PIT': {
        'NAME': "Up Up Up Up Up of Pit",
        'DESC': "What could you possibly want to go all the way up here? If you keep going, I'll have no choice "
                "but to call god.",
        'PATHS': {
            'NORTH': 'N_OF_PIT',
            'SOUTH': 'S_OF_PIT',
            'EAST': 'E_OF_PIT',
            'WEST': 'W_OF_PIT',
            'TO PIT': 'EDGE_OF_PIT',
            'UP': 'UP6_OF_PIT'
        }
    },
    'UP6_OF_PIT': {
        'NAME': "I'm really getting tired of writing all these ups.",
        'DESC': "Listen. This is Jack speaking. Yeah, THE Jack Elliot Janzen. The guy who made you and put you here."
                " \nThe guy that made the world around you. If you keep going, I'm gonna have to send you back to West"
                " of Pit. Neither of us want that, do we? \nSo, I'll cut you a deal. You go back NOW, or I'll send you "
                "back by force.",
        'PATHS': {
            'NORTH': 'N_OF_PIT',
            'SOUTH': 'S_OF_PIT',
            'EAST': 'E_OF_PIT',
            'WEST': 'W_OF_PIT',
            'TO PIT': 'EDGE_OF_PIT',
            'UP': 'W1_OF_PIT'
        }
    },
    'W1_OF_PIT': {
        'NAME': "West of Pit",
        'DESC': "Told you so. Welcome to 14 Qyzpn at Chili's: A Choose Your Own Adventure game! "
                "You stand in a clearing with a pit in the center. Near the edge of the pit, "
                "a camp sits. It seems it has been abandoned for a long"
                " time. \nTo the far south, you can see"
                " the dark spires of a castle. "
                "\nOn the ground beside you there is a letter. You should probably "
                "read it "
                "before going further.",
        'PATHS': {
            'NORTH': "N1_OF_PIT",
            'TO PIT': "EDGE1_OF_PIT",
            'EAST': "E1_OF_PIT",
            'SOUTH': "S1_OF_PIT",
            'UP': "UP1_OF_PIT"
        }
    },
    'N1_OF_PIT': {
        'NAME': "North of Pit",
        'DESC': "You can see more of the castle now. A large insignia is visible with the letters "
                '"HW". \nColumns of smoke rise from the area behind the castle. They are extra'
                " visible against the "
                "orange sunset sky.",
        'PATHS': {
            'SOUTH': 'S1_OF_PIT',
            'TO PIT': 'EDGE1_OF_PIT',
            'EAST': 'E1_OF_PIT',
            'WEST': 'W1_OF_PIT',
            'UP': 'UP1_OF_PIT'
        }
    },
    'S1_OF_PIT': {
        'NAME': "South of Pit",
        'DESC': "The smell of steel and oil combined with the feeling that an awful"
                " artist is near dissuades you from going "
                "further south.",
        'PATHS': {
            'NORTH': 'N1_OF_PIT',
            'TO PIT': 'EDGE1_OF_PIT',
            'EAST': 'E1_OF_PIT',
            'WEST': 'W1_OF_PIT',
            'UP': 'UP1_OF_PIT'
        }
    },
    'E1_OF_PIT': {
        'NAME': "East of Pit",
        'DESC': "You can see the camp more clearly now. A lantern sits on top of a chest, the contents"
                " of which are unknown",
        'PATHS': {
            'NORTH': 'N1_OF_PIT',
            'TO PIT': 'EDGE1_OF_PIT',
            'WEST': 'W1_OF_PIT',
            'UP': 'UP1_OF_PIT',
            'SOUTH': 'S1_OF_PIT'
        }
    },
    'EDGE1_OF_PIT': {
        'NAME': "Edge of Pit",
        'DESC': "There is an abandoned camp here. There is an unlocked chest in front of you, and a sword lying "
                "to the left of the chest.",
        'PATHS': {
            'NORTH': 'N1_OF_PIT',
            'SOUTH': 'S1_OF_PIT',
            'EAST': 'E1_OF_PIT',
            'WEST': 'W1_OF_PIT',
            'UP': 'UP1_OF_PIT',
            'DOWN': 'BOT_OF_PIT'
        }
    },
    'UP1_OF_PIT': {
        'NAME': "Up of Pit. Again. You don't quit, do you?",
        'DESC': "Nice try, buddy. Now this was fun, but go play the game. I won't hesitate to send you back again.",
        'PATHS': {
            'NORTH': 'N1_OF_PIT',
            'SOUTH': 'S1_OF_PIT',
            'EAST': 'E1_OF_PIT',
            'WEST': 'W1_OF_PIT',
            'UP': 'W1_OF_PIT',
            'DOWN': 'BOT_OF_PIT'
        }
    },
    'EDGE_OF_PIT': {
        'NAME': "Edge of Pit",
        'DESC': "There is a chest here with a lantern "
                "sitting on top. It appears to \nbe unlocked. "
                "The pit before you is deep. If you jump down, you"
                "\nprobably won't be able to"
                " get back up.",
        'PATHS': {
            'NORTH': 'N_OF_PIT',
            'SOUTH': 'S_OF_PIT',
            'EAST': 'E_OF_PIT',
            'WEST': 'W_OF_PIT',
            'UP': 'UP_OF_PIT',
            'DOWN': 'BOT_OF_PIT'
        }
    },
    'BOT_OF_PIT': {
        'NAME': 'Bottom Of Pit',
        'DESC': "You land on the wet stone floor at the bottom of the pit. "
                "It was stupid to jump that far down and everything hurts."
                " If we're being realistic you'd be dead right now."
                " \nBut, for the plot's sake, you lived. "
                "\nTo the west there is a bustling restaraunt with a sign over the door"
                " that reads, 'Popeye's'. To the south there is a dark room with strange noises"
                " coming from it. It would be wise to have a light with you before entering."
                " \nTo the east, there is a room with various pieces of "
                "battle-ready equipment.",
        'PATHS': {
            'WEST': 'POPEYES1',
            'EAST': 'EQ_ROOM_PIT',
            'SOUTH': 'SCHAM_N'
        }
    },
    'POPEYES1': {
        'NAME': 'Popeyes',
        'DESC': "The fluorescent lights on the ceiling make the restaurant impressively bright."
                "\nThe smell of fried chicken fills the air. A nice lady is standing behind the counter."
                " Perhaps you should ask her "
                "about the nature of this whimsical place.",
        'PATHS': {
            'EAST': 'BOT_OF_PIT'
        }
    },
    'EQ_ROOM_PIT': {
        'NAME': 'Equipment Room',
        'DESC': "There are various racks and armor stands arranged about the room."
                " Three swords are hung on one of the racks: a greatsword, a broadsword, and "
                "a longsword. \nYes, I use the Oxford "
                "Comma.\nThere is an armor stand. It has armor on it. "
                "\nThere is a locked gate on the "
                "northern wall.",
        'PATHS': {
            'WEST': 'BOT_OF_PIT'
        }
    },
    'SCHAM_N': {
        'NAME': 'South Chamber'
                'North Hall',
        'DESC': "Some guy that puts milk in before cereal blocks your path."
                " No one knows why he does this, he just"
                " does, and will argue with anyone that disagrees.\n"
                "To the East and West, there are two hallways. They curve to the south,"
                " but you can't see any "
                "light coming from "
                'there.',
        'PATHS': {
            'WEST': 'SCHAM_W',
            'EAST': 'SCHAM_E',
            'NORTH': 'BOT_OF_PIT'
        }
    },
    'SCHAM_W': {
        'NAME': 'South Chamber'
                'West Hall',
        'DESC': "Two Flat Earthers block your path. As soon as you walk into the room,"
                " they tell you about themselves. It's a married vegan couple named"
                " Marge and Ethan, \nwho have two children. \nWho are, of course,"
                " unvaccinated.\nAfter getting into a heated debate with them"
                " on the SHAPE OF THE EARTH, they begin to instigate a battle."
                "\nTo the North and the South, there are hallways.",
        'PATHS': {
            'NORTH': 'SCHAM_N',
            'SOUTH': 'SCHAM_S'
        }
    },
    'SCHAM_S': {
        'NAME': 'South Chamber'
                'South Hall',
        'DESC': "A Climate Change"
                "denier and a Flat Earther block your path. Need I say more?"
                "\nTo the East, West, and North there are hallways.",
        'PATHS': {
            'NORTH': 'SCHAM_C',
            'EAST': 'SCHAM_E',
            'WEST': 'SCHAM_W'

        }
    },
    'SCHAM_E': {
        'NAME': 'South Chamber'
                'East Hall',
        'DESC': "Two Flat Earthers block your path. As soon as you walk into the room,"
                " they tell you about themselves. \nIt's a married couple named"
                " John and Katherine, who have three children. Who are, of course,"
                " unvaccinated. \nKatherine says that crystal therapy"
                " is the only safe alternative to vaccines."
                "\nWhat an idiot.\nAfter getting into a heated debate with them"
                " on the SHAPE OF THE EARTH, they begin to instigate a battle."
                "\nTo the North and the South, there are "
                "hallways.",
        'PATHS': {
            'NORTH': 'SCHAM_N',
            'SOUTH': 'SCHAM_S'
        }
    },
    'SCHAM_C': {
        'NAME': 'South Chamber'
                'Center',
        'DESC': "Ben Shapiro himself blocks your path."
                "\n Rumor has it he ate 50,000 liberals in one sitting.\nWith his sharp wit,"
                "he dumbfounds you with pure FACTS and LOGIC, and begins to instigate a battle"
                ".\nTo the South there is a hallway.",
        'PATHS': {
            'SOUTH': 'SCHAM_S'
        }
    }
}


# Controller
playing = True
current_node = world_map['W_OF_PIT']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
misc_comm = ["TO PIT"]
short_mc = ["pit"]
while playing:
    print(current_node["NAME"])
    print(current_node['DESC'])
    command = input(">_")
    if command.lower() in short_directions:
        index = short_directions.index(command.lower())
        command = directions[index]
    elif command.lower() in short_mc:
        index = short_mc.index(command.lower())
        command = misc_comm[index]
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions or command.upper() in misc_comm:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")
