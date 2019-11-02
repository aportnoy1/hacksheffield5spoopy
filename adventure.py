#We can make a module for each possible main path of the day
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
    