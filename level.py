level = 20
stats_points = 1200
actual_beacon = True
actual_knight = True
actual_orb_of_truth = True
actual_orb_slot = True
inventory = {
    "beacon": actual_beacon,
    "knight": actual_knight,
    "orb_of_truth": actual_orb_of_truth,
    "orb_slot": actual_orb_slot
}

player_name = ""
player_class = ""
player_health = 100
player_mana = 50
gold = 100

print("\n" + "="*50)
print("=== CHARACTER CREATION ===")
print("="*50)


name_valid = False
while not name_valid:
    player_name = input("Enter your character name: ")
    if len(player_name) >= 2 and len(player_name) <= 15:
        name_valid = True
    else:
        print("Name must be between 2 and 15 characters!")

print("\nAvailable classes:")
print("1. Warrior - High health, low mana")
print("2. Mage - Low health, high mana")
print("3. Rogue - Balanced stats")
print("4. Knight - High health, balanced mana")

class_choice = input("Select your class (1-4): ")
match class_choice:
    case "1":
        player_class = "Warrior"
        player_health = 150
        player_mana = 30
    case "2":
        player_class = "Mage"
        player_health = 70
        player_mana = 150
    case "3":
        player_class = "Rogue"
        player_health = 100
        player_mana = 80
    case "4":
        player_class = "Knight"
        player_health = 140
        player_mana = 70
    case _:
        player_class = "Adventurer"
        player_health = 100
        player_mana = 50

print(f"\nWelcome, {player_name} the {player_class}!")
print(f"Health: {player_health} | Mana: {player_mana} | Gold: {gold}")


stats = {"Health": player_health, "Mana": player_mana, "Gold": gold, "Level": level}
print("\n--- Character Stats ---")
for stat_name, stat_value in stats.items():
     
    if stat_value > 0:
        print(f"  {stat_name}: {stat_value}")
    else:
        print(f"  {stat_name}: 0 (Needs attention!)")


print("\n" + "="*50)
print("=== AVAILABLE QUESTS ===")
print("="*50)

quests = [
    {"name": "Find the Ancient Beacon", "reward": 500, "completed": False},
    {"name": "Defeat the Shadow Knight", "reward": 750, "completed": False},
    {"name": "Retrieve the Orb of Truth", "reward": 1000, "completed": False},
    {"name": "Locate the Orb Slot", "reward": 600, "completed": False}
]


quest_num = 1
for quest in quests:
    if not quest["completed"]:
        print(f"{quest_num}. {quest['name']} - Reward: {quest['reward']} gold")
        quest_num += 1


quest_active = True
while quest_active:
    print("\n--- Quest Menu ---")
    print("1. Accept a quest")
    print("2. View quest progress")
    print("3. Complete a quest")
    print("4. Return to main game")
    
    quest_choice = input("Select option (1-4): ")
    
    
    match quest_choice:
        case "1":
            quest_index = input("Enter quest number to accept: ")
            if quest_index.isdigit() and 1 <= int(quest_index) <= len(quests):
                idx = int(quest_index) - 1
                if not quests[idx]["completed"]:
                    print(f"You accepted: {quests[idx]['name']}")
                else:
                    print("This quest is already completed!")
            else:
                print("Invalid quest number!")
        case "2":
            print("\n--- Quest Progress ---")
            
            for i, quest in enumerate(quests):
                status = "✓ Completed" if quest["completed"] else "○ Available"
                print(f"  {i+1}. {quest['name']}: {status}")
        case "3":
            complete_index = input("Enter quest number to complete: ")
            if complete_index.isdigit() and 1 <= int(complete_index) <= len(quests):
                idx = int(complete_index) - 1
                if not quests[idx]["completed"]:
                    quests[idx]["completed"] = True
                    gold += quests[idx]["reward"]
                    print(f"Quest completed! You earned {quests[idx]['reward']} gold!")
                else:
                    print("This quest is already completed!")
            else:
                print("Invalid quest number!")
        case "4":
            quest_active = False
            print("Returning to your journey...")
        case _:
            print("Invalid option!")


print("\n" + "="*50)
print("=== ADVANCED STATUS CHECK ===")
print("="*50)


if level >= 20 and stats_points >= 1000 and gold >= 100:
    print("✓ You meet all requirements for the dungeon!")
elif level >= 20 and stats_points >= 1000:
    print("⚠ You meet level/stats but need more gold!")
elif level >= 20 or stats_points >= 1000:
    print("⚠ You meet only one requirement!")
else:
    print("✗ You do not meet the requirements!")


print("\n--- Dungeon Floor Analysis ---")
for floor in range(1, 6):
    if floor == 1:
        difficulty = "Easy"
    elif floor == 2 or floor == 3:
        difficulty = "Medium"
    elif floor == 4:
        difficulty = "Hard"
    else:
        difficulty = "Extreme"
    
    
    if floor <= 3 and player_health > 50:
        accessible = "Accessible"
    elif floor > 3 and player_health > 100:
        accessible = "Accessible"
    else:
        accessible = "Locked"
    
    print(f"  Floor {floor}: {difficulty} - {accessible}")


continue_playing = True
while continue_playing:
    print("\n--- Main Game Options ---")
    print("1. Check full status")
    print("2. View inventory")
    print("3. Start dungeon attempt")
    print("4. Quit game")
    
    main_choice = input("Select (1-4): ")
    
    match main_choice:
        case "1":
            
            if player_class == "Warrior" and player_health >= 100:
                print(f"\n{player_name} - {player_class}")
                print(f"Health: {player_health} | Mana: {player_mana}")
                print(f"Gold: {gold} | Level: {level}")
                print("Status: Ready for combat!")
            elif player_class == "Mage" and player_mana >= 50:
                print(f"\n{player_name} - {player_class}")
                print(f"Health: {player_health} | Mana: {player_mana}")
                print(f"Gold: {gold} | Level: {level}")
                print("Status: Ready for magic!")
            elif player_class == "Rogue" and (player_health >= 50 or player_mana >= 30):
                print(f"\n{player_name} - {player_class}")
                print(f"Health: {player_health} | Mana: {player_mana}")
                print(f"Gold: {gold} | Level: {level}")
                print("Status: Ready for stealth!")
            else:
                print("\nYou need to rest and recover before continuing!")
        case "2":
            print("\n--- Full Inventory ---")
            
            item_count = 0
            for item, has_item in inventory.items():
                if has_item:
                    print(f"  ✓ {item.replace('_', ' ').title()}")
                    item_count += 1
            print(f"Total items: {item_count}/4")
        case "3":
            if level >= 20 and stats_points >= 1000 and item_count == 4:
                print("\n=== ENTERING DUNGEON OF RA ===")
                continue_playing = False
            else:
                print("\nYou cannot enter yet!")
                print(f"Requirements: Level 20+ ({level}), Stats 1000+ ({stats_points}), All items ({item_count}/4)")
        case "4":
            print("Thanks for playing!")
            continue_playing = False
        case _:
            print("Invalid choice!")


player_claims_beacon = input("-| Do you have the beacon? |- (yes/no): ").lower() == "yes"
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

player_claims_knight = input("-| Are you a knight? |- (yes/no): ").lower() == "yes"
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

player_claims_orb = input("-| Do you have the Orb of Truth? |- (yes/no): ").lower() == "yes"
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

player_claims_slot = input("-| Do you have the Orb Slot? |- (yes/no): ").lower() == "yes"
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


def enter_dungeon(player_class, player_health, player_mana, gold, inventory):
    print("\n=== DUNGEON OF RA ===")
    print("You step into the ancient dungeon...")
    
    dungeon_floors = [
        {"name": "Hall of Echoes", "enemies": 2, "trap": True},
        {"name": "Chamber of Shadows", "enemies": 3, "trap": False},
        {"name": "Sanctum of Light", "enemies": 1, "trap": True},
        {"name": "Vault of Kings", "enemies": 4, "trap": False},
        {"name": "Heart of Ra", "enemies": 1, "trap": True}
    ]
    floor_num = 1
    for floor in dungeon_floors:
        print(f"\n--- Floor {floor_num}: {floor['name']} ---")
       
        if floor["trap"]:
            print("A trap is triggered!")
            if player_class == "Rogue" or (player_class == "Knight" and player_health > 100):
                print("You skillfully avoid the trap!")
            else:
                print("You take damage from the trap!")
                player_health -= 20
        else:
            print("No traps here.")
        
        enemies_left = floor["enemies"]
        while enemies_left > 0 and player_health > 0:
            print(f"Enemy appears! {enemies_left} left.")
            
            print("Choose action: 1. Attack 2. Defend 3. Use Mana")
            action = input("Action (1-3): ")
            match action:
                case "1":
                    print("You attack the enemy!")
                    enemies_left -= 1
                case "2":
                    print("You defend and take less damage.")
                    player_health -= 5
                case "3":
                    if player_mana >= 10:
                        print("You use a mana spell!")
                        player_mana -= 10
                        enemies_left -= 1
                    else:
                        print("Not enough mana!")
                case _:
                    print("You hesitate and the enemy strikes!")
                    player_health -= 10
            
            if player_health <= 0:
                print("You have fallen in the dungeon...")
                return False
        print("Floor cleared!")
        floor_num += 1
    
    all_items = all(inventory[item] for item in inventory)
    if all_items and player_health > 0:
        print("\nYou reach the Heart of Ra with all relics!")
        print("A great treasure is revealed. You win!")
        gold += 1000
    elif player_health > 0:
        print("\nYou reach the Heart of Ra, but lack some relics.")
        print("You escape with your life, but not the ultimate prize.")
    print(f"Final Health: {player_health} | Mana: {player_mana} | Gold: {gold}")
    return True


if __name__ == "__main__":
    
    dungeon_ready = False
   
    if level >= 20 and stats_points >= 1000 and all(inventory[item] for item in inventory):
        dungeon_ready = True
    if dungeon_ready:
        enter_dungeon(player_class, player_health, player_mana, gold, inventory)
ngeon.")
