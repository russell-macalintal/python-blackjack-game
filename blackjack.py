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

