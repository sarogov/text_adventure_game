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

# Here is two general functions used for inventory.
def contest_of_invetory():
    """This prints the contest of inventory."""
    for r in inventory:
        print("\t", r)

def use_item(item):
    """This checks if item is in the inventory and then removes it."""
    if item in inventory:
        inventory.remove(item)
        return True
    else:
        return False

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

    def dead(self):
        """This is the sadest ending of the game."""
        print("    You died.")
        sleep(3)
        print("    Sorry.")
        sleep(2)
        print("            GAME OVER\n")
        print("    "+"*"*40+"\n\n")
        exit(0) # This ends the program.




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

    def __init__(self, description):
        super().__init__()
        self.sweet_tooth = random.choice([True, False])
        self.description = description

    def play(self):
        """To clear the room the player has to face the monster. There are
        several options what to do."""

        #Descrition of the room and its contests.
        super().play()
        print(f"    In the middle of the room stands a {self.description} monster")
        print("    staring at you. You see a door behind the monster, but you")
        print("    wonder how you pass this monster.\n")


        # Choosing what to do. While loop keeps asking until player aswers so
        # that the game can go forward.
        while True:
            choice = input("    What will you do? " )

            #If player wants to use the gun. Gun is only once usable and it
            # hits with 60% propability.
            if "gun" in choice:
                if use_item("a gun"):
                    print("\n    You aim the monster with your gun and shoot.")
                    sleep(3)

                    if random.randint(1,10)>3: #Here is defined the probability for the gun to hit.
                        print(f"\n    The bullet hits the monster and the {self.description} monster dies.")
                        print("\n    This is sad.")
                        sleep(3)
                        print("\n\n    After using the gun. Let check the bag.")
                        print("    Now there are these items:")
                        contest_of_invetory()
                        sleep(3)
                        break # This ends the while loop.
                    else:
                        print(f"\n    The bullet doesn't hit the monster.")
                        sleep(1)
                        print("    The monster gets angry and comes to you. He takes grip on you and eats you.")
                        sleep(2)
                        self.dead()
                else:
                    print("    You don't have a gun anymore.\n")


            #Player can offer sweet to the monster.
            elif "candy bar" in choice:
                if use_item("a candy bar"):
                    print("    You offer a candy bar to the monster.")
                    if self.sweet_tooth:
                        print("    The monster likes the candy bar and takes it.")
                        print("    He moves out of the way so that you can go freely.")
                        break # This ends the while loop.
                    else:
                        print("    The monster takes your candy bar and throws it away.")
                        print("    The monster doesn't like the candy bar.")


                    print("\n\n    After giving away the candy bar. Let's check the bag.")
                    print("    Now there are these items:")
                    contest_of_invetory()
                    sleep(3)


                else:
                    print("    You don't have a candy bar anymore.\n")

            # Here is the choice of hitting the moster. There is different outcomes
            # based on those random functions.
            elif "hit" in choice:
                if random.randint(1,10)>5:
                    print("    You hit the monster and the monster gets out of the way.")
                    break # This ends the while loop.
                elif random.randint(1,10) == 1:
                    print("    You try to hit the monster but he gets annoyed about you.")
                    print("    He comes and grabs you and eats you.")
                    self.dead()
                else:
                    print("    You try to hit the monster but he manages block it.")
                    print("    He still stands on the way.\n")
                    sleep(1)


            #Here is the escape or flee choice for the player.
            elif "flee" in choice or "escape" in choice or "run" in choice:
                print("    You run away so fast that you return to the very first room.\n\n")
                sleep(3)
                return False # This finishes the execution of the play function. Returning False gets player bac to the first room.

            else:
                print("    The choices to do are the following: escape, offer")
                print("    something sweet or use violence.")

        print("    Now you can go to the next door. You go there and open it.")
        input("    > ")
        return True




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
room1 = Monster_Room("big eyed bright green Gulabu")
room2 = Problem_Room()
room3 = Monster_Room("tiny, tiny pink but big teeth having")
room4 = Exit_Room()

rooms = [room1,room2,room3,room4]


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
