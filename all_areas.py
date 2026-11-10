from playing_cards import *

# A general area class, capable of storing cards & serves as the location of the card
class Area:
    def __init__(self, area_id, cards, capacity=float('inf'), slots=[], slot_capacities=[]):
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

        

    def add_card(self, card: Card, slot_type=None):
        # adds a card to area (with consideration to slots)
        if slot_type is not None:
            if self.slot_available(slot_type):
                self.slots[slot_type].append(card)
                return
            else:
                raise ValueError(f"Slot {slot_type} is at capacity")
        if self.capacity != float('inf') and len(self.cards) >= self.capacity:
            raise ValueError("Area is at capacity")
        self.cards.append(card)
        self.capacity += 1

    def remove_card(self, card, slot_type=None):
        # removes a card from area
        if slot_type is not None:
            self.slots[slot_type].remove(card)
            return
        self.cards.remove(card)
        self.capacity -= 1

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

    def slot_available(self, slot_type):
        # checks if a slot is available for a given slot type
        slot_id = self.slots.index(slot_type)
        return len(self.slots[slot_id]) < self.slot_capacities[slot_id]

    def check_card_slot(self, card):
        # checks which slot a card is in
        for slot in self.slots:
            if card in slot:
                return slot

# AREA SUBCLASS - Player's Hand
class Hand(Area):
    def __init__(self, area_id, cards):
        super().__init__(area_id, cards)


# AREA SUBCLASS - Player's Equipment Zone
class EquipmentZone(Area):
    def __init__(self, area_id, cards, weapon_slot, equipment_slot, terrain_slot, infrastructure_slot):
        super().__init__(area_id, cards)
        self.slots = ["weapon", "equipment", "terrain", "infrastructure"]
        self.slot_capacities = [1, 1, 1, 1]
    


class ReligionZone(Area):
    def __init__(self, area_id, cards, religion_slots):
        super().__init__(area_id, cards)
        self.slots = religion_slots
        self.slot_capacities = [float('inf')] * len(religion_slots)





class PlayerZone:
    def __init__(self, player_id, hand, equipment_zone, religion_zone, policy_zone, judgement_zone):
        self.player_id = player_id
        self.hand = hand
        self.equipment_zone = equipment_zone
        self.religion_zone = religion_zone
        self.policy_zone = policy_zone
        self.judgement_zone = judgement_zone

