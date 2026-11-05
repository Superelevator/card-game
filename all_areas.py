from playing_cards import *

# A general area class, capable of storing cards & serves as the location of the card
class Area:
    def __init__(self, area_id, cards, capacity, slots=[], slot_capacities=[]):
        # area id is the unique id of the area (formatted {type_id}_{player_id (if necessary else 0)}_{area_type})
        self.area_id = area_id

        # list of cards stored in the area
        self.cards = cards

        # capacity is the maximum number of cards that can be stored in the area
        self.capacity = capacity

        # slots is a list of slots in the area (formatted as slot type)
        self.slots = slots

        # slot_capacities is a list of the maximum number of cards that can be stored in each slot, float('inf') to remove limit
        self.slot_capacities = slot_capacities

        

    def add_card(self, card: Card):
        # adds a card to area (with consideration to slots)
        if self.slots != []:
            for slot_type in self.slots:
                if card.card_class == slot_type:
                    pass
        self.cards.append(card)

    def remove_card(self, card):
        # removes a card from area
        self.cards.remove(card)

    def get_cards(self):
        # returns all cards within the area
        return self.cards

    def get_card_count(self):
        # returns number of cards in the area
        return len(self.cards)

    def get_card_by_id(self, card_id):
        # returns card by id for consideration
        for card in self.cards:
            if card.card_id == card_id:
                return card
        return None

    def get_card_by_type(self, card_type):
        # returns cards by type for consideration
        for card in self.cards:
            if card.card_type == card_type:
                return card
        return None


# AREA SUBCLASS - Player's Hand
class Hand(Area):
    def __init__(self, area_id, cards):
        super().__init__(area_id, cards)


# AREA SUBCLASS - Player's Equipment Zone
class EquipmentZone(Area):
    def __init__(self, area_id, cards, weapon_slot, equipment_slot, terrain_slot, infrastructure_slot):
        super().__init__(area_id, cards)
        self.weapon_slot = weapon_slot
        self.equipment_slot = equipment_slot
        self.terrain_slot = terrain_slot
        self.infrastructure_slot = infrastructure_slot
    def add_card(self, card):
        if card.card_type == "weapon" and len(self.weapon_slot.cards) != 0:
            self.weapon_slot.append(card)
        elif card.card_type == "equipment" and len(self.equipment_slot.cards) != 0:
            self.equipment_slot.append(card)
        elif card.card_type == "terrain" and len(self.equipment_slot.cards) != 0:
            self.terrain_slot.append(card)
        elif card.card_type == "infrastructure" and len(self.infrastructure_slot.cards) != 0:
            self.infrastructure_slot.append(card)
        else:
            raise ValueError("Card cannot be added to the equipment zone")
    def remove_card(self, card):
        if card.card_type == "weapon":
            self.weapon_slot.remove(card)
        elif card.card_type == "equipment":
            self.equipment_slot.remove(card)
        elif card.card_type == "terrain":
            self.terrain_slot.remove(card)
        elif card.card_type == "infrastructure":
            self.infrastructure_slot.remove(card)
        else:
            raise ValueError("Card cannot be removed from the equipment zone")


class ReligionZone(Area):
    pass





class PlayerZone:
    def __init__(self, player_id, hand, equipment_zone, religion_zone, policy_zone, judgement_zone):
        self.player_id = player_id
        self.hand = hand
        self.equipment_zone = equipment_zone
        self.religion_zone = religion_zone
        self.policy_zone = policy_zone
        self.judgement_zone = judgement_zone

