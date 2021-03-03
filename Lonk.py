# Setup
yes_no = ["yes", "no"]
directions = ["north", "south", "east", "west"]

# Introduction
name = input("What is your name, adventurer?\n")
print("Greetings," + name + ". You have quite the journey ahead of you.\n\n")
print("You find yourself lying in a small meadow.\n")

# Start of game
response = ""
choseLayDown = 0
while response not in yes_no:
    response = input("Would you like to sit up?\nyes/no\n")
    if response == "yes":
        print("you sit up.")
    elif response == "no":
        choseLayDown += 1
        if choseLayDown == 1:
            print("you decide to stay lying down, gazing up at the clouds. You lay there for a while. You get pretty bored, and you start to wonder where exactly you are.")
            response = ""
        elif choseLayDown == 2:
            print("For some reason, you resist your curiousity to look around and remain exactly where you woke up, unmoving.")
            response = ""
        elif choseLayDown == 3:
            print("By now a few hours have passed, and the sun is getting low. Soon, the sun will set, and you're still laying in the dirt like a bum.")
            response = ""
        elif choseLayDown == 4:
            print("Never before in history has someone been so dedicated to doing absolutely nothing.")
            response = ""
        elif choseLayDown == 10:
            print("New Achievement: You died in the meadow!")
            quit()
        else:
            print("Who would've guessed it, you continued napping")
            response = ""
    else:
        print("huh?")

# You sat up
response = ""
print("\n\nYou look around and see that the meadow is surrounded on three sides by a forest, and that there is a steep clif with a waterfall to the west.\n")
print("to the north is a path leading to the forest")
print("to the west is the waterfall")
print("to the south and to the east are an unforgiving tanlge of brush\n")
response = input("Where would you like to go?\nnorth, south, east, west\n")
if response == "south" or "east":
    print("you inspect the thick foliage and find it covered in thorns, yowch. Traversing it would not be wise\n")
    response = ""

elif response == "west":
    print("The spray from the waterfall cools your face. You gaze through the crystaline water at the small pebbles and fishes, and your eyes follow the waterfall upwards to its source. Only a fool would try to climb such a slippery slope.\n")
