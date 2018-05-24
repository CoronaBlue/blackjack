from random import shuffle

class Card():
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck():
    
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    ranks = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Jack', 'Queen', 'King', 'Ace']
    values = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    
    def __init__(self):
        self._cards = []

        for suit in self.suits:
            for rank in self.ranks:
                self._cards.append(Card(suit, rank))
                
    def draw(self):
        if not self.is_empty():
            return self._cards.pop(0)
        else:
            print('The deck is empty.')
    
    def deck_shuffle(self):
        shuffle(self._cards)
        
    def reload(self):
        self._cards.clear()
        
        for suit in self.suits:
            for rank in self.ranks:
                self._cards.append(Card(suit, rank))
                
    def is_empty(self):
        return len(self._cards) == 0
    
    def __str__(self):
        result = ''
        
        for card in self._cards:
            result = result + str(card) + '\n'
        return result

class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += Deck.values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def clear_hand(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        result = ''

        for card in self.cards:
            result += f'{card}\n'

        result += f'Total Value: {self.value}'

        return result 

class Chips():

    def __init__(self):
        self.value = 100
        self.bet = 0

    def win_bet(self):
        self.value += self.bet

    def lose_bet(self):
        self.value -= self.bet

    def __str__(self):
        return str(self.value)
