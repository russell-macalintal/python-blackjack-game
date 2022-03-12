# python-blackjack-game

Basic Python-based Black Jack game for a single player against House/Dealer. The goal of the game is for the Player to accrue cards whose values shall total to as close as 21 as possible without going over. The Player wins if their cards do not sum up to a number higher than 21 AND if their total is higher than that of the Dealer's hand.

INSTRUCTIONS
- Start the game by executing 'python3 blackjack.py' on the command line.
- Game will show the Player's hand (set of 2 cards) against the Dealer's hand (set of 2 cards with 1 card hidden).
- When prompted, the Player must Hit (h) or Stay (s).
  *Hitting indicates that the Player wants to be dealt another card whose value shall be added to the Player's current hand.
  *Staying indicates the the Player wants to keep their current hand and move on to the Dealer's turn.
- If the Player's hand does not go over a total value of 21, the Dealer is then forced to show their second card and be dealt an additional card, until a) their hand's total value is higher than that of the Player's hand without exceeding a total value of 21 (DEALER WIN CONDITION) or b) their hand's total value exceeds 21 (PLAYER WIN CONDTION)