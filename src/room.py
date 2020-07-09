import textwrap
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
        if self.items:
            for i, items in enumerate(self. items):
                # if there are items in the room, they should display
                if self.items[0]:
                    # after printing, looks like this will need text wrapped.
                    wrapper = textwrap.TextWrapper(width=60)
                    itemsDesc = wrapper.fill(text=f"{i} - {items}") 
                    i += 1
                    print()
                    print(itemsDesc)
                # else if there are not any items, print out that there is nothing else in the room
        else:
            print("# There is no items in the room. #")