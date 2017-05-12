'''
    @author: HenriBlacksmith
'''
# -- imports
from Card import Card

class Game(object):
    def __init__(self):
        self.n_tokens = 8
        self.active_tokens = self.n_tokens
        self.card_shoe = []
        
        self.COLORS = ['Blue', 'Red', 'Green', 'Yellow', 'White']
        self.NUMBERS = ['1', '2', '3', '4', '5']
        self.AMOUNTS = [3, 2, 2, 2, 1]
        
    # -- getters
    def get_tokens(self):
        return self.__Tokens
    
    # -- public methods
    def burn_token(self):
        self.active_tokens -= 1
        if self.active_tokens < 0:
            print 'Game Over'
        return None
    
    def generate_card_shoe(self):
        self.card_shoe = self.__generate_ordered_shoe()
    
    def display_shoe(self):
        for card in self.card_shoe:
            card.display_card()
            
    # -- private methods
    def __generate_ordered_shoe(self):
        ordered_shoe = []
        for color in self.COLORS:
            for i,number in enumerate(self.NUMBERS):
                for k in xrange(self.AMOUNTS[i]):
                    current_card = Card(color, number, k)
                    ordered_shoe.append(current_card)
        return ordered_shoe
    