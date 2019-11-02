#We can make a module for each possible main path of the day

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
    print("Not ready")

def test():
    print("Not ready")

def bunk():
    print("Not ready")

def win():
    print("Not ready")

def valid():
    print("Please print a valid option: ")

#Start
morning()
    