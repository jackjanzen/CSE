class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Instantiate the Dog object
mikey = Dog("Mikey", 6)

# call our instance methods
print(mikey.description())
print(mikey.speak("Gruff Gruff"))


class Human:

    species = 'Homosapien'

    def __init__(self, name, age, toxicity):
        self.name = name
        self.age = age
        self.toxicity = toxicity

    def description(self):
        return "{0} is {1} years old. {0} is a {3}. {0}'s toxicity level is {2}.".format(self.name, self.age,
                                                                                         self.toxicity, self.species)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


alecks = Human("Alecks", 15, "Defcon 10")

print(alecks.description())
print(alecks.speak("Jak is the greatest coder of all time."))

dict1 = {
        'name': 'Alecks',
        'age': 15
        }
dictnest = {
           'names': {'name1': 'Alecks', "name2": "Jak"},
           'ages': {'age1': 15, 'age2': 14}
           }
print("{0} is {1} years old.".format(dict1["name"], dictnest["ages"]['age1']))
print(dict1.get("name"))
print(dict1.get("age"))
print('{0} is {1} years old.'.format(dict1.get("name"), dict1.get("age")))
print(dict1)
# Updating Age in dict1
dict1["age"] = 16
print("{0} had a birthday! {0} is now {1} years old.".format(dict1.get("name"), dict1.get("age")))
print(dict1)
# Adding Address in dict1
dict1["address"] = "3294 N. Toxic Ave."
print("{0} bought a house. {0}'s address is {1}".format(dict1.get("name"), dict1.get("address")))
print(dict1)
# Updating age1 in ages in dictnest
dictnest['ages']['age1'] = 16
print(dictnest['ages']['age1'])




