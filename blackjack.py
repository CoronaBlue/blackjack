'''
Name: Blackjack
Author: Adam Huffman
Date: 5/18/17
Description: Text based Blackjack game, where one player faces off against an AI-controlled dealer.
'''
#Import my classes from the playing_cards.py file.
import playing_cards

# Player class
# Needs a hand
# Needs a bankroll
# Needs to be able to bet
# Needs to be able to draw
# Needs to be able to stay

# Dealer class
# Needs a hand
# Needs to be able to draw

# Card class
# Needs a suit
# Needs a value
# Needs to be able to flip

# Deck Class
# Needs 52 Cards
# Needs to be able to shuffle
# Needs to be able to be drawn from

################## Function Definitions ####################
def place_bet(chips):

    while True:
        try:
            chips.bet = abs(int(input('Player, place your bet: ')))
            break
        except TypeError:
            print('That is not a valid input! Please try again.\n')
    print('\n')

def hit(hand, deck):
    hand.add_card(deck.draw())

def hit_or_stand(deck, hand):
    global standing
    standing = False
    player_choice = ''

    while player_choice != 'stand' or player_choice != 'hit':

        player_choice = input('Player, do you want to Hit or Stand?: ').lower()

        if player_choice == 'stand':
            standing = True
        elif player_choice == 'hit':
            hit(hand, deck)
        else:
            print('That is not a valid choice! Please try again.\n')

    print('\n')

def show_some(player, dealer):
    print("Dealer's Hand:")
    print(f'{dealer.cards[0]}')
    print('???')
    print(f'Total Value: {Deck.values[dealer.cards[0].rank]}')
    print('\n')
    print("Player's Hand:")
    print(f'{player}')
    print('\n')

def show_all(player, dealer):
    print("Dealer's Hand:")
    print(f'{dealer}')
    print('\n')
    print("Player's Hand:")
    print(f'{player}')
    print('\n')

def player_wins(chips):
    chips.win_bet()
    print('Congratulations! You have beaten the dealer!\n')

def player_busts(chips):
    chips.lose_bet()
    print('You have busted!\n')

def dealer_busts(chips):
    chips.win_bet()
    print('The dealer has busted! You win!\n')

def dealer_wins(chips):
    chips.lose_bet()
    print('The dealer has beaten you!\n')

def push():
    print('This match is a draw!\n')

def play_again():
    return input('Would you like to play again? y/n: ').lower() == 'y'

################## Get Objects Ready #######################
# Player
player = Hand()
player_chips = Chips()

# Dealer
dealer = Hand()

# Deck
deck = Deck()

################# Game Starts Here ###########################
# Infinite game loop.
while True:
    # Shuffle the deck.
    deck.reload()
    deck.deck_shuffle()

    # Reset the hands.
    player.clear_hand()
    dealer.clear_hand()

    # Player is not standing.
    standing = False

    # Player places a bet.
    place_bet(player_chips)

    # Player gets one Card from the Deck, face up.
    hit(player, deck)

    # Dealer gets one Card from the Deck, face up.
    hit(dealer, deck)

    # Player gets one Card from the Deck, face up.
    hit(player, deck)

    # Dealer gets one Card from the Deck, face down
    hit(dealer, deck)

    # Display cards, and calculate totals.
    show_some(player, dealer)

    # Is there a NATURAL?
    if player.value == 21:
        player_wins(player_chips)
        standing = True

    ################### Player's Turn ########################
    while not standing and player.value < 21:

        # Player chooses to hit, or stay.
        hit_or_stand(deck, player)
        
        # Adjust for aces.
        player.adjust_for_aces()

        # Display cards, and calculate totals.
        show_some(player, dealer)

    ################### Player's Turn ########################
    while dealer.value < 17 and player.value <= 21 and not standing:
        #The dealer hits.
        hit(dealer, deck)

    #Show all cards.
    show_all(player, dealer)

    if dealer.value > 21:
        dealer_busts(player_chips)
    elif player.value > 21:
        player_busts(player_chips)
    elif dealer.value > player.value:
        dealer_wins(player_chips)
    elif dealer.value < player.value:
        player_wins(player_chips)
    elif dealer.value == player.value:
        push()

    # Print the player's chip total.
    print(f'Your final chip total is {player_chips}.\n')

    # Play again?
    if not play_again():
        break