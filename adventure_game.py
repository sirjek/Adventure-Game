import time
import random
items = []
monsters = random.choice(["dragon", "troll", "pirate"])
weapon = random.choice(["sword", "axe"])


def print_pause(yeah):
    print(yeah)
    time.sleep(1)


def intro():
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wild flowers")
    print_pause(f"Rumor has it that a {monsters} is somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("In your hand you hold your trusty(but not very effective) "
                "dagger")


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                f"and out steps a {monsters}")
    print_pause(f"Eep! This is the {monsters} house!")
    print_pause(f"The {monsters} attacks you!")
    boss = input("would you like to (1) fight or (2) run away?\n")
    if boss == "1" and weapon not in items:
        print_pause("You feel a bit under-prepared for this, "
                    "with only having a tiny dagger.")
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {monsters}.")
        print_pause("You have been defeated!")

    elif boss == "1" and weapon in items:
        print_pause(f"As the wicked {monsters} moves to attack,"
                    f"you unsheath your new {weapon}.")
        print_pause(f"The {weapon} of Ogoroth "
                    "shines brightly in your hand as you brace yourself")
        print_pause(f"But the wicked {monsters} "
                    "takes one look at your shiny new toy and runs away!")
        print_pause(f"You have rid the town of the wicked {monsters}. "
                    "You are victorious!")
        end()
    elif boss == "2":
        print_pause("You run back into the field. "
                    "You don\'t seem to have been followed.")
        game()

    else:
        boss = input("would you like to (1) fight or (2) run away?\n")


def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause(f"You have found the magical {weapon} of Ogoroth!")
    print_pause(f"You discard your silly old dagger and take the {weapon}"
                "with you")
    items.append(weapon)
    print_pause("You walk back out to the field")
    game()


def game():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    great = input("What would you like to do?\n"
                  "(please enter 1 or 2.)")
    if great == "1":
        house()
    elif great == "2":
        cave()
    else:
        while great != "1" and great != "2":
            great = input("please enter 1 or 2.")
        if great == "1":
            house()
        if great == "2":
            cave()


def end():
    follow = input("would you like to play again? (y/n)\n")
    if "y" in follow:
        print_pause("Excellent! Restarting the game...")
        intro()
        game()

    if "n" in follow:
        return


intro()
game()
end()
