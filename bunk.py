#the bunk module for the adventure

def bunk():
    print("You decide to bunk. What a rebel.")
    print("But where do you go in your rebellious spree?")
    print("(1): You could go for a walk. There are plenty of places around.")
    bunkOption = input("Where will you go: ")
    if bunkOption == "1":
        walk()
    elif bunkOption == "2":
        print("Not ready")
    elif bunkOption == "3":
        print("Not ready")
    else:
        print("Please input a valid option: ")


def walk():
    print("You decide to go on a walk. Trying to decide on where, you can think of a forest nearby, as well as a park.")
    print("(1)The forest would be a nice scenic nature walk.")
    print("(2)The park has some climbing frames with kids, but is also a favourite with dog walkers.")
    optionWalk = int(input("Where will you go: "))
    if optionWalk == "1":
        print("The scenic walk it is!")
        print("You put on your coat and shoes and walk out the door. A quick ten minute walk to the forest passes.")
        print("...")
        print("You arrive at the forest entrance and continue onwards.")
        print("As you walk further into the forest the sounds of the outside get quieter, and the light of the sun dims.")
        print("Before you know it, the forest has become almost pitch black, and the path behind you seems swallowed up by the darkness.")
        print("You get out your phone and turn the flashlight on, using it to follow the path in front.")
        success = 0
        while success <3:
            if success <-3:
                print("You become hopelessley lost, and are stranded in the forest following the wrong path for days.")
                print("Eventually you die of dehydration, and your body is found by a young teen with a stick.")
                print('''"Poke!"''')
                print()
                print("DEATH: Lost")
                print("THE RIDDLER")
                #morning()
            print("There is a fork in the path.")
            print("(1)The path to the left is dark, and surrounded by foliage.")
            print("(2)The path to the right does not differ.")
            forkOne = input("Which path do you take: ")
            if forkOne == "1":
                success = success + 1
            elif forkOne == "2":
                success = success - 1
                break
            else:
                print("Please enter a valid input")
                break
            print("There's another fork ahead.")
            print("(1)The path to the left looks well worn but offers no light.")
            print("(2)The path to the right is not worn but there is a faint light.")
            forkTwo = input("Which path do you take: ")
            if forkTwo == "1":
                success = success - 1
                break
            elif forkTwo == "2":
                success = success + 1
            else:
                print("Please enter a valid input")
                break
            print("All light is gone again, but there's another fork ahead")
            print("(1)The path to the left has a faint voice ahead.")
            print("(2)The path to the right is quiet.")
            print("(3)Looking closesly you think you can see a path amid some bushes to the right of you. It's an option, but likely not a good one.")
            forkThree = input("Which path do you take: ")
            if forkThree == "1":
                success = success - 1
            elif forkThree == "2":
                success = success + 1
            elif forkThree == "3":
                killer()
            else:
                print("Please enter a valid input")
                break
        print()
        print("You finally emerge from the forest!")
        print("Thank goodness!")
        print("You've had enough walking today - you decide to head back home.")
        trip()

def killer():
    print("Wow, seriously?")
    troll = input("Are you sure (Y/N): ")
    troll = troll.upper()
    if troll == "Y":
        print("Fine. Whatever.")
    else:
        print("Too late.")
    


def trip():
    print("Shaken by the day's events, you feel a little lightheaded on your walk back.")
    print("You zone out, losing concentration of where you are putting your feet, imaginging your comfy bed back home.")
    print("Your lack of concentration leads to tragedy!")
    print("You slip on the ground, falling on your back and cracking your skull on the pavvement.")
    print()
    print("DEATH: Zone out")
    print("RIDDLE ZONE")
    #morning()




                



#start
bunk()