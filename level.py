class UIFormatter:
    """Handles all UI formatting and display"""
    BORDER = "═" * 60
    DOUBLE_BORDER = "╔" + "═" * 58 + "╗"
    
    def __init__(self):
        self.colors = {
            "header": "✦",
            "quest": "◈",
            "item": "◆",
            "enemy": "⚔",
            "success": "✓",
            "fail": "✗",
            "warning": "⚠"
        }
    
    def print_header(self, title):
        print("\n" + self.DOUBLE_BORDER)
        print("║" + f" {title:^56} " + "║")
        print("╚" + "═" * 58 + "╝")
    
    def print_section(self, title):
        print("\n" + self.BORDER)
        print(f">>> {title} <<<")
        print(self.BORDER)
    
    def print_stat_line(self, label, value, max_val=None):
        if max_val:
            percentage = (value / max_val) * 100
            bar_length = int(percentage / 5)
            bar = "█" * bar_length + "░" * (20 - bar_length)
            print(f"  {label:15} [{bar}] {value}/{max_val}")
        else:
            print(f"  {label:15}: {value}")
    
    def print_divider(self):
        print("─" * 60)


class Inventory:
    """Manages player inventory with items"""
    def __init__(self):
        self.items = {
            "beacon": False,
            "knight": False,
            "orb_of_truth": False,
            "orb_slot": False
        }
        self.equipment = {
            "weapon": "Iron Sword",
            "armor": "Leather Armor",
            "shield": "Wooden Shield"
        }
        self.potions = {"health_potion": 5, "mana_potion": 3}
    
    def get_item(self, item_name):
        return self.items.get(item_name, False)
    
    def has_all_items(self):
        return all(self.items[item] for item in self.items)
    
    def get_item_count(self):
        return sum(1 for item in self.items.values() if item)
    
    def display_full_inventory(self, ui):
        print("\n" + "─" * 60)
        print("  ▶ RELICS INVENTORY:")
        for item, has_it in self.items.items():
            status = f"{ui.colors['success']} {item.replace('_', ' ').title()}" if has_it else f"{ui.colors['fail']} {item.replace('_', ' ').title()}"
            print(f"    {status}")
        
        print("\n  ▶ EQUIPMENT:")
        for equip, name in self.equipment.items():
            print(f"    {ui.colors['item']} {equip.title()}: {name}")
        
        print("\n  ▶ CONSUMABLES:")
        for potion, count in self.potions.items():
            print(f"    {ui.colors['item']} {potion.replace('_', ' ').title()}: {count}")
        print("─" * 60)


class Quest:
    """Represents a single quest"""
    def __init__(self, name, description, reward, completed=False):
        self.name = name
        self.description = description
        self.reward = reward
        self.completed = completed
        self.progress = 0
    
    def complete(self):
        self.completed = True
        self.progress = 100
    
    def get_status(self):
        return "✓ Completed" if self.completed elseclass UIFormatter:
    """Handles all UI formatting and display"""
    BORDER = "═" * 60
    DOUBLE_BORDER = "╔" + "═" * 58 + "╗"
    
    def __init__(self):
        self.colors = {
            "header": "✦",
            "quest": "◈",
            "item": "◆",
            "enemy": "⚔",
            "success": "✓",
            "fail": "✗",
            "warning": "⚠"
        }
    
    def print_header(self, title):
        print("\n" + self.DOUBLE_BORDER)
        print("║" + f" {title:^56} " + "║")
        print("╚" + "═" * 58 + "╝")
    
    def print_section(self, title):
        print("\n" + self.BORDER)
        print(f">>> {title} <<<")
        print(self.BORDER)
    
    def print_stat_line(self, label, value, max_val=None):
        if max_val:
            percentage = (value / max_val) * 100
            bar_length = int(percentage / 5)
            bar = "█" * bar_length + "░" * (20 - bar_length)
            print(f"  {label:15} [{bar}] {value}/{max_val}")
        else:
            print(f"  {label:15}: {value}")
    
    def print_divider(self):
        print("─" * 60)


class Inventory:
    """Manages player inventory with items"""
    def __init__(self):
        self.items = {
            "beacon": False,
            "knights_resonance": False,
            "orb_of_truth": False,
            "orb_slot": False
        }
        self.equipment = {
            "weapon": "Iron Sword",
            "armor": "Leather Armor",
            "shield": "Wooden Shield"
        }
        self.potions = {"health_potion": 5, "mana_potion": 3}
    
    def get_item(self, item_name):
        return self.items.get(item_name, False)
    
    def has_all_items(self):
        return all(self.items[item] for item in self.items)
    
    def get_item_count(self):
        return sum(1 for item in self.items.values() if item)
    
    def display_full_inventory(self, ui):
        print("\n" + "─" * 60)
        print("  ▶ RELICS INVENTORY:")
        for item, has_it in self.items.items():
            display_name = item.replace('_', ' ').title()
            if item == "knights_resonance":
                display_name = "Knight's Resonance"
            status = f"{ui.colors['success']} {display_name}" if has_it else f"{ui.colors['fail']} {display_name}"
            print(f"    {status}")
        
        print("\n  ▶ EQUIPMENT:")
        for equip, name in self.equipment.items():
            print(f"    {ui.colors['item']} {equip.title()}: {name}")
        
        print("\n  ▶ CONSUMABLES:")
        for potion, count in self.potions.items():
            print(f"    {ui.colors['item']} {potion.replace('_', ' ').title()}: {count}")
        print("─" * 60)


class Quest:
    """Represents a single quest"""
    def __init__(self, name, description, reward, completed=False):
        self.name = name
        self.description = description
        self.reward = reward
        self.completed = completed
        self.progress = 0
    
    def complete(self):
        self.completed = True
        self.progress = 100
    
    def get_status(self):
        return "✓ Completed" if self.completed else "○ Available"


class QuestManager:
    """Manages all quests for the player"""
    def __init__(self):
        self.quests = [
            Quest("Find the Ancient Beacon", "Locate the powerful beacon artifact", 500),
            Quest("Defeat the Shadow Knight", "Vanquish the dark knight guardian and claim the Knight's Resonance", 750),
            Quest("Retrieve the Orb of Truth", "Claim the mystical orb", 1000),
            Quest("Locate the Orb Slot", "Find where the orb belongs", 600)
        ]
        self.quest_artifacts = {
            0: "beacon",
            1: "knights_resonance",
            2: "orb_of_truth",
            3: "orb_slot"
        }
    
    def get_available_quests(self):
        return [q for q in self.quests if not q.completed]
    
    def complete_quest(self, quest_index, artifact_name=None):
        if 0 <= quest_index < len(self.quests):
            if not self.quests[quest_index].completed:
                self.quests[quest_index].complete()
                return self.quests[quest_index].reward, artifact_name
        return 0, None
    
    def display_quests(self, ui):
        for i, quest in enumerate(self.quests):
            status = quest.get_status()
            print(f"  {i+1}. {ui.colors['quest']} {quest.name}")
            print(f"     Reward: {quest.reward} gold | {status}")
            print(f"     {quest.description}")


class Skill:
    """Represents a player skill/ability"""
    def __init__(self, name, mana_cost, damage, description):
        self.name = name
        self.mana_cost = mana_cost
        self.damage = damage
        self.description = description
    
    def can_use(self, current_mana):
        return current_mana >= self.mana_cost


class Player:
    """Main player character class with all stats and methods"""
    
    CLASSES = {
        "Warrior": {"health": 150, "mana": 30, "damage": 25},
        "Mage": {"health": 70, "mana": 150, "damage": 15},
        "Rogue": {"health": 100, "mana": 80, "damage": 22},
        "Knight": {"health": 140, "mana": 70, "damage": 20},
        "Adventurer": {"health": 100, "mana": 50, "damage": 18}
    }
    
    def __init__(self):
        self.name = ""
        self.player_class = ""
        self.level = 20
        self.experience = 0
        self.health = 100
        self.max_health = 100
        self.mana = 50
        self.max_mana = 50
        self.gold = 100
        self.stats_points = 1200
        self.inventory = Inventory()
        self.skills = self._initialize_skills()
    
    def _initialize_skills(self):
        """Create skills based on class"""
        skills = {
            "Power Strike": Skill("Power Strike", 0, 30, "Physical attack"),
            "Fireball": Skill("Fireball", 20, 45, "Magical spell"),
            "Heal": Skill("Heal", 15, 0, "Restore health")
        }
        return skills
    
    def create_character(self):
        """Character creation process"""
        ui = UIFormatter()
        ui.print_header("CHARACTER CREATION")
        
        
        name_valid = False
        while not name_valid:
            self.name = input("\n  Enter your character name: ").strip()
            if 2 <= len(self.name) <= 15:
                name_valid = True
            else:
                print("  ✗ Name must be between 2 and 15 characters!")
        
        
        # Get class
        class_selected = False
        while not class_selected:
            print("\n  Available Classes:")
            print("  ════════════════════════════════════════")
            for num, (class_name, stats) in enumerate(self.CLASSES.items(), 1):
                if class_name == "Knight":
                    if self.gold >= 200:
                        cost = " (COST: 200 gold)"
                    else:
                        cost = " (COST: 200 gold - LOCKED)"
                else:
                    cost = ""
                print(f"  {num}. {class_name:12} | HP: {stats['health']:3} | Mana: {stats['mana']:3} | DMG: {stats['damage']:2}{cost}")
            
            class_choice = input("\n  Select your class (1-5): ").strip()
            
            match class_choice:
                case "1":
                    self._set_class("Warrior")
                    class_selected = True
                case "2":
                    self._set_class("Mage")
                    class_selected = True
                case "3":
                    self._set_class("Rogue")
                    class_selected = True
                case "4":
                    if self.gold >= 200:
                        self.gold -= 200
                        self._set_class("Knight")
                        print("  ✓ You purchased the Knight class for 200 gold!")
                        class_selected = True
                    else:
                        print(f"  ✗ Not enough gold! You have {self.gold} gold but need 200.")
                        print("  ✗ Please choose another class (1-3).")
                case "5":
                    self._set_class("Adventurer")
                    class_selected = True
                case _:
                    print("  ✗ Invalid option! Please enter 1-5.")
        
        print(f"\n  ✓ Welcome, {self.name} the {self.player_class}!")
        ui.print_stat_line("Health", self.health, self.max_health)
        ui.print_stat_line("Mana", self.mana, self.max_mana)
        ui.print_stat_line("Gold", self.gold)
        ui.print_stat_line("Level", self.level)
    
    def _set_class(self, class_name):
        """Set player class and update stats"""                                   
        self.player_class = class_name
        stats = self.CLASSES[class_name]
        self.max_health = stats["health"]
        self.health = stats["health"]
        self.max_mana = stats["mana"]
        self.mana = stats["mana"]
    
    def display_status(self, ui):
        """Display detailed player status"""
        ui.print_header(f"{self.name} - {self.player_class} Status")
        print("\n  ▶ VITAL STATISTICS:")
        ui.print_stat_line("Health", self.health, self.max_health)
        ui.print_stat_line("Mana", self.mana, self.max_mana)
        
        print("\n  ▶ PROGRESS:")
        ui.print_stat_line("Level", self.level)
        ui.print_stat_line("Experience", self.experience)
        ui.print_stat_line("Stats Points", self.stats_points)
        
        print("\n  ▶ RESOURCES:")
        ui.print_stat_line("Gold", self.gold)
        ui.print_stat_line("Relics Collected", self.inventory.get_item_count(), 4)
        
        
        if self.health > self.max_health * 0.7:
            print("\n  ✓ Status: Ready for combat!")
        elif self.health > self.max_health * 0.3:
            print("\n  ⚠ Status: Needs healing!")
        else:
            print("\n  ✗ Status: Critical condition!")
    
    def take_damage(self, damage):
        """Take damage and reduce health"""
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def heal(self, amount):
        """Restore health"""
        self.health = min(self.health + amount, self.max_health)
    
    def use_mana(self, amount):
        """Use mana for abilities"""
        if self.mana >= amount:
            self.mana -= amount
            return True
        return False
    
    def restore_mana(self, amount):
        """Restore mana"""
        self.mana = min(self.mana + amount, self.max_mana)
    
    def gain_gold(self, amount):
        """Add gold to inventory"""
        self.gold += amount
    
    def is_alive(self):
        """Check if player is still alive"""
        return self.health > 0


class DungeonFloor:
    """Represents a single dungeon floor"""
    def __init__(self, floor_num, name, enemies, has_trap, difficulty):
        self.floor_num = floor_num
        self.name = name
        self.enemies = enemies
        self.has_trap = has_trap
        self.difficulty = difficulty
        self.cleared = False
    
    def display_info(self, ui):
        """Display floor information"""
        print(f"\n  {ui.colors['enemy']} Floor {self.floor_num}: {self.name}")
        print(f"     Difficulty: {self.difficulty} | Enemies: {self.enemies} | Trap: {'Yes' if self.has_trap else 'No'}")


class Dungeon:
    """Manages the entire dungeon experience"""
    def __init__(self):
        self.floors = [
            DungeonFloor(1, "Hall of Echoes", 2, True, "Easy"),
            DungeonFloor(2, "Chamber of Shadows", 3, False, "Easy"),
            DungeonFloor(3, "Sanctum of Light", 1, True, "Medium"),
            DungeonFloor(4, "Vault of Kings", 4, False, "Hard"),
            DungeonFloor(5, "Heart of Ra", 1, True, "Extreme")
        ]
        self.boss_name = "The Eternal Guardian"
        self.boss_health = 100
    
    def get_accessible_floors(self, player):
        """Return floors accessible to player"""
        accessible = []
        for floor in self.floors:
            if floor.floor_num <= 3 and player.health > 50:
                accessible.append(floor)
            elif floor.floor_num > 3 and player.health > 100:
                accessible.append(floor)
        return accessible


class GameManager:
    """Main game manager - orchestrates all game flow"""
    def __init__(self):
        self.player = Player()
        self.quest_manager = QuestManager()
        self.dungeon = Dungeon()
        self.ui = UIFormatter()
        self.game_active = True
    
    def start_game(self):
        """Initialize and start the game"""
        self.player.create_character()
        self.quest_manager.display_quests(self.ui)
        self.show_stats_check()
    
    def show_stats_check(self):
        """Show character requirements check"""
        self.ui.print_section("ADVANCED STATUS CHECK")
        
        level_ok = self.player.level >= 20
        stats_ok = self.player.stats_points >= 1000
        gold_ok = self.player.gold >= 100
        items_ok = self.player.inventory.has_all_items()
        
        print(f"  {self.ui.colors['success'] if level_ok else self.ui.colors['fail']} Level 20+ ({self.player.level})")
        print(f"  {self.ui.colors['success'] if stats_ok else self.ui.colors['fail']} Stats Points 1000+ ({self.player.stats_points})")
        print(f"  {self.ui.colors['success'] if gold_ok else self.ui.colors['fail']} Gold 100+ ({self.player.gold})")
        print(f"  {self.ui.colors['success'] if items_ok else self.ui.colors['fail']} All Relics ({self.player.inventory.get_item_count()}/4)")
        
        if level_ok and stats_ok and items_ok:
            print(f"\n  ✓ You can enter the dungeon!")
        else:
            print(f"\n  ✗ You cannot enter yet!")
    
    def show_dungeon_floors(self):
        """Display available dungeon floors"""
        self.ui.print_section("DUNGEON FLOOR ANALYSIS")
        
        print("\n  Analysis of accessible floors based on your health:\n")
        for floor in self.dungeon.floors:
            if self.player.health > (50 if floor.floor_num <= 3 else 100):
                status = f"{self.ui.colors['success']} Accessible"
            else:
                status = f"{self.ui.colors['fail']} Locked"
            
            floor_info = f"Floor {floor.floor_num}: {floor.name:20} [{floor.difficulty:7}] - {status}"
            print(f"  {floor_info}")
    
    def minigame_beacon_hunt(self):
        """Mini-game for finding the beacon - riddle challenge"""
        self.ui.print_section("BEACON HUNT CHALLENGE")
        print("\n  A mystical guardian blocks your path...")
        print("  'Answer my riddle correctly and claim the beacon!\n")
        
        riddles = [
            {"q": "  I am not alive, but I grow. I don't have lungs, but I need air. What am I?", "a": "fire"},
            {"q": "  What has cities but no houses, forests but no trees, and water but no fish?", "a": "map"},
            {"q": "  I speak without a mouth and hear without ears. I have no body, but come alive with the wind. What am I?", "a": "echo"}
        ]
        
        import random
        riddle = random.choice(riddles)
        print(riddle["q"])
        
        answer = input("\n  Your answer: ").strip().lower()
        
        if answer == riddle["a"]:
            print("\n  ✓ Correct! The beacon glows in your hands!")
            return True
        else:
            print(f"\n  ✗ Wrong! The answer was: {riddle['a']}")
            return False
    
    def minigame_shadow_knight_battle(self):
        """Mini-game for defeating shadow knight - simple combat"""
        self.ui.print_section("SHADOW KNIGHT BATTLE")
        print("\n  A dark figure emerges from the shadows...\n")
        
        import random
        enemy_hp = 30
        player_hp = self.player.health
        rounds = 0
        max_rounds = 5
        
        while enemy_hp > 0 and rounds < max_rounds:
            rounds += 1
            print(f"  Round {rounds}:")
            self.ui.print_stat_line("Health", player_hp, self.player.max_health)
            self.ui.print_stat_line("Mana", self.player.mana, self.player.max_mana)
            print(f"    Enemy HP: {enemy_hp}")
            print("    (1) Heavy Attack  (2) Quick Dodge  (3) Magic Strike")
            print("    (4) Block  (5) Heal")
            
            choice = input("    Choose action (1-5): ").strip()
            
            match choice:
                case "1":
                    damage = random.randint(8, 15)
                    enemy_hp -= damage
                    print(f"    ⚔ You strike hard! Deal {damage} damage!")
                    enemy_damage = random.randint(5, 12)
                case "2":
                    damage = random.randint(2, 5)
                    enemy_hp -= damage
                    print(f"    🛡 You dodge and counter! Deal {damage} damage!")
                    enemy_damage = random.randint(3, 7)
                case "3":
                    if self.player.mana >= 20:
                        self.player.use_mana(20)
                        damage = random.randint(12, 20)
                        enemy_hp -= damage
                        print(f"    ✨ Magical strike! Deal {damage} damage!")
                        enemy_damage = random.randint(5, 9)
                    else:
                        print(f"    ✗ Not enough mana! You fumble your spell...")
                        enemy_damage = random.randint(8, 12)
                case "4":
                    print(f"    🛡 You raise your guard and block incoming damage!")
                    block_raw = random.randint(5, 12)
                    enemy_damage = max(1, int(block_raw * 0.2))
                    print(f"    ⚔ You block 80% of the attack, taking only {enemy_damage} damage.")
                case "5":
                    if self.player.mana >= 15:
                        self.player.use_mana(15)
                        heal_amount = random.randint(12, 22)
                        player_hp = min(player_hp + heal_amount, self.player.max_health)
                        print(f"    ✚ You heal for {heal_amount} HP! Your health improves.")
                        enemy_damage = random.randint(6, 10)
                    else:
                        print(f"    ✗ Not enough mana to heal! You fail to recover.")
                        enemy_damage = random.randint(9, 13)
                case _:
                    print(f"    ⚠ You hesitate! The enemy seizes the opening.")
                    enemy_damage = random.randint(8, 13)
            
            if enemy_hp <= 0:
                print(f"\n  ✓ Victory! The shadow knight falls!")
                return True
            
            player_hp -= enemy_damage
            player_hp = max(player_hp, 0)
            print(f"    Enemy counter-attacks! Take {enemy_damage} damage.")
            self.ui.print_stat_line("Health", player_hp, self.player.max_health)
            self.ui.print_stat_line("Mana", self.player.mana, self.player.max_mana)
            print()
            
            if player_hp <= 0:
                print(f"  ✗ Defeat! You fall in combat...")
                return False
        
        if rounds >= max_rounds:
            print(f"  ✗ You couldn't defeat the knight in time!")
            return False
        return False
    
    def minigame_truth_puzzle(self):
        """Mini-game for orb of truth - logic puzzle"""
        self.ui.print_section("ORB OF TRUTH PUZZLE")
        print("\n  An ancient puzzle stands before you...")
        print("  Solve it to claim the Orb of Truth!\n")
        
        puzzles = [
            {
                "q": "  In a room with 3 switches and 3 lightbulbs:\n"
                     "  - You can flip switches, but only see the bulbs once\n"
                     "  - How do you match switches to bulbs?",
                "a": "turn on one, leave one on, leave one off, then feel them",
                "hints": ["bulb", "heat", "warm", "temperature", "feel", "touch"]
            },
            {
                "q": "  A man pushes his car and tells his wife he's ruined.\n"
                     "  Why?",
                "a": "he's playing monopoly",
                "hints": ["game", "board", "monopoly", "play"]
            },
            {
                "q": "  What 4-letter word can be written forward, backward, or upside down?",
                "a": "noon",
                "hints": ["time", "clock", "symmetry", "mirror"]
            }
        ]
        
        import random
        puzzle = random.choice(puzzles)
        print(puzzle["q"])
        
        attempts = 0
        while attempts < 2:
            answer = input("\n  Your answer: ").strip().lower()
            
            if any(hint in answer for hint in puzzle["hints"]) or answer == puzzle["a"]:
                print("\n  ✓ Brilliant! The Orb resonates with your wisdom!")
                return True
            else:
                attempts += 1
                if attempts < 2:
                    print(f"  ✗ Not quite... Try again! (Attempt {attempts}/2)")
        
        print(f"\n  ✗ You couldn't solve the puzzle. The orb remains hidden.")
        return False
    
    def minigame_slot_search(self):
        """Mini-game for orb slot - search/find challenge"""
        self.ui.print_section("ORB SLOT SEARCH")
        print("\n  You must search for the hidden Orb Slot in the temple...\n")
        
        temple_locations = ["Altar", "Fountain", "Pillar", "Statue", "Floor"]
        correct_location = temple_locations[0]
        
        import random
        random.shuffle(temple_locations)
        
        print("  Available search locations:")
        for i, location in enumerate(temple_locations, 1):
            print(f"    {i}. {location}")
        
        attempts = 0
        while attempts < 3:
            choice = input("\n  Where will you search? (1-5): ").strip()
            
            if choice.isdigit() and 1 <= int(choice) <= len(temple_locations):
                selected = temple_locations[int(choice) - 1]
                
                if selected == correct_location:
                    print(f"\n  ✓ Found it! The Orb Slot was in the {selected}!")
                    return True
                else:
                    attempts += 1
                    if attempts < 3:
                        print(f"  ✗ Not here... Try another location! ({attempts}/3 attempts)")
                    else:
                        print(f"  ✗ You've searched everywhere but found nothing...")
            else:
                print("  ✗ Invalid choice!")
        
        return False
    
    def run_quest_minigame(self, quest_idx):
        """Run the appropriate mini-game for a quest"""
        minigames = [
            self.minigame_beacon_hunt,
            self.minigame_shadow_knight_battle,
            self.minigame_truth_puzzle,
            self.minigame_slot_search
        ]
        
        if 0 <= quest_idx < len(minigames):
            return minigames[quest_idx]()
        return False
    
    
    def quest_menu(self):
        """Handle quest management menu"""
        in_quest_menu = True
        while in_quest_menu:
            self.ui.print_section("QUEST MANAGEMENT")
            
            print("\n  ▶ Available Quests:")
            for i, quest in enumerate(self.quest_manager.quests, 1):
                status = quest.get_status()
                print(f"    {i}. {quest.name:30} | Reward: {quest.reward:4} gold | {status}")
            
            print("\n  Menu Options:")
            print("  1. Accept a quest")
            print("  2. View quest progress")
            print("  3. Complete a quest")
            print("  4. Return to main game")
            
            choice = input("\n  Select (1-4): ").strip()
            
            match choice:
                case "1":
                    quest_num = input("  Enter quest number to accept: ").strip()
                    if quest_num.isdigit() and 1 <= int(quest_num) <= len(self.quest_manager.quests):
                        idx = int(quest_num) - 1
                        if not self.quest_manager.quests[idx].completed:
                            print(f"  ✓ You accepted: {self.quest_manager.quests[idx].name}")
                        else:
                            print(f"  ✗ This quest is already completed!")
                    else:
                        print("  ✗ Invalid quest number!")
                
                case "2":
                    print("\n  ▶ Quest Progress:")
                    for i, quest in enumerate(self.quest_manager.quests, 1):
                        print(f"    {i}. {quest.name:30} | {quest.get_status()}")
                
                case "3":
                    quest_num = input("  Enter quest number to complete: ").strip()
                    if quest_num.isdigit() and 1 <= int(quest_num) <= len(self.quest_manager.quests):
                        idx = int(quest_num) - 1
                        if not self.quest_manager.quests[idx].completed:
                            print(f"\n  Starting quest challenge...\n")
                            if self.run_quest_minigame(idx):
                                reward, artifact_name = self.quest_manager.complete_quest(idx, self.quest_manager.quest_artifacts.get(idx))
                                self.player.gain_gold(reward)
                                artifact_key = self.quest_manager.quest_artifacts.get(idx)
                                self.player.inventory.items[artifact_key] = True
                                display_artifact = "Knight's Resonance" if artifact_key == "knights_resonance" else artifact_key.replace('_', ' ').title()
                                print(f"\n  ✓ Quest completed! You earned {reward} gold!")
                                print(f"  ✓ You obtained: {display_artifact}!")
                            else:
                                print(f"  ✗ Quest failed! Try again later.")
                        else:
                            print(f"  ✗ This quest is already completed!")
                    else:
                        print("  ✗ Invalid quest number!")
                
                case "4":
                    in_quest_menu = False
                    print("  Returning to main game...")
                
                case _:
                    print("  ✗ Invalid option!")
    
    def verify_artifacts(self):
        """Verify player has all required artifacts"""
        self.ui.print_section("ARTIFACT VERIFICATION")
        
        artifacts = {
            "beacon": self.player.inventory.items.get("beacon"),
            "knights_resonance": self.player.inventory.items.get("knights_resonance"),
            "orb_of_truth": self.player.inventory.items.get("orb_of_truth"),
            "orb_slot": self.player.inventory.items.get("orb_slot")
        }
        
        print("\n  The guardian of the dungeon appears before you...\n")
        print("  'Tell me truthfully, wanderer:'\n")
        
        response = input("  -| Do you have the beacon? |- (yes/no): ").lower() == "yes"
        if response and not artifacts['beacon']:
            print("\n  Filthy Lies!, a kind of thou jest shall not enter the dungeon.")
            return False
        if not response and artifacts['beacon']:
            print("\n  Filthy Lies!, thou pretendest to be humble but you do have the beacon!")
            return False
        
        response = input("  -| Are you a knight? |- (yes/no): ").lower() == "yes"
        if response and self.player.player_class != "Knight":
            print("\n  Filthy Lies!, a kind of thou jest shall not enter the dungeon.")
            return False
        if not response and self.player.player_class == "Knight":
            print("\n  Filthy Lies!, thou pretendest to be false, yet the knight's blood runs in you!")
            return False
        
        response = input("  -| Do you possess the Knight's Resonance? |- (yes/no): ").lower() == "yes"
        if response and not artifacts['knights_resonance']:
            print("\n  Filthy Lies!, a kind of thou jest shall not enter the dungeon.")
            return False
        if not response and artifacts['knights_resonance']:
            print("\n  Filthy Lies!, thou deny the resonance yet it hums in your hands!")
            return False
        
        response = input("  -| Do you have the Orb of Truth? |- (yes/no): ").lower() == "yes"
        if response and not artifacts['orb_of_truth']:
            print("\n  Filthy Lies!, a kind of thou jest shall not enter the dungeon.")
            return False
        if not response and artifacts['orb_of_truth']:
            print("\n  Filthy Lies!, thou deny the orb although it is thine!")
            return False
        
        response = input("  -| Do you have the Orb Slot? |- (yes/no): ").lower() == "yes"
        if response and not artifacts['orb_slot']:
            print("\n  Filthy Lies!, a kind of thou jest shall not enter the dungeon.")
            return False
        if not response and artifacts['orb_slot']:
            print("\n  Filthy Lies!, thou deny the slot though it is present with thee!")
            return False
        
        print("  ✓ The guardian nods... 'You speak truth, wanderer.'")
        print("  ✓ The dungeon entrance glows with acceptance.")
        return True
        
        if lies:
            for lie in lies:
                print(lie)
            print("\n  FILTHY LIES, THOU SHALL NOT ENTER THE DUNGEON!")
            print("  ✗ The guardian blocks your path with magical force.")
            return False
        else:
            print("  ✓ The guardian nods... 'You speak truth, wanderer.'")
            print("  ✓ The dungeon entrance glows with acceptance.")
            return True     
    
    def enter_dungeon(self):
        """Enter the dungeon and engage in combat"""
        if self.player.level < 20 or self.player.stats_points < 1000:
            print("\n  ✗ You cannot enter yet! Insufficient level or stats.")
            return
        
        if self.player.player_class != "Knight":
            print("\n  ✗ Only the Knight class may enter this dungeon. Become a Knight to proceed.")
            return
        
        if not self.verify_artifacts():
            print("\n  ✗ The dungeon rejects you!")
            return
        
        self.ui.print_header("ENTERING DUNGEON OF RA")
        print("\n  You step into the ancient dungeon, ready to face its challenges...\n")
        
        for floor in self.dungeon.floors:
            if not self.player.is_alive():
                break
            
            self._explore_floor(floor)
        
        
        self._dungeon_finale()
    
    def _explore_floor(self, floor):
        """Explore a single dungeon floor"""
        floor.display_info(self.ui)
        
        
        if floor.has_trap:
            print(f"    ⚠ A trap is triggered!")
            trap_damage = 25 if self.player.player_class != "Rogue" else 10
            self.player.take_damage(trap_damage)
            if self.player.player_class == "Rogue" or (self.player.player_class == "Knight" and self.player.health > 100):
                print(f"    ✓ You skillfully avoid most damage! ({trap_damage} damage avoided)")
            else:
                print(f"    ✗ You take {trap_damage} damage from the trap!")
        
        
        enemies_left = floor.enemies
        while enemies_left > 0 and self.player.is_alive():
            self._handle_combat(enemies_left)
            enemies_left -= 1
        
        if self.player.is_alive():
            print(f"    ✓ Floor cleared! Moving forward...")
        
        print("    " + "─" * 56)
    
    def _handle_combat(self, enemies_remaining):
        """Handle single combat encounter"""
        print(f"\n    {self.ui.colors['enemy']} Enemy appears! ({enemies_remaining} more)")
        self.ui.print_stat_line("Health", self.player.health, self.player.max_health)
        self.ui.print_stat_line("Mana", self.player.mana, self.player.max_mana)
        print("    Actions: (1) Attack  (2) Defend  (3) Use Skill  (4) Heal  (5) Block")
        
        action = input("    Choose action (1-5): ").strip()
        
        match action:
            case "1":
                damage = 15 + (5 if self.player.player_class == "Warrior" else 0)
                print(f"    ⚔ You attack! Deal {damage} damage!")
                enemy_damage = max(0, 10 - (3 if self.player.player_class == "Knight" else 0))
            case "2":
                print(f"    🛡 You defend! Reduced damage incoming...")
                enemy_damage = max(0, 5 - (2 if self.player.player_class == "Knight" else 0))
            case "3":
                if self.player.mana >= 15:
                    self.player.use_mana(15)
                    print(f"    ✨ Powerful spell! {self.player.mana}/{self.player.max_mana} mana left")
                    enemy_damage = 2
                else:
                    print(f"    ✗ Not enough mana! You hesitate...")
                    enemy_damage = 15
            case "4":
                if self.player.mana >= 15 and self.player.health < self.player.max_health * 0.5:
                    self.player.use_mana(15)
                    self.player.heal(30)
                    print(f"    ✚ You heal with mana! Health is now {self.player.health}/{self.player.max_health}")
                    enemy_damage = 8
                elif self.player.health >= self.player.max_health * 0.5:
                    print(f"    ✗ You're not hurt enough to need healing!")
                    enemy_damage = 15
                else:
                    print(f"    ✗ Not enough mana to heal! You hesitate...")
                    enemy_damage = 15
            case "5":
                print(f"    🛡 You brace yourself and block the attack!")
                raw_damage = max(0, 10 - (3 if self.player.player_class == "Knight" else 0))
                enemy_damage = max(1, int(raw_damage * 0.2))
                print(f"    ⚔ You block 80% of incoming damage, taking only {enemy_damage}!")
            case _:
                print(f"    ⚠ You hesitate and the enemy strikes!")
                enemy_damage = 15
        
        self.player.take_damage(enemy_damage)
        self.ui.print_stat_line("Health", self.player.health, self.player.max_health)
        self.ui.print_stat_line("Mana", self.player.mana, self.player.max_mana)
        print(f"    Enemy deals {enemy_damage} damage! Your HP: {self.player.health}/{self.player.max_health}")
    
    def _dungeon_finale(self):
        """Display dungeon completion status"""
        self.ui.print_section("DUNGEON FINALE")
        
        if not self.player.is_alive():
            print("\n  ✗ You have fallen in the dungeon...")
            print(f"  Final Stats: HP {self.player.health}/{self.player.max_health} | Mana: {self.player.mana}/{self.player.max_mana}")
            return
        
        all_items = self.player.inventory.has_all_items()
        
        if all_items and self.player.is_alive():
            print("\n  ✓✓✓ YOU REACHED THE HEART OF RA WITH ALL RELICS! ✓✓✓")
            print("  A great treasure is revealed! You have won!")
            self.player.gain_gold(1000)
            print(f"  Treasure acquired: 1000 gold!")
        else:
            print("\n  ✓ You reached the Heart of Ra, but lack some relics.")
            print("  You escape with your life, but not the ultimate prize.")
            self.player.gain_gold(200)
        
        print(f"\n  Final Status:")
        print(f"    HP: {self.player.health}/{self.player.max_health}")
        print(f"    Mana: {self.player.mana}/{self.player.max_mana}")
        print(f"    Gold: {self.player.gold}")
        print(f"    Level: {self.player.level}")
    
    def purchase_class_menu(self):
        """Allow player to buy a class from the main menu"""
        print("\n  ▶ Class Purchase Menu")
        print("    1. Knight - 200 gold")
        print("    2. Return")
        choice = input("\n  Select an option (1-2): ").strip()
        match choice:
            case "1":
                if self.player.player_class == "Knight":
                    print("  ✗ You already have the Knight class.")
                    return
                if self.player.gold >= 200:
                    self.player.gold -= 200
                    self.player._set_class("Knight")
                    print("  ✓ You purchased the Knight class and your stats have been updated!")
                else:
                    print(f"  ✗ Not enough gold! You need 200 gold but have {self.player.gold}.")
            case "2":
                print("  Returning to main menu...")
            case _:
                print("  ✗ Invalid option!")

    def main_game_loop(self):
        """Main game loop"""
        while self.game_active:
            self.ui.print_section("MAIN GAME MENU")
            print("\n  1. Check full status")
            print("  2. View inventory")
            print("  3. Manage quests")
            print("  4. View dungeon floors")
            print("  5. Start dungeon attempt")
            print("  6. Buy class")
            print("  7. Quit game")
            
            choice = input("\n  Select (1-7): ").strip()
            
            match choice:
                case "1":
                    self.player.display_status(self.ui)
                case "2":
                    self.player.inventory.display_full_inventory(self.ui)
                case "3":
                    self.quest_menu()
                case "4":
                    self.show_dungeon_floors()
                case "5":
                    self.enter_dungeon()
                case "6":
                    self.purchase_class_menu()
                case "7":
                    self.ui.print_header("THANKS FOR PLAYING!")
                    print("\n  Your adventure ends here, brave wanderer.")
                    self.game_active = False
                case _:
                    print("  ✗ Invalid option!")
    
    def run(self):
        """Run the complete game"""
        self.start_game()
        self.main_game_loop()



print("DUNGEON OF RA - EXPANDED RPG ADVENTURE")
print("="*50 + "\n")

if __name__ == "__main__":
    game = GameManager()
    game.run()


