import playing_cards as cards
import all_areas as areas

# Class for storing the state of the game
class Game:
    def __init__(self, players, general_areas):
        # initialize players
        self.players = players
        self.general_areas = general_areas

class Player:
    def __init__(self, player_id, name, hand, equipment_zone, religion_zone, policy_zone, judgement_zone):
        self.player_id = player_id
        self.name = name
        self.hand = hand
        self.equipment_zone = equipment_zone
        self.religion_zone = religion_zone
        self.policy_zone = policy_zone
        self.judgement_zone = judgement_zone

# initialize game
player_count = int(input("Enter the number of players: "))
for player in player_count:
    # general information on player
    player_name = input(f"Please enter your name: ")
    player_avatar = input(f"Enter avatar you'd like to use: ")

    # initialize player's information

    # player's hand
    hand = areas.Hand(f"hand_{player_name}", [])
    
    # player's equipment zone
    equipment_zone_slots = ["weapon", "equipment", "terrain", "infrastructure"]
    equipment_zone_slot_capacities = [1, 1, 1, 1]
    equipment_zone = areas.EquipmentZone(f"equipment_zone_{player_name}", [], equipment_zone_slots, equipment_zone_slot_capacities)

    # player's religion zone
    religion_zone_slots = ["slot 1", "slot 2"]
    religion_zone_slot_capacities = [1, 1]
    religion_zone = areas.ReligionZone(f"religion_zone_{player_name}", [], religion_zone_slots, religion_zone_slot_capacities)

    # player's policy zone
    policy_zone_slots = ["slot 1", "slot 2"]
    policy_zone_slot_capacities = [1, 1]
    policy_zone = areas.PolicyZone(f"policy_zone_{player_name}", [], policy_zone_slots, policy_zone_slot_capacities)

    # player's judgement zone
    judgement_zone_slots = ["slot 1", "slot 2"]
    judgement_zone_slot_capacities = [1, 1]
    judgement_zone = areas.JudgementZone(f"judgement_zone_{player_name}", [], judgement_zone_slots, judgement_zone_slot_capacities)

    # initialize player
    player = Player(player_name, hand, equipment_zone, religion_zone, policy_zone, judgement_zone)