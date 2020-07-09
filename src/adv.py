import textwrap
# importing from different files
from room import Room
from player import Player
from item import Item

# Declare all the rooms

roomsList = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons", [
        Item("House key", "The key to your house.")
    ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost Brinks brand treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers.The only exit is to the south. """, [
    Item("Key", "By the looks of it, it's a Master brand key. That's strange. Who has a Master brand lock around here? ")
]),
}


# Room(room)
# setting all the room names to an object
room = {}
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



# have an input to start off the player and maketheir player.
print('Welcome to the text adventure game!')
# get the players name to start the text adventure
playerName = input('Please input your player\'s name:\n')
# Make a new player object that is currently in the 'outside' room.
# creating a new player with the player class
player=Player(playerName, room['outside'], [])
# setup possible directions
possibleDirections = ['n', 'e', 'w', 's']
# a message to let the player know they started.

print()
print(f'And so, {playerName} commenced the adventure.')
# Write a loop that:
while True:
# * Prints the current room name
    print()
    print(player)
# * Prints the current description (the textwrap module might be useful here).
    wrapper = textwrap.TextWrapper(width=60)
    roomDesc = wrapper.fill(text=player.currentRoom.description) 
    print(roomDesc)
# * Waits for user input and decides what to do.
# when input comes in, strip off whitespace, lowercase the input, and 
    action = input("What should the player do?\n").strip().lower().split()[0]
    action = action[0]
# If the user enters "q", quit the game.
    if action == 'q':
        #print them a message as well
        print()
        print("Thanks for playing!")
        break

    # action to look at items in the room.
    elif action == 'l':
        player.currentRoom.printItems()


# If the user enters a cardinal direction, attempt to move to the room there.
    # if the players action is either n, w, s, or e, then attempt to have the player.currentRoom change according to direction

    elif action in possibleDirections:
        # check to see if we can go in a direction
        # if so, head that direction
        player.tryDirection(action)

    # if the player types i or inventory, they can see their inventory
    elif action == 'i':
        player.showInv()
