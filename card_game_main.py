import playing_cards as cards
import all_areas as areas
import json

# Class for storing the state of the game
class Game:
    def __init__(self, players, general_areas):
        # initialize players
        self.players = players
        self.general_areas = general_areas

class Player:
    def __init__(self, player_id, name, country, player_zone):
        self.player_id = player_id
        self.name = name
        self.country = country
        self.player_zone = player_zone

# INITIALIZE GAME

# players
player_count = int(input("Enter the number of players: "))
for player in range(player_count):
    # general information on player
    player_name = input(f"Please enter your name: ")
    player_country = input(f"Enter country you'd like to use: ")

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

    # player's zone
    player_zone = areas.PlayerZone(player_name, hand, equipment_zone, religion_zone, policy_zone, judgement_zone)

    # initialize player
    player = Player(player_name, player_country, hand, player_zone)

# general areas
discard_pile = areas.Area(f"discard_pile", [])
deck = areas.Area(f"deck", [])
policy_deck = areas.Area(f"policy_deck", [])

# cards
card_info = json.load(open("card_information.json"))
for card in card_info.keys():
    card_name = card_info[card]["name"]
    print(card_name)