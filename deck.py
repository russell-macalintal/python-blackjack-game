import card
import random

class Deck:
    def __init__(self):
        self.all_cards = []                         # Create empty list to store all cards

        for suit in card.suits:                     # Populate deck with newly created cards
            for rank in card.ranks:
                new_card = card.Card(suit, rank)
                self.all_cards.append(new_card)

    def shuffle(self):                              # Shuffle cards destructively
        random.shuffle(self.all_cards)

    def deal_card(self):
        return self.all_cards.pop()