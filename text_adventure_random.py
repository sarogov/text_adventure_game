###############################################################################
# A simple text based adventure game.
# Game consist of different type of rooms: monster rooms,
# riddle rooms, locked door rooms and gold room. It uses random library
# to make the game different each time it is played.
###############################################################################


import random
from sys import exit
from time import sleep


###############################################################################
# Some data lists needed for the game. With these the game can be customized
# and make also more complicated.
###############################################################################

# This list contains adjective description of rooms.
looks = ['light navy blue','very dark green', 'bright yellow','screaming pink',
    'murky, almost blood colored red','very, very black','plain boring brown',
    'misty grey', ' grey and full of annoying mosquitos']

# This list contains the items that the player has with him.
inventory = ['a key', 'a gun', 'a candy bar']

#Here is a general function used for inventory.
def contest_of_invetory():
    """This prints the contest of inventory."""
    for r in inventory:
        print("\t", r)

###############################################################################
#  ROOMS
# The main function they contain is play that defines if the room is cleared
# and the player can continue the trip. There is lot of sleep() -commands
# added to the play functions so that the text on the screen doesn't scroll
# so fast forward.
###############################################################################

class Room():
    """This is the parent class of all the other rooms. As attribute is the
    general look of the room."""

    def __init__(self):
        self.look = random.choice(looks)
        looks.remove(self.look) # This so that the rooms are unique looking.

    def play(self):
        """This descripes the room for the player. It returns True if the
        obstacles in the room are cleared and it returns false if they
        are not."""

        print("\n\n    " + "*"*65 + "\n")
        print(f"    You enter a room that is {self.look}. ")
        print("    There is a one door at the other side of the room." )
        sleep(1)
        return True


class Start_Room(Room):
    """This room is the room where game starts."""

    def play(self):
        print("\n    " + "*"*65 + "\n")
        print(f"    You are in a room that is {self.look}.")
        print("    You have a bag labelled use only once with you. ")
        print("    The bag contains the following items:")
        contest_of_invetory()
        print("    There is only one door at the room. Nothing else.")
        print("    No hints or what so ever about where are you or what to do.")
        print("    You aproach the door and try if you can open it.")
        print("    The door is open and you go throught it.")
        input("    >")
        return True

class Monster_Room(Room):
    """This room contains a monster. The monster has a description and
    sweet_tooth attributes. Sweet_tooth attribute decides if the monster
    can be passed by giving it a sweet."""
    pass

class Problem_Room(Room):
    """This room has a locked room and the player has to solve a math problem
    to proceed."""
    pass

class Exit_Room(Room):
    """The room that ends the game if the player has not died before."""

    def __init__(self):
        self.look = "full of light coming from a big window"


    def play(self):
        super().play()
        print("\n    The door is open to outside where the sun is shining ")
        print("    brightly. You recognize the place outside.")
        print("    Now you know how to get back to home. ")
        print("    You think maybe ... ")
        sleep(3)
        print("                       ... maybe this was just a bad dream.")
        sleep(2)

        print("\n\n\t\t\t The End.")
        print("    " + "*"*75 + "\n\n")
        exit(0)
        return(True)



###############################################################################
# Here is the setup for the game. The game can be customized here.
###############################################################################
start = Start_Room()
room1 = Monster_Room()
room2 = Problem_Room()
room3 = Exit_Room()

rooms = [room1,room2,room3]


###############################################################################
#The beginning of the game.
###############################################################################
print("""



                     START OF THE ADVENTURE
    ***************************************************************************

    After the group of monsters kidnapped you. You lost your consciousness.
    Now you are waking up in a room with a one door. You close your eyes
    hoping you are just dreaming. You open them again and you are still
    in same room.

""")

#First room
start.play()

# Here we go thought the rooms. One of the room is exit room and there the
# game ends if the player has not died before that. If obstacles in room are
# not solved the game goes back to start but those rooms that were solved are
# not any more in the list. The game can be really short in case the exit room
# is picked up first. But it is okay.

while len(rooms) > 0:
    next_room = random.choice(rooms)
    if next_room.play():
        rooms.remove(next_room)
    else:
        start.play()
