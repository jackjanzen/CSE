
world_map = {
    'W_OF_PIT': {
        'NAME': "West of Pit",
        'DESC': "You wake up in a clearing in the middle of a vast forest. "
                "There is a piece of paper with what seems to be instructions on it on the ground beside you. "
                "In the center, there is a large pit with something glowing at the bottom of it,"
                " casting a spotlight into the moonlit sky. It's probably wise to do some exploring after reading the"
                " page.",
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
        'DESC': "Having moved further north, you can see columns of smoke and black spires reaching over the treetops.",
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
        'DESC': "A strong smell of steel and oil combined with a feeling that a poor artist lies somewhere beyond the"
                " trees futher to the south leaves a crater in your stomach. It's probably not best to go back there"
                " before you have completed the page's task.",
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
        'DESC': "There looks to be an abandoned camp near the edge of the pit; it might be wise to go check it for "
                "supplies. You can see the orange sun slowly begin to hide itself behind the treetops, which are "
                "dressed in silhouette.",
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
                " The guy that made the world around you. If you keep going, I'm gonna have to send you back to West"
                " of Pit. Neither of us want that, do we? So, I'll cut you a deal. You go back NOW, or I'll send you "
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
        'DESC': "Told you so. You wake up in a clearing in the middle of a vast forest. "
                "There is a piece of paper with what seems to be instructions on it on the ground beside you. "
                "In the center, there is a large pit with something glowing at the bottom of it,"
                " casting a spotlight into the orange sky. It's probably wise to do some exploring after reading the"
                " page.",
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
        'DESC': "Having moved further north, you can see columns of smoke and black spires reaching over the treetops.",
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
        'DESC': "A strong smell of steel and oil combined with a feeling that a poor artist lies somewhere beyond the"
                " trees futher to the south leaves a crater in your stomach. It's probably not best to go back there"
                " before you have completed the page's task.",
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
        'DESC': "There looks to be an abandoned camp near the edge of the pit; it might be wise to go check it for "
                "supplies. You can see the orange sun slowly begin to hide itself behind the treetops, which are "
                "dressed in silhouette.",
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
        'DESC': "There is an abandoned camp here. There is an unlocked chest in front of you, and a sword lying "
                "to the left of the chest.",
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
        'DESC': "The old willow tree in the center of the pit broke your fall, and you find yourself "
                "face-down on the hard rock floor.",
        'PATHS': {
            'WEST': 'POPEYES1',
            'EAST': 'EQ_ROOM_PIT',
            'SOUTH': 'SCHAM_N'
        }
    },
    'POPEYES1': {
        'NAME': 'Popeyes',
        'DESC': "x",
        'PATHS': {
            'EAST': 'BOT_OF_PIT'
        }
    },
    'EQ_ROOM_PIT': {
        'NAME': 'Equipment Room',
        'DESC': 'x',
        'PATHS': {
            'WEST': 'BOT_OF_PIT'
        }
    },
    'SCHAM_N': {
        'NAME': 'South Chamber'
                'North Hall',
        'DESC': 'x',
        'PATHS': {
            'WEST': 'SCHAM_W',
            'EAST': 'SCHAM_E',
            'NORTH': 'BOT_OF_PIT'
        }
    },
    'SCHAM_W': {
        'NAME': 'South Chamber'
                'West Hall',
        'DESC': 'x',
        'PATHS': {
            'NORTH': 'SCHAM_N',
            'SOUTH': 'SCHAM_S'
        }
    },
    'SCHAM_S': {
        'NAME': 'South Chamber'
                'South Hall',
        'DESC': 'x',
        'PATHS': {
            'NORTH': 'SCHAM_C',
            'EAST': 'SCHAM_E',
            'WEST': 'SCHAM_W'

        }
    },
    'SCHAM_E': {
        'NAME': 'South Chamber'
                'East Hall',
        'DESC': 'x',
        'PATHS': {
            'NORTH': 'SCHAM_N',
            'SOUTH': 'SCHAM_S'
        }
    },
    'SCHAM_C': {
        'NAME': 'South Chamber'
                'Center',
        'DESC': 'x',
        'PATHS': {
            'SOUTH': 'SCHAM_S'
        }
    }
}

overworld = ["N_OF_PIT", "S_OF_PIT", "E_OF_PIT", "W_OF_PIT", "UP_OF_PIT", "EDGE_OF_PIT"]
in_pit_1 = ['BOT_OF_PIT', 'POPEYES1']

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
