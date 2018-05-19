from random import shuffle

class Card():
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __str__(self):
        return f'{self.value} of {self.suit}'

class Deck():
    
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King', 'Ace']
    _cards = []
    
    def __init__(self):
        for suit in self.suits:
            for value in self.values:
                self._cards.append(Card(suit, value))
                
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
            for value in self.values:
                self._cards.append(Card(suit, value))
                
    def is_empty(self):
        return len(self._cards) == 0
    
    def __str__(self):
        result = ''
        
        for card in self._cards:
            result = result + str(card) + '\n'
        return result