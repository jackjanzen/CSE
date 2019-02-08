'''
print("Hello world!")
# This is a single line comment.
cars = 5
driving = True
print("I have %d cars." % cars)
print("I have " + str(cars) + " cars.")
age = input("How old are you?")
print("%s?! You're ancient!" % age)
colors = ["Green", "Yellow", "Red", "Blue", "Purple"]
colors.append("Cyan")
print(colors)
colors.pop(0)
print(colors)
print(colors[2])
'''

# Dictionaries

states = {
    "CA": "California",
    "FL": "Florida",
    "AK": "Alaska",
    "GA": "Georgia"
}

print(states)
print(states["AK"])

nested_dict = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000
    }
}
print("Population of " + nested_dict["GA"]["NAME"] + ":")
print(nested_dict["GA"]["POPULATION"])
print(nested_dict["FL"]["NAME"])

georgia = nested_dict["GA"]
print(georgia)

comp_dict = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000,
        "CITIES": [
            "Fresno",
            "San Francisco",
            "Los Angeles"
        ]
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000,
        "CITIES": [
            "Miami",
            "Orlando",
            "Tampa",
            "Jacksonville"
        ]
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000,
        "CITIES": [
            "Anchorage",
            "Fairbanks",
            "Juneau"
        ]
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000,
        "CITIES": [
            "Atlanta",
            "Savannah",
            "Augusta"
        ]
    }
}
print(comp_dict["AK"]["CITIES"][0])
print(comp_dict["FL"]["NAME"])
print(comp_dict["GA"]["CITIES"][0])

print(comp_dict.keys())
print(comp_dict.items())
print(nested_dict.items())

for key, value in comp_dict.items():
    print(key)
    print(value)
    print("-" * 20)
# this is what makes it look pretty
print()
for state, info in comp_dict.items():
    for label, stats in info.items():
        print(label)
        print(stats)
        print("-" * 20)
    print("=" * 20)

# other notes
states["AR"] = "Arizona?"  # it isnt arizona

states['AR'] = "Arkansas"  # fixed it.
print(states['AR'])
