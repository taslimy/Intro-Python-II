from room import Room
from player import Player
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
new_player = Player('Tas', room['outside'])
new_player.print_current_room()
d = input('[n] North [s] South [e] East [w] West [q] Quit\n')


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

# Game loop from rock paper
while not d == 'q':
    if d == 'n':
        if new_player.current_room.n_to is not None:
            new_player.current_room = new_player.current_room.n_to
        print("im in north")
    elif d == 's':
        if new_player.current_room.s_to is not None:
            new_player.current_room = new_player.current_room.s_to
            print("im in south")
    elif d == 'e':
         if new_player.current_room.e_to is not None:
            new_player.current_room = new_player.current_room.e_to
            print("im in east")
    elif d == 'w':
        if new_player.current_room.w_to is not None:
           new_player.current_room = new_player.current_room.w_to
           print("im in west")
    else:
        print('invalid selection')
    new_player.print_current_room()
    d = input('[n] North [s] South [e] East [w] West [q] Quit\n')
    print('choose a way n , s , e , w')
