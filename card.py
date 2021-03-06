suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit



# Test functionality
if __name__ == '__main__':
    jack_hearts = Card('Hearts', 'Jack')
    print(jack_hearts)
    print(f'Value: {jack_hearts.value}')

    ace_spades = Card('Spades', 'Ace')
    print(ace_spades)
    print(f'Value: {ace_spades.value}')