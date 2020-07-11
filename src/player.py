import textwrap
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    # Class for player that has a name and current room
    def __init__(self, name, currentRoom, inventory):
        self.name = name
        self.currentRoom = currentRoom
        # player will need an inventory.
        self.inventory = inventory
    #string for it as well.
    def __str__(self):
        return f"~ {self.name}'s current location, {self.currentRoom}"
    def tryDirection(self, action):
        attribute = action + '_to'
        #see if the current loaciton has the attribute
        if hasattr(self.currentRoom, attribute):
            #use getattr to move to the location
            self.currentRoom = getattr(self.currentRoom, attribute)
        else:
            # Print an error message if the movement isn't allowed.
            print()
            print('#### Err, that is not a possible direction. You are redirected back to the same location. ####')
    # have a function to display a players inventory
    def showInv(self):
        # if theres items in the inventory, display them
        if self.inventory:
            for i, inventory in enumerate(self.inventory):
            # if there are items in the room, they should display
                if self.inventory[0]:
                # after printing, looks like this will need text wrapped.
                    i += 1
                    wrapper = textwrap.TextWrapper(width=60)
                    itemsDesc = wrapper.fill(text=f"{i} - {inventory}") 
                    print()
                    print(itemsDesc)
            
        # otherwise, let the player know there is nothing in the inventory
        else:
            print(f"# There is no items in {self.name}'s inventory. #")
    
    # add a item to a players inv
    def addItemToInv(self, item):
        self.inventory.append(item)