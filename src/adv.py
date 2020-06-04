from room import Room

from player import Player

import textwrap

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

# Make a new player object that is currently in the 'outside' room.
player = Player("Jojo", room["outside"])

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

# welcome message
print("Welcome to the adventure game")
print(player.current_room)
print(textwrap.wrap(player.current_room.description, width=70))

# loop starts
while True:

    # take user input
    user_cmd = input(
        "[n] North   [s] South  [e] East  [w] West  [q] Quit\n").lower()
    print(f"You chose {user_cmd}")
# user choose a cardinal direction
    # if the option is available/not none then go to that room
    # elif the option is not available/none then throw error and back to user input
    if user_cmd == "q":
        print("Bye, hope to see you next time!")
        exit()

    if user_cmd in ("n", "s", "e", "w"):
        user_cmd = f"{user_cmd}_to"
        if hasattr(player.current_room, user_cmd):
            player.current_room = getattr(
                player.current_room, user_cmd)
            print(player.current_room)
            print(textwrap.wrap(player.current_room.description, width=70))
        else:
            print("There's not room with your chosen direction.")
    else:
        print(
            "Please choose 1 of the 5 given options: [n] North   [s] South  [e] East  [w] West  [q] Quit")
