# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        if hasattr(self.current_room, direction):
            self.current_room = getattr(self.current_room, direction)
        else:
            print("You cannot move in that direction")
