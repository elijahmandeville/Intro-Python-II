# Write a class to hold player information, e.g. what room they are in
# currently.
from random import randint


class Player:
    def __init__(self, name, current_room, weapon, inventory):
        self.name = name
        self.health = 20
        self.current_room = current_room
        self.inventory = inventory
        self.weapon = weapon

    def __str__(self):
        return f"\n Greetings, adventurer {self.name}, you're currently in the {self.current_room}. \n You currently have {self.health} health, and wield {self.weapon}"

    def attack(self, enemy):
        enemy.health -= self.weapon["damage"]
        print(
            f"You attacked for {self.weapon} damage! \n Your remaining health is {self.health}")

    def getInventory(self):
        return [item.name for item in self.inventory]

    def move(self, direction):
        try:
            if direction == 'w':
                self.current_room = self.current_room.n_to
            elif direction == 'd':
                self.current_room = self.current_room.e_to
            elif direction == 's':
                self.current_room = self.current_room.s_to
            elif direction == 'a':
                self.current_room = self.current_room.w_to
            print(f"\n {self.current_room}")
        except AttributeError:
            print("\n You cannot move in that direction")

    def search(self):

        if len(self.current_room.inventory) == 0:
            return print("You find nothing in the room")

        num = randint(0, len(self.current_room.inventory) - 1)
        current_item = self.current_room.inventory[num]
        selection = input(
            f"You've found {current_item}. Take it with you? \n Y for yes \n N for no ")
        if selection.lower() == 'y':
            if len(self.inventory.items) < self.inventory.capacity:
                print("No more room in your inventory!")
            self.inventory.items.append(current_item)
            self.current_room.inventory.remove(
                current_item)

            print(f"\n You've pickup up {current_item}")
        elif selection.lower() == 'n':
            print(
                f"\n You throw the {current_item} back on the ground and move on")
