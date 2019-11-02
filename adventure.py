#We can make a module for each possible main path of the day

#Morning module
def morning():
    snooze = "S"
    while snooze == "S":
        print("You wake up to the sound of your alarm clock blaring.")
        snooze = input("Do you snooze the alarm (S), or turn it off (T): ")
        snooze = snooze.upper()
        if snooze == "S":
            print("You hit the button and go back to sleep")
        elif snooze == "T":
            print("You go into your phone and turn off the alarm.")
        else:
            print("Please enter a valid option")
            snooze = "S"
    option = 0
    while option not in [1,2,3,4]:
        print()
        print("You heave a sigh and reluctantly get out of bed. Time to face the day. But what shall you do today?")
        print("You go have some breakfast as you think over your options...")
        print("(1) You could go to your morning class. I mean, you are paying to take this course after all.")
        print("(2) You have a test this afternoon. You could skip your lecture this morning and cram for it.")
        print("(3) You could ditch them both to go to the sports centre. You haven't been eating that well this week...")
        print("(4) Or you could just ditch completely. You could use a day off after all.")
        print()
        option = int(input("What should you do today: "))
        if option == 1:
            course()
        elif option == 2:
            test()
        elif option == 3:
            sports()
        elif option == 4:
            bunk()
        else:
            print("Please input a valid option")
    print("Sounds good.")
    
    
def sports():
    print("Not ready")

def course():
    print("Not ready")

def test():
    print("Not ready")

def bunk():
    print("Not ready")

#Start
morning()
    