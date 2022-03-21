import deck
import player
import dealer
import time

player = player.Player('Jack Black')
dealer = dealer.Dealer()
new_deck = deck.Deck()
new_deck.shuffle()
has_ace = 0
dealer_has_ace = 0

if new_deck.all_cards[-1].rank == "Ace":
    has_ace += 1
player.get_card(new_deck.deal_card())

if new_deck.all_cards[-1].rank == "Ace":
    has_ace += 1
player.get_card(new_deck.deal_card())

if new_deck.all_cards[-1].rank == "Ace":
    dealer_has_ace += 1
dealer.get_card(new_deck.deal_card())       # Only give the dealer one card for now to avoid having to hide the second card - second card will be dealt and 'revealed' once the player has completed their turn


print(player)
print(f'Card total: {player.get_total()}')
print(dealer)
print(f'Card total: {dealer.get_total()}')


if player.get_total() == 21:                # Checks for default win condition
    print(f'BLACKJACK!!! {player.name} WINS!!!')
    quit()


end_player_turn = False

while not end_player_turn and player.get_total() <= 21:
    move = input('Hit (h) or Stay (s)? ')
    if move == 'h':
        if new_deck.all_cards[-1].rank == "Ace":
            has_ace += 1
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
        if has_ace == 0:
            print('BUST! GAME OVER. DEALER WINS!')
            quit()                                      # If player goes above 21, game automatically closes. Dealer does not need to show cards.
        else:
            for card in player.hand:
                if card.value == 11:
                    card.value = 1
                    has_ace -= 1
                    break

            print(f'Ace is automatically set to 1. New card total: {player.get_total()}')




if new_deck.all_cards[-1].rank == "Ace":
    dealer_has_ace += 1
dealer.get_card(new_deck.deal_card())
print('\nDealer shows both cards...')
print(dealer)
print(f'Card total: {dealer.get_total()}')


if dealer.get_total() == 21:                # Checks for default win condition
    print(f'BLACKJACK!!! DEALER WINS!!!')
    quit()


while dealer.get_total() <= 21 and dealer.get_total() <= player.get_total():
    print('Dealer is hitting...')
    time.sleep(1)
    if new_deck.all_cards[-1].rank == "Ace":
        dealer_has_ace += 1
    dealer.get_card(new_deck.deal_card())

    print(dealer)
    print(f'Card total: {dealer.get_total()}')

    if dealer.get_total() > 21:
        if dealer_has_ace == 0:
            print(f'BUST! GAME OVER. PLAYER {player.name} WINS!')
            quit()
        else:
            for card in dealer.hand:
                if card.value == 11:
                    card.value = 1
                    dealer_has_ace -= 1
                    break

            print(f'Ace is automatically set to 1. New card total: {dealer.get_total()}')


# Check winning conditions at the end
if dealer.get_total() > 21:
    print(f'DEALER BUSTS! GAME OVER. {player.name} WINS!')
else:
    print('DEALER WINS!')