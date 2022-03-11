import deck
import player
import dealer
import time

player = player.Player('Jack Black')
dealer = dealer.Dealer()
new_deck = deck.Deck()
new_deck.shuffle()

player.get_card(new_deck.deal_card())
player.get_card(new_deck.deal_card())

dealer.get_card(new_deck.deal_card())       # Only give the dealer one card for now to avoid having to hide the second card - second card will be dealt and 'revealed' once the player has completed their turn

print(player)
print(f'Card total: {player.get_total()}')
print(dealer)
print(f'Card total: {dealer.get_total()}')

end_player_turn = False

while not end_player_turn and player.get_total() <= 21:
    move = input('Hit (h) or Stay (s)? ')
    if move == 'h':
        player.get_card(new_deck.deal_card())
    elif move == 's':
        end_player_turn = True
        break
    else:
        print('Invalid input. Try again')
        continue
    
    print(player)
    print(f'Card total: {player.get_total()}')

    if player.get_total() > 21:
        print('BUST! GAME OVER. DEALER WINS!')
        quit()                                      # If player goes above 21, game automatically closes. Dealer does not need to show cards.


dealer.get_card(new_deck.deal_card())
print('\nDealer shows both cards...')
print(dealer)
print(f'Card total: {dealer.get_total()}')


while dealer.get_total() <= 21 and dealer.get_total() < player.get_total():
    print('Dealer is hitting...')
    time.sleep(1)
    dealer.get_card(new_deck.deal_card())

    print(dealer)
    print(f'Card total: {dealer.get_total()}')


# Check winning conditions at the end
if dealer.get_total() > 21:
    print(f'DEALER BUSTS! GAME OVER. {player.name} WINS!')
else:
    print('DEALER WINS!')