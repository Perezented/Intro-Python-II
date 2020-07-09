# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    # Class for player that has a name and current room
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
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