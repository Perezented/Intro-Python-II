class Item:
    # Class for item that has a name and description
    def __init__(self, name, description):
        self.name = name
        self.description = description
# string for it as well
    def __str__(self):
        return f"Item Name: {self.name}, Item Description: {self.description}"
    def printName(self):
        print(f'{self.name}')