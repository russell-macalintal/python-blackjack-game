import deck

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []                  # List of cards that the player has on hand

    def __str__(self):
        if self.hand == []:
            return f'Player {self.name} has no cards'
        else:
            return f'Player {self.name} has the following cards: {", ".join([str(x) for x in self.hand])}'

    def get_card(self, new_card):
        self.hand.append(new_card)


if __name__ == "__main__":
    deck = deck.Deck()
    deck.shuffle()
    player = Player('Stewart')
    player.get_card(deck.deal_card())
    player.get_card(deck.deal_card())
    print(player)