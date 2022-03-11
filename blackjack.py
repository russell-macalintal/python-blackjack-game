import deck
import player
import dealer

player = player.Player('Jack Black')
dealer = dealer.Dealer()
new_deck = deck.Deck()
new_deck.shuffle()

player.get_card(new_deck.deal_card())
player.get_card(new_deck.deal_card())

dealer.get_card(new_deck.deal_card())       # Only give the dealer one card for now to avoid having to hide the second card - second card will be dealt and 'revealed' once the player has completed their turn

print(player)
print(dealer)