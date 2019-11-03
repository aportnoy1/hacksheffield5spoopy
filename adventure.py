#We can make a module for each possible main path of the day
import random

#Morning module
import time
from time import sleep
def morning():
    snooze = "S"
    while snooze == "S":
        print("You wake up to the sound of your alarm clock blaring.")
        snooze = input("Do you snooze the alarm (S), or turn it off (T): ")
        snooze = snooze.upper()
        if snooze == "S":
            print("You hit the button and go back to sleep")
            print(".",end="")
            sleep(0.5)
            print(".",end="")
            sleep(0.5)
            print(". ",end="")
            sleep(0.5)
            print("\n")
        elif snooze == "T":
            print("You go into your phone and turn off the alarm.")
        else:
            valid()
            snooze = "S"
    print()
    print("You heave a sigh and reluctantly get out of bed. You go downstairs to get some coffee.")
    print("As the kettle boils you absentmindedly stare at the coffee package.")
    serialNum = input("What does the serial number say: ")
    if serialNum == "d7b25e4c5a":
        win()
    else:
        print("That's not quite right...")

    option = 0
    while option not in ["1","2","3","4"]:
        print()
        print("Time to face the day. But what shall you do?")
        print("You go have some breakfast as you think over your options...")
        print("(1) You could go to your morning class. I mean, you are paying to take this course after all.")
        print("(2) You have a test this afternoon. You could skip your lecture this morning and cram for it.")
        print("(3) You could ditch them both to go to the gym. You haven't been eating that well this week...")
        print("(4) Or you could just ditch completely. You could use a day off after all.")
        print()
        option = input("What should you do today: ")
        if option == "1":
            course()
        elif option == "2":
            test()
        elif option == "3":
            sports()
        elif option == "4":
            bunk()
        else:
            valid()
    
def sports():
    option = 0
    while option not in ["W","P"]:
        option = input("You head to the gym. What do you want to do, lift some weights (W), or go to the pool (P): ")
        option = option.upper()
        if not(option == "W" or option == "P"):
            valid()
    if option == "P":
        armband = 0
        armband = input("Do you want to wear armbands? (Y/N): ")
        armband = armband.upper()
        if armband == "Y":
            print("Eww why would you want to wear armbands. You're a grown adult, you don't need them")
        elif armband == "N":
            print("That's not very safe!")
        else:
            print("I'll take that as a no. Armbands are for kids anyway")
        sleep(1.8)    
        print("You finally decide to jump into the pool. It's pretty empty today, except for this one old woman \nwho looks at you a bit funny and then gets in.")
        sleep(1.8)
        print("You start swimming, when suddenly you notice that the old woman is swimming right behind you. \nYou feel a bit nervous now")
        sleep(1.8)
        print("Suddenly, the old woman grabs your leg")
        sleep(1.8)
        kick = 0
        start = time.time()
        kick = input("QUICK! Press K to kick her away: ")
        end = time.time()
        inputTime = (end - start)
        kick = kick.upper()
        
        if kick == "K" and inputTime < 1.8:
            print("You kick her")
        elif kick == "K":
            sleep(0.5)
            print("You try to kick her but you took too long to press the button, so she is able to hold on")
            sleep(2)
            print("Slowly, the old lady drags you down into the pool. \nYou desperately try to escape the her clutches but it's no use!")
            sleep(2)
            print("You're running out of breath.. you can't breathe.. YOU START TO PANIC OH GOD WHA-")
            sleep(3)
            print("\n\n\n\n\n\n\n\n\n\n")
            morning()
    elif option == "W":
        print("hi")
    else:
        valid()  

def pool():
    option = 0
    while option not in ["W","P"]:
       
        if option != "W" or "P":
            print("please select a valid option")
    if option == "W":
        print("yay")


def course():
    print("Under development")

def test():
    print("Under development")

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
        print("Please input a valid option")
        print()
        bunk()

def walk():
    print("You decide to go on a walk. Trying to decide on where, you can think of a forest nearby, as well as a park.")
    print("(1)The forest would be a nice scenic nature walk.")
    print("(2)The park has some climbing frames with kids, but is also a favourite with dog walkers.")
    optionWalk = input("Where will you go: ")
    if optionWalk == "1":
        print("The scenic walk it is!")
        print("You put on your coat and shoes and walk out the door. A quick ten minute walk to the forest passes.")
        print("...")
        print("You arrive at the forest entrance and continue onwards.")
        print("As you walk further into the forest the sounds of the outside get quieter, and the light of the sun dims.")
        print("Before you know it, the forest has become almost pitch black, and the path behind you seems swallowed up by the darkness.")
        print("You get out your phone and turn the flashlight on, using it to follow the path in front.")
        success = 0
        while success < 3:
            if success < -2:
                print()
                print("You become hopelessley lost, and are stranded in the forest following the wrong path for days.")
                print("Eventually you die of dehydration, and your body is found by a young teen with a stick.")
                print('''"Poke!"''')
                print()
                print("DEATH: Poke")
                #code
                print()
                morning()
            print("There is a fork in the path.")
            print("(1)The path to the left is dark, and surrounded by foliage.")
            print("(2)The path to the right does not differ.")
            forkOne = input("Which path do you take: ")
            if forkOne == "1":
                success = success + 1
            elif forkOne == "2":
                success = success - 1
            else:
                print("Please enter a valid input")
            print("There's another fork ahead.")
            print("(1)The path to the left looks well worn but offers no light.")
            
            print("(2)The path to the right is not worn but there is a faint light.")
            forkTwo = input("Which path do you take: ")
            if forkTwo == "1":
                success = success - 1
            elif forkTwo == "2":
                success = success + 1
            else:
                print("Please enter a valid input")
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
                print("Killer")
                killer()
            else:
                print("Please enter a valid input")
        else:        
            print()
            print("You finally emerge from the forest!")
            print("Thank goodness!")
            print("You've had enough walking today - you decide to head back home.")
            trip()
    elif optionWalk == "2":
        print("Option under development")
        walk()
    else:
        print("Please input a valid option")
        walk()

def killer():
    print("Wow, seriously?")
    troll = input("Are you sure (Y/N): ")
    troll = troll.upper()
    if troll == "Y":
        print("Fine. Whatever.")
    else:
        print("Too late.")
    print("You crouch down and start pushing your way through into the path.")
    print("Eventually the path forces you onto your hands and knees as you move forwards through the undergrowth.")
    print("You're not sure for how long you have been crawling, but your knees and hands were throbbing.")
    successCrawl = False
    while successCrawl == False:
        print("Suddenly you hear a quiet murmur. Do you;")
        print("(1)Stop")
        print("(2)Crawl faster")
        crawlOne = input("What do you do: ")
        if crawlOne == "1":
            print("You stop")
            successCrawl = True
        elif crawlOne == "2":
            print("The murmering pauses, and you hear rapid footsteps through the undergrowth.")
            chase()
        else:
            print("Please input a valid option")
    print("After a while you start moving again, trying to be as quiet as possible.")
    print("The murmur stops.")
    print("Suddenly you hear laughter above you, and through a gap in the bushes you can see a woman swaying between the dense forest.")
    successCrawlTwo = False
    while successCrawlTwo == False:
        print("Fear grips you as you watch her move.")
        print("(1)You stay still and hope she leaves.")
        print("(2)You try to back up through the bush")
        print("(3)You move forward, hoping she can't hear you past her laughter.")
        crawlTwo = input("Which option do you pick: ")
        if crawlTwo == "1":
            print("She sways closer and closer to you, and you can see a glimpse of metal in her hand.")
            print("In her strange movement, she slowly turns around and starts to approach the bush where you're stationed.")
            print("In a panic you begin to crawl as fast as you can.")
            chase()
        elif crawlTwo == "2":
            print("You hope that if you back up far enough you can get back to the fork in the path and run back home.")
            print("You don't stand a chance while crawling.")
            print("You begin to quietly back up through the undergrowth, hoping she doesn't see.")
            print("She sways closer and closer to where you were, and you can see a glimpse of metal in her hand.")
            print("In her strange movement, she slowly turns around and starts to approach the bush where you had been.")
            print("Glad you were out the way, your stay still as she passes through the bush, her knife cutting through the path.")
            print("She pauses a moment, staring at the ground where you once were.")
            print("You hold your breath.")
            print("...")
            print("She looks back up and carries on moving forwards.")
            print("You breathe out a sigh of relief as you can no longer hear her.")
            print("As you're about to start moving again, then knife bursts through the bush and lands directly behind you.")
            chase()
        elif crawlTwo == "3":
            print("You quietly try to keep pace with the woman, hoping her laughs will drown out the noise of your movement.")
            print("She turns around and sways closer to where you had been, and you can see a glimpse of metal in her hand.")
            print("Glad you were out the way, your stay still as she passes through the bush, her knife cutting through the path.")
            print("Over your shoulder you can see her pause a moment, staring at the ground where you once were.")
            print("You hold your breath.")
            print("...")
            print("She looks back up and carries on moving forwards.")
            print("You breathe out a sigh of relief as you can no longer hear her.")
            print("As you're about to start moving again, then knife bursts through the bush and lands directly behind you.")
            chase()
        else:
            print("Please enter a valid option")

def chase():
    print("You burst forward, your adrenaline pushing you forward as fast as you can go.")
    print("The woman gives chase, her shrieks and laughter filling the air.")
    print("Knowing that you'll never outrun her on all fours you break out of the bush and start running through the undergrowth.")
    print("She seems pleased by this.")
    print("You start running as fast as you can through the forest, jumping over bits of undergrowth.")
    print("You can see the light of the outside ahead! But how many more jumps do you have to make to escape?")
    jumps = random.randint(1,6)
    guess = int(input("Enter a number between 1 and 5: "))
    if guess == jumps:
        print("You got it! You jump",jumps,"times and break through the line of trees.")
        print("You can see the woman lurch to a stop in the darkness, eyes almost glowing.")
        print("After locking eyes with you for a few seconds, she turns around and stalks away. Thank goodness.")
        print("After all that, you decide to head home.")
    else:
        print("Incorrect guess.")
        print("Having misjudged the jumps, you trip and fall, twisting your ankle.")
        print("Easy prey for the woman she runs towards you.")
        print("She plunges her knife into your chest, the last thing you see being the image of her eyes as she leans her face into yours.")
        print()
        print("DEATH: Woman")
        #code
        print()
        morning()

def trip():
    print("Shaken by the day's events, you feel a little lightheaded on your walk back.")
    print("You zone out, losing concentration of where you are putting your feet, imaginging your comfy bed back home.")
    print("Your lack of concentration leads to tragedy!")
    print("You slip on the ground, falling on your back and cracking your skull on the pavvement.")
    print()
    print("DEATH: Zone out")
    #code
    print()
    morning()

def win():
    print("Under development")

def valid():
    print("Please print a valid option: ")

#Start
morning()
    