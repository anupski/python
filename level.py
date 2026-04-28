level = 20
stats_points = 1200


actual_beacon = True
actual_knight = False
actual_orb_of_truth = True
actual_orb_slot = True


player_claims_beacon = input("Do you have the beacon? (yes/no): ").lower() == "yes"
if player_claims_beacon:
    if actual_beacon:
        if level >= 20 and stats_points >= 1000:
            print("The beacon radiates with a powerful energy.")
        else:
            print("Filthy lies. You should be ashamed wanderer.")
    else:
        print("Filthy lies. You should be ashamed wanderer.")
else:
    if actual_beacon:
        print("Liar! You have the beacon but deny it!")
    else:
        print("Filthy Lies. You cannot enter the dungeon of Ra without the beacon.")

player_claims_knight = input("Are you a knight? (yes/no): ").lower() == "yes"
if player_claims_knight:
    if actual_knight:
        if level >= 20 and stats_points >= 1000:
            print("Your soul resonates with the power of the beacon.")
        else:
            print("Filthy lies. You should be ashamed wanderer.")
    else:
        print("Filthy lies. You should be ashamed wanderer.")
else:
    if actual_knight:
        print("Liar! You are a knight but deny it!")
    else:
        print("Only a knight shall resonate with the dungeon of Ra.")

player_claims_orb = input("Do you have the Orb of Truth? (yes/no): ").lower() == "yes"
if player_claims_orb:
    if actual_orb_of_truth:
        if level >= 20 and stats_points >= 1000:
            print("The Orb of Truth glows with an inner light.")
        else:
            print("Filthy lies. You should be ashamed wanderer.")
    else:
        print("Filthy lies. You should be ashamed wanderer.")
else:
    if actual_orb_of_truth:
        print("Liar! You have the Orb of Truth but deny it!")
    else:
        print("Only those who possess the Orb of Truth may enter the dungeon of Ra.")

player_claims_slot = input("Do you have the Orb Slot? (yes/no): ").lower() == "yes"
if player_claims_slot:
    if actual_orb_slot:
        if level >= 20 and stats_points >= 1000:
            print("The Orb Slot closes as the orb finds the beacon.")
        else:
            print("Filthy lies. You should be ashamed wanderer.")
    else:
        print("Filthy lies. You should be ashamed wanderer.")
else:
    if actual_orb_slot:
        print("Liar! You have the Orb Slot but deny it!")
    else:
        print("The Orb Slot remains open, waiting for the correct orb.")


if level >= 20 and stats_points >= 1000:
    if actual_beacon and actual_knight:
        if actual_orb_of_truth and actual_orb_slot:
            print("\nYou can enter the dungeon of Ra.")
            print("You are able to place the orb of truth on the beacon.")
        else:
            print("\nYou cannot enter because you are still weak.")
    else:
        print("\nYou do not meet the requirements to enter the dungeon of Ra.")
        print("You are not fit for this type of dungeon.")
        print("The Orb Of Truth forbids you from entering the dungeon.")
else:
    print("\nYou do not meet the requirements to enter the dungeon of Ra.")
    print("You are too weak to face the dungeon.")
