# Mia Currin
# 5/12/25
# P5LAB
# Create an adventure game

#Time library use with help from AI - documented in submission

import time

def intro():
    print("🌲 Welcome to Our Magical Treasure Hunt! 🌲")
    print("You wake up at the edge of a mysterious forest.")
    print("Rumors say treasure lies within, but danger awaits those who enter.\n")
    time.sleep(2)

def forest_path():
    print("\nYou step onto the forest path.")
    time.sleep(1.5)
    print("After a while, you see two paths ahead.")
    print("One leads toward a glowing cave, the other deeper into the forest.")
    choice = input("Do you go to the CAVE or continue DEEPER into the forest? ").lower()

    if choice == "cave":
        return cave()
    elif choice == "deeper":
        return deep_forest()
    else:
        print("You hesitate and waste time. Try to decide faster.")
        return forest_path()

def cave():
    print("\nYou enter the glowing cave.")
    time.sleep(1.5)
    print("Inside, you find a small wooden chest. It’s locked.")
    choice = input("Do you try to PICK the lock or LEAVE it alone? ").lower()

    if choice == "pick":
        print("You manage to open it with ease! Inside is a MAGIC STONE.")
        inventory.append("magic stone")
    else:
        print("You leave the chest untouched and walk away.")
    time.sleep(1)
    print("You return to the fork and take the forest path instead.")
    return deep_forest()

def deep_forest():
    print("\nYou walk deeper into the forest.")
    time.sleep(1.5)
    print("You hear wolves howling. You spot an abandoned cottage nearby.")
    choice = input("Do you HIDE in the cottage or KEEP walking? ").lower()

    if choice == "hide":
        print("You quickly run inside the cottage.")
        if "magic stone" in inventory:
            print("The wolves hesitate at the door, scared by the glow of your magic stone. You survive the night!")
        else:
            print("The wolves break in. You try to fight but are overwhelmed. Game over.")
            return False
    else:
        print("You keep walking quietly, but the wolves catch your scent.")
        print("You run and manage to escape — barely.")
    time.sleep(2)
    return mountain()

def mountain():
    print("\nAs dawn breaks, you find a steep path leading to a mountain.")
    print("Legend says a guardian spirit protects a treasure at the top.")
    choice = input("Do you CLIMB the mountain or REST at the base? ").lower()

    if choice == "climb":
        print("\nYou begin your ascent.")
        time.sleep(2)
        print("Halfway up, the foretold spirit appears.")
        if "magic stone" in inventory:
            print("It recognizes the stone and grants you safe passage.")
            print("At the summit, you find more ancient treasure! You win!")
        else:
            print("The spirit sees you as a threat and casts you down. Game over.")
            return False
    else:
        print("\nYou rest peacefully, but someone steals your supplies overnight. You barely survive.")
        print("You limp home — alive, but empty-handed.")
    return True

def play_game():
    global inventory
    inventory = []
    intro()
    
    playing = True
    while playing:
        survived = forest_path()
        time.sleep(1.5)
        if survived is False:
            print("\nWould you like to try again?")
        else:
            print("\nThanks for playing!")
        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            playing = False
        else:
            inventory = []
            print("\nRestarting your adventure...\n")
            time.sleep(2)

if __name__ == "__main__":
    play_game()
