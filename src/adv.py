# importing from different files
from room import Room
from player import Player
from item import Item

# Declare all the rooms

roomsList = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

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


# Room(room)
# setting all the room names to an array
room = {}
# and all their descriptions with text in another array
roomDesc = []
# made a dict to hold all the locations and their descriptions
for k, v in roomsList.items():
    #set the key and values from roomsList into the dict
    room.__setitem__(k, v)

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Make a new player object that is currently in the 'outside' room.

# have an input to start off the player and maketheir player.
print('Welcome to the text game!')
# get the players name to start the text adventure
playerName = input('Please input your player\'s name:\
    ')

# creating a new player with the player class
player=Player(playerName, room['outside'])
# a message to let the player know they started.
print()
print(f'And so, {playerName} comemnced their quest')

location = player.currentRoom
# Write a loop that:
while True:
# * Prints the current room name
    print()
    print(player)
# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.
    action = input("Where should the character do? ")
# If the user enters "q", quit the game.
    if action == 'q':
        #print them a message as well
        print()
        print("Thanks for playing!")
        break
# If the user enters a cardinal direction, attempt to move to the room there.
    # if the players action is either n, w, s, or e, then attempt to have the player.currentRoom change according to direction
    elif action == 'n':
        if hasattr(player.currentRoom, 'n_to'):
            player.currentRoom = player.currentRoom.n_to
        else:
# Print an error message if the movement isn't allowed.
            print('#### Err, that is not a possible direction. You are redirected back to the same room. ####')
    elif action == 's':
        if hasattr(player.currentRoom, 's_to'):
            player.currentRoom = player.currentRoom.s_to
        else:
            print('#### Err, that is not a possible direction. You are redirected back to the same room. ####')
    elif action == 'w':
        if hasattr(player.currentRoom, 'w_to'):
            player.currentRoom = player.currentRoom.w_to
        else:
            print('#### Err, that is not a possible direction. You are redirected back to the same room. ####')
    elif action == 'e':
        if hasattr(player.currentRoom, 'e_to'):
            player.currentRoom = player.currentRoom.e_to
        else:
            print('#### Err, that is not a possible direction. You are redirected back to the same room. ####')
            print()

