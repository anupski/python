level = 20
stats_points = 1200
has_beacon = False
is_knight = False
has_orb_of_truth = False
has_orb_slot = False
has_beacon = input("Do you have the beacon? (yes/no): ").lower() == "yes"
if has_beacon:
    print("Filthy Lies.You cannot enter the dungeon of Ra without the beacon.")
is_knight = input("Are you a knight? (yes/no): ").lower() == "yes"
if is_knight:
    print("Filthy Lies.Only knights can enter the dungeon of Ra.")
has_orb_of_truth = input("Do you have the Orb of Truth? (yes/no): ").lower() == "yes"
if has_orb_of_truth:
    print("Filthy Lies.You cannot enter the dungeon of Ra without the Orb of Truth.")
has_orb_slot = input("Do you have the Orb Slot? (yes/no): ").lower() == "yes"
if has_orb_slot:
    print("Filthy Lies.You cannot enter the dungeon of Ra without the Orb Slot.") 
if level >= 20 and stats_points >= 1000:
    if has_beacon and is_knight:
        if has_orb_of_truth and has_orb_slot:
            print("You can enter the dungeon of Ra.")
            print("You are able to place the orb of truth on the beacon.")
        else:
            print("You cannot enter because you are still weak..")
    else:
        print("You do not meet the requirements to enter the dungeon of Ra.")
        print("You are not fit for this type of dungeon.")
        print("The Orb Of Truth forbids you from entering the dungeon")
else:
    print("You do not meet the requirements to enter the dungeon of Ra.")
    print("You are too weak to face the dungeon")

