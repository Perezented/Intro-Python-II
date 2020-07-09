# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    # Class for room that has a name and description
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        # add a property to the rooms where they can hold items.
        self.items = items
    # string for it as well
    def __str__(self):
        return f"{self.name}."
    # print the items of the room with a function.
    def printItems(self):
        for i, items in enumerate(self.items):
            print(f"{i + 1} - {items}")