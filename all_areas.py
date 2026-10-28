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
    