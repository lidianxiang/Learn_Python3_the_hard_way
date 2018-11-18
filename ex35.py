from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    chioce = input("> ")
    if "0" in chioce or "1" in chioce:
        how_much = int(chioce)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        chioce = input("> ")

        if chioce == "take money":
            dead("The bear looks at you then slaps your face off.")
        elif chioce == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif chioce == "taunt bear" and bear_moved:
            dead("The bear gets pissed off chews your leg off.")
        elif chioce == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def Cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for you life or eat your head?")

    chioce = input("> ")

    if "flee" in chioce:
        start()
    elif "head" in chioce:
        dead("Well that was tasty!")
    else:
        Cthulhu_room()

def dead(why):
    print(why,"Good job!")
    exit(0)

def start():
    print("You are in a drak room.")
    print("There is door to your right and left.")
    print("Which one do you take?")

    chioce = input(">")

    if chioce == "left":
        bear_room()
    elif chioce == "right":
        Cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
