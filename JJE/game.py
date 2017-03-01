# This is the new main game file.
class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "I guess this is a weapon. " \
                "About the size of your hand."
        self.damage = 1

class Blunt_Sword(Weapon):
    def __init__(self):
        self.name = "Blunt Sword"
        self.description = "More useful as a club than a cutting tool."
        self.damage = 5

class Pistol(Weapon):
    def __init__(self):
        self.name = "9mm Pistol"
        self.description = "Bang bang!"
        self.damage = 20

def play():
    inventory = [Rock(), Blunt_Sword(), 'Pennies(2)', 'Moldy Bread']
    print("Escape from the abandoned mansion!")
    while True:
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            print("Go North!")
        elif action_input in ['s', 'S']:
            print("Go South!")
        elif action_input in ['e', 'E']:
            print("Go East!")
        elif action_input in ['w', 'W']:
            print("Go West young man!")
        elif action_input in ['i', 'I']:
            print("Inventory: ")
            for item in inventory:
                print('* ' + str(item))
        else:
            print("Invalid option!")

def get_player_command():
    return input('Action (N, S, E, W, I: ')

def strongest_weapon(inventory):
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

play()