# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    # Class for room that has a name and description
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
    # string for it as well
    def __str__(self):
        return f"Room: {self.name}, Description: {self.desc}"
