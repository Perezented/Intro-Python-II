# importing from different files
from room import Room
from player import Player
from item import Item

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


# Room(room)
# setting all the room names to an array
rooms = []
# and all their descriptions with text in another array
roomDesc = []
# for each room item, I want to move each location name to rooms array
# and each class made to roomDesc array
for k, v in room.items():
    # print(f'key: {k}, value: {v}')
    rooms.append(k)
    roomDesc.append(v)
print(rooms)

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
playerName = input('Please input your player\'s name:\
    ')
player = Player(playerName, rooms[0])
print(f'And so, {playerName} comemnced their quest')

# Write a loop that:
while True:
# * Prints the current room name
    print(player)
# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.
    moving = input("Where should the character go?")
# If the user enters "q", quit the game.
    if moving == 'q':
        print("Thanks for playing!")
        break
    player.current_room.moving


# If the user enters a cardinal direction, attempt to move to the room there.

# Print an error message if the movement isn't allowed.

