class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []                  # List of cards that the player has on hand

    def __str__(self):
        return f'Player {self.name} has the following cards: {"".join([str(x) for x in self.hand])}'


if __name__ == "__main__":
    player = Player('Stewart')
    print(player)