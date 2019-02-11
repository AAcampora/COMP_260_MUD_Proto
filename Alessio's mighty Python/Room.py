# this class contains the definition for the rooms in the MUD

# define the class


class Room:
    # initialise the class
    def __init__(self, name, floor, desc, north, south, west, east):

        # assign the class parameters to strings
        self.name = name
        self.floor = floor
        self.desc = desc
        self.north = north
        self.south = south
        self.west = west
        self.east = east
    # this function dictates which way is the exit for the player

    def hasExit(self, direction):
        #  the direction chosen by the player is chosen and if that direction is not empty
        if(direction == "north") and (self.north != ""):
            return True

        if (direction == "south") and (self.south != ""):
            return True

        if (direction == "west") and (self.west != ""):
            return True

        if (direction == "east") and (self.east != ""):
            return True

        return False
