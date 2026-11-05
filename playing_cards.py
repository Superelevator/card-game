import card_game_main as game

class Card:
    def __init__(self, card_id, display_name, card_class, card_type, temp_status=None, rank=0, suit=None, location=None):
        # card_id is the unique id of the card
        self.card_id = card_id

        # display_name is the displayed name of the card (within the UI)
        self.display_name = display_name

        # card_class is the type of card (e.g. "basic", "action", "weapon", "equipment", "terrain", "infrastructure")
        self.card_class = card_class

        # card_type is the specific type of card (e.g. "ATTACK!", "DODGE!", "Supplies", "Oil", "Fortifications", "")
        self.card_type = card_type

        # temp_status denotes any temporary status of the card (used as judgement card, unit, substitute as per ability or policy or action card, etc.)
        self.temp_status = temp_status

        # rank is the rank of the card (e.g. A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
        self.rank = rank

        # suit is the suit of the card (e.g. "hearts", "diamonds", "clubs", "spades")
        self.suit = suit

        # location is the location of the card (i.e. "player 2 hand", "deck", "discard", "player 1 equipment zone", "player 3 religion zone", etc.)
        self.location = location


    def __repr__(self):
        # return display name & card rank and suit
        return f"{self.display_name} ({self.rank} of {self.suit})"

    def get_location(self):
        # returns where the card is located
        return self.location

    def use_card(self):
        # use the card (functionality specified per card subclass)
        self.location = game.discard

    def move_card(self, destination):
        # moves the card to a new location
        self.location.remove_card(self)
        self.location = destination
        destination.add_card(self)
    
