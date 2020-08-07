###############################################################
# A simple text based adventure game.
# Game consist of different type of rooms: monster rooms,
# riddle rooms, locked door rooms and gold room.
##############################################################


import random
import sys
from time import sleep


##########################################################################
# Here are the rooms. The main function they contain is play
# that defines if the room is cleared and the player can continue the trip.
##########################################################################

class Room():
    """This is the parent class of all the other rooms. As attribute is the
    general look of the room."""
    def play(self):
        return True

class Start_Room(Room):
    """This room is the room where game starts."""
    pass

class Monster_Room(Room):
    """This room contains a monster. The monster has a description
    and sweet_tooth attributes.  Sweet_tooth attribute decides if the monster can be
    passed by giving it a sweet."""
    pass

class Problem_Room(Room):
    """This room has a locked room and the player has to solve a math problem to proceed."""
    pass

class Exit_Room(Room):
    """The room that ends the game if the player has not died before."""

    def play(self):
        super().play()
        print("    This room has a big window and an open door to outside.")
        print("    You see that the sun is shining outside. And you recognize")
        print("    the place. Now you know how to get back to home. You think")
        print("    maybe this was just a bad dream.")
        sleep(3) # This added so that the text on the screen doesn't go so fast forward.

        print("\n\n\t\t The End.")
        print("    ***********************************************************************************\n\n")
        sys.exit(0)
        return(True)



#############################################################################################
# Here is the setup for the game. The game can be customized here.
#############################################################################################
start = Start_Room()
room1 = Monster_Room()
room2 = Problem_Room()
room3 = Exit_Room()

rooms = [room1,room2,room3]


###########################################################################################
#The beginning of the game.
print("""



                    START OF THE ADVENTURE
    ***********************************************************************

    After the group of monsters kidnapped you. You lost your consciousness.
    Now you wake up in a room with a one door. You close your eyes
    hoping you are just dreaming. You open them again. 

""")

#First room
start.play()


# Here we go thought the rooms. One of the room is exit room and there the game ends if
# the player has not died before that. If obstacles in room are not solved the game goes
# back to start but those rooms that were solved are not any more in the list.
# The game can be really short in case the exit room is picked up first. But it is okay.

while len(rooms) > 0:
    next_room = random.choice(rooms)
    if next_room.play():
        rooms.remove(next_room)
    else:
        start.play()
