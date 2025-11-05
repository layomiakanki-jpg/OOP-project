from room import Room
from character import Enemey, Character
from item import Item

maths_classroom= Room("maths")
maths_classroom.set_description("A small room with textbooks and a broken window.")

english_classroom = Room("English")
english_classroom.set_description("A larger room with scattered book pages everywhere.")

science_lab = Room("science")
science_lab.set_description("Rusted faucets drip onto cracked counters")

gymnasium = Room("gym")
gymnasium_classroom.set_description("Basketballs deflated and hoops bent")

maths.link_room(english, "south")
English.link_room(science, "north")
science.link_room(gym, "west")
gym.link_room(maths, "east")

damon = Enemy("damon", "A scary vampire")
damon.set_conversation("hey there! I'm hungry.")
damon.set_weakness("light")
maths.set_character(damon)

katerina = Enemy("katerina", "Another vampire who's faster.")
katerina.set_conversation("Sssss...Let's play a game...")
katerina.set_weakness("fire")
science_lab.set_character(katerina)

light = Item("torch")
light.set_description("An old torch with cracks")
english_classroom.set_item(light)

fire = Item("matchsticks")
fire.set_description("A packet of matches")
gym.set_item(fire)

current_room = kitchen
backpack = []

dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("well done, you won the fight!")
                    current_room.character = None
                    if inhabitant.get_defeated() == 2:
                        print("Congratulations, you have vanquished the vampires!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Better luck next time.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)




