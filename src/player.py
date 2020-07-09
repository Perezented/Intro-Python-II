# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    # Class for player that has a name and current room
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
    #string for it as well.
    def __str__(self):
        return f"~ {self.name}'s current {self.currentRoom}"
