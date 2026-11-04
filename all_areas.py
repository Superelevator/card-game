class Area:
    def __init__(self, area_id, cards):
        self.area_id = area_id
        self.cards = cards
    def add_card(self, card):
        self.cards.append(card)
    def remove_card(self, card):
        self.cards.remove(card)
    def get_cards(self):
        return self.cards
    def get_card_count(self):
        return len(self.cards)
    def get_card_by_id(self, card_id):
        for card in self.cards:
            if card.card_id == card_id:
                return card
        return None


class Hand(Area):
    pass


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

