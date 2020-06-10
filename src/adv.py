from room import Room
from player import Player
from weapon import Weapon

# Declare the meaning of life itself
life = True

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# Initalize name and weapon
new_name = input("What is your name, adventurer? ")
initial_weapon = Weapon("Bare Fists", 5, 1)

# Make a new player object that is currently in the 'outside' room.

new_player = Player(new_name, room["outside"], initial_weapon)

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


def check_movement(player, direction):
    global life
    try:
        # North
        if direction == "w":
            if(player.current_room.n_to == None):
                print("Sorry, you can't move here!")
            else:
                player.current_room = player.current_room.n_to
                print("You have moved!")
            print(f"Current location: {new_player.current_room.name}")
        # East
        if direction == "d":
            if(player.current_room.e_to == None):
                print("Sorry, you can't move here!")
            else:
                player.current_room = player.current_room.e_to
                print("You have moved!")
            print(f"Current location: {new_player.current_room.name}")
        # South
        if direction == "s":
            if(player.current_room.s_to == None):
                print("Sorry, you can't move here!")
            else:
                player.current_room = player.current_room.s_to
                print("You have moved!")
            print(f"Current location: {new_player.current_room.name}")
        # West
        if direction == "a":
            if(player.current_room.w_to == None):
                print("Sorry, you can't move here!")
            else:
                player.current_room = player.current_room.w_to
                print("You have moved!")
            print(f"Current location: {new_player.current_room.name}")
    except Exception:
        print("You cannot move here")


while life == True:

    selection = input(
        f"{new_player.name}, what would you like to do from here? ")

    try:
        check_movement(new_player, selection)

    except Exception:
        print("Please enter a valid value")
