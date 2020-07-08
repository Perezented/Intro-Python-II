# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    # Class for player that has a name and current room
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    #string for it as well.
    def __str__(self):
        return f"{self.name} is located at {self.current_room}"
