import deck

class Dealer:

    def __init__(self):
        self.hand = []              # List of cards that the dealer/house has on hand

    def __str__(self):
        if self.hand == []:
            return f'Dealer has no cards'
        elif len(self.hand) == 1:
            return f'Dealer has the following cards: {self.hand[0]} and a hidden card'
        else:
            return f'Dealer has the following cards: {", ".join([str(x) for x in self.hand])}'

    def get_card(self, new_card):
        self.hand.append(new_card)

    def get_total(self):
        total = 0
        if len(self.hand) > 0:
            for card in self.hand:
                total += card.value
        return total



if __name__ == "__main__":
    deck = deck.Deck()
    deck.shuffle()
    dealer = Dealer()
    dealer.get_card(deck.deal_card())
    dealer.get_card(deck.deal_card())
    print(dealer)
    print(f'Total value of cards: {dealer.get_total()}')
