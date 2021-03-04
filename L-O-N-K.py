
class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name


class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5


class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust. " \
                           "Somewhat more dangerous than a rock."
        self.damage = 10


class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty sword"
        self.description = "This sword is showing its age, " \
                           "but still has some fight in it."
        self.damage = 20

inventory = ['Dagger','Gold(5)','Crusty Bread']

def play():
    action_input = get_player_command()
    user_name = input("What is your name? ")

    print("Hello, " + user_name)

    print("You find yourself lying in a small meadow.\n")
    print(action_input)

def get_player_command():
    return input('>> ')

def display_inventory():
    print(inventory)
    for item in inventory:
        print('* ' + str(item))
    best_weapon = most_powerful_weapon(inventory)
    print("Your best weapon is your {}".format(best_weapon))

def most_powerful_weapon(inventory):
    max_damage = 0
    best_weapon = None
    for item in inventory:
        try:
            if item.damage > max_damage:
                best_weapon = item
                max_damage = item.damage
        except AttributeError:
            pass

    return best_weapon