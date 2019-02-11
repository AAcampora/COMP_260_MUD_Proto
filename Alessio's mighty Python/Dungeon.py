# import from the room class
# this is the model
from Room import Room

# make a new class for the dungeon layout
class Dungeon:
    def __init__(self):
        # make the parameters that will check the current room
        self.currentRoom = 0
        self.roomMap = {} # <- that is a struct

        # initialise the map of the dungeon
    def Init (self):

        # check that the the function is initialised
        print ("init")

        self.roomMap["room 0"] = Room("room 0", "Ground floor", "You are at Ghenna's gates " "\n Ready to open them and Face the EdgeLords?", "room 1", "", "", "")
        self.roomMap["room 1"] = Room("room 1", "first floor"," You are in the first room ", "room 2", "room 0", "room 3", "")
        self.roomMap["room 2"] = Room("room 2", "second floor", " You are in the second room ", "room 5", "room 2", "room 3", "")
        self.roomMap["room 3"] = Room("room 3", "second floor", " You are in the third room ", "room 4", "room 1", "", "room 2")
        self.roomMap["room 4"] = Room("room 4", "third floor", " You are in the fourth room ", "", "room 3", "", "room 5")
        self.roomMap["room 5"] = Room("room 5", "third floor", " You are in the fifth room ", "", "room 2", "room 4", "")

        self.currentRoom = "room 0"

    # display the current room to the player
    def DisplayCurrentRoom(self):

        print(self.roomMap[self.currentRoom].desc)
        print("Exits")

        # set a new variable for the available exits
        exits = ["NORTH", " SOUTH", "WEST","EAST"]
        exitStr = ""

        # check if the hasExit is triggered, then print the available exits
        for i in exits:
            if self.roomMap[self.currentRoom].hasExit(i.lower()):
                exitStr += i + " "

        print(exitStr)

        # check if the move made by the player is possible
    def isValidMove(self, direction):
        return self.roomMap[self.currentRoom].hasExit(direction)

    # move the player accordingly
    def MovePlayer(self, direction):
        if self.isValidMove(direction):

            if direction == "north":
                self.currentRoom = self.roomMap[self.currentRoom].north
                return
            if direction == "south":
                self.currentRoom = self.roomMap[self.currentRoom].south
                return
            if direction == "west":
                self.currentRoom = self.roomMap[self.currentRoom].west
                return
            if direction == "east":
                self.currentRoom = self.roomMap[self.currentRoom].east
                return

