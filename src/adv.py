from room import Room
from player import Player
from item import Weapon, Item
from inventory import Inventory
from add_items import addItems


# Declare the meaning of life itself
life = True

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Initalize room items

addItems(room)

# Initalize player, name and weapon
new_name = input("What is your name, adventurer? ")
initial_weapon = Weapon("Bare Fists", "It's literally just your fists", 5)
player_inventory = Inventory([], 2)

new_player = Player(new_name, room["outside"],
                    initial_weapon, player_inventory)


print(new_player)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def check_input():
    selection = input("\n What would you like to do next? ")

    if selection == "m":
        check_movement(new_player)

    elif selection == "i":
        print(new_player.inventory)

    elif selection == "s":
        new_player.search()


def check_movement(player):
    global life

    selection = input("\n Where would you like to move? ")

    new_player.move(selection)


while life == True:
    try:
        check_input()

    except Exception:
        print("Please enter a valid value")
