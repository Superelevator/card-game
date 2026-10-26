class Card:
    def __init__(self, card_id, display_name, type, rank, suit, location):
        self.card_id = card_id
        self.display_name = display_name
        self.bg_type = bg_type
        self.rank = rank
        self.suit = suit
        self.location = location
    def __repr__(self):
        return f"{self.display_name} ({self.rank} of {self.suit})"
    def get_location(self):
        return self.location
    def use_card(self):
        