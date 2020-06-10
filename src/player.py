# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, weapon):
        self.name = name
        self.health = 20
        self.current_room = current_room
        self.inventory = []
        self.weapon = weapon

    def __str__(self):
        return f"Greetings, adventurer {self.name}, you're currently in the {self.current_room}. \n You currently have {self.health} health, and wield {self.weapon}"

    def attack(self, enemy):
        enemy.health -= self.weapon["damage"]
        print(
            f"You attacked for {self.weapon} damage! \n Your remaining health is {self.health}")

    def getInventory(self):
        return [item.name for item in self.inventory]
