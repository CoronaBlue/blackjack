'''
Name: Blackjack
Author: Adam Huffman
Date: 5/18/17
Description: Text based Blackjack game, where one player faces off against an AI-controlled dealer.
'''
#Import my classes from the playing_cards.py file.
from playing_cards import *

################## Function Definitions ####################
def place_bet(chips):

    while True:
        try:
            chips.bet = abs(int(input('Player, place your bet: ')))
        except ValueError:
            print('\nThat is not a valid input! Please try again.\n')
        else:
            if chips.bet > chips.value:
                print("Sorry, you don't have that many chips. Please try again.\n")
            elif chips.bet < 0:
                print("Please enter a positive integer!\n")
            else:
                break
    print('\n')

def hit(hand, deck):
    hand.add_card(deck.draw())
    player.adjust_for_aces()

def hit_or_stand(deck, hand):
    global standing

    while True:
        player_choice = input('Player, do you want to Hit or Stand?: ').lower()

        if player_choice[0] == 'h':
            hit(hand, deck)
            break
        elif player_choice[0] == 's':
            print("\nThe player stands. It is now the dealer's turn.\n")
            standing = True
            break
        else:
            print('That is not a valid input. Please try again.\n')
    print('\n')

def show_some(player, dealer):
    print("DEALER'S HAND:")
    print(f'{dealer.cards[0]}')
    print('???')
    print(f'Total Value: {Deck.values[dealer.cards[0].rank]}')
    print('\n')
    print("PLAYER'S HAND:")
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
# Instantiating the game objects.
player = Hand()
dealer = Hand()
player_chips = Chips()
deck = Deck()

################# Game Starts Here ###########################
# Infinite game loop.
while True:
    # Player is not standing, and a natural hasn't been achieved.
    standing = False
    natural = False

    # Opening statement.
    print('\nWELCOME TO BLACKJACK!\n')

    # Shuffle the deck.
    deck.reload()
    deck.deck_shuffle()

    # Reset the hands.
    player.clear_hand()
    dealer.clear_hand()

    # Player places a bet.
    if player_chips.value > 0:
        place_bet(player_chips)
    else:
        print("\nYou're out of chips! Get out of my casino!\n")
        break

    # Distribute cards, according to the rules of Blackjack.
    hit(player, deck)
    hit(dealer, deck)
    hit(player, deck)
    hit(dealer, deck)

    # Is there a NATURAL?
    if player.value == 21:
        player_wins(player_chips)
        natural = True

    ################### Player's Turn ########################
    while not standing and player.value <= 21 and not natural:

        # Display cards, and calculate totals.
        show_some(player, dealer)

        # Player chooses to hit, or stay.
        hit_or_stand(deck, player)

    ################### Dealer's Turn ########################
    if player.value <= 21 and not natural:
        while dealer.value < 17:
            #The dealer hits.
            hit(dealer, deck)

    # Show all cards.
    show_all(player, dealer)

    # Determine end game condition.
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

    print('\n')