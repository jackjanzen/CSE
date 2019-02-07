
world_map = {
    'W_OF_PIT': {
        'NAME': "West of Pit",
        'DESC': "x",
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
        'DESC': "x",
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
        'DESC': "x",
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
        'DESC': "x",
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
            'TO PIT': 'EDGE_OF_PIT'
        }
    },
    'EDGE_OF_PIT': {
        'NAME': "Edge of Pit",
        'DESC': "x",
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
        'DESC': "x",
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
